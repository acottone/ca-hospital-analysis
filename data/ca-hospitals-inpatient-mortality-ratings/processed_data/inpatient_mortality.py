import pandas as pd

# Load the datasets
data1 = pd.read_csv('2010-2015-california-hospital-inpatient-mortality-rates-and-quality-ratings-.csv', encoding='ISO-8859-1')

data2 = pd.read_csv('2016-2022-california-hospital-inpatient-mortality-rates-and-quality-ratings-.csv', encoding='ISO-8859-1')

# Clean the 'hospital', 'county', 'procedure', and 'hospital_rating' columns by stripping beginning/end spaces, converting to 
# lowercase, and replacing multiple spaces with single space
data1['HOSPITAL'] = data1['HOSPITAL'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['HOSPITAL'] = data2['HOSPITAL'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['COUNTY'] = data1['COUNTY'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['COUNTY'] = data2['COUNTY'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['Procedure/Condition'] = data1['Procedure/Condition'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Procedure/Condition'] = data2['Procedure/Condition'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['Hospital Ratings'] = data1['Hospital Ratings'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Hospital Ratings'] = data2['Hospital Ratings'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

# Rename select columns for consistency
data1.rename(columns={'OSHPDID': 'oshpd_id', 'Risk Adjuested Mortality Rate': 'risk_adjusted_rate', 'Procedure/Condition': 'procedure_condition', 'Hospital Ratings': 'hospital_rating'}, inplace=True)
data2.rename(columns={'OSHPDID': 'oshpd_id', 'Risk Adjuested Mortality Rate': 'risk_adjusted_rate', 'Procedure/Condition': 'procedure_condition', 'Hospital Ratings': 'hospital_rating'}, inplace=True)

# Clean column names to ensure consistency
data1.columns = data1.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
data2.columns = data2.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)

# Ensure numeric consistency for columns of interest
columns_to_convert = ['risk_adjusted_mortality_rate', '#_of_deaths', '#_of_cases']
for col in columns_to_convert:
    if col in data1.columns:
        data1[col] = pd.to_numeric(data1[col], errors='coerce')
    if col in data2.columns:
        data2[col] = pd.to_numeric(data2[col], errors='coerce')

# Ensure 'oshpd_id' does not end with '.0'
data1['oshpd_id'] = data1['oshpd_id'].astype(str).str.rstrip('.0').str.strip()
data2['oshpd_id'] = data2['oshpd_id'].astype(str).str.rstrip('.0').str.strip()

# Remove unnecessary columns
columns_to_remove = ['latitude', 'longitude']
data1.drop(columns=[col for col in columns_to_remove if col in data1.columns], inplace=True)
data2.drop(columns=[col for col in columns_to_remove if col in data2.columns], inplace=True)

# Ensure there is only one 'year' column
if 'ï»¿year' in data1.columns:
    data1.rename(columns={'ï»¿year': 'year'}, inplace=True)
if 'ï»¿year' in data2.columns:
    data2.rename(columns={'ï»¿year': 'year'}, inplace=True)

# Drop duplicate columns
data1 = data1.loc[:, ~data1.columns.duplicated()]
data2 = data2.loc[:, ~data2.columns.duplicated()]

# Combine the datasets
combined_data = pd.concat([data1, data2], ignore_index=True)

# Create a mapping of 'oshpd_id' to the first hospital name encountered for each 'oshpd_id' for consistency
hospital_mapping = (combined_data.groupby('oshpd_id')['hospital'].first().to_dict())
combined_data['hospital'] = combined_data['oshpd_id'].map(hospital_mapping)

# Sort the combined dataset by 'county', 'hospital', and 'year' and reset index
combined_data = combined_data.sort_values(by=['county', 'hospital', 'year']).reset_index(drop=True)

# Save the combined data to a CSV file
combined_data.to_csv('2_2010-2022_combined_ca_hospital_inpatient_mortality_rates.csv', index=False)

# Print the first few rows of the combined data to verify
print(combined_data.head())
