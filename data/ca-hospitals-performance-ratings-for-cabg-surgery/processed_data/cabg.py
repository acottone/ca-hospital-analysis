import pandas as pd

# Load the datasets
data1 = pd.read_csv('2011-2018-california-hospital-performance-ratings-for-coronary-artery-bypass-graft-cabg-surgery.csv', encoding='ISO-8859-1')
data2 = pd.read_csv('2018-2022-california-hospital-performance-ratings-for-coronary-artery-bypass-graft-cabg-surgery.csv', encoding='ISO-8859-1')

# Clean the 'hospital', 'county', 'performance_measure', and 'performance_rating' columns by stripping beginning/end spaces, converting to 
# lowercase, and replacing multiple spaces with single space
data1['Hospital'] = data1['Hospital'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Hospital'] = data2['Hospital'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['County'] = data1['County'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['County'] = data2['County'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['Performance Measure'] = data1['Performance Measure'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Performance Measure'] = data2['Performance Measure'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

data1['Performance Rating'] = data1['Performance Rating'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
data2['Performance Rating'] = data2['Performance Rating'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

# Rename select columns for consistency
data1.rename(columns={'Performance Rating': 'hospital_rating'}, inplace=True)
data2.rename(columns={'Hospital ID': 'oshpd_id', 'Performance Rating': 'hospital_rating'}, inplace=True)

# Clean column names to ensure consistency datasets
data1.columns = data1.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
data2.columns = data2.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)

# Convert relevant columns to numeric
columns_to_convert = ['#_of_cases', '#_of_adverse_events', 'risk-adjusted_rate', 'total_hospital_cabg_cases', 'hospital_adverse_events', 
                      'hospital_risk-adjusted_adverse_events_rate_(%,raaer)']
for col in columns_to_convert:
    if col in data1.columns:
        data1[col] = pd.to_numeric(data1[col], errors='coerce')
    if col in data2.columns:
        data2[col] = pd.to_numeric(data2[col], errors='coerce')

# Clean 'oshpd_id' column: remove ".0" if it exists
data1['oshpd_id'] = data1['oshpd_id'].astype(str).str.rstrip('.0').str.strip()
data2['oshpd_id'] = data2['oshpd_id'].astype(str).str.rstrip('.0').str.strip()

# Remove unnecessary columns
columns_to_remove = ['latitude', 'longitude', 'hospital_upper_95%_ci_for_raaer', 'hospital_lower_95%_ci_for_raaer', 
                     'total_statewide_cabg_cases']
data1.drop(columns=[col for col in columns_to_remove if col in data1.columns], inplace=True)
data2.drop(columns=[col for col in columns_to_remove if col in data2.columns], inplace=True)

# Ensure there is only one 'year' column
if 'ï»¿year' in data2.columns:
    data2.rename(columns={'ï»¿year': 'year'}, inplace=True)

# Normalize and convert 'year' column
def normalize_year(year):
    if '-' in str(year):
        return str(year).split('-')[0]
    return year

data1['year'] = data1['year'].apply(normalize_year)
data2['year'] = data2['year'].apply(normalize_year)
data1['year'] = pd.to_numeric(data1['year'], errors='coerce')
data2['year'] = pd.to_numeric(data2['year'], errors='coerce')

# Merge the datasets
combined_data = pd.concat([data1, data2], ignore_index=True)

# Fix column names and merge without replacing missing values with 0
combined_data['#_of_cases'] = combined_data['#_of_cases'].astype(float).add(
                              combined_data['total_hospital_cabg_cases'].astype(float), fill_value=0)

combined_data['#_of_adverse_events'] = combined_data['#_of_adverse_events'].astype(float).add(
                                       combined_data['hospital_adverse_events'].astype(float), fill_value=0)

combined_data['risk_adjusted_rate'] = combined_data['risk-adjusted_rate'].astype(float).add(
                                      combined_data['hospital_risk-adjusted_adverse_events_rate_(%,raaer)'].astype(float), fill_value=0)

# Remove unnecessary columns
columns_to_drop = ['total_hospital_cabg_cases', 'hospital_adverse_events', 'hospital_risk-adjusted_adverse_events_rate_(%,raaer)', 
                   'total_statewide_cabg_cases']
combined_data.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Aggregate without replacing missing values
combined_data = combined_data.groupby(['year', 'oshpd_id', 'county', 'hospital', 'performance_measure', 'hospital_rating']).agg({
    '#_of_cases': 'first', 
    '#_of_adverse_events': 'first', 
    'risk_adjusted_rate': 'first',
}).reset_index()

# Sort the combined dataset by 'county', 'hospital', and 'year' and reset index
combined_data = combined_data.sort_values(by=['county', 'hospital', 'year']).reset_index(drop=True)

# Clean 'year' column to avoid truncating valid year values
combined_data['year'] = combined_data['year'].apply(lambda x: str(int(x)) if isinstance(x, float) else str(x)).str.strip()

# Round the final data for presentation
combined_data = combined_data.round(2)

# Save the final combined data to CSV
combined_data.to_csv('3_2011-2022_combined_ca_hospital_performance_ratings_cabg_surgery.csv', index=False)

# Print the first few rows of the final data
print(combined_data.head())