import pandas as pd

# Load the dataset
data = pd.read_csv('california-hospital-performance-ratings-for-transcatheter-aortic-valve-replacement-procedures.csv', encoding='ISO-8859-1')

# Clean the 'hospital', 'county', 'system', and 'performance_measure' columns by stripping beginning/end spaces, converting to lowercase, 
# and replacing multiple spaces with single space
data['Hospital'] = data['Hospital'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data['County'] = data['County'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data['Hospital System'] = data['Hospital System'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data['Performance Measure'] = data['Performance Measure'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

# Clean column names to ensure consistency across datasets
data.columns = data.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)

# Clean the 'performance_rating' column
data['performance_rating'] = data['performance_rating'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

# Rename select columns for consistency
data.rename(columns={'hospital_id': 'oshpd_id', 'hospital_system': 'system', 
                     'hospital_risk-adjusted_adverse_event_rate_(%,_raaer)': 'risk_adjusted_rate', 'total_hospital_tavr_cases': '#_of_cases', 
                     'hospital_adverse_events': '#_of_adverse_events', 'performance_rating': 'hospital_rating'}, inplace=True)

# Convert relevant numeric columns to numeric, coercing errors to NaN
columns_to_convert = ['total_hospital_tavr_cases', 'hospital_adverse_events', 'hospital_observed_adverse_event_rate_(%)', 'hospital_expected_adverse_event_rate_(%)', 'hospital_risk-adjusted_adverse_event_rate_(%,_raaer)']
for col in columns_to_convert:
    if col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

# Clean 'oshpd_id' column: remove ".0" if it exists
data['oshpd_id'] = data['oshpd_id'].astype(str).str.rstrip('.0').str.strip()

# Remove unnecessary columns
columns_to_remove = ['latitude', 'longitude', 'hospital_upper_95%_ci_for_raaer', 'hospital_lower_95%_ci_for_raaer', 'total_statewide_tavr_cases', 'statewide_adverse_events', 'statewide_observed_adverse_event_rate_(%)', 'hospital_observed_adverse_event_rate_(%)', 'hospital_expected_adverse_event_rate_(%)']
data.drop(columns=[col for col in columns_to_remove if col in data.columns], inplace=True)

# Ensure there is only one 'year' column: column named 'ï»¿year' caused by encoding issues is renamed to 'year'
if 'ï»¿year' in data.columns:
    data.rename(columns={'ï»¿year': 'year'}, inplace=True)

# Drop duplicate columns
data = data.loc[:, ~data.columns.duplicated()]

# Create a mapping of 'oshpd_id' to the first hospital name encountered for each 'oshpd_id' for consistency
hospital_mapping = (data.groupby('oshpd_id')['hospital'].first().to_dict())
data['hospital'] = data['oshpd_id'].map(hospital_mapping)

# Sort the combined dataset by 'county', 'hospital', and 'year' and reset index
data = data.sort_values(by=['county', 'hospital', 'year']).reset_index(drop=True)

# Round the final data for presentation
data = data.round(2)

# Save final data to CSV
data.to_csv('5_2022_processed_ca_hospital_performance_ratings_tavr_data.csv', index=False)

# Print the first few rows of the final data
print(data.head())
