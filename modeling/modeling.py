# --- Importing Libraries ---

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import pandas as pd
import numpy as np
import xgboost as xgb
import shap
import os
from sklearn.model_selection import KFold, StratifiedKFold, TimeSeriesSplit, train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, precision_score, accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTEN
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
from matplotlib import cm
from matplotlib.colors import to_hex

# --- Global Settings ---
plt.rcParams['font.family'] = 'Helvetica' # Set font to Helvetica

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Glyph.*missing")
warnings.filterwarnings("ignore", category=UserWarning, message=".*precision is ill-defined.*")

# Set seaborn stile to 'ticks'
sns.set(style="ticks")

# Define color map
viridis = plt.cm.viridis(np.linspace(0, 1, 10))

# --- Directory Setup ---
directories = [
    './plots/time-series/', './plots/arima/', './plots/xgboost/', './plots/rfc-prediction/', './plots/rfr-prediction/'
]

# Create directories if they don't exist
for dir in directories:
    os.makedirs(dir, exist_ok=True) # No error if directory exists

# --- 1. Loading the Dataset ---
df = pd.read_csv('combined_2011-2022_ca_hospital_ratings.csv')

# Remove rows corresponding to years 2005-2008 (all performance_measure values are 0)
df = df[~df['year'].isin([2005, 2006, 2007, 2008])]

# Convert 'year' to datetime format
df['year'] = pd.to_datetime(df['year'], format='%Y')
df.set_index('year', inplace=True) # Set 'year' as index

# Convert index to a period with yearly frequency
df.index = pd.to_datetime(df.index)  # Datetime format
df.index = df.index.to_period('Y')

# Sort dataframe by index for time-series analysis
df = df.sort_index()

# 1.1 Prepare Markdown File
model_file = "model_results.md"
with open(model_file, "w") as file:
    file.write("# Modeling\n\n")

# --- 2. Risk Adjustment Analysis and Adverse Events Prediction ---
# 2.1 Prepare features and target variable
X = df[['risk_adjusted_rate']]  # Feature
y = df['#_of_adverse_events']  # Target

# 2.2 Train-test split using KFold cross-validation
# Split dataset into 5 folds, shuffling data for randomness
skf = KFold(n_splits=5, shuffle=True, random_state=42) 

# 2.3 Initialize lists to store metrics across folds
rf_metrics = {"MSE": [], "R2": [], "MAE": [], "RMSE": []}
lr_metrics = {"MSE": [], "R2": [], "MAE": [], "RMSE": []}

fold = 1 # Fold counter

# 2.4 Train and evaluate models across each fold
# for loop iterates through each fold and trains/evaluates models
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index] # Split features
    y_train, y_test = y.iloc[train_index], y.iloc[test_index] # Split targer

    # Random forest regressor
    rf = RandomForestRegressor(n_estimators=100, random_state=42) # Initialize model
    rf.fit(X_train, y_train) # Train model on training set
    y_pred_rf = rf.predict(X_test) # Predict on test set

    # Calculate evaluation metrics
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)
    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mse_rf)

    # Store random forest metrics in dictionary
    rf_metrics["MSE"].append(mse_rf)
    rf_metrics["R2"].append(r2_rf)
    rf_metrics["MAE"].append(mae_rf)
    rf_metrics["RMSE"].append(rmse_rf)

    # Linear regression
    lr = LinearRegression() # Initialize linear regression model
    lr.fit(X_train, y_train) # Train model on training set
    y_pred_lr = lr.predict(X_test) # Predict on test set

    # Calculate evaluation metrics
    mse_lr = mean_squared_error(y_test, y_pred_lr)
    r2_lr = r2_score(y_test, y_pred_lr)
    mae_lr = mean_absolute_error(y_test, y_pred_lr)
    rmse_lr = np.sqrt(mse_lr)

    # Store linear regression metrics in dictionary
    lr_metrics["MSE"].append(mse_lr)
    lr_metrics["R2"].append(r2_lr)
    lr_metrics["MAE"].append(mae_lr)
    lr_metrics["RMSE"].append(rmse_lr)

    # Add fold results to markdown file
    with open(model_file, "a") as file:
        file.write(f"### Fold {fold} Results\n")
        file.write("#### Random Forest Regressor\n")
        file.write(f"- MSE: {mse_rf:.2f}, R²: {r2_rf:.2f}, MAE: {mae_rf:.2f}, RMSE: {rmse_rf:.2f}\n")
        file.write("#### Linear Regression\n")
        file.write(f"- MSE: {mse_lr:.2f}, R²: {r2_lr:.2f}, MAE: {mae_lr:.2f}, RMSE: {rmse_lr:.2f}\n\n")

    # Plot predicted vs. actual values for random forest regressor and linear regression models
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred_rf, alpha=0.6, label="Random Forest", color="blue")
    plt.scatter(y_test, y_pred_lr, alpha=0.6, label="Linear Regression", color="orange")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--") # Line of perfect prediction
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title(f"Predicted vs Actual Values (Fold {fold})")
    plt.legend()
    plot_path = f"./plots/rfr-prediction/fold_{fold}_predicted_vs_actual.png"
    plt.savefig(plot_path)
    plt.close()

    # Add scatterplot to markdown
    with open(model_file, "a") as file:
        file.write(f"#### Predicted vs Actual Scatter Plot\n")
        file.write(f"![Fold {fold} Predicted vs Actual]({plot_path})\n\n")

    fold += 1 # Increment fold counter

