import pandas as pd

# Load datasets
data1 = pd.read_csv("3_2011-2022_combined_ca_hospital_performance_ratings_cabg_surgery.csv")
data2 = pd.read_csv("4_2016-2022_combined_ca_hospital_performance_ratings.csv")
data3 = pd.read_csv("5_2022_processed_ca_hospital_performance_ratings_tavr_data.csv")
data4 = pd.read_csv("18_2011-2014_processed_ca_hospital_ischemic_stroke_ratings_data.csv")
data5 = pd.read_csv("21_2012-2014_processed_ca_hospital_mortality_following_hip_fracture_repair_data.csv")
data6 = pd.read_csv("25_2019-2022_processed_ca_hospital_postoperative_sepsis_rates_data.csv")
data7 = pd.read_csv("2_2010-2022_combined_ca_hospital_inpatient_mortality_rates.csv")
data8 = pd.read_csv("7_2016-2022_processed_ca_hospital_elective_pcis_without_on_site_cardiac_surgery_data.csv")
data9 = pd.read_csv("22_2013-2023_processed_ca_hospital_cancer_surgeries_volume_data.csv")
data10 = pd.read_csv("23_2005-2017_combined_ca_hospital_inpatient_medical_procedures_data.csv")
data11 = pd.read_csv("24_2005-2015_processed_ca_hospital_number_of_weight_loss_surgeries_data.csv")

# Standardize column names across datasets
data2.rename(columns={"risk-adjusted_rate": "risk_adjusted_rate"}, inplace=True)
data6.rename(columns={"#_of_cases": "#_of_adverse_events", "elective_surgical_discharges": "#_of_cases", 
                      "performance_rating": "hospital_rating"}, inplace=True)
data7.rename(columns={"#_of_deaths": "#_of_adverse_events", "procedure_condition": "performance_measure"}, 
             inplace=True)
data8.rename(columns={"hospital_adverse_events": "#_of_adverse_events"}, inplace=True)
data9.rename(columns={"surgery": "performance_measure"}, inplace=True)
data11.rename(columns={"surgery": "performance_measure"}, inplace=True)

# Add 'performance_measure' columns where missing
data5["performance_measure"] = "hip fracture repair"
data6["performance_measure"] = "elective surgeries"

# Drop unnecessary columns
data2.drop(columns=["type_of_report"], inplace=True)

# Convert 'oshpd_id' to string and remove '.0'
for dataset in [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]:
    dataset["oshpd_id"] = dataset["oshpd_id"].astype(str).str.rstrip(".0")

# Adjust performance measures for specific datasets
data4["performance_measure"] = data4["performance_measure"].replace({
    "30-day readmission": "30-day readmission (ischemic stroke)", 
    "30-day mortality": "30-day mortality (ischemic stroke)"
})
data3["performance_measure"] = data3["performance_measure"].replace({
    "tavr in-hospital/30-day mortality": "tavr in-hospital/30-day mortality (tavr)",
    "tavr in-hospital/30-day stroke": "tavr in-hospital/30-day stroke (tavr)"
})
data9["performance_measure"] = data9["performance_measure"].replace({
    "colon": "colon (cancer surgery)", "breast": "breast (cancer surgery)", "stomach": "stomach (cancer surgery)", 
    "rectum": "rectum (cancer surgery)", "prostate": "prostate (cancer surgery)", 
    "bladder": "bladder (cancer surgery)", "liver": "liver (cancer surgery)", 
    "esophagus": "esophagus (cancer surgery)", "brain": "brain (cancer surgery)", "lung": "lung (cancer surgery)",
    "pancreas": "pancreas (cancer surgery)"
})
data11["performance_measure"] = data11["performance_measure"].replace({
    "bpd": "bpd (weight loss surgery)", "lapband": "lapband (weight loss surgery)", 
    "labprygb": "labprygb (weight loss surgery)", "openrygb": "openrygb (weight loss surgery)", 
    "vsg": "vsg (weight loss surgery)"
})

# Merge datasets with similar structures
data8_and_data9 = pd.merge(data8, data9, on=["year", "county", "hospital", "oshpd_id", 
                                             "performance_measure", "#_of_cases"], how="outer")
data8_9_and_10 = pd.merge(data8_and_data9, data10, on=["year", "county", "hospital", 
                                                       "oshpd_id", "performance_measure", 
                                                       "#_of_cases"], how="outer")
