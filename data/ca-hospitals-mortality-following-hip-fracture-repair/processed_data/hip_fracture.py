import pandas as pd

# Load the dataset
data = pd.read_csv('mortality-following-hip-fracture-repair-in-california-hospitals-.csv', encoding='ISO-8859-1')

# Clean the 'hospital', 'county', and 'hospital_rating' columns by stripping beginning/end spaces, converting to 
# lowercase, and replacing multiple spaces with single space
data['Hospital'] = data['Hospital'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data['County'] = data['County'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data['Hospital Ratings'] = data['Hospital Ratings'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

# Rename select columns for consistency
data.rename(columns={'OSHPDID': 'oshpd_id', 'Risk Adjusted Mortality Rate': 'risk_adjusted_rate', 
                     '# of Deaths': '#_of_adverse_events', 'Hospital Ratings': 'hospital_rating'}, inplace=True)

# Clean column names to ensure consistency
data.columns = data.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)

# Convert relevant columns to numeric, coercing errors to NaN
columns_to_convert = ['#_of_cases', '#_of_adverse_events', 'risk_adjusted_rate']
for col in columns_to_convert:
    if col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

# Clean 'oshpd_id' column: remove ".0" if it exists
data['oshpd_id'] = data['oshpd_id'].astype(str).str.rstrip('.0').str.strip()

# Remove unnecessary columns
columns_to_remove = ['location', 'unnamed:_11', 'observed_rate', 'expected_rate']
data.drop(columns=[col for col in columns_to_remove if col in data.columns], inplace=True)

# Ensure there is only one 'year' column
if 'ï»¿year' in data.columns:
    data.rename(columns={'ï»¿year': 'year'}, inplace=True)

# Drop duplicate columns
data = data.loc[:, ~data.columns.duplicated()]

def normalize_year(year):
    if '-' in str(year):
        return str(year).split('-')[0]
    return year

data['year'] = data['year'].apply(normalize_year)

data['year'] = pd.to_numeric(data['year'], errors='coerce')

# Create a mapping of 'oshpd_id' to the first hospital name encountered for each 'oshpd_id' for consistency
hospital_mapping = (data.groupby('oshpd_id')['hospital'].first().to_dict())
data['hospital'] = data['oshpd_id'].map(hospital_mapping)

# Sort the combined dataset by 'county', 'hospital', and 'year' and reset index
data = data.sort_values(by=['county', 'hospital', 'year']).reset_index(drop=True)

# Round the final data for presentation
data = data.round(2)

# Save the final data to CSV
data.to_csv('21_2012-2014_processed_ca_hospital_mortality_following_hip_fracture_repair_data.csv', index=False)

# Print the first few rows of the final data
print(data.head())