# 2.5 Compute averages across folds
avg_rf_metrics = {key: np.mean(values) for key, values in rf_metrics.items()}
avg_lr_metrics = {key: np.mean(values) for key, values in lr_metrics.items()}

# 2.6 Save overall model performance summary to markdown
with open(model_file, "a") as file:
    file.write("## Overall Model Performance Summary\n")
    file.write("### Random Forest Regressor\n")
    file.write(f"- Avg MSE: {avg_rf_metrics['MSE']:.2f}, Avg R²: {avg_rf_metrics['R2']:.2f}, ")
    file.write(f"Avg MAE: {avg_rf_metrics['MAE']:.2f}, Avg RMSE: {avg_rf_metrics['RMSE']:.2f}\n\n")
    file.write("### Linear Regression\n")
    file.write(f"- Avg MSE: {avg_lr_metrics['MSE']:.2f}, Avg R²: {avg_lr_metrics['R2']:.2f}, ")
    file.write(f"Avg MAE: {avg_lr_metrics['MAE']:.2f}, Avg RMSE: {avg_lr_metrics['RMSE']:.2f}\n")

# 2.7 Generate comparison bar chart for MSE and R²
x = np.arange(5) # x-axis labels for each fold
width = 0.35 # Bar width

plt.figure(figsize=(12, 6))
plt.bar(x - width / 2, rf_metrics["MSE"], width, label="Random Forest MSE", color="blue")
plt.bar(x + width / 2, lr_metrics["MSE"], width, label="Linear Regression MSE", color="orange")
plt.xlabel("Fold")
plt.ylabel("MSE")
plt.title("MSE Comparison Across Folds")
plt.legend()
comparison_path = "./plots/rfr-prediction/mse_comparison.png"
plt.savefig(comparison_path)
plt.close()

# Add comparison chart plot to markdown
with open(model_file, "a") as file:
    file.write("### MSE Comparison Across Folds\n")
    file.write(f"![MSE Comparison]({comparison_path})\n")

# --- 3. Random Forest Classifier for Predicting Hospital Ratings ---
# 3.1 Prepare features and target variable
# Group dataset by 'oshpd_id' and 'performance_measure'
df_rf = df.groupby(['oshpd_id', 'performance_measure']).agg({
    'hospital_rating': lambda x: x.mode()[0], # Most common rating
    'risk_adjusted_rate': 'mean', # Average risk_adjusted_rate
    '#_of_cases': 'sum', # Total number of cases
    '#_of_adverse_events': 'sum', # Total number of adverse events
})

# Encode 'hospital_rating' as numerical values
le = LabelEncoder()
df_rf['hospital_rating_encoded'] = le.fit_transform(df_rf['hospital_rating'])

# Define features and target
X = df_rf.drop(columns=['hospital_rating', 'hospital_rating_encoded']) # Features
y = df_rf['hospital_rating_encoded'] # Target

# 3.2 Train-test split and cross-validation setup
# SMOTEN for balancing classes
smoten = SMOTEN(random_state=42, k_neighbors=3)

# Stratified K-Fold cross validation to ensure each fold has balanced representation of classes
skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

fold = 1 # Initialize fold counter