data8_9_10_and_11 = pd.merge(data8_9_and_10, data11, on=["year", "county", "hospital", 
                                                         "oshpd_id", "performance_measure", "#_of_cases"], 
                                                         how="outer")

# Combine data2 and data3 while consolidating the 'system' columns
data2_3 = pd.merge(data2, data3, on=[col for col in data2.columns if col != "system"], how="outer")
data2_3.drop(columns=["system_x", "system_y"], inplace=True)

# Define the common columns for merging
common_columns = ["year", "oshpd_id", "hospital", "county", "performance_measure", "risk_adjusted_rate", 
                  "#_of_adverse_events", "#_of_cases", "hospital_rating"]

# Sequentially merge all datasets on common columns
df_merged = pd.merge(data1, data2_3, on=common_columns, how="outer")
df_merged = pd.merge(df_merged, data4, on=common_columns, how="outer")
df_merged = pd.merge(df_merged, data5, on=common_columns, how="outer")
df_merged = pd.merge(df_merged, data6, on=common_columns, how="outer")

# Ensure consistency for 'risk_adjusted_rate'
data7["risk_adjusted_rate"] = pd.to_numeric(data7["risk_adjusted_rate"], errors='coerce')
df_merged["risk_adjusted_rate"] = pd.to_numeric(df_merged["risk_adjusted_rate"], errors='coerce')

# Merge remaining datasets
df_merged = pd.merge(df_merged, data7, on=common_columns, how="outer")
df_merged = pd.merge(df_merged, data8_9_10_and_11, on=["year", "oshpd_id", "hospital", "county", 
                                                       "performance_measure", "#_of_cases"], how="outer")

# Map the first instance of 'hospital' for each 'oshpd_id' to all rows with the same 'oshpd_id'
df_merged["hospital"] = df_merged.groupby("oshpd_id")["hospital"].transform("first")

# Remove duplicate rows from the dataset
df_merged = df_merged.drop_duplicates()

# Combine the '_x' and '_y' columns into a single column
df_merged["#_of_adverse_events"] = df_merged["#_of_adverse_events_x"].combine_first(df_merged["#_of_adverse_events_y"])
df_merged["risk_adjusted_rate"] = df_merged["risk_adjusted_rate_x"].combine_first(df_merged["risk_adjusted_rate_y"])

# Drop redundant columns
df_merged.drop(columns=["#_of_adverse_events_x", "#_of_adverse_events_y", "risk_adjusted_rate_x", 
                        "risk_adjusted_rate_y", "hospital_elective_pci_cases", "hospital_primary_pci_cases"], 
                        inplace=True)

# Correct spelling of performance measure categories
df_merged["performance_measure"] = df_merged["performance_measure"].replace({
    "espophageal resection": "esophageal resection"
})

# Clean and standardize county names
df_merged["county"] = df_merged["county"].replace({
    "aaaa": "aaa", "statewide": "aaa", "": "aaa", "calaver": "calaveras", "contra": "contra costa", 
    "del nor": "del norte", "el dora": "el dorado", "humbold": "humboldt", "imperia": "imperial", 
    "los ang": "los angeles", "maripos": "mariposa", "mendoci": "mendocino", "mono": "imperial", "montere": "monterey", 
    "riversi": "riverside", "sacrame": "sacramento", "san ben": "san benito", "san ber": "san bernardino", 
    "san bernardi": "san bernardino", "san die": "san diego", "san fra": "san francisco", 
    "san francisc": "san francisco", "san joa": "san joaquin", "san lui": "san luis obispo", 
    "san luis obis": "san luis obispo", "san luis obi": "san luis obispo", "san luis obisp": "san luis obispo",
    "san mat": "san mateo", "santa b": "santa barbara", "santa barbar": "santa barbara", "santa c": "santa clara", 
    "siskiyo": "siskiyou", "stanisl": "stanislaus", "tuolumn": "tuolumne", "san bernardin": "san bernardino"
})

# Exclude OSHPD IDs if they cannot be found in the HCAI facility database
df_merged = df_merged[~df_merged['oshpd_id'].isin(['106010805', '106010858', '106010856', '106040875', '106070904', 
                                                   '106070904', '106100745', '106150808', '106160787', '106160702', 
                                                   '106160725', '106190475', '106190159', '10619043', '106190455', 
                                                   '106190854', '106190534', '106190307', '106190762', '106190784', 
                                                   '106201281', '106230949', '106250956', '106301132', '106341052', 
                                                   '106370705', '106370755', '106380929', '106380964', '106410804', 
                                                   '106430805', '106490919', '106510882', '106190468', '106190712',
                                                   '106281297', '106301325', '106374084', '106551034'])]

