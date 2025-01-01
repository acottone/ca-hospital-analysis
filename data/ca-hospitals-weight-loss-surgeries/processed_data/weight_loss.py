import pandas as pd

# Load the dataset
data = pd.read_csv('number-of-weight-loss-surgeries-performed-in-california-hospitals-.csv', encoding='ISO-8859-1')

# Clean the 'hospital', 'county', and 'surgery' columns by stripping beginning/end spaces, converting to lowercase, 
# and replacing multiple spaces with single space
data['Hospital'] = data['Hospital'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data['County'] = data['County'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data['Surgery'] = data['Surgery'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

# Rename 'OSHPDID' to 'oshpd_id' for consistency
data.rename(columns={'OSHPDID': 'oshpd_id'}, inplace=True)

# Clean column names by stripping beginning/end spaces, converting to lowercase, and replacing spaces with '_'
data.columns = data.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)

# Convert relevant columns to numeric, coercing errors to NaN
columns_to_convert = ['#_of_cases']
for col in columns_to_convert:
    if col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

# Clean 'oshpd_id' column: remove ".0" if it exists
data['oshpd_id'] = data['oshpd_id'].astype(str).str.rstrip('.0').str.strip()

# Remove 'location_1' column
columns_to_remove = ['location_1']
data.drop(columns=[col for col in columns_to_remove if col in data.columns], inplace=True)

# Ensure there is only one 'year' column: column named 'ï»¿year' caused by encoding issues is renamed to 'year'
if 'ï»¿year' in data.columns:
    data.rename(columns={'ï»¿year': 'year'}, inplace=True)

# Drop duplicate columns
data = data.loc[:, ~data.columns.duplicated()]

# Create a mapping of 'oshpd_id' to the first hospital name encountered for each 'oshpd_id' for consistency
hospital_mapping = (data.groupby('oshpd_id')['hospital'].first().to_dict())
data['hospital'] = data['oshpd_id'].map(hospital_mapping)

# Sort data by 'county', 'hospital', and 'year' and reset index
data = data.sort_values(by=['county', 'hospital', 'year']).reset_index(drop=True)

# Round the final data for presentation
data = data.round(2)

# Save final data to CSV
data.to_csv('24_2005-2015_processed_ca_hospital_number_of_weight_loss_surgeries_data.csv', index=False)

# Print the first few rows of the final data
print(data.head())
