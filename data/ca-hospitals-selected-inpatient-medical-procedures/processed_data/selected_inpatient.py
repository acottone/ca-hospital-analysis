import pandas as pd

# Load the datasets
data1 = pd.read_csv('number-of-selected-inpatient-medical-procedures-in-california-hospitals-2005-2015-.csv', encoding='ISO-8859-1')
data2 = pd.read_csv('number-of-selected-inpatient-medical-procedures-in-california-hospitals-2016-2017-.csv', encoding='ISO-8859-1')

# Clean the 'hospital', 'county', and 'procedure' columns by stripping beginning/end spaces, converting to lowercase, 
# and replacing multiple spaces with single space
data1['Hospital Name'] = data1['Hospital Name'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['HOSPITAL'] = data2['HOSPITAL'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['County'] = data1['County'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['COUNTY'] = data2['COUNTY'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['Procedure'] = data1['Procedure'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Procedure'] = data2['Procedure'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

# Rename the 'hospital', 'oshpd_id', 'county', 'procedure', and 'volume' columns for consistency
data1.rename(columns={'Hospital Name': 'hospital', 'OSHPDID': 'oshpd_id', 'County': 'county', 
                      'Procedure': 'performance_measure', 'Volume': '#_of_cases'}, inplace=True)
data2.rename(columns={'HOSPITAL': 'hospital', 'OSHPDID': 'oshpd_id', 'COUNTY': 'county', 
                      'Procedure': 'performance_measure', 'Volume': '#_of_cases'}, inplace=True)

# Clean column names to ensure consistency across both datasets
data1.columns = data1.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
data2.columns = data2.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)

# Convert relevant numeric columns to numeric, coercing errors to NaN
columns_to_convert = ['#_of_cases']
for col in columns_to_convert:
    if col in data1.columns:
        data1[col] = pd.to_numeric(data1[col], errors='coerce')
    if col in data2.columns:
        data2[col] = pd.to_numeric(data2[col], errors='coerce')

# Clean 'oshpd_id' column: remove ".0" if it exists
data1['oshpd_id'] = data1['oshpd_id'].astype(str).str.rstrip('.0').str.strip()
data2['oshpd_id'] = data2['oshpd_id'].astype(str).str.rstrip('.0').str.strip()

# Remove latitude, longitude, and location columns
columns_to_remove = ['latitude', 'longitude', 'location']
data1.drop(columns=[col for col in columns_to_remove if col in data1.columns], inplace=True)
data2.drop(columns=[col for col in columns_to_remove if col in data2.columns], inplace=True)

# Ensure there is only one 'year' column: columns named 'ï»¿year' caused by encoding issues are renamed to 'year'
if 'ï»¿year' in data1.columns:
    data1.rename(columns={'ï»¿year': 'year'}, inplace=True)
if 'ï»¿year' in data2.columns:
    data2.rename(columns={'ï»¿year': 'year'}, inplace=True)

# Drop duplicate columns
data1 = data1.loc[:, ~data1.columns.duplicated()]
data2 = data2.loc[:, ~data2.columns.duplicated()]

# Combine the two datasets
combined_data = pd.concat([data1, data2], ignore_index=True)

# Create a mapping of 'oshpd_id' to the first hospital name encountered for each 'oshpd_id' for consistency
hospital_mapping = (combined_data.groupby('oshpd_id')['hospital'].first().to_dict())
combined_data['hospital'] = combined_data['oshpd_id'].map(hospital_mapping)

# Sort the combined dataset by 'county', 'hospital', and 'year' and reset index
combined_data = combined_data.sort_values(by=['county', 'hospital', 'year']).reset_index(drop=True)

# Round the final data for presentation
combined_data = combined_data.round(2)

# Save final data to CSV
combined_data.to_csv('23_2005-2017_combined_ca_hospital_inpatient_medical_procedures_data.csv', index=False)

# Print the first few rows of the combined dataset
print(combined_data.head())

