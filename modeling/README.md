# Modeling

### Fold 1 Results
#### Random Forest Regressor
- MSE: 716.71, R²: -0.07, MAE: 5.16, RMSE: 26.77
#### Linear Regression
- MSE: 646.82, R²: 0.04, MAE: 6.52, RMSE: 25.43

#### Predicted vs Actual Scatter Plot
![Fold 1 Predicted vs Actual](./plots/rfr-prediction/fold_1_predicted_vs_actual.png)

### Fold 2 Results
#### Random Forest Regressor
- MSE: 722.67, R²: -0.00, MAE: 5.30, RMSE: 26.88
#### Linear Regression
- MSE: 693.68, R²: 0.04, MAE: 6.77, RMSE: 26.34

#### Predicted vs Actual Scatter Plot
![Fold 2 Predicted vs Actual](./plots/rfr-prediction/fold_2_predicted_vs_actual.png)

### Fold 3 Results
#### Random Forest Regressor
- MSE: 678.25, R²: 0.07, MAE: 5.13, RMSE: 26.04
#### Linear Regression
- MSE: 698.56, R²: 0.04, MAE: 6.80, RMSE: 26.43

#### Predicted vs Actual Scatter Plot
![Fold 3 Predicted vs Actual](./plots/rfr-prediction/fold_3_predicted_vs_actual.png)

### Fold 4 Results
#### Random Forest Regressor
- MSE: 611.42, R²: 0.01, MAE: 5.10, RMSE: 24.73
#### Linear Regression
- MSE: 590.72, R²: 0.04, MAE: 6.62, RMSE: 24.30

#### Predicted vs Actual Scatter Plot
![Fold 4 Predicted vs Actual](./plots/rfr-prediction/fold_4_predicted_vs_actual.png)

### Fold 5 Results
#### Random Forest Regressor
- MSE: 639.03, R²: -0.07, MAE: 5.01, RMSE: 25.28
#### Linear Regression
- MSE: 575.66, R²: 0.04, MAE: 6.41, RMSE: 23.99

#### Predicted vs Actual Scatter Plot
![Fold 5 Predicted vs Actual](./plots/rfr-prediction/fold_5_predicted_vs_actual.png)

## Overall Model Performance Summary
### Random Forest Regressor
- Avg MSE: 673.62, Avg R²: -0.01, Avg MAE: 5.14, Avg RMSE: 25.94

### Linear Regression
- Avg MSE: 641.09, Avg R²: 0.04, Avg MAE: 6.62, Avg RMSE: 25.30
### MSE Comparison Across Folds
![MSE Comparison](./plots/rfr-prediction/mse_comparison.png)
## Fold 1 Results

### Random Forest Performance Metrics
- Accuracy: 0.96
- Weighted Precision: 0.96
- Weighted F1 Score: 0.96

### Classification Report
              precision    recall  f1-score   support

           0       0.43      0.09      0.15        32
           1       0.96      0.97      0.96      2219
           2       1.00      0.05      0.09        21
           3       0.97      0.97      0.97      1842

    accuracy                           0.96      4114
   macro avg       0.84      0.52      0.54      4114
weighted avg       0.96      0.96      0.96      4114

### Confusion Matrix Heatmap
![Confusion Matrix for Fold 1](./plots/rfc-prediction/confusion_matrix_fold_1.png)

## Fold 2 Results

### Random Forest Performance Metrics
- Accuracy: 0.96
- Weighted Precision: 0.95
- Weighted F1 Score: 0.95

### Classification Report
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        33
           1       0.95      0.97      0.96      2218
           2       0.33      0.05      0.08        21
           3       0.97      0.97      0.97      1842

    accuracy                           0.96      4114
   macro avg       0.56      0.50      0.50      4114
weighted avg       0.95      0.96      0.95      4114

### Confusion Matrix Heatmap
![Confusion Matrix for Fold 2](./plots/rfc-prediction/confusion_matrix_fold_2.png)

## Fold 3 Results

### Random Forest Performance Metrics
- Accuracy: 0.96
- Weighted Precision: 0.95
- Weighted F1 Score: 0.95

### Classification Report
              precision    recall  f1-score   support

           0       0.43      0.09      0.15        32
           1       0.96      0.96      0.96      2218
           2       0.00      0.00      0.00        21
           3       0.95      0.98      0.97      1842

    accuracy                           0.96      4113
   macro avg       0.59      0.51      0.52      4113
