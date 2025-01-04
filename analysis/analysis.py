# --- Importing Libraries ---

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os
import warnings
import random
from matplotlib import cm
from matplotlib.colors import to_hex
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from statsmodels.tools.tools import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.stats import f_oneway, chi2_contingency

# --- Global Settings ---
plt.rcParams['font.family'] = 'Helvetica' # Set font to Helvetica

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Glyph.*missing")
warnings.filterwarnings("ignore", category=UserWarning, message=".*The palette list has more values.*")

# Set Seaborn style to 'ticks'
sns.set(style="ticks")

# Define color map
viridis = plt.cm.viridis(np.linspace(0, 1, 10))

def generate_viridis_colors(num_colors):
    return [to_hex(cm.viridis(i / num_colors)) for i in range(num_colors)]

# --- Directory Setup ---
# Function to create necessary directories
def create_directories(directories):
    for dir in directories:
        os.makedirs(dir, exist_ok=True) # No error if directory exists

directories = [
    './plots/trends/', './plots/boxplots/', './plots/correlation/', './plots/distributions/', './plots/counties/', 
    './plots/performance/', './plots/pca/', './plots/hospitals/', './plots/barplots/', './plots/vif/', 
    './plots/clusters/', './plots/chi-square/', './tables/chi-square/'
]
create_directories(directories)

# --- 1. Loading the Dataset ---
df = pd.read_csv('combined_2011-2022_ca_hospital_ratings.csv')

# Remove rows corresponding to years 2005-2008 (all performance_measure values are 0)
df = df[~df['year'].isin([2005, 2006, 2007, 2008])]

# Convert the 'year' column to datetime format
df['year'] = pd.to_datetime(df['year'], format='%Y')

# Prepare markdown file
eda_file = "eda_results.md"
with open(eda_file, "w") as file:
    file.write("# Exploratory Data Analysis\n\n")

# --- 2. Exploratory Data Analysis (EDA) ---

# Get the number of rows and columns in the dataset
num_rows, num_columns = df.shape

# Add this information to the markdown file along with outliers
with open(eda_file, "a") as file:
    file.write("## Dataset Overview\n\n")
    file.write(f"Number of rows: {num_rows}\n")
    file.write(f"Number of columns: {num_columns}\n\n")
    
# 2.1 Summary Statistics
# Function to write summary statistics for selected numeric and categorical columns
def write_summary_stats(df, columns, file, categorical_columns=None):
    """
    Write summary statistics for selected columns (numeric and categorical).
    """

    # Calculate descriptive statistics for numeric columns
    numeric_summary = df[columns].describe()
    file.write("## Numeric Summary Statistics\n\n")
    file.write(numeric_summary.to_markdown() + "\n\n")
    
    # Calculate summary statistics for categorical columns
    if categorical_columns:
        categorical_summary = df[categorical_columns].describe()
        file.write("## Categorical Summary Statistics\n\n")
        file.write(categorical_summary.to_markdown() + "\n\n")

# Add summary statistics to markdown file
with open(eda_file, "a") as file:
    write_summary_stats(df, ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate'], file, 
                        categorical_columns=['county', 'hospital', 'hospital_rating'])

# Function to calculate additional statistics
def write_additional_stats(df, columns, file):
    """
    Write additional summary statistics (median, variance, skewness, kurtosis).
    """
    additional_stats = df[columns].agg(['median', 'var', 'skew', 'kurt'])
    file.write("## Additional Summary Statistics\n\n")
    file.write(additional_stats.to_markdown() + "\n\n")

