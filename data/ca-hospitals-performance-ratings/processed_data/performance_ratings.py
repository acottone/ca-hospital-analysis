import pandas as pd

# Load the datasets
data1 = pd.read_csv('california-hospital-performance-ratings-2016-2021.csv', encoding='ISO-8859-1')
data2 = pd.read_csv('california-hospital-performance-ratings-2017-2022.csv', encoding='ISO-8859-1')

# Clean the 'hospital', 'county', 'system', 'type_of_report', 'performance_measure', and 'hospital_rating' columns by stripping 
# beginning/end spaces, converting to lowercase, and replacing multiple spaces with single space
data1['hospital'] = data1['hospital'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Hospital'] = data2['Hospital'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['County'] = data1['County'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['County'] = data2['County'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['system'] = data1['system'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['system'] = data2['system'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['Type of Report'] = data1['Type of Report'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Type of Report'] = data2['Type of Report'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['Performance Measure'] = data1['Performance Measure'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Performance Measure'] = data2['Performance Measure'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['Hospital Ratings'] = data1['Hospital Ratings'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Hospital Ratings'] = data2['Hospital Ratings'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

# Rename select columns for consistency
data1.rename(columns={'OSHPDID': 'oshpd_id', 'Risk-Adjusted Rate': 'risk_adjusted_rate', 'Hospital Ratings': 'hospital_rating'}, 
             inplace=True)
data2.rename(columns={'OSHPDID': 'oshpd_id', 'Risk-Adjusted Rate': 'risk_adjusted_rate', 'Hospital Ratings': 'hospital_rating'}, 
             inplace=True)

# Clean column names to ensure consistency
data1.columns = data1.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
data2.columns = data2.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)

# Convert relevant columns to numeric, coercing errors to NaN
columns_to_convert = ['risk_adjusted_rate', '#_of_cases', '#_of_adverse_events']
for col in columns_to_convert:
    if col in data1.columns:
        data1[col] = pd.to_numeric(data1[col], errors='coerce')
    if col in data2.columns:
        data2[col] = pd.to_numeric(data2[col], errors='coerce')

# Clean 'oshpd_id' column: remove ".0" if it exists
data1['oshpd_id'] = data1['oshpd_id'].astype(str).str.rstrip('.0').str.strip()
data2['oshpd_id'] = data2['oshpd_id'].astype(str).str.rstrip('.0').str.strip()

# Remove unnecessary columns
columns_to_remove = ['latitude', 'longitude', 'performance_measure2', 'cnt_worse', 'cnt_better', 'rating', 'procedure_condition']
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

# Round the final data for presentation
combined_data = combined_data.round(2)

# Rename specific performance measure
combined_data['performance_measure'] = combined_data['performance_measure'].replace('isolated cabg operative mor', 'isolated cabg operative mortality')
combined_data['performance_measure'] = combined_data['performance_measure'].replace('postop sepsis', 'postoperative sepsis')
combined_data['type_of_report'] = combined_data['type_of_report'].replace('pdi', 'psi')
combined_data['type_of_report'] = combined_data['type_of_report'].replace('cab', 'cabg')
combined_data['type_of_report'] = combined_data['type_of_report'].replace('elective pci', 'pci')

# Save final data to CSV
combined_data.to_csv('4_2016-2022_combined_ca_hospital_performance_ratings.csv', index=False)

# Print the first few rows of the final data
print(combined_data.head())