# Standardize hospital names using a predefined mapping
hospital_name_mapping = {
    'alameda county medical center â highland campus': 'highland hospital',
    'alta bates summit medical center â summit campus â hawthorne': 'alta bates summit medical center',
    'alta bates summit medical center â alta bates campus': 'alta bates summit medical center - alta bates campus',
    'childrenâs hospital and research center at oakland': "ucsf benioff children's hospital oakland",
    'kaiser foundation hospital â fremont': 'kaiser foundation hospital - fremont',
    'kaiser foundation hospital â oakland/richmond': 'kaiser foundation hospital - oakland/richmond',
    'kaiser foundation hospital â san leandro': 'kaiser foundation hospital - san leandro',
    'kindred hospital â san francisco bay area': 'kindred hospital - san francisco bay area',
    'saint rose hospital': 'st. rose hospital',
    'valley memorial hospital': 'stanford health care tri-valley (livermore)',
    'valleycare medical center': 'stanford health care tri-valley (pleasanton)',
    'washington hospital â fremont': 'washington hospital - fremont',
    'biggs gridley memorial hospital': 'orchard hospital',
    'enloe medical center â esplanade': 'enloe health',
    'mark twain saint josephâs hospital': 'mark twain medical center',
    'colusa regional medical center': 'colusa medical center',
    'john muir medical center': 'john muir medical center - walnut creek campus',
    'john muir medical center â concord campus': 'john muir medical center - concord campus',
    'kaiser foundation hospital â antioch': 'kaiser foundation hospital - antioch',
    'kaiser foundation hospital â walnut creek': 'kaiser foundation hospital - walnut creek',
    'kaiser foundation hospital â richmond campus': 'kaiser foundation hospital - richmond campus',
    'community regional medical center â fresno': 'community regional medical center - fresno',
    'fresno heart hospital': 'fresno heart and surgical hospital',
    'kaiser foundation hospital â fresno': 'kaiser foundation hospital - fresno',
    'saint agnes medical center': 'st. agnes medical center',
    'sierra kings district hospital': 'adventist health reedley',
    'redwood memorial hospital': 'providence redwood memorial hospital',
    'saint joseph hospital â eureka': 'providence st. joseph hospital - eureka',
    'delano regional medical center': 'adventist health delano',
    'good samaritan hospital â bakersfield': 'good samaritan hospital - bakersfield',
    'mercy hospital â bakersfield': 'mercy hospital - bakersfield',
    'san joaquin community hospital': 'adventist health bakersfield',
    'adventist medical center': 'adventist health hanford',
    'redbud community hospital': 'adventist health clearlake',
    'antelope valley hospital': 'antelope valley medical center',
    'bellflower medical center': 'los angeles community hospital at bellflower',
    'beverly hospital': 'adventist health white memorial montebello',
    'brotman medical center': 'southern california hospital at culver city',
    'california hospital medical center â los angeles': 'california hospital medical center - los angeles',
    'cedars sinai medical center': 'cedars-sinai medical center',
    'centinela freeman regional medical center â memorial campus': 'del amo behavior health system',
    'century city doctors hospital': 'california rehabilitation institute, llc',
    'childrenâs hospital of los angeles': "children's hospital of los angeles",
    'citrus valley medical center â inter community campus': 'emanate health inter-community hospital',
    'citrus valley medical center â queen of the valley campus': 'emanate health queen of the valley hospital',
    'community and mission hospital of huntington park â slauson': 'community hospital of huntington park',
    'doctors hospital of west covina, inc.': 'west covina medical center',
    'downey regional medical center': 'pih health hospital - downey',
    'earl and lorraine miller childrenâs hospital': "memorialcare miller children's & women's hospital long beach",
    'east valley hospital medical center': 'glendora hospital',
    'foothill presbyterian hospital â johnston memorial': 'emanate health foothill presbyterian hospital',
    'glendale adventist medical center': 'adventist health glendale',
    'good samaritan hospital â los angeles': 'pih health good samaritan hospital',
    'helford clinical research hospital at city of hope': 'city of hope helford clinical research hospital',
    'henry mayo newhall memorial hospital': 'henry mayo newhall hospital',
    'hollywood community hospital': 'southern california hospital at hollywood',
    'huntington memorial hospital': 'huntington hospital',
    'kaiser foundation hospital â south bay': 'kaiser foundation hospital - south bay',
    'kaiser foundation hospital â baldwin park': 'kaiser foundation hospital - baldwin park',
    'kaiser foundation hospital â downey': 'kaiser foundation hospital - downey',
    'kaiser foundation hospital â panorama city': 'kaiser foundation hospital - panorama city',
    'kaiser foundation hospital â sunset': 'kaiser foundation hospital - los angeles',
    'kaiser foundation hospital â west los angeles': 'kaiser foundation hospital - west la',
    'kaiser foundation hospital â woodland hills': 'kaiser foundation hospital - woodland hills',
    'keck hospital of university of southern california': 'keck hospital of usc',
    'lakewood regional medical center': 'uci health - lakewood',
    'little company of mary hospital â torrance': 'providence little company of mary medical center torrance',
    'long beach memorial medical center': 'memorialcare long beach medical center',
    'los angeles county/harbor â ucla medical center': 'lac/harbor-ucla medical center',
    'los angeles county/olive view â ucla medical center': 'los angeles county olive view-ucla medical center',
    'los angeles county/rancho los amigos national rehabilitation center': 'lac/rancho los amigos national rehab center',
    'los angeles county/university of southern california medical center': 'los angeles general medical center',
    'marina del rey hospital': 'cedars-sinai marina hospital',
    'martin luther king jr. â harbor hospital': 'kaiser foundation hospital - south bay',
    'methodist hospital of southern california': 'usc arcadia hospital',
    'miracle mile medical center': 'docs surgical hospital',
    'mission community hospital â panorama campus': 'mission community hospital - panorama campus',
    'pacific hospital of long beach': 'college medical center',
    'presbyterian intercommunity hospital': 'pih health whittier hospital',
    'providence little company of mary medical center â san pedro': 'providence little company of mary medical center - san pedro',
    'providence tarzana medical center': 'providence cedars-sinai tarzana medical center',
    'saint francis medical center': 'st. francis medical center',
    "saint johnâs health center": "saint john's health center",
    'saint mary medical center': 'st. mary medical center - long beach',
    'santa monica â ucla medical center and orthopedic hospital': 'santa monica-ucla medical center and orthopedic hospital',
    'silver lake medical center â downtown campus': 'l.a. downtown medical center',
    'university of southern california kenneth norris, jr. cancer hospital': 'usc kenneth norris, jr. cancer hospital',
    'verdugo hills hospital': 'usc verdugo hills hospital',
    'west hills hospital and medical center': 'ucla west valley medical center',
    'white memorial medical center': 'adventist health white memorial medical center',
    'kaiser foundation hospital â san rafael': 'kaiser foundation hospital - san rafael',
    'marin general hospital': 'marinhealth medical center',
    'mendocino coast district hospital': 'adventist health mendocino coast',
    'mercy medical center â merced': 'mercy medical center - merced',
    'salinas valley memorial hospital': 'salinas valley health medical center',
    'queen of the valley hospital â napa': 'providence queen of the valley medical center',
    'saint helena hospital': 'adventist health st. helena',
    'anaheim general hospital': 'anaheim community hospital, llc',
    'chapman medical center': 'chapman global medical center',
    "childrenâs hospital at mission": "children's hospital at mission",
    'childrenâs hospital of orange county': "children's hospital of orange county",
    'coastal communities hospital': 'south coast global medical center',
    'fountain valley regional hospital and medical center â euclid': 'uci health - fountain valley',
    'irvine medical center': 'hoag hospital irvine',
    'kaiser foundation hospital  orange county  irvine': 'kaiser foundation hospital - orange county - irvine',
    'kaiser foundation hospital â orange county â anaheim': 'kaiser foundation hospital - orange county - anaheim',
    'los alamitos medical center': 'uci health - los alamitos',
    'mission hospital laguna beach': 'providence mission hospital - laguna beach',
    'mission hospital regional medical center': 'providence mission hospital',
    'newport specialty hospital': 'foothill regional medical center',
    'orange coast memorial medical center': 'memorialcare orange coast medical center',
    'placentia linda hospital': 'uci health - placentia linda',
    'saddleback memorial medical center': 'memorialcare saddleback medical center',
    'saint joseph hospital â orange': 'providence st. joseph hospital',
    'saint jude medical center': 'providence st. jude medical center',
    'western medical center â anaheim': 'anaheim global medical center',
    'western medical center â santa ana': 'orange county global medical center',
    'kaiser foundation hospital â sacramento/roseville-eureka': 'kaiser foundation hospital - roseville',
    'eastern plumas hospital â portola campus': 'eastern plumas hospital -portola campus',
    'corona regional medical center â main': 'corona regional medical center - main',
    'hemet valley medical center': 'hemet global medical center',
    'kaiser foundation hospital â riverside': 'kaiser foundation hospital - riverside',
    'loma linda murrieta*': 'loma linda university medical center - murrieta',
    'menifee valley medical center': 'menifee global medical center',
    'moreno valley community hospital': 'kaiser foundation hospital - moreno valley',
    'parkview community hospital medical center': 'doctors hospital of riverside',
    'riverside county regional medical center': 'riverside university health system - medical center',
    'southwest healthcare system â murrieta': 'southwest healthcare rancho springs hospital',
    'temecula valley': 'temecula valley hospital',
    'vibra rehab hospital of rancho mirage': 'rehabilitation hospital of southern california',
    'kaiser foundation hospital â sacramento': 'kaiser foundation hospital - sacramento',
    'kaiser foundation hospital â south sacramento': 'kaiser foundation hospital - south sacramento',
    'mercy hospital â folsom': 'mercy hospital of folsom',
    'mercy san juan hospital': 'mercy san juan medical center',
    'sutter general hospital': 'sutter medical center, sacramento',
    'kaiser foundation hospital â fontana': 'kaiser foundation hospital - fontana',
    'kindred hospital â rancho': 'kindred hospital rancho',
    'saint bernardine medical center': 'st. bernardine medical center',
    'saint mary regional medical center': 'providence st. mary medical center',
    'san antonio community hospital': 'san antonio regional hospital',
    'alvarado hospital': 'uc san diego health - east campus medical center',
    'childrenâs hospital â san diego': "rady children's hospital - san diego",
    'kaiser foundation hospital â san diego': 'kaiser foundation hospital - san diego - zion',
    'pomerado hospital': 'palomar medical center poway',
    'scripps memorial hospital â la jolla': 'scripps memorial hospital - la jolla',
    'scripps memorial hospital â encinitas': 'scripps memorial hospital - encinitas',
    'scripps mercy hospital â chula vista': 'scripps mercy hospital - chula vista',
    'tri-city medical center â oceanside': 'tri-city medical center',
    'uc san diego health - sulpizio cardiovascular center': 'ucsd health la jolla - jacobs medical center & sulpizio cardiovascular center',
    'uc san diego health system â hillcrest medical center': 'uc san diego health hillcrest - hillcrest medical center',
    'vibra hospital of san diego': 'select specialty hospital - san diego',
    'california pacific medical center  mission bernal c': 'california pacific medical center - mission bernal campus',
    'california pacific medical center â davies campus': 'california pacific medical center - davies campus hospital',
    'kaiser foundation hospital â san francisco': 'kaiser foundation hospital - san francisco',
    'saint francis memorial hospital': 'ucsf health - saint francis hospital',
    'saint maryâs medical center, san francisco': "ucsf health - st. mary's hospital",
    'san francisco general hospital': 'priscilla chan & mark zuckerberg san francisco general hospital & trauma center',
    'uc san francisco medical center': 'ucsf medical center',
    'kaiser foundation hospital â manteca': 'kaiser foundation hospital - manteca',
    'lodi memorial hospital': 'adventist health lodi memorial',
    'saint josephâs medical center of stockton': "st. joseph's medical center of stockton",
    'arroyo grande community hospital': 'marian regional medical center, arroyo grande',
    'sierra vista regional medical center': 'adventist health sierra vista',
    'twin cities community hospital': 'adventist health twin cities',
    'kaiser foundation hospital â south san francisco': 'kaiser foundation hospital - south san francisco',
    'kaiser foundation hospital â redwood city': 'kaiser foundation hospital - redwood city',
    'peninsula medical center': 'mills-peninsula medical center',
    'seton medical center': 'ahmc seton medical center',
    'marian medical center': 'marian regional medical center',
    'community hospital of los gatos': 'el camino hospital los gatos',
    'el camino hospital': 'el camino health',
    'good samaritan hospital â san jose': 'good samaritan hospital - san jose',
    'kaiser foundation hospital â san jose': 'kaiser foundation hospital - san jose',
    'lucile salter packard childrenâs hospital at stanford': "lucile packard children's hospital stanford",
    'oâconnor hospital â san jose': "o'connor hospital",
    'regional medical of san jose': 'regional medical center of san jose',
    'saint louise regional hospital': 'st. louise regional hospital',
    'stanford hospital': 'stanford health care',
    'mercy medical center â redding': 'mercy medical center - redding',
    'kaiser foundation hospital â rehabilitation center vallejo': 'kaiser foundation hospital & rehab center - vallejo',
    'kaiser foundation hospital â vacaville': 'kaiser foundation hospital - vacaville',
    'north bay medical center': 'northbay medical center',
    'healdsburg district hospital': 'healdsburg hospital',
    'kaiser foundation hospital â santa rosa': 'kaiser foundation hospital - santa rosa',
    'palm drive hospital': 'sonoma specialty hospital',
    'santa rosa memorial hospital â montgomery': 'providence santa rosa memorial hospital - montgomery',
    'sutter santa ros': 'sutter santa rosa regional hospital',
    'emanuel medical center, inc.': 'emanuel medical center',
    'memorial hospital medical center â modesto': 'memorial medical center - modesto',
    'oak valley district hospital': 'oak valley hospital district',
    'sutter surgical hospital â north valley': 'sutter surgical hospital - north valley',
    'saint elizabeth community hospital': 'st. elizabeth community hospital',
    'kaweah delta medical center': 'kaweah health medical center',
    'sierra view district hospital': 'sierra view medical center',
    'tulare regional medical center': 'adventist health tulare',
    'sonora regional medical center â greenley': 'adventist health sonora - greenley',
    'community memorial hospital â san buenaventura': 'community memorial hospital - san buenaventura',
    'ojai valley community hospital': 'community memorial hospital - ojai',
    'saint johnâs regional medical center': "st. john's regional medical center",
    'saint johnâs pleasant valley hospital': "st. john's hospital camarillo",
    'simi valley hospital and healthcare services â sycamore': 'adventist health simi valley',
    'rideout memorial hospital': 'adventist health and rideout',
    '': 'statewide',
    'kindred hospital â baldwin park': 'kindred hospital - baldwin park',
    'kindred hospital â south bay': 'kindred hospital - south bay',
    'kindred hospital â los angeles': 'kindred hospital - los angeles',
    'kindred hospital â la mirada': 'kindred hospital - la mirada',
    'promise hospital of east los angeles â suburban campus': 'kindred hospital - paramount',
    'childrenâs hospital central california': "valley children's hospital",
    'kindred hospital â brea': "kindred hospital - brea",
    'kindred hospital â westminster': "kindred hospital westminster",
    'eastern plumas hospital -portola campus': "eastern plumas hospital - portola campus",
    'kindred hospital â riverside': "kindred hospital - riverside",
    'kindred hospital â sacramento': "vibra hospital of sacramento",
    'kindred hospital â ontario': "kindred hospital - ontario",
    'kindred hospital â san diego': "kindred hospital - san diego",
    'kaiser foundation hospital â santa clara': "kaiser foundation hospital - santa clara",
    'patientsâ hospital of redding': "patients' hospital of redding",
    'seton medical center â coastside': "ahmc seton medical center coastside"
}
df_merged['hospital'] = df_merged['hospital'].map(hospital_name_mapping).fillna(df_merged['hospital'])