# Add additional statistics to markdown file
with open(eda_file, "a") as file:
    write_additional_stats(df, ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate'], file)

# 2.2 Grouped Summary by County
# Function to calculate grouped summary statistics for selected columns
def write_grouped_summary(df, group_by_col, columns, file):
    """
    Write grouped summary statistics.
    """
    grouped_summary = df.groupby(group_by_col)[columns].mean()
    file.write("## Grouped Summary by County\n\n")
    file.write(grouped_summary.to_markdown() + "\n\n")

# Add grouped summary statistics to markdown file
with open(eda_file, "a") as file:
    write_grouped_summary(df, 'county', ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate'], file)

# 2.3 Function to detect outliers using Interquartile Range method
def detect_outliers(df, columns):
    """
    Detect outliers using IQR method.
    """
    Q1 = df[columns].quantile(0.25)
    Q3 = df[columns].quantile(0.75)
    IQR = Q3 - Q1
    return df[((df[columns] < (Q1 - 1.5 * IQR)) | (df[columns] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Detect outliers in the specified columns
outliers = detect_outliers(df, ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate'])

# Subset of outliers (You can modify this to limit how many are written)
outliers_subset = outliers.head(10)  # Example: Take the first 10 outliers

# Count of outliers
num_outliers = outliers.shape[0]

# Add outlier detection results to markdown file
with open(eda_file, "a") as file:
    file.write("## Outlier Detection\n\n")
    file.write(f"Total number of outliers detected: {num_outliers}\n\n")
    file.write(outliers_subset.to_markdown() + "\n\n")

# --- 3. Visualizations ---
# 3.1 Trends in Performance Measures Over Time
def plot_trends(data, x, y, hue, titles, y_labels, save_paths, markdown_file):
    """
    Generate line plots for trends over time with unique viridis colors.
    """
    num_plots = len(y) # Number of metrics to plot
    viridis_colors = generate_viridis_colors(num_plots) # Generate list of colors from the viridis colormap

    # Create a subplot for each metric to be plotted
    fig, axes = plt.subplots(num_plots, 1, figsize=(12, 4 * num_plots))
    
    # for loop iterates through each performance metric 
    for i, metric in enumerate(y):
        sns.lineplot(data=data, x=x, y=metric, hue=hue, palette=[viridis_colors[i]] * len(data[hue].unique()), ax=axes[i], 
                     legend=False)
        
        # Set the title, x and y labels for each plot
        axes[i].set_title(titles[i])
        axes[i].set_xlabel(x.capitalize())
        axes[i].set_ylabel(y_labels[i])

    plt.tight_layout()
    plt.savefig(save_paths)
    plt.close()

    # Add plot to markdown file
    with open(markdown_file, "a") as file:
        file.write(f"## Trends Over Time\n")
        file.write(f"![Trends Over Time]({save_paths})\n\n")

# Define metrics, titles and labels for trend plots
trend_metrics = ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate']
trend_titles = [
    'Trends in Number of Cases Over Time',
    'Trends in Adverse Events Over Time',
    'Trends in Risk-Adjusted Rate Over Time'
]
trend_ylabels = ['# of Cases', '# of Adverse Events', 'Risk-Adjusted Rate']
trend_save_path = './plots/trends/trend_over_time.png'

# Call function to plot trends
plot_trends(df, 'year', trend_metrics, 'county', trend_titles, trend_ylabels, trend_save_path, eda_file)

# 3.2 Boxplots for Performance Metrics Across Counties
def save_boxplot(data, x, y, title, xlabel, ylabel, save_path, markdown_file):
    """
    Save a boxplot visualization for a given metric with unique viridis colors for each county.
    """
    counties = data[x].unique() # Get unique counties
    num_counties = len(counties) # Number of unique counties
    
    # Generate unique color for each county using viridis colormap
    county_colors = generate_viridis_colors(num_counties)
    color_map = dict(zip(counties, county_colors)) # Map counties to respective colors

    plt.figure(figsize=(12, 8))
    sns.boxplot(data=data, x=x, y=y, hue=x, palette=color_map)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    # Add plot to markdow file
    with open(markdown_file, "a") as file:
        file.write(f"## {title}\n")
        file.write(f"![{title}]({save_path})\n\n")

# Define boxplot metrics and settings
boxplot_metrics = [
    ('#_of_cases', 'Distribution of # of Cases Across Counties', 'County', '# of Cases', 
        './plots/boxplots/cases_by_county.png'),
    ('#_of_adverse_events', 'Distribution of Adverse Events Across Counties', 'County', '# of Adverse Events', 
        './plots/boxplots/adverse_events_by_county.png'),
    ('risk_adjusted_rate', 'Distribution of Risk Adjusted Rate Across Counties', 'County', 'Risk Adjusted Rate', 
        './plots/boxplots/risk_adjusted_rate_by_county.png')
]

# Generate and save boxplots for each metric
for metric, title, xlabel, ylabel, path in boxplot_metrics:
    save_boxplot(df, 'county', metric, title, xlabel, ylabel, path, eda_file)

# 3.3 Correlation Matrix Heatmap
def plot_correlation_matrix(data, cols, save_path, markdown_file):
    """
    Plot and save a heatmap of the correlation matrix.
    """
    corr_matrix = data[cols].corr() # Create correlation matrix for specified columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt='.2f', linewidths=0.5, 
                cbar_kws={'label': 'Correlation Coefficient'})
    plt.title('Correlation Matrix of Performance Measures')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    # Add plot to markdown file
    with open(markdown_file, "a") as file:
        file.write("## Correlation Matrix\n")
        file.write(f"![Correlation Matrix]({save_path})\n\n")

# Define the columns for the correlation matrix
correlation_cols = ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate']
correlation_save_path = './plots/correlation/correlation_matrix.png'

# Generate correlation matric heatmap
plot_correlation_matrix(df, correlation_cols, correlation_save_path, eda_file)

# 3.4 Distributions of Key Variables
def plot_distributions(data, metrics, dist_metrics, transformed_metrics, dist_titles, save_path, markdown_file):
    """
    Plot histograms for multiple metrics.
    """
    # Generate color for each metric using the viridis colormap
    viridis_colors = [to_hex(cm.viridis(i / len(metrics))) for i in range(len(metrics))]

    # Create subplots for all metrics
    fig, axes = plt.subplots(len(metrics), 1, figsize=(12, 4 * len(metrics)))

    # Plot hisograms for each metric
    for i, metric in enumerate(metrics):
        sns.histplot(data[metric], kde=True, bins=30, color=viridis_colors[i], ax=axes[i])
        axes[i].set_title(dist_titles[i], fontsize=14)
        axes[i].set_xlabel(metric.replace('_', ' ').capitalize(), fontsize=12)
        axes[i].set_ylabel('Frequency', fontsize=12)

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    # Add plot to markdown file
    with open(markdown_file, "a") as file:
        file.write("## Distributions of Key Variables\n")
        file.write(f"![Distributions of Key Variables]({save_path})\n\n")

# Add log-transformed columns to handle skewness and zero values
df['log_cases'] = np.log1p(df['#_of_cases'])  # Use log1p to handle zero values
df['log_adverse_events'] = np.log1p(df['#_of_adverse_events'])
df['log_risk_adjusted_rate'] = np.log1p(df['risk_adjusted_rate'])

# Metrics to visualize
dist_metrics = ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate']
transformed_metrics = ['log_cases', 'log_adverse_events', 'log_risk_adjusted_rate']
metrics = dist_metrics + transformed_metrics

# Titles for plots
dist_titles = ['Distribution of # of Cases', 'Distribution of Adverse Events', 'Distribution of Risk-Adjusted Rate', 
               'Log-Transformed Distribution of # of Cases', 'Log-Transformed Distribution of Adverse Events', 
               'Log-Transformed Distribution of Risk-Adjusted Rate']

# Save path
distribution_save_path = './plots/distributions/distribution_with_transformed_metrics.png'

# Call function to plot distributions
plot_distributions(df, metrics, dist_metrics, transformed_metrics, dist_titles, distribution_save_path, markdown_file=eda_file)

# 3.5 County-Specific Visualizations
def plot_county_visualizations(data, metric, ylabel, title, markdown_file):
    """
    Generate and save visualizations for each county.
    """
    # Get unique counties and assign a color for each
    unique_counties = data['county'].unique()
    county_colors = {county: to_hex(cm.viridis(i / len(unique_counties))) for i, county in enumerate(unique_counties)}

    # for loop iterates through each county
    for county in unique_counties:
        # Filter data for the specific county
        county_data = data[data['county'] == county]

        # Skip if there is no data for the county
        if county_data.empty:
            continue

        # Create a bar plot for the county
        plt.figure(figsize=(12, 8))
        sns.barplot(data=county_data, x='hospital', y=metric, color=county_colors[county])
        plt.title(f'{title} in {county}')
        plt.xlabel('Hospital')
        plt.ylabel(ylabel)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        save_path = f"./plots/counties/{county}_{metric}.png"
        plt.savefig(save_path)
        plt.close()

        # Add the plot to the markdown file
        with open(markdown_file, "a") as file:
            file.write(f"### {title} in {county}\n")
            file.write(f"![{title} in {county}]({save_path})\n\n")

# Metrics to visualize at the county level
county_metrics = [
    ('#_of_cases', '# of Cases', 'Number of Cases by Hospital'),
    ('#_of_adverse_events', '# of Adverse Events', 'Adverse Events by Hospital'),
    ('risk_adjusted_rate', 'Risk Adjusted Rate', 'Risk Adjusted Rate by Hospital')
]

# Generate visualizations for each county and each metric
for metric, ylabel, title in county_metrics:
    plot_county_visualizations(df, metric, ylabel, title, eda_file)

# 3.6 Performance Measure Visualization
def sanitize_filename(name):
    """
    Sanitize file or directory names by replacing problematic characters.
    """
    return name.replace('acc puncture', 'acc_puncture').replace('/', '_')

def plot_performance_measure_vs_metrics(df, metrics, title, palette, markdown_file=None):
    """
    Plot performance measures against metrics using boxplots, save the plots, 
    and optionally document them in a markdown file.
    """
    # Get unique performance measures and assign colors to each
    performance_measures = df['performance_measure'].unique()
    measure_colors = {measure: to_hex(cm.viridis(i / len(performance_measures))) 
                      for i, measure in enumerate(performance_measures)}

    # Generate a boxplot for each performance measure
    for performance_measure in performance_measures:
        sanitized_measure = sanitize_filename(performance_measure) # Clean up file name
        performance_data = df[df['performance_measure'] == performance_measure] # Filter data

        # Reshape data for visualization
        data_melted = performance_data.melt(id_vars=['performance_measure'], value_vars=metrics, var_name='metric', 
                                            value_name='value')

        # Use the assigned color for the current performance measure
        current_palette = [measure_colors[performance_measure]]

        # Plot the boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=data_melted, x='metric', y='value', hue='performance_measure', palette=current_palette)
        plt.title(f'{title} for {performance_measure}', fontsize=16)
        plt.xlabel('Metric', fontsize=14)
        plt.ylabel('Value', fontsize=14)
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.tight_layout()
        plot_filename = f"./plots/performance/{sanitized_measure}_performance_vs_metrics.png"
        plt.savefig(plot_filename, dpi=300)
        plt.close()

        # Add the plot to the markdown file
        if markdown_file:
            with open(markdown_file, "a") as file:
                file.write(f"### {title} for {performance_measure}\n")
                file.write(f"![{title} for {performance_measure}]({plot_filename})\n\n")

# Metrics to visualize
metrics = ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate']

# Call the function to generate the plots
plot_performance_measure_vs_metrics(df, metrics, 'Performance Measure', palette="viridis", markdown_file=eda_file)

# 3.7 County Specific Hospital Metrics
def plot_county_hospital_metrics(data, metrics, metric_labels, title, markdown_file):
    """
    Generate and save subplots of multiple performance metrics for each county.
    Excludes rows with all metric values as 0.
    """
    # Get the list of unique counties
    unique_counties = data['county'].unique()

    # Assign colors for the metrics using the viridis colormap
    viridis_colors = [to_hex(cm.viridis(i / 3)) for i in range(3)] 

    metric_colors = {
        metrics[0]: viridis_colors[0],
        metrics[1]: viridis_colors[1], 
        metrics[2]: viridis_colors[2] 
    }

    # for loop iterates through each county
    for county in unique_counties:
        # Filter data for current county
        county_data = data[data['county'] == county]

        # Exclude rows where all metrics are zero
        county_data = county_data.loc[(county_data[metrics] > 0).any(axis=1)]
        if county_data.empty:
            continue

        # Determine the number of hospitals and layout for subplots
        num_hospitals = len(county_data['hospital'].unique())
        num_columns = 2  # Number of columns in subplot
        num_rows = 2 # Number of rows in subplot

        # Divide hospitals into chunks of 4 for visualization
        hospital_chunks = [county_data['hospital'].unique()[i:i+4] for i in range(0, num_hospitals, 4)]

        # Plot each chunk of hospitals
        for chunk_idx, chunk in enumerate(hospital_chunks): 
            num_hospitals_in_chunk = len(chunk)
            num_rows = (num_hospitals_in_chunk // num_columns) + (num_hospitals_in_chunk % num_columns > 0)

            plt.figure(figsize=(15, 5 * num_rows))
            plt.suptitle(f'{title} in {county} - Chunk {chunk_idx + 1}', fontsize=10, y=0.9)

            # Assign colors for each hospital
            hospital_colors = {hospital: to_hex(cm.tab20c(i / num_hospitals)) for i, hospital in enumerate(chunk)}

            valid_hospitals = []  # Track hospitals with non-zero metrics
            
            # for loop creates subplot for each hospital
            for i, hospital in enumerate(chunk):
                hospital_data = county_data[county_data['hospital'] == hospital]

                # Skip hospitals with all-zero metrics
                if (hospital_data[metrics].sum().sum() == 0):
                    continue

                valid_hospitals.append(hospital) # Track valid hospitals

                ax = plt.subplot(num_rows, num_columns, len(valid_hospitals))

                # Reshape data for plotting
                plot_data = hospital_data.melt(id_vars=['performance_measure'], value_vars=metrics, var_name='Metric', 
                                               value_name='Value')
                plot_data['Color'] = plot_data['Metric'].map(metric_colors)

                # Plot the data
                sns.barplot(data=plot_data, x='performance_measure', y='Value', hue='Metric', palette=metric_colors, ax=ax)
                ax.set_title(f'{hospital}')
                ax.set_xlabel('Performance Measure')
                ax.set_ylabel('Value')
                ax.set_xticks(range(len(hospital_data['performance_measure'].unique())))
                ax.set_xticklabels(hospital_data['performance_measure'].unique(), rotation=45, ha='right', fontsize=8)
                ax.legend(loc='upper right', fontsize='small')

            if not valid_hospitals:
                continue

            plt.tight_layout()
            save_path = f"./plots/hospitals/{county}_hospital_metrics_chunk_{chunk_idx + 1}.png"
            plt.savefig(save_path)
            plt.close()

            # Add the plot to the markdown files
            with open(markdown_file, "a") as file:
                file.write(f"### {title} in {county} - Chunk {chunk_idx + 1}\n")
                file.write(f"![{title} in {county} - Chunk {chunk_idx + 1}]({save_path})\n\n")

# Metrics and labels
metrics = ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate']
metric_labels = ['# of Cases', '# of Adverse Events', 'Risk Adjusted Rate']

# Call the function to generate plots
plot_county_hospital_metrics(data=df, metrics=metrics, metric_labels=metric_labels, 
                             title="Hospital Performance Metrics by County", markdown_file=eda_file)

# 3.8 Average risk-adjusted rate by county
# Calculate the average risk adjusted rate for each county and sort the values
random_color = to_hex(cm.viridis(random.uniform(0, 1)))
avg_performance_by_county = df.groupby('county')['risk_adjusted_rate'].mean().sort_values()

# Plot the average risk adjusted rate as a bar chart
fig, ax = plt.subplots(figsize=(12, 8))
avg_performance_by_county.plot(kind='bar', ax=ax, color=random_color)
ax.set_title('Average Risk Adjusted Rate by County', fontsize=16)
ax.set_xlabel('County', fontsize=14)
ax.set_ylabel('Average Risk Adjusted Rate', fontsize=14)
ax.grid(axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
avg_performance_bar_path = './plots/barplots/avg_performance_by_county.png'
plt.savefig(avg_performance_bar_path)
plt.close()

# Add the bar chart to the markdown file
with open(eda_file, "a") as file:
    file.write("## Average Risk Adjusted Rate by County\n")
    file.write(f"![Average Risk Adjusted Rate by County]({avg_performance_bar_path})\n\n")

# --- 4. Multicollinearity Check using VIF ---
# Function to calculate the Variance Inflation Factor for features
def check_vif(X):
    X_with_const = add_constant(X)  # Add constant term for VIF calculation
    vif_data = pd.DataFrame({
        'Feature': X_with_const.columns,
        'VIF': [variance_inflation_factor(X_with_const.values, i) for i in range(X_with_const.shape[1])]
    })
    vif_data['VIF'] = vif_data['VIF'].round(2) # Round VIF values to 2 decimal points
    return vif_data

# Compute the VIF for the feature matrix
vif_data = check_vif(X)

# Add VIF results to markdown file
with open(eda_file, "a") as file:
    file.write("## Variance Inflation Factor (VIF) Check\n\n")
    file.write("- **Thresholds**: VIF > 5 suggests high multicollinearity, while VIF > 10 indicates severe multicollinearity.\n\n")
    file.write(vif_data.to_markdown(index=False) + "\n\n")

# Visualize VIF as barplot
plt.figure(figsize=(8, 6))
sns.barplot(x='VIF', y='Feature', data=vif_data, hue='Feature', palette="viridis", legend=False)
plt.title('Variance Inflation Factor (VIF) by Feature')
plt.xlabel('VIF')
plt.ylabel('Feature')
vif_plot_path = './plots/vif/vif_plot.png'
plt.tight_layout()
plt.savefig(vif_plot_path)
plt.close()

# Add VIF plot to markdown files
with open(eda_file, "a") as file:
    file.write(f"![VIF Bar Plot]({vif_plot_path})\n\n")

# --- 5. PCA Analysis ---
# Normalize to have zero mean and unit variance
features = ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate']
X_normalized = StandardScaler().fit_transform(df[features])

# Apply Principal Component Analysis to reduce dimensionality
pca = PCA(n_components=2) # Retain top 2 principal components
principal_components = pca.fit_transform(X_normalized)
df['PCA1'], df['PCA2'] = principal_components[:, 0], principal_components[:, 1]

# Create scatterplot of PCA results
plt.figure(figsize=(12, 8))
sns.scatterplot(x='PCA1', y='PCA2', hue='county', data=df, palette='viridis', s=120, alpha=0.7)
plt.title('PCA of Performance Measures by County', fontsize=18)
plt.xlabel('PCA1', fontsize=14)
plt.ylabel('PCA2', fontsize=14)
plt.legend(title='County', bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=6, title_fontsize=8, markerscale=0.7)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()
pca_analysis_path = './plots/pca/pca_analysis.png'
plt.savefig(pca_analysis_path)
plt.close()

# Add plot to markdown file
with open(eda_file, "a") as file:
    file.write("## PCA\n")
    file.write(f"![PCA]({pca_analysis_path})\n\n")

# --- 6. Clustering Analysis ---
# Standardize the features to have zero mean and unit variance for clustering
scaler = StandardScaler()
features_scaled = scaler.fit_transform(df[features]) 

# Perform K-means clustering to group hospitals based on performance metrics
kmeans_performance = KMeans(n_clusters=3, random_state=42)
df['Cluster_Performance'] = kmeans_performance.fit_predict(features_scaled)

# Calulate the silhouette score to evaluate the quality of clustering
silhouette_avg_performance = silhouette_score(features_scaled, df['Cluster_Performance'])

# Add results to markdown file
with open(eda_file, "a") as file:
    file.write("## Silhouette Score for Clustering (Performance Metrics)\n\n")
    file.write(f"{silhouette_avg_performance:.2f}\n\n")

# Identify numeric columns and exclude specific columns
numeric_columns = df.select_dtypes(include=['float64']).columns
columns_to_exclude = ['hospital', 'county', 'year', 'oshpd_id', 'Cluster_Performance']
df_excluded = df.drop(columns=columns_to_exclude)

# Perform clustering for numeric features
kmeans = KMeans(n_clusters=3, random_state=42) 
df_excluded['Cluster_Performance'] = kmeans.fit_predict(df_excluded[numeric_columns])

# Calculate the mean for each cluster
cluster_means_performance = df_excluded.groupby('Cluster_Performance')[numeric_columns].mean().round(2)

# Aggregate non numeric data
cluster_means_non_numeric = df_excluded.groupby('Cluster_Performance').agg({
    'performance_measure': lambda x: x.mode()[0],
    'hospital_rating': lambda x: x.mode()[0] 
}).round(2)

# Combine numeric and non numeric cluster means
cluster_means_performance_combined = pd.concat([cluster_means_performance, cluster_means_non_numeric], axis=1)

# Add cluster means to markdown file
with open(eda_file, "a") as file:
    file.write("## Cluster Means (Performance Metrics)\n\n")
    file.write(cluster_means_performance_combined.to_markdown() + "\n\n")

# Count the number of hospitals in each cluster
cluster_sizes_performance = df['Cluster_Performance'].value_counts()

# Add cluster sizes to markdown file
with open(eda_file, "a") as file:
    file.write("## Cluster Sizes (Performance Metrics)\n\n")
    file.write(cluster_sizes_performance.to_markdown() + "\n\n")

# Create a scatter plot to visualze the clusters
plt.figure(figsize=(12, 8))
sns.scatterplot(x=features_scaled[:, 0], y=features_scaled[:, 1], hue=df['Cluster_Performance'], palette='viridis', s=100, 
                alpha=0.8)
plt.title("Hospital Clustering by Performance Metrics", fontsize=16)
plt.xlabel("Feature 1 (scaled)", fontsize=14)  
plt.ylabel("Feature 2 (scaled)", fontsize=14) 
plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc='upper left') 
plt.grid(True, linestyle='--', linewidth=0.5) 
plt.tight_layout() 
clustering_analysis_path = './plots/clusters/cluster_analysis.png'
plt.savefig(clustering_analysis_path) 
plt.close() 

# Add clustering plot to markdown file
with open(eda_file, "a") as file:
    file.write("## Hospital Clustering by Performance Metrics\n")
    file.write(f"![Hospital Clustering by Performance Metrics]({clustering_analysis_path})\n\n")

# Perform K-means clustering on numeric columns
X = df[['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate']]
kmeans_cases = KMeans(n_clusters=3, random_state=42)
df['Cluster_Cases'] = kmeans_cases.fit_predict(X)

# Extract cluster centers and calculate cluster sizes
cluster_centers_cases = pd.DataFrame(kmeans_cases.cluster_centers_, columns=X.columns)
cluster_counts_cases = df['Cluster_Cases'].value_counts().sort_index()

# Add results to markdown file
with open(eda_file, "a") as file:
    file.write("## K-means Clustering of Cases vs Adverse Events\n\n")
    file.write("- **Cluster Statistics:**\n")
    file.write(cluster_centers_cases.to_markdown(index=False) + "\n\n")
    file.write("- **Cluster Sizes:**\n")
    file.write(cluster_counts_cases.to_markdown() + "\n\n")

# --- 8. ANOVA Test: Group Data by County and Perform ANOVA ---
# Function to perform one-way ANOVA
def perform_anova(df):
    """
    Perform one-way ANOVA across all counties for 'risk_adjusted_rate'.
    """
    grouped_data = df.groupby('county')['risk_adjusted_rate']
    
    # Filter groups to ensure valid input
    valid_groups = {county: data.dropna() for county, data in grouped_data if len(data) > 1}

    # Perform ANOVA test across valid groups
    f_stat, p_val = f_oneway(*valid_groups.values())
    return {"F-statistic": round(f_stat, 2), "p-value": round(p_val, 3)}

# Perform ANOVA and get results
anova_results = perform_anova(df)

# Add results to markdown file
with open(eda_file, "a") as file:
    file.write("## Overall ANOVA Results Across Counties\n\n")
    file.write(f"- **F-statistic:** {anova_results['F-statistic']}\n")
    file.write(f"- **p-value:** {anova_results['p-value']}\n\n")
    significance = "Significant" if anova_results['p-value'] < 0.05 else "Not Significant"
    file.write(f"The difference in means across counties is **{significance}**.\n\n")

# --- 9. Chi-Square Test of Independence ---

# Bin 'risk_adjusted_rate' to create risk categories
bins = [0, 33, 66, 99, 132, 165]
labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
df['risk_category'] = pd.cut(df['risk_adjusted_rate'], bins=bins, labels=labels)

# Generate contingency table comparing risk categories and hospital ratings
contingency_table = pd.crosstab(df['risk_category'], df['hospital_rating'])

# Perform Chi-Square test of independence using contingency table
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Add results to markdown file
with open(eda_file, "a") as file:
    file.write("## Chi-Square Test Results\n\n")
    file.write(f"- Chi2 Statistic: {chi2:.2f}\n")
    file.write(f"- Degrees of Freedom: {dof}\n")
    file.write(f"- p-value: {p:.2e}\n\n")

# Save contingency table
contingency_table_path = "./tables/chi-square/chi_square_contingency_table.csv"
contingency_table.to_csv(contingency_table_path)

# Add
with open(eda_file, "a") as file:
    file.write("### Contingency Table\n\n")
    file.write(f"Contingency Table ({contingency_table_path}).\n\n")

# Create heatmap of contingency table
plt.figure(figsize=(10, 6))
sns.heatmap(contingency_table, annot=True, fmt='d', cmap='viridis')
plt.title('Contingency Table Heatmap')
plt.xlabel('Hospital Rating')
plt.ylabel('Risk Category')
heatmap_path = "./plots/chi-square/chi_square_heatmap.png"
plt.savefig(heatmap_path)
plt.close()

# Save heatmap to file
with open(eda_file, "a") as file:
    file.write("### Contingency Table Heatmap\n\n")
    file.write(f"![Contingency Table Heatmap]({heatmap_path})\n\n")

# Interpret results
interpretation = ""
if p < 0.05:
    interpretation = (
        "The Chi-Square test shows a statistically significant association "
        "between risk categories and hospital ratings (p < 0.05)."
    )
else:
    interpretation = (
        "The Chi-Square test does not show a statistically significant association "
        "between risk categories and hospital ratings (p >= 0.05)."
    )

# Save interpretations to file
with open(eda_file, "a") as file:
    file.write("### Interpretation\n\n")
    file.write(f"{interpretation}\n\n")