weighted avg       0.95      0.96      0.95      4113

### Confusion Matrix Heatmap
![Confusion Matrix for Fold 3](./plots/rfc-prediction/confusion_matrix_fold_3.png)

## Cross-Validation Summary
The results for all folds are summarized in the markdown file.
## Exponential Smoothing Predictions for carotid endarterectomy

Predictions for the next 2 years: [0.32296348613212644, 0.41576609945529125]

![Exponential Smoothing Forecast for carotid endarterectomy](./plots/time-series/exp_smooth_forecast_carotid endarterectomy.png)

![Cross Validation Forecast for carotid endarterectomy](./plots/time-series/cross_validation_forecast_carotid endarterectomy.png)

![Cross Validation Forecast for carotid endarterectomy](./plots/time-series/cross_validation_forecast_carotid endarterectomy.png)

![Cross Validation Forecast for carotid endarterectomy](./plots/time-series/cross_validation_forecast_carotid endarterectomy.png)

![Cross Validation Forecast for carotid endarterectomy](./plots/time-series/cross_validation_forecast_carotid endarterectomy.png)

![Cross Validation Forecast for carotid endarterectomy](./plots/time-series/cross_validation_forecast_carotid endarterectomy.png)

## Exponential Smoothing Predictions for esophageal resection

Predictions for the next 2 years: [0.6190106547016877, 0.64594919710916]

![Exponential Smoothing Forecast for esophageal resection](./plots/time-series/exp_smooth_forecast_esophageal resection.png)

![Cross Validation Forecast for esophageal resection](./plots/time-series/cross_validation_forecast_esophageal resection.png)

![Cross Validation Forecast for esophageal resection](./plots/time-series/cross_validation_forecast_esophageal resection.png)

![Cross Validation Forecast for esophageal resection](./plots/time-series/cross_validation_forecast_esophageal resection.png)

![Cross Validation Forecast for esophageal resection](./plots/time-series/cross_validation_forecast_esophageal resection.png)

![Cross Validation Forecast for esophageal resection](./plots/time-series/cross_validation_forecast_esophageal resection.png)

## Exponential Smoothing Predictions for pancreatic resection

Predictions for the next 2 years: [0.961004142204866, 0.96133147835756]

![Exponential Smoothing Forecast for pancreatic resection](./plots/time-series/exp_smooth_forecast_pancreatic resection.png)

![Cross Validation Forecast for pancreatic resection](./plots/time-series/cross_validation_forecast_pancreatic resection.png)

![Cross Validation Forecast for pancreatic resection](./plots/time-series/cross_validation_forecast_pancreatic resection.png)

![Cross Validation Forecast for pancreatic resection](./plots/time-series/cross_validation_forecast_pancreatic resection.png)

![Cross Validation Forecast for pancreatic resection](./plots/time-series/cross_validation_forecast_pancreatic resection.png)

![Cross Validation Forecast for pancreatic resection](./plots/time-series/cross_validation_forecast_pancreatic resection.png)

## Exponential Smoothing Predictions for pci

Predictions for the next 2 years: [2.4600298024583402, 2.709510271240393]

![Exponential Smoothing Forecast for pci](./plots/time-series/exp_smooth_forecast_pci.png)

![Cross Validation Forecast for pci](./plots/time-series/cross_validation_forecast_pci.png)

![Cross Validation Forecast for pci](./plots/time-series/cross_validation_forecast_pci.png)

![Cross Validation Forecast for pci](./plots/time-series/cross_validation_forecast_pci.png)

![Cross Validation Forecast for pci](./plots/time-series/cross_validation_forecast_pci.png)

![Cross Validation Forecast for pci](./plots/time-series/cross_validation_forecast_pci.png)

## Exponential Smoothing Predictions for aaa repair

Predictions for the next 2 years: [0.10114291381134688, -5.8991370818078925e-06]

![Exponential Smoothing Forecast for aaa repair](./plots/time-series/exp_smooth_forecast_aaa repair.png)

![Cross Validation Forecast for aaa repair](./plots/time-series/cross_validation_forecast_aaa repair.png)

![Cross Validation Forecast for aaa repair](./plots/time-series/cross_validation_forecast_aaa repair.png)