# Update OSHPD IDs using a predefined mapping
oshpd_id_mapping = {
    '106': 'nan', '106311': '106311000', '1061902': '106190200', '1061904': '106190400', '1061905': '106190500', 
    '10601405': '106014050', '10606087': '106060870', '10607099': '106070990', '10612108': '106121080', 
    '10613076': '106130760', '10619011': '106190110', '10619023': '106190230', '10619024': '106190240',
    '10619028': '106190280', '10619038': '106190380', '10619047': '106190470', '10619057': '106190570', 
    '10619063': '106190630', '10619068': '106190680', '10619145': '106191450', '10630114': '106301140', 
    '10630134': '106301340', '10634095': '106340950', '10636111': '106361110', '10636137': '106361370',
    '10636443': '106364430', '10637073': '106370730', '10637078': '106370780', '10638096': '106380960', 
    '10639101': '106391010', '10640048': '106400480', '10645094': '106450940', '10651403': '106514030', 
    '10657401': '106574010', '10619017': '106190170', '10619123': '106191230', '10630446': '106304460',
    '10643404': '106434040', 
}
if 'oshpd_id' in df_merged.columns:
    df_merged['oshpd_id'] = df_merged['oshpd_id'].map(oshpd_id_mapping).fillna(df_merged['oshpd_id'])