# 3.3 Train and evaluate the Random Forest model
# for loop iterates through each fold and trains/evaluates models
for train_index, test_index in skf.split(X, y): 
    # Split data into training/testing sets based on K-fold indices
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # Apply SMOTEN to balance training data by generating synthetic data for minority classes
    X_train_balanced, y_train_balanced = smoten.fit_resample(X_train, y_train)

    # Initialize random forest classifier with class balancing
    rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    
    # Fit random forest model on balanced training set
    rf.fit(X_train_balanced, y_train_balanced)

    # Make predictions on test set
    y_pred = rf.predict(X_test)

    # Compute evaluation metrics for model performance
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=1) # Weighted precision
    accuracy = accuracy_score(y_test, y_pred) # Accuracy score
    f1_weighted = f1_score(y_test, y_pred, average='weighted') # Weighted F1 score
    classification_report_result = classification_report(y_test, y_pred) # Classification report
    confusion_matrix_result = confusion_matrix(y_test, y_pred) # Confusion matrix

    # Add results from fold to markdown file
    with open(model_file, "a") as file:
        file.write(f"## Fold {fold} Results\n\n")
        file.write(f"### Random Forest Performance Metrics\n")
        file.write(f"- Accuracy: {accuracy:.2f}\n")
        file.write(f"- Weighted Precision: {precision:.2f}\n")
        file.write(f"- Weighted F1 Score: {f1_weighted:.2f}\n\n")
        file.write(f"### Classification Report\n")
        file.write(classification_report_result + "\n")

    # Create a heatmap for the confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrix_result, annot=True, fmt='d', cmap='viridis', xticklabels=le.classes_, 
                yticklabels=le.classes_, cbar_kws={'label': 'Frequency'})
    plt.title(f'Confusion Matrix for Fold {fold}')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    heatmap_path = f"./plots/rfc-prediction/confusion_matrix_fold_{fold}.png"
    plt.savefig(heatmap_path)
    plt.close()

    # Add confusion matrix plot to markdown file
    with open(model_file, "a") as file:
        file.write(f"### Confusion Matrix Heatmap\n")
        file.write(f"![Confusion Matrix for Fold {fold}]({heatmap_path})\n\n")

    fold += 1 # Increment fold counter

# Add cross validation summary to markdown file
with open(model_file, "a") as file:
    file.write("## Cross-Validation Summary\n")
    file.write(f"The results for all folds are summarized in the markdown file.\n")

# --- 4. Time Series Forecasting with Exponential Smoothing ---

def sanitize_filename(name):
    """
    Sanitize file/directory names by replacing problematic characters.
    """
    if isinstance(name, (list, np.ndarray)): # Recursively apply sanitization for lists/arrays
        return [sanitize_filename(n) for n in name]
    
    # Replace specific problematic characters
    return name.replace('acc puncture', 'acc_puncture').replace('/', '_')

# Get all unique performance_measures from dataframe
performance_measures = df['performance_measure'].unique()