![Cross Validation Forecast for aaa repair](./plots/time-series/cross_validation_forecast_aaa repair.png)

![Cross Validation Forecast for aaa repair](./plots/time-series/cross_validation_forecast_aaa repair.png)

![Cross Validation Forecast for aaa repair](./plots/time-series/cross_validation_forecast_aaa repair.png)

## Exponential Smoothing Predictions for gi hemorrhage

Predictions for the next 2 years: [2.6661576558407902, 2.818218988721661]

![Exponential Smoothing Forecast for gi hemorrhage](./plots/time-series/exp_smooth_forecast_gi hemorrhage.png)

## Exponential Smoothing Predictions for heart failure

Predictions for the next 2 years: [2.6174947299900535, 2.7331982674230813]

![Exponential Smoothing Forecast for heart failure](./plots/time-series/exp_smooth_forecast_heart failure.png)

## Exponential Smoothing Predictions for pneumonia

Predictions for the next 2 years: [8.832126070696837, 9.537368564284602]

![Exponential Smoothing Forecast for pneumonia](./plots/time-series/exp_smooth_forecast_pneumonia.png)

## Exponential Smoothing Predictions for craniotomy

Predictions for the next 2 years: [4.027816518641115, 4.020968140198912]

![Exponential Smoothing Forecast for craniotomy](./plots/time-series/exp_smooth_forecast_craniotomy.png)

## Exponential Smoothing Predictions for hip fracture

Predictions for the next 2 years: [1.4013451045423253, 1.29614583176129]

![Exponential Smoothing Forecast for hip fracture](./plots/time-series/exp_smooth_forecast_hip fracture.png)

## Exponential Smoothing Predictions for ami

Predictions for the next 2 years: [4.445886302526294, 4.599876156046165]

![Exponential Smoothing Forecast for ami](./plots/time-series/exp_smooth_forecast_ami.png)

## Exponential Smoothing Predictions for acute stroke

Predictions for the next 2 years: [7.231710232637744, 6.946980982467859]

![Exponential Smoothing Forecast for acute stroke](./plots/time-series/exp_smooth_forecast_acute stroke.png)

## Exponential Smoothing Predictions for 30-day readmission (ischemic stroke)

Predictions for the next 2 years: [10.951573991360815, 10.823433361348737]

![Exponential Smoothing Forecast for 30-day readmission (ischemic stroke)](./plots/time-series/exp_smooth_forecast_30-day readmission (ischemic stroke).png)

## Exponential Smoothing Predictions for 30-day mortality (ischemic stroke)

Predictions for the next 2 years: [9.765271458075805, 9.571516856248344]

![Exponential Smoothing Forecast for 30-day mortality (ischemic stroke)](./plots/time-series/exp_smooth_forecast_30-day mortality (ischemic stroke).png)

## Exponential Smoothing Predictions for pancreatic cancer

Predictions for the next 2 years: [0.5819306537202552, 0.11457189330831147]

![Exponential Smoothing Forecast for pancreatic cancer](./plots/time-series/exp_smooth_forecast_pancreatic cancer.png)

## Exponential Smoothing Predictions for pancreatic other

Predictions for the next 2 years: [0.4009091838805826, 0.12003499935575139]

![Exponential Smoothing Forecast for pancreatic other](./plots/time-series/exp_smooth_forecast_pancreatic other.png)

## Exponential Smoothing Predictions for acute stroke subarachnoid

Predictions for the next 2 years: [9.429249227229581, 9.481869853107954]

![Exponential Smoothing Forecast for acute stroke subarachnoid](./plots/time-series/exp_smooth_forecast_acute stroke subarachnoid.png)

![Cross Validation Forecast for acute stroke subarachnoid](./plots/time-series/cross_validation_forecast_acute stroke subarachnoid.png)

![Cross Validation Forecast for acute stroke subarachnoid](./plots/time-series/cross_validation_forecast_acute stroke subarachnoid.png)

![Cross Validation Forecast for acute stroke subarachnoid](./plots/time-series/cross_validation_forecast_acute stroke subarachnoid.png)

![Cross Validation Forecast for acute stroke subarachnoid](./plots/time-series/cross_validation_forecast_acute stroke subarachnoid.png)

![Cross Validation Forecast for acute stroke subarachnoid](./plots/time-series/cross_validation_forecast_acute stroke subarachnoid.png)