# Standardize rows with 'statewide' hospitals
df_merged.loc[df_merged['hospital'] == 'statewide', ['county', 'oshpd_id']] = ['aaa', '1']
df_merged.loc[df_merged['county'] == 'aaa', ['hospital', 'oshpd_id']] = ['statewide', '1']

# Remove rows where 'hospital' is 'statewide'
df_merged = df_merged[df_merged['hospital'] != 'statewide']

# Standardize performance measure descriptions
df_merged['performance_measure'] = df_merged['performance_measure'].replace({
    'aaa repair endo unrupture': 'aaa repair (un-ruptured, endovascular)',
    'aaa repair open unrupture': 'aaa repair (un-ruptured, open)', 
    'cabg+valve operative mortality': 'cabg + valve operative mortality', 
    '30-day readmission': 'cabg 30-day readmission', 'operative mortality': 'cabg operative mortality',
    'aaa repair endo unruptured': 'aaa repair (un-ruptured, endovascular)', 
    'aaa repair open unruptured': 'aaa repair (un-ruptured, open)'
})

# Standardize hospital rating descriptions
df_merged['hospital_rating'] = df_merged['hospital_rating'].replace({
    'better': 'above average', 'worse': 'below average', 'not appplicable': 'none', 'as expected': 'average'
})