# 4.1 Fit Exponential Smoothing model
# for loop iterates through each performance measure in the dataset
# Loop through each performance measure
for measure in performance_measures:
    sanitized_measure = sanitize_filename(measure)  # Sanitize file name
    measure_data = df[df['performance_measure'] == measure]  # Filter data for specific measure

    # Aggregate data by year
    df_aggregated = measure_data.groupby('year').agg({
        '#_of_cases': 'mean',
        '#_of_adverse_events': 'mean',
        'risk_adjusted_rate': 'mean'
    })

    # Ensure index is in datetime format
    if isinstance(df_aggregated.index, pd.PeriodIndex):
        # Convert PeriodIndex to DatetimeIndex using .to_timestamp()
        df_aggregated.index = df_aggregated.index.to_timestamp()
    else:
        # Ensure the index is already a DatetimeIndex
        df_aggregated.index = pd.to_datetime(df_aggregated.index)

    # Set frequency to yearly start ('YS') if needed
    df_aggregated = df_aggregated.asfreq('YS')


    # Skip measures with insufficient or invalid data
    if len(df_aggregated['risk_adjusted_rate']) < 2 or \
            df_aggregated['risk_adjusted_rate'].isnull().any() or \
            df_aggregated['risk_adjusted_rate'].nunique() == 1:
        continue

    try:
        # Fit Exponential Smoothing Model
        seasonal_periods = 2
        exp_smooth_model = ExponentialSmoothing(
            df_aggregated['risk_adjusted_rate'], 
            trend='add', 
            seasonal='add', 
            seasonal_periods=seasonal_periods
        )
        exp_smooth_model_fit = exp_smooth_model.fit(optimized=True)

        # Skip if Sum of Squared Errors (SSE) is 0
        if exp_smooth_model_fit.sse == 0:
            continue

        # Forecast Future Values
        exp_smooth_predictions = exp_smooth_model_fit.forecast(steps=2)
        last_date = df_aggregated.index[-1]  # Get last date
        future_dates = pd.date_range(start=last_date, periods=3, freq='YE')[1:]  # Generate future dates

        # Save predictions to markdown file
        with open(model_file, "a") as file:
            file.write(f"## Exponential Smoothing Predictions for {sanitized_measure}\n\n")
            file.write(f"Predictions for the next 2 years: {exp_smooth_predictions.tolist()}\n\n")

        # Plot Actual vs Predicted Values
        plt.figure(figsize=(10, 6))
        plt.plot(df_aggregated.index, df_aggregated['risk_adjusted_rate'], label="Actual", color='purple')
        plt.plot(future_dates, exp_smooth_predictions, label="Exponential Smoothing Forecast", color='green')
        plt.legend()
        plt.title(f"Exponential Smoothing Forecast for {measure}")
        exp_smooth_plot_path = f"./plots/time-series/exp_smooth_forecast_{sanitized_measure}.png"
        plt.savefig(exp_smooth_plot_path)
        plt.close()

        # Save the plot to the markdown file
        with open(model_file, "a") as file:
            file.write(f"![Exponential Smoothing Forecast for {measure}]({exp_smooth_plot_path})\n\n")

        # 4.2 Perform time series cross validation
        tscv = TimeSeriesSplit(n_splits=5)
        for train_index, test_index in tscv.split(df_aggregated):
            train, test = df_aggregated.iloc[train_index], df_aggregated.iloc[test_index]

            # Fit exponential smoothing model to training data
            exp_smooth_model = ExponentialSmoothing(train['risk_adjusted_rate'], trend='add', seasonal='add', 
                                                    seasonal_periods=seasonal_periods)
            exp_smooth_model_fit = exp_smooth_model.fit()

            # Forecast on test data
            exp_smooth_predictions_cv = exp_smooth_model_fit.forecast(steps=len(test))

            # Plot cross validation results
            plt.figure(figsize=(10, 6))
            plt.plot(train.index, train['risk_adjusted_rate'], label="Train", color='blue')
            plt.plot(test.index, test['risk_adjusted_rate'], label="Test", color='orange')
            plt.plot(test.index, exp_smooth_predictions_cv, label="Forecast", color='green')
            plt.legend()
            plt.title(f"Cross-validation forecast for {measure}")
            exp_smooth_cv_plot_path = f"./plots/time-series/cross_validation_forecast_{sanitized_measure}.png"
            plt.savefig(exp_smooth_cv_plot_path)
            plt.close()

            # Save cross validation plot to markdown file
            with open(model_file, "a") as file:
                file.write(f"![Cross Validation Forecast for {measure}]({exp_smooth_cv_plot_path})\n\n")

    except ValueError:
        continue # Skip if there is error fitting model