## Exponential Smoothing Predictions for acute stroke ischemic

Predictions for the next 2 years: [4.003885012510752, 3.9481384189791395]

![Exponential Smoothing Forecast for acute stroke ischemic](./plots/time-series/exp_smooth_forecast_acute stroke ischemic.png)

![Cross Validation Forecast for acute stroke ischemic](./plots/time-series/cross_validation_forecast_acute stroke ischemic.png)

![Cross Validation Forecast for acute stroke ischemic](./plots/time-series/cross_validation_forecast_acute stroke ischemic.png)

![Cross Validation Forecast for acute stroke ischemic](./plots/time-series/cross_validation_forecast_acute stroke ischemic.png)

![Cross Validation Forecast for acute stroke ischemic](./plots/time-series/cross_validation_forecast_acute stroke ischemic.png)

![Cross Validation Forecast for acute stroke ischemic](./plots/time-series/cross_validation_forecast_acute stroke ischemic.png)

## Exponential Smoothing Predictions for acute stroke hemorrhagic

Predictions for the next 2 years: [12.12347783328433, 12.324098619371382]

![Exponential Smoothing Forecast for acute stroke hemorrhagic](./plots/time-series/exp_smooth_forecast_acute stroke hemorrhagic.png)

![Cross Validation Forecast for acute stroke hemorrhagic](./plots/time-series/cross_validation_forecast_acute stroke hemorrhagic.png)

![Cross Validation Forecast for acute stroke hemorrhagic](./plots/time-series/cross_validation_forecast_acute stroke hemorrhagic.png)

![Cross Validation Forecast for acute stroke hemorrhagic](./plots/time-series/cross_validation_forecast_acute stroke hemorrhagic.png)

![Cross Validation Forecast for acute stroke hemorrhagic](./plots/time-series/cross_validation_forecast_acute stroke hemorrhagic.png)

![Cross Validation Forecast for acute stroke hemorrhagic](./plots/time-series/cross_validation_forecast_acute stroke hemorrhagic.png)

## Exponential Smoothing Predictions for cabg operative mortality

Predictions for the next 2 years: [3.140299984032837, 3.361262664348765]

![Exponential Smoothing Forecast for cabg operative mortality](./plots/time-series/exp_smooth_forecast_cabg operative mortality.png)

## Exponential Smoothing Predictions for isolated cabg operative mortality

Predictions for the next 2 years: [2.4597910708336532, 2.8282619652682914]

![Exponential Smoothing Forecast for isolated cabg operative mortality](./plots/time-series/exp_smooth_forecast_isolated cabg operative mortality.png)

## Exponential Smoothing Predictions for elective pci stroke

Predictions for the next 2 years: [0.12755252983607393, 0.14820085132605337]

![Exponential Smoothing Forecast for elective pci stroke](./plots/time-series/exp_smooth_forecast_elective pci stroke.png)

## Exponential Smoothing Predictions for elective pci mortality

Predictions for the next 2 years: [0.050184564699646134, 0.36924130940077093]

![Exponential Smoothing Forecast for elective pci mortality](./plots/time-series/exp_smooth_forecast_elective pci mortality.png)

## Exponential Smoothing Predictions for isolated cabg 30-day readmission

Predictions for the next 2 years: [20.737399804971435, 17.181461456500475]

![Exponential Smoothing Forecast for isolated cabg 30-day readmission](./plots/time-series/exp_smooth_forecast_isolated cabg 30-day readmission.png)

## Exponential Smoothing Predictions for elective surgeries

Predictions for the next 2 years: [0.5263722558193977, 0.5154551648106618]

![Exponential Smoothing Forecast for elective surgeries](./plots/time-series/exp_smooth_forecast_elective surgeries.png)

## XGBoost Model Performance

- Test MSE: 11.92
- Test RMSE (Cross-Validation): 3.91
- Test R²: 0.74
- Test MAE: 0.93

### XGBoost Feature Importance

![Feature Importance](./plots/xgboost/xgboost_feature_importance.png)

### Residual Plot

![Residual Plot](./plots/xgboost/xgboost_residual_plot.png)

### Predicted vs Actual Values

![Predicted vs Actual Values](./plots/xgboost/xgboost_predicted_vs_actual.png)

### SHAP Summary Plot

![SHAP Summary Plot](./plots/xgboost/xgboost_shap_summary.png)