# Group by the specified columns and aggregate data
aggregated_df = df_merged.groupby(['oshpd_id', 'hospital', 'year', 'performance_measure'], as_index=False).agg({
    'hospital_rating': lambda x: x.dropna().mode().iloc[0] if not x.dropna().empty else None,
    '#_of_cases': lambda x: x.mean(skipna=True),
    '#_of_adverse_events': lambda x: x.mean(skipna=True),
    'risk_adjusted_rate': lambda x: x.mean(skipna=True),
    'hospital': 'first',
    'county': 'first'
})

# Reset the index after grouping
aggregated_df.reset_index(drop=True, inplace=True)

# Round numeric values to 2 decimal places for consistency
aggregated_df = aggregated_df.round(2)

# Reorder columns
custom_column_order = ["year", "oshpd_id", "county", "hospital", "performance_measure", "#_of_cases", 
                       "#_of_adverse_events", "risk_adjusted_rate", "hospital_rating"]

# Only include columns that are present in the aggregated dataframe
available_columns = [col for col in custom_column_order if col in aggregated_df.columns]
aggregated_df = aggregated_df[available_columns]

# Filter out inconsistent rows where #_of_cases is NaN or 0 but other columns are not, rows where #_of_cases is not 
# missing/0 but other columns are
aggregated_df = aggregated_df[~((aggregated_df['#_of_cases'].isnull()) & ((aggregated_df['#_of_adverse_events'] > 0) | 
                              (aggregated_df['risk_adjusted_rate'] > 0) | (aggregated_df['hospital_rating'].notnull())))]
aggregated_df = aggregated_df[~((aggregated_df['#_of_cases'] == 0) & ((aggregated_df['#_of_adverse_events'] > 0) | 
                              (aggregated_df['risk_adjusted_rate'] > 0) | (aggregated_df['hospital_rating'].notnull())))]
aggregated_df = aggregated_df[~((aggregated_df['#_of_cases'].notnull()) & 
    (aggregated_df[['#_of_adverse_events', 'risk_adjusted_rate', 'hospital_rating']].isnull().any(axis=1)))]

# Impute missing values for numeric columns with zero, and hospital_rating with 'none'
aggregated_df['#_of_cases'] = aggregated_df['#_of_cases'].fillna(0)
aggregated_df['#_of_adverse_events'] = aggregated_df['#_of_adverse_events'].fillna(0)
aggregated_df['risk_adjusted_rate'] = aggregated_df['risk_adjusted_rate'].fillna(0)
aggregated_df['hospital_rating'] = aggregated_df['hospital_rating'].fillna('none')

# Save the final dataset to CSV file
aggregated_df.to_csv("combined_2011-2022_ca_hospital_ratings.csv", index=False)

print(aggregated_df.head())