# --- 5. Time Series Forecasting with ARIMA ---
# 5.1 Fit Arima model
# for loop iterates through all performance measures in dataset
for measure in performance_measures:

    # Sanitize file name
    sanitized_measure = sanitize_filename(measure)

    # Filter data for current performance measure
    measure_data = df[df['performance_measure'] == measure]

    # Group data by year and calculate mean for numeric columns
    df_aggregated = df.groupby('year').agg({
        '#_of_cases': 'mean',
        '#_of_adverse_events': 'mean',
        'risk_adjusted_rate': 'mean'
    })

    # Ensure index is in datetime format
    if isinstance(df_aggregated.index, pd.PeriodIndex):
        # Convert PeriodIndex to DatetimeIndex using .to_timestamp()
        df_aggregated.index = df_aggregated.index.to_timestamp()
    else:
        # Ensure the index is already a DatetimeIndex (no conversion needed)
        df_aggregated.index = pd.to_datetime(df_aggregated.index)

    # Set frequency to yearly start ('YS') if needed
    df_aggregated = df_aggregated.asfreq('YS')

    # Perform Augmented Dickey-Fuller (ADF) to test if data is stationary
    adf_result = adfuller(df_aggregated['risk_adjusted_rate'])
    adf_statistic, adf_p_value = adf_result[0], adf_result[1]

    # 5.2 Time Series Split and ARIMA Model Training
    tscv = TimeSeriesSplit(n_splits=3)  # Split data into 3 folds for cross-validation

    for split_idx, (train_idx, test_idx) in enumerate(tscv.split(df_aggregated['risk_adjusted_rate'])):
        # Extract train and test data for the current fold
        train_data = df_aggregated['risk_adjusted_rate'].iloc[train_idx]
        test_data = df_aggregated['risk_adjusted_rate'].iloc[test_idx]

        # Fit ARIMA model using auto_arima
        best_model = auto_arima(train_data, start_p=0, max_p=3, start_q=0, max_q=3, seasonal=False, stepwise=True, trace=True)

        # Forecast for the test data
        forecast, conf_int = best_model.predict(n_periods=len(test_data), return_conf_int=True, alpha=0.05)

        # Calculate mean squared error between actual and predicted values
        mse = mean_squared_error(test_data, forecast)
        
        # Calculate residuals for the training data
        residuals = train_data - best_model.predict_in_sample()

        # Ensure residuals have proper datetime index
        if isinstance(residuals.index, pd.PeriodIndex):
            residuals.index = residuals.index.to_timestamp()

        # Plot Residuals 
        plt.figure(figsize=(10, 6))

        # Plot residuals over time
        plt.subplot(211)
        plt.plot(residuals, label="Residuals")
        plt.axhline(0, color='red', linestyle='--', linewidth=0.8)
        plt.title(f"Residuals Over Time (Split {split_idx + 1})")
        plt.xlabel("Time")
        plt.ylabel("Residuals")

        # Plot histogram of residuals
        plt.subplot(212)
        plt.hist(residuals, bins=20, edgecolor='k', color='blue')
        plt.title("Residual Histogram")
        plt.xlabel("Residual Value")
        plt.ylabel("Frequency")

        plt.tight_layout()
        residuals_plot_path = f"./plots/arima/residuals_split_{split_idx + 1}.png"
        plt.savefig(residuals_plot_path)
        plt.close()

        # Plot Forecast vs. Actual
        plt.figure(figsize=(10, 6))

        # Define colors for actual, forecast, and confidence intervals
        viridis_colors = cm.viridis(np.linspace(0, 1, 3))
        plt.plot(df_aggregated.index, df_aggregated['risk_adjusted_rate'], label="Actual", color=to_hex(viridis_colors[0]))
        plt.plot(test_data.index, forecast, label="ARIMA Forecast", color=to_hex(viridis_colors[1]))
        plt.fill_between(test_data.index, conf_int[:, 0], conf_int[:, 1], color=to_hex(viridis_colors[2]), alpha=0.3, label="95% Confidence Interval")

        plt.legend()
        plt.title(f"ARIMA Forecast with Confidence Intervals (Split {split_idx + 1})")
        plt.xlabel("Time")
        plt.ylabel("Risk-Adjusted Rate")
        arima_forecast_plot_path = f"./plots/arima/arima_forecast_split_{split_idx + 1}.png"
        plt.savefig(arima_forecast_plot_path)
        plt.close()

        # Add results and plots to markdown file
        with open(model_file, "a") as file:
            file.write(f"## ARIMA Analysis for {measure}\n")
            file.write(f"### Augmented Dickey-Fuller Test\n")
            file.write(f"ADF Statistic: {adf_statistic:.4f}, p-value: {adf_p_value:.4f}\n\n")
            file.write(f"### ARIMA Forecast Results\n")
            file.write(f"RMSE: {np.sqrt(mse):.4f}\n\n")
            file.write("### Automatic ARIMA Model Summary\n")
            file.write(str(best_model.summary()) + "\n\n")
            file.write(f"![Residual Histogram for {measure}]({residuals_plot_path})\n\n")
            file.write(f"![ARIMA Forecast for {measure}]({arima_forecast_plot_path})\n\n")

# --- 6. Model Optimization: XGBoost ---

# 6.1 Define features and target
# Exclude non-numeric columns
X = df.drop(columns=['hospital', 'year', 'county', 'oshpd_id', 'performance_measure', 'hospital_rating', 
                     'risk_adjusted_rate'], errors='ignore')
y = df['risk_adjusted_rate'] # Target

# Split into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6.2 Define parameter grid for hyperparameter turning of XGBoost model
param_grid = {
    'n_estimators': [50, 100, 200], # Number of trees in model
    'learning_rate': [0.01, 0.05, 0.1], # Learning rate for boosting
    'max_depth': [3, 5, 7, 9], # Maximum depth of trees
    'subsample': [0.6, 0.8, 1.0], # Fraction of samples used for training for each tree
    'colsample_bytree': [0.6, 0.8, 1.0], # Fraction of samples used for each tree
    'min_child_weight': [1, 3, 5] # Minimum sum of instance weight required in child
}

# Perform grid search with cross validation to find best model parameters
grid_search = GridSearchCV(
    estimator=xgb.XGBRegressor(random_state=42), # Initialize XGBoost regressor
    param_grid=param_grid, # Define parameter grid
    cv=5, # 5-fold cross validation
    scoring='neg_mean_squared_error', # Score based on negative MSE
    n_jobs=-1 # Parallel processiong
)
grid_search.fit(X_train, y_train) # Fit model using training data

# Use best hyperparameters from grid search
best_params = grid_search.best_params_

# Train XGBoost model with best hyperparameters
xg_model = xgb.XGBRegressor(**best_params, random_state=42)
xg_model.fit(X_train, y_train) # Train model with training data

# 6.3 Make predictions using test set
y_pred_xg = xg_model.predict(X_test) 

# Calculate evaluation metrics
xgboost_mse = mean_squared_error(y_test, y_pred_xg)
xgboost_r2 = r2_score(y_test, y_pred_xg)
cv_scores = -cross_val_score(xg_model, X, y, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
cv_rmse = np.sqrt(cv_scores.mean())
mae = mean_absolute_error(y_test, y_pred_xg)

# Add results to markdown file
with open(model_file, "a") as file:
    file.write("## XGBoost Model Performance\n\n")
    file.write(f"- Test MSE: {xgboost_mse:.2f}\n")
    file.write(f"- Test RMSE (Cross-Validation): {cv_rmse:.2f}\n")
    file.write(f"- Test R²: {xgboost_r2:.2f}\n")
    file.write(f"- Test MAE: {mae:.2f}\n\n")

# 6.4 Get feature performance for trained model
xgboost_feature_importance = pd.DataFrame({
    'Feature': X.columns, 
    'Importance': xg_model.feature_importances_
}).sort_values(by='Importance', ascending=False)

# Plot feature performance
plt.figure(figsize=(10, 6))
plt.barh(xgboost_feature_importance['Feature'], xgboost_feature_importance['Importance'])
plt.gca().invert_yaxis()
plt.title('XGBoost Feature Importance')
plt.xlabel('Importance Score')
feature_importance_plot_path = "./plots/xgboost/xgboost_feature_importance.png"
plt.savefig(feature_importance_plot_path)
plt.close()

# Add feature importance plot to markdown file
with open(model_file, "a") as file:
    file.write("### XGBoost Feature Importance\n\n")
    file.write(f"![Feature Importance]({feature_importance_plot_path})\n\n")

# 6.5 Plot residuals of model
residuals = y_test - y_pred_xg
plt.figure(figsize=(8, 6))
plt.scatter(y_pred_xg, residuals, alpha=0.6)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residual Plot')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
residual_plot_path = "./plots/xgboost/xgboost_residual_plot.png"
plt.savefig(residual_plot_path)
plt.close()

# Add residuals plot to markdown file
with open(model_file, "a") as file:
    file.write("### Residual Plot\n\n")
    file.write(f"![Residual Plot]({residual_plot_path})\n\n")

# 6.6 Plot predicted vs. actual values for test set
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_xg, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.title('Predicted vs Actual Values')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
predicted_vs_actual_plot_path = "./plots/xgboost/xgboost_predicted_vs_actual.png"
plt.savefig(predicted_vs_actual_plot_path)
plt.close()

# Add plot to markdown file
with open(model_file, "a") as file:
    file.write("### Predicted vs Actual Values\n\n")
    file.write(f"![Predicted vs Actual Values]({predicted_vs_actual_plot_path})\n\n")

# 6.7 Use Shapley Additive Explanations (SHAP) to explain model's predictions
explainer = shap.Explainer(xg_model, X_test) # Initialize SHAP explainer
shap_values = explainer(X_test) # Get SHAP values

shap_summary_plot_path = "./plots/xgboost/xgboost_shap_summary.png"
shap.summary_plot(shap_values, X_test, show=False)
plt.savefig(shap_summary_plot_path, bbox_inches="tight")
plt.close()

# Add SHAP summary plot to markdown file
with open(model_file, "a") as file:
    file.write("### SHAP Summary Plot\n\n")
    file.write(f"![SHAP Summary Plot]({shap_summary_plot_path})\n\n")