# Exploratory Data Analysis (EDA) for California Hospital Ratings
This section explores the combined dataset of California hospital ratings, covering the years 2011 to 2022. The goal of this EDA is to uncover patterns, relationships and insights related to hospital performance, risk-adjusted rates, and adverse events.

## Dependencies
This section uses the following libraries:
- **matplotlib**: For generating visualizations and plots.
  - **matplotlib.cm**: For colormaps.
  - **matplotlib.colors**: For converting color formats and color maps.
- **seaborn**: For data visualization and enhanced plotting.
- **numpy**: For operations and array manipulations
- **pandas**: For data manipulation, cleaning, and analysis
- **os**: For file and directory management
- **warnings**: For suppressing warnings.
- **random**: For random number generation.
- **sklearn**:
  - **sklearn.preprocessing**: For scaling and encoding data.
  - **sklearn.ensemble**: For building ensemble models.
  - **sklearn.decomposition**: For performing PCA.
  - **sklearn.cluster**: For clustering algorithms.
  - **sklearn.metrics**: For evaluating the performance of clustering algorithms.
- **statsmodels**:
  - **statsmodels.tools.tools**: For adding constants to data.
  - **statsmodels.stats.outliers_influence**: For VIF calculations.
- **spicy**:
  - **spicy.stats**: For statistical tests.

## Global Settings
- The font family for plots was set to 'Helvetica' to ensure consistancy across visualizations.
- Warnings for font redering and palette issues were suppressed.
- Plots were set to the stile "ticks" using Seaborn for readability.
- A color map and color generation function were set using the "viridis" paletter for consistency.

## Directory Setup
A `create_directories` function was set to create directories for the plots, keeping them organized.

## Loading the Dataset
Data for the years 2005-2008 for removed for analysis since all relevant columns have values of 0. The `year` columns was also converted into a datetime format to ensure consistent and efficient handling of the year-based data.

## Dataset Overview
The dataset contained 89,762 rows and 9 columns, each represented a hospital performance record over the years 2011-2022. 
Number of rows: 89762
Number of columns: 9

The function `write_summary_stats` calculates the summary statistics for numeric and catergorical columns.

- Numeric columns: `#_of_cases`, `#_of_adverse_events`, `risk_adjusted_rate`.
- Categorical columns: `county`, `hospital`, `hospital_rating`.

## Numeric Summary Statistics

|       |   #_of_cases |   #_of_adverse_events |   risk_adjusted_rate |
|:------|-------------:|----------------------:|---------------------:|
| count |   89762      |           89762       |          89762       |
| mean  |      99.0713 |               5.43209 |              3.04433 |
| std   |     281.783  |              25.8092  |              6.80677 |
| min   |       0      |               0       |              0       |
| 25%   |       0      |               0       |              0       |
| 50%   |       6      |               0       |              0       |
| 75%   |     104      |               3       |              3.49    |
| max   |   15523      |             969       |            161.8     |

The dataset covers 55 unique counties, with Los Angeles County being the most frequent, making up 24.19% of the data alone. There are also 374 unique hospitals, with UCLA West Valley Medical Center being the most frequent at 0.004% of the data, and 4 unique hospital_rating categories with `average` being the most common at 49.41% of the data.

## Categorical Summary Statistics

|        | county      | hospital                        | hospital_rating   |
|:-------|:------------|:--------------------------------|:------------------|
| count  | 89762       | 89762                           | 89762             |
| unique | 55          | 374                             | 4                 |
| top    | los angeles | ucla west valley medical center | average           |
| freq   | 21709       | 317                             | 44355             |

Additional summary statistics were calculated using the `write_additional_stats` function, which finds the median, variance, skewness, and kurtosis for each numeric column. Thes results show particularly high variability for `#_of_cases`, and high positive skew for all columns. This suggests that lower values are much more common for each column. Kurtosis is also very high.

## Additional Summary Statistics

|        |   #_of_cases |   #_of_adverse_events |   risk_adjusted_rate |
|:-------|-------------:|----------------------:|---------------------:|
| median |       6      |                0      |              0       |
| var    |   79401.6    |              666.115  |             46.3321  |
| skew   |      14.8423 |               16.5413 |              5.33334 |
| kurt   |     434.225  |              354.975  |             50.534   |

Grouped summaries for each county were generated to find the mean values for each numeric column. Sacramento County has the highest average `#_of_cases` at 198.098 and the highest average `#_of_adverse_events` at 11.1602. Yuba County has the highest average `risk_adjusted_rate` at 5.11691. Modoc County has the lowest average `#_of_cases` at 0.458333. Glenn County has the lowest average of `#_of_adverse_events` at 0.0262172. Madera County has the lowest average `risk_adjusted_rate` at 0.119643.

## Grouped Summary by County

| county          |   #_of_cases |   #_of_adverse_events |   risk_adjusted_rate |
|:----------------|-------------:|----------------------:|---------------------:|
| alameda         |   101.813    |             5.41672   |            3.3794    |
| amador          |    24.2897   |             1.83793   |            2.477     |
| butte           |   102.196    |             5.61604   |            2.92765   |
| calaveras       |    10.0944   |             0.758741  |            2.01738   |
| colusa          |     3.97266  |             0.179688  |            1.51758   |
| contra costa    |   110.248    |             6.47453   |            3.18486   |
| del norte       |    19.9703   |             1.88811   |            2.24374   |
| el dorado       |    30.6241   |             1.84263   |            2.92363   |
| fresno          |   138.608    |             7.88602   |            2.85672   |
| glenn           |     1.43446  |             0.0262172 |            0.225094  |
| humboldt        |    26.1806   |             1.63465   |            2.71229   |
| imperial        |    29.171    |             2.15511   |            2.18304   |
| inyo            |     3.76349  |             0.149378  |            2.16494   |
| kern            |    70.0876   |             3.9582    |            3.22554   |
| kings           |    83.8664   |             5.03971   |            3.02202   |
| lake            |    11.4081   |             0.518389  |            1.17021   |
| lassen          |     4.97143  |             0.260714  |            2.30714   |
| los angeles     |   108.521    |             5.88175   |            3.19041   |
| madera          |   158.732    |             0.892857  |            0.119643  |
| marin           |    53.5011   |             3.22412   |            2.61454   |
| mariposa        |     2.0632   |             0.063197  |            1.01933   |
| mendocino       |    19.7455   |             1.0846    |            2.36968   |
| merced          |    52.0612   |             2.70804   |            1.93393   |
| modoc           |     0.458333 |             0.0416667 |            0.5875    |
| monterey        |    80.72     |             4.48253   |            3.33763   |
| napa            |    74.7509   |             4.12182   |            3.60549   |
| nevada          |    26.4771   |             1.62852   |            1.68648   |
| orange          |   103.014    |             5.61347   |            2.64335   |
| placer          |   164.201    |             8.57206   |            3.24033   |
| plumas          |     1.63558  |             0.0552147 |            1.25755   |
| riverside       |   107.005    |             6.10919   |            3.09963   |
| sacramento      |   198.098    |            11.1602    |            3.5671    |
| san benito      |    14.3741   |             0.917241  |            3.56831   |
| san bernardino  |   100.924    |             5.33007   |            2.55454   |
| san diego       |   169.665    |             8.91589   |            3.61327   |
| san francisco   |   128.188    |             6.03817   |            3.37491   |
| san joaquin     |    85.2977   |             4.43159   |            3.29922   |
| san luis obispo |    52.6112   |             2.99627   |            3.19644   |
| san mateo       |    82.6998   |             4.78247   |            3.30856   |
| santa barbara   |    76.767    |             4.55235   |            2.75766   |
| santa clara     |   180.776    |             9.22698   |            4.25579   |
| santa cruz      |    65.123    |             3.72566   |            2.71616   |
| shasta          |    73.7063   |             4.839     |            3.07415   |
| siskiyou        |    11.8806   |             0.686275  |            2.94283   |
| solano          |    72.1672   |             4.87689   |            3.4665    |
| sonoma          |    50.7444   |             3.01311   |            2.7414    |
| stanislaus      |   129.426    |             7.54262   |            3.61104   |
| sutter          |    18.3217   |             0.0347826 |            0.0191304 |
| tehama          |    24.0261   |             1.49477   |            2.40714   |
| trinity         |     2.79182  |             0.0855019 |            0.95316   |
| tulare          |   113.767    |             7.12915   |            3.46525   |
| tuolumne        |    43.6208   |             3.03717   |            2.38896   |
| ventura         |    82.2052   |             4.62402   |            3.50768   |
| yolo            |    29.2114   |             1.625     |            2.50833   |
| yuba            |   147.357    |             9.62268   |            5.11691   |

## Outlier Detection

The number of outliers in the dataset was detected using the function `detect_outliers` which utilizes the Interquartile Range (IQR) method to identify outliers in the numeric columns. 21,869 rows were identified to contain outliers in the dataset, making up 24.36% of the data.

Example: Alameda Hospital in Alameda County had a risk-adjusted rate of 17.1 for acute stroke

Total number of outliers detected: 21869

|     | year                |   oshpd_id | county   | hospital         | performance_measure                  |   #_of_cases |   #_of_adverse_events |   risk_adjusted_rate | hospital_rating   |
|----:|:--------------------|-----------:|:---------|:-----------------|:-------------------------------------|-------------:|----------------------:|---------------------:|:------------------|
|  49 | 2010-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | acute stroke                         |           53 |                     9 |                17.1  | average           |
|  61 | 2011-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | 30-day mortality (ischemic stroke)   |           95 |                    12 |                12.22 | average           |
|  62 | 2011-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | 30-day readmission (ischemic stroke) |           92 |                    18 |                18.66 | average           |
|  67 | 2011-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | acute stroke                         |           52 |                     8 |                13.5  | average           |
|  81 | 2012-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | 30-day mortality (ischemic stroke)   |          123 |                    13 |                10.03 | average           |
|  82 | 2012-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | 30-day readmission (ischemic stroke) |          117 |                    22 |                17.96 | average           |
|  86 | 2012-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | acute stroke                         |           72 |                     7 |                 8.8  | average           |
|  87 | 2012-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | acute stroke hemorrhagic             |           11 |                     5 |                25.1  | average           |
| 106 | 2013-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | 30-day mortality (ischemic stroke)   |           16 |                   124 |                10.28 | average           |
| 107 | 2013-01-01 00:00:00 |  106010735 | alameda  | alameda hospital | 30-day readmission (ischemic stroke) |           18 |                   109 |                16.56 | average           |

## Plots

### Trends Over Time

The `plot_trends` function generates line plots to visualize the trends for each performance metric over time.

![Trends Over Time](./plots/trends/trend_over_time.png)

`#_of_adverse_events` peaks between years 2012-2014. `#_of_cases` increases steadily after 2017. `risk_adjusted_rate` has the highest peaks at the years 2016 and 2020.

## Boxplots for Performance Metrics Across Counties 

The `save_boxplot` function generates boxplots for each performance metric across counties.

### Distribution of # of Cases Across Counties
![Distribution of # of Cases Across Counties](./plots/boxplots/cases_by_county.png)

### Distribution of Adverse Events Across Counties
![Distribution of Adverse Events Across Counties](./plots/boxplots/adverse_events_by_county.png)

### Distribution of Risk Adjusted Rate Across Counties
![Distribution of Risk Adjusted Rate Across Counties](./plots/boxplots/risk_adjusted_rate_by_county.png)

## Correlation Matrix

The `plot_correlation_matrix` function generates a heatmap of the correlaton matrix for selected performance metrics.

![Correlation Matrix](./plots/correlation/correlation_matrix.png)

The metrics all have slight positive correlations.

## Distributions of Key Variables

The `plot_distributions` function generates histograms for performance metrics and their log-transformed versions (to address skew) to visualize their distributions.

![Distributions of Key Variables](./plots/distributions/distribution_with_transformed_metrics.png)

## County-Specific Visualizations

The function `plot_county_visualizations` function generates separate visualizations for each county, showing the metrics for each hospital in the county.

Plots showing the metrics for only one hospital were note included (Yuba, Tuolumne, Trinity, Tehama, Sutter, San Benito, Mariposa, Madera, Lassen, Kings, Glenn, Del Norte, Colusa, Calaveras,

### Number of Cases by Hospital in alameda
![Number of Cases by Hospital in alameda](./plots/counties/alameda_#_of_cases.png)

### Number of Cases by Hospital in amador
![Number of Cases by Hospital in amador](./plots/counties/amador_#_of_cases.png)

### Number of Cases by Hospital in butte
![Number of Cases by Hospital in butte](./plots/counties/butte_#_of_cases.png)

### Number of Cases by Hospital in contra costa
![Number of Cases by Hospital in contra costa](./plots/counties/contra costa_#_of_cases.png)

### Number of Cases by Hospital in el dorado
![Number of Cases by Hospital in el dorado](./plots/counties/el dorado_#_of_cases.png)

### Number of Cases by Hospital in fresno
![Number of Cases by Hospital in fresno](./plots/counties/fresno_#_of_cases.png)

### Number of Cases by Hospital in humboldt
![Number of Cases by Hospital in humboldt](./plots/counties/humboldt_#_of_cases.png)

### Number of Cases by Hospital in imperial
![Number of Cases by Hospital in imperial](./plots/counties/imperial_#_of_cases.png)

### Number of Cases by Hospital in inyo
![Number of Cases by Hospital in inyo](./plots/counties/inyo_#_of_cases.png)

### Number of Cases by Hospital in kern
![Number of Cases by Hospital in kern](./plots/counties/kern_#_of_cases.png)

### Number of Cases by Hospital in lake
![Number of Cases by Hospital in lake](./plots/counties/lake_#_of_cases.png)

### Number of Cases by Hospital in los angeles
![Number of Cases by Hospital in los angeles](./plots/counties/los angeles_#_of_cases.png)

### Number of Cases by Hospital in marin
![Number of Cases by Hospital in marin](./plots/counties/marin_#_of_cases.png)

### Number of Cases by Hospital in mendocino
![Number of Cases by Hospital in mendocino](./plots/counties/mendocino_#_of_cases.png)

### Number of Cases by Hospital in merced
![Number of Cases by Hospital in merced](./plots/counties/merced_#_of_cases.png)

### Number of Cases by Hospital in modoc
![Number of Cases by Hospital in modoc](./plots/counties/modoc_#_of_cases.png)

### Number of Cases by Hospital in monterey
![Number of Cases by Hospital in monterey](./plots/counties/monterey_#_of_cases.png)

### Number of Cases by Hospital in napa
![Number of Cases by Hospital in napa](./plots/counties/napa_#_of_cases.png)

### Number of Cases by Hospital in nevada
![Number of Cases by Hospital in nevada](./plots/counties/nevada_#_of_cases.png)

### Number of Cases by Hospital in orange
![Number of Cases by Hospital in orange](./plots/counties/orange_#_of_cases.png)

### Number of Cases by Hospital in placer
![Number of Cases by Hospital in placer](./plots/counties/placer_#_of_cases.png)

### Number of Cases by Hospital in plumas
![Number of Cases by Hospital in plumas](./plots/counties/plumas_#_of_cases.png)

### Number of Cases by Hospital in riverside
![Number of Cases by Hospital in riverside](./plots/counties/riverside_#_of_cases.png)

### Number of Cases by Hospital in sacramento
![Number of Cases by Hospital in sacramento](./plots/counties/sacramento_#_of_cases.png)

### Number of Cases by Hospital in san bernardino
![Number of Cases by Hospital in san bernardino](./plots/counties/san bernardino_#_of_cases.png)

### Number of Cases by Hospital in san diego
![Number of Cases by Hospital in san diego](./plots/counties/san diego_#_of_cases.png)

### Number of Cases by Hospital in san francisco
![Number of Cases by Hospital in san francisco](./plots/counties/san francisco_#_of_cases.png)

### Number of Cases by Hospital in san joaquin
![Number of Cases by Hospital in san joaquin](./plots/counties/san joaquin_#_of_cases.png)

### Number of Cases by Hospital in san luis obispo
![Number of Cases by Hospital in san luis obispo](./plots/counties/san luis obispo_#_of_cases.png)

### Number of Cases by Hospital in san mateo
![Number of Cases by Hospital in san mateo](./plots/counties/san mateo_#_of_cases.png)

### Number of Cases by Hospital in santa barbara
![Number of Cases by Hospital in santa barbara](./plots/counties/santa barbara_#_of_cases.png)

### Number of Cases by Hospital in santa clara
![Number of Cases by Hospital in santa clara](./plots/counties/santa clara_#_of_cases.png)

### Number of Cases by Hospital in santa cruz
![Number of Cases by Hospital in santa cruz](./plots/counties/santa cruz_#_of_cases.png)

### Number of Cases by Hospital in shasta
![Number of Cases by Hospital in shasta](./plots/counties/shasta_#_of_cases.png)

### Number of Cases by Hospital in siskiyou
![Number of Cases by Hospital in siskiyou](./plots/counties/siskiyou_#_of_cases.png)

### Number of Cases by Hospital in solano
![Number of Cases by Hospital in solano](./plots/counties/solano_#_of_cases.png)

### Number of Cases by Hospital in sonoma
![Number of Cases by Hospital in sonoma](./plots/counties/sonoma_#_of_cases.png)

### Number of Cases by Hospital in stanislaus
![Number of Cases by Hospital in stanislaus](./plots/counties/stanislaus_#_of_cases.png)

### Number of Cases by Hospital in tulare
![Number of Cases by Hospital in tulare](./plots/counties/tulare_#_of_cases.png)

### Number of Cases by Hospital in ventura
![Number of Cases by Hospital in ventura](./plots/counties/ventura_#_of_cases.png)

### Number of Cases by Hospital in yolo
![Number of Cases by Hospital in yolo](./plots/counties/yolo_#_of_cases.png)

### Adverse Events by Hospital in alameda
![Adverse Events by Hospital in alameda](./plots/counties/alameda_#_of_adverse_events.png)

### Adverse Events by Hospital in amador
![Adverse Events by Hospital in amador](./plots/counties/amador_#_of_adverse_events.png)

### Adverse Events by Hospital in butte
![Adverse Events by Hospital in butte](./plots/counties/butte_#_of_adverse_events.png)

### Adverse Events by Hospital in contra costa
![Adverse Events by Hospital in contra costa](./plots/counties/contra costa_#_of_adverse_events.png)

### Adverse Events by Hospital in el dorado
![Adverse Events by Hospital in el dorado](./plots/counties/el dorado_#_of_adverse_events.png)

### Adverse Events by Hospital in fresno
![Adverse Events by Hospital in fresno](./plots/counties/fresno_#_of_adverse_events.png)

### Adverse Events by Hospital in humboldt
![Adverse Events by Hospital in humboldt](./plots/counties/humboldt_#_of_adverse_events.png)

### Adverse Events by Hospital in imperial
![Adverse Events by Hospital in imperial](./plots/counties/imperial_#_of_adverse_events.png)

### Adverse Events by Hospital in inyo
![Adverse Events by Hospital in inyo](./plots/counties/inyo_#_of_adverse_events.png)

### Adverse Events by Hospital in kern
![Adverse Events by Hospital in kern](./plots/counties/kern_#_of_adverse_events.png)

### Adverse Events by Hospital in lake
![Adverse Events by Hospital in lake](./plots/counties/lake_#_of_adverse_events.png)

### Adverse Events by Hospital in los angeles
![Adverse Events by Hospital in los angeles](./plots/counties/los angeles_#_of_adverse_events.png)

### Adverse Events by Hospital in marin
![Adverse Events by Hospital in marin](./plots/counties/marin_#_of_adverse_events.png)

### Adverse Events by Hospital in mendocino
![Adverse Events by Hospital in mendocino](./plots/counties/mendocino_#_of_adverse_events.png)

### Adverse Events by Hospital in merced
![Adverse Events by Hospital in merced](./plots/counties/merced_#_of_adverse_events.png)

### Adverse Events by Hospital in modoc
![Adverse Events by Hospital in modoc](./plots/counties/modoc_#_of_adverse_events.png)

### Adverse Events by Hospital in monterey
![Adverse Events by Hospital in monterey](./plots/counties/monterey_#_of_adverse_events.png)

### Adverse Events by Hospital in napa
![Adverse Events by Hospital in napa](./plots/counties/napa_#_of_adverse_events.png)

### Adverse Events by Hospital in nevada
![Adverse Events by Hospital in nevada](./plots/counties/nevada_#_of_adverse_events.png)

### Adverse Events by Hospital in orange
![Adverse Events by Hospital in orange](./plots/counties/orange_#_of_adverse_events.png)

### Adverse Events by Hospital in placer
![Adverse Events by Hospital in placer](./plots/counties/placer_#_of_adverse_events.png)

### Adverse Events by Hospital in plumas
![Adverse Events by Hospital in plumas](./plots/counties/plumas_#_of_adverse_events.png)

### Adverse Events by Hospital in riverside
![Adverse Events by Hospital in riverside](./plots/counties/riverside_#_of_adverse_events.png)

### Adverse Events by Hospital in sacramento
![Adverse Events by Hospital in sacramento](./plots/counties/sacramento_#_of_adverse_events.png)

### Adverse Events by Hospital in san bernardino
![Adverse Events by Hospital in san bernardino](./plots/counties/san bernardino_#_of_adverse_events.png)

### Adverse Events by Hospital in san diego
![Adverse Events by Hospital in san diego](./plots/counties/san diego_#_of_adverse_events.png)

### Adverse Events by Hospital in san francisco
![Adverse Events by Hospital in san francisco](./plots/counties/san francisco_#_of_adverse_events.png)

### Adverse Events by Hospital in san joaquin
![Adverse Events by Hospital in san joaquin](./plots/counties/san joaquin_#_of_adverse_events.png)

### Adverse Events by Hospital in san luis obispo
![Adverse Events by Hospital in san luis obispo](./plots/counties/san luis obispo_#_of_adverse_events.png)

### Adverse Events by Hospital in san mateo
![Adverse Events by Hospital in san mateo](./plots/counties/san mateo_#_of_adverse_events.png)

### Adverse Events by Hospital in santa barbara
![Adverse Events by Hospital in santa barbara](./plots/counties/santa barbara_#_of_adverse_events.png)

### Adverse Events by Hospital in santa clara
![Adverse Events by Hospital in santa clara](./plots/counties/santa clara_#_of_adverse_events.png)

### Adverse Events by Hospital in santa cruz
![Adverse Events by Hospital in santa cruz](./plots/counties/santa cruz_#_of_adverse_events.png)

### Adverse Events by Hospital in shasta
![Adverse Events by Hospital in shasta](./plots/counties/shasta_#_of_adverse_events.png)

### Adverse Events by Hospital in siskiyou
![Adverse Events by Hospital in siskiyou](./plots/counties/siskiyou_#_of_adverse_events.png)

### Adverse Events by Hospital in solano
![Adverse Events by Hospital in solano](./plots/counties/solano_#_of_adverse_events.png)

### Adverse Events by Hospital in sonoma
![Adverse Events by Hospital in sonoma](./plots/counties/sonoma_#_of_adverse_events.png)

### Adverse Events by Hospital in stanislaus
![Adverse Events by Hospital in stanislaus](./plots/counties/stanislaus_#_of_adverse_events.png)

### Adverse Events by Hospital in tulare
![Adverse Events by Hospital in tulare](./plots/counties/tulare_#_of_adverse_events.png)

### Adverse Events by Hospital in ventura
![Adverse Events by Hospital in ventura](./plots/counties/ventura_#_of_adverse_events.png)

### Adverse Events by Hospital in yolo
![Adverse Events by Hospital in yolo](./plots/counties/yolo_#_of_adverse_events.png)

### Risk Adjusted Rate by Hospital in alameda
![Risk Adjusted Rate by Hospital in alameda](./plots/counties/alameda_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in amador
![Risk Adjusted Rate by Hospital in amador](./plots/counties/amador_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in butte
![Risk Adjusted Rate by Hospital in butte](./plots/counties/butte_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in contra costa
![Risk Adjusted Rate by Hospital in contra costa](./plots/counties/contra costa_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in el dorado
![Risk Adjusted Rate by Hospital in el dorado](./plots/counties/el dorado_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in fresno
![Risk Adjusted Rate by Hospital in fresno](./plots/counties/fresno_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in humboldt
![Risk Adjusted Rate by Hospital in humboldt](./plots/counties/humboldt_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in imperial
![Risk Adjusted Rate by Hospital in imperial](./plots/counties/imperial_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in inyo
![Risk Adjusted Rate by Hospital in inyo](./plots/counties/inyo_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in kern
![Risk Adjusted Rate by Hospital in kern](./plots/counties/kern_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in lake
![Risk Adjusted Rate by Hospital in lake](./plots/counties/lake_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in los angeles
![Risk Adjusted Rate by Hospital in los angeles](./plots/counties/los angeles_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in marin
![Risk Adjusted Rate by Hospital in marin](./plots/counties/marin_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in mendocino
![Risk Adjusted Rate by Hospital in mendocino](./plots/counties/mendocino_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in merced
![Risk Adjusted Rate by Hospital in merced](./plots/counties/merced_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in modoc
![Risk Adjusted Rate by Hospital in modoc](./plots/counties/modoc_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in monterey
![Risk Adjusted Rate by Hospital in monterey](./plots/counties/monterey_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in napa
![Risk Adjusted Rate by Hospital in napa](./plots/counties/napa_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in nevada
![Risk Adjusted Rate by Hospital in nevada](./plots/counties/nevada_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in orange
![Risk Adjusted Rate by Hospital in orange](./plots/counties/orange_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in placer
![Risk Adjusted Rate by Hospital in placer](./plots/counties/placer_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in plumas
![Risk Adjusted Rate by Hospital in plumas](./plots/counties/plumas_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in riverside
![Risk Adjusted Rate by Hospital in riverside](./plots/counties/riverside_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in sacramento
![Risk Adjusted Rate by Hospital in sacramento](./plots/counties/sacramento_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in san bernardino
![Risk Adjusted Rate by Hospital in san bernardino](./plots/counties/san bernardino_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in san diego
![Risk Adjusted Rate by Hospital in san diego](./plots/counties/san diego_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in san francisco
![Risk Adjusted Rate by Hospital in san francisco](./plots/counties/san francisco_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in san joaquin
![Risk Adjusted Rate by Hospital in san joaquin](./plots/counties/san joaquin_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in san luis obispo
![Risk Adjusted Rate by Hospital in san luis obispo](./plots/counties/san luis obispo_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in san mateo
![Risk Adjusted Rate by Hospital in san mateo](./plots/counties/san mateo_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in santa barbara
![Risk Adjusted Rate by Hospital in santa barbara](./plots/counties/santa barbara_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in santa clara
![Risk Adjusted Rate by Hospital in santa clara](./plots/counties/santa clara_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in santa cruz
![Risk Adjusted Rate by Hospital in santa cruz](./plots/counties/santa cruz_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in shasta
![Risk Adjusted Rate by Hospital in shasta](./plots/counties/shasta_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in siskiyou
![Risk Adjusted Rate by Hospital in siskiyou](./plots/counties/siskiyou_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in solano
![Risk Adjusted Rate by Hospital in solano](./plots/counties/solano_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in sonoma
![Risk Adjusted Rate by Hospital in sonoma](./plots/counties/sonoma_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in stanislaus
![Risk Adjusted Rate by Hospital in stanislaus](./plots/counties/stanislaus_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in tulare
![Risk Adjusted Rate by Hospital in tulare](./plots/counties/tulare_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in ventura
![Risk Adjusted Rate by Hospital in ventura](./plots/counties/ventura_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in yolo
![Risk Adjusted Rate by Hospital in yolo](./plots/counties/yolo_risk_adjusted_rate.png)

## Performance Measure Visualizations

A helper function `santize_filename` was implemented to address performance measures contained '/' which causes issues with directories. The `plot_performance_measure_vs_metrics` function generates boxplots for each performance measure against the performance metrics.
Plots where the value is 0 for all metrics were removed (vsg, pancreatic resection (other), pancreatic resection (cancer), openrygb, laprygb, lapband, cabg, bpd, aaa repair (ruptured, open), aaa repair (ruptured, endovascular).

### Performance Measure for aaa repair (un-ruptured, endovascular)
![Performance Measure for aaa repair (un-ruptured, endovascular)](./plots/performance/aaa repair (un-ruptured, endovascular)_performance_vs_metrics.png)

### Performance Measure for aaa repair (un-ruptured, open)
![Performance Measure for aaa repair (un-ruptured, open)](./plots/performance/aaa repair (un-ruptured, open)_performance_vs_metrics.png)

### Performance Measure for esophageal resection
![Performance Measure for esophageal resection](./plots/performance/esophageal resection_performance_vs_metrics.png)

### Performance Measure for pancreatic resection
![Performance Measure for pancreatic resection](./plots/performance/pancreatic resection_performance_vs_metrics.png)

The risk-adjusted rate is relatively high compared to number of cases.

### Performance Measure for pci
![Performance Measure for pci](./plots/performance/pci_performance_vs_metrics.png)

The amount of adverse events and risk-adjusted rate are relatively low compared to number of cases.

### Performance Measure for aaa repair unruptured
![Performance Measure for aaa repair unruptured](./plots/performance/aaa repair unruptured_performance_vs_metrics.png)

### Performance Measure for acute stroke
![Performance Measure for acute stroke](./plots/performance/acute stroke_performance_vs_metrics.png)

### Performance Measure for ami
![Performance Measure for ami](./plots/performance/ami_performance_vs_metrics.png)

### Performance Measure for carotid endarterectomy
![Performance Measure for carotid endarterectomy](./plots/performance/carotid endarterectomy_performance_vs_metrics.png)

### Performance Measure for craniotomy
![Performance Measure for craniotomy](./plots/performance/craniotomy_performance_vs_metrics.png)

### Performance Measure for gi hemorrhage
![Performance Measure for gi hemorrhage](./plots/performance/gi hemorrhage_performance_vs_metrics.png)

### Performance Measure for heart failure
![Performance Measure for heart failure](./plots/performance/heart failure_performance_vs_metrics.png)

The risk-adjusted rate is somewhat high.

### Performance Measure for hip fracture
![Performance Measure for hip fracture](./plots/performance/hip fracture_performance_vs_metrics.png)

The risk-adjusted rate is somewhat high compared to number of cases.

### Performance Measure for pneumonia
![Performance Measure for pneumonia](./plots/performance/pneumonia_performance_vs_metrics.png)

The number of adverse events and risk-adjusted rate are relatively proportional to number of cases.

### Performance Measure for 30-day mortality (ischemic stroke)
![Performance Measure for 30-day mortality (ischemic stroke)](./plots/performance/30-day mortality (ischemic stroke)_performance_vs_metrics.png)

### Performance Measure for 30-day readmission (ischemic stroke)
![Performance Measure for 30-day readmission (ischemic stroke)](./plots/performance/30-day readmission (ischemic stroke)_performance_vs_metrics.png)

### Performance Measure for acute stroke hemorrhagic
![Performance Measure for acute stroke hemorrhagic](./plots/performance/acute stroke hemorrhagic_performance_vs_metrics.png)

### Performance Measure for acute stroke ischemic
![Performance Measure for acute stroke ischemic](./plots/performance/acute stroke ischemic_performance_vs_metrics.png)

### Performance Measure for acute stroke subarachnoid
![Performance Measure for acute stroke subarachnoid](./plots/performance/acute stroke subarachnoid_performance_vs_metrics.png)

### Performance Measure for hip fracture repair
![Performance Measure for hip fracture repair](./plots/performance/hip fracture repair_performance_vs_metrics.png)

The number of adverse events and risk-adjusted rate is somewhat high compared to number of cases.

### Performance Measure for pancreatic cancer
![Performance Measure for pancreatic cancer](./plots/performance/pancreatic cancer_performance_vs_metrics.png)

The risk-adjusted rate is high compared to number of cases

### Performance Measure for pancreatic other
![Performance Measure for pancreatic other](./plots/performance/pancreatic other_performance_vs_metrics.png)

The risk-adjusted rate is high compared to number of cases.

### Performance Measure for aaa repair
![Performance Measure for aaa repair](./plots/performance/aaa repair_performance_vs_metrics.png)

### Performance Measure for elective surgeries
![Performance Measure for elective surgeries](./plots/performance/elective surgeries_performance_vs_metrics.png)

### Performance Measure for postoperative sepsis
![Performance Measure for postoperative sepsis](./plots/performance/postoperative sepsis_performance_vs_metrics.png)

The amount of adverse events and risk-adjusted rate are relatively low compared to number of cases.

### Performance Measure for acc puncture/lac
![Performance Measure for acc puncture/lac](./plots/performance/acc_puncture_lac_performance_vs_metrics.png)

### Performance Measure for cent venous catheter bsi
![Performance Measure for cent venous catheter bsi](./plots/performance/cent venous catheter bsi_performance_vs_metrics.png)

### Performance Measure for neonatal bsi
![Performance Measure for neonatal bsi](./plots/performance/neonatal bsi_performance_vs_metrics.png)

The amount of adverse events and risk-adjusted rate are relatively low compared to number of cases.

### Performance Measure for postop resp failure
![Performance Measure for postop resp failure](./plots/performance/postop resp failure_performance_vs_metrics.png)

All metrics are relatively low.

### Performance Measure for elective pci emergency cabg
![Performance Measure for elective pci emergency cabg](./plots/performance/elective pci emergency cabg_performance_vs_metrics.png)

### Performance Measure for elective pci mortality
![Performance Measure for elective pci mortality](./plots/performance/elective pci mortality_performance_vs_metrics.png)

### Performance Measure for elective pci stroke
![Performance Measure for elective pci stroke](./plots/performance/elective pci stroke_performance_vs_metrics.png)

### Performance Measure for post-operative stroke
![Performance Measure for post-operative stroke](./plots/performance/post-operative stroke_performance_vs_metrics.png)

The amount of adverse events and risk-adjusted rate are relatively low compared to number of cases.

### Performance Measure for cabg 30-day readmission
![Performance Measure for cabg 30-day readmission](./plots/performance/cabg 30-day readmission_performance_vs_metrics.png)

### Performance Measure for cabg operative mortality
![Performance Measure for cabg operative mortality](./plots/performance/cabg operative mortality_performance_vs_metrics.png)

### Performance Measure for cabg + valve operative mortality
![Performance Measure for cabg + valve operative mortality](./plots/performance/cabg + valve operative mortality_performance_vs_metrics.png)

### Performance Measure for isolated cabg operative mortality
![Performance Measure for isolated cabg operative mortality](./plots/performance/isolated cabg operative mortality_performance_vs_metrics.png)

The amount of adverse events and risk-adjusted rate are relatively low compared to number of cases.

### Performance Measure for isolated cabg 30-day readmission
![Performance Measure for isolated cabg 30-day readmission](./plots/performance/isolated cabg 30-day readmission_performance_vs_metrics.png)

The number of adverse events and risk-adjust rate appear proportional to number of cases.

### Performance Measure for isolated cabg post-operative stroke
![Performance Measure for isolated cabg post-operative stroke](./plots/performance/isolated cabg post-operative stroke_performance_vs_metrics.png)

The amount of adverse events and risk-adjusted rate are relatively low compared to number of cases.

### Performance Measure for tavr in-hospital/30-day mortality (tavr)
![Performance Measure for tavr in-hospital/30-day mortality (tavr)](./plots/performance/tavr in-hospital_30-day mortality (tavr)_performance_vs_metrics.png)

The amount of adverse events and risk-adjusted rate are relatively low compared to number of cases.

### Performance Measure for tavr in-hospital/30-day stroke (tavr)
![Performance Measure for tavr in-hospital/30-day stroke (tavr)](./plots/performance/tavr in-hospital_30-day stroke (tavr)_performance_vs_metrics.png)

The amount of adverse events and risk-adjusted rate are relatively low compared to number of cases.

## County-Specific Hospital Metrics

The `plot_county_hospital_metrics` function generates subplots for performance metrics for hospitals in each county. Subplots are limited by four for each plot for readability.

Several hospitals show high adverse event numbers for measures regarding ischemic strokes.

### Hospital Performance Metrics by County in alameda - Chunk 1
![Hospital Performance Metrics by County in alameda - Chunk 1](./plots/hospitals/alameda_hospital_metrics_chunk_1.png)

Alameda Hospital had the largest risk-adjusted rate for acute stroke hemorhagic. There is also a higher risk-adjusted rate than number of cases for acute stroke subarachnoid.

Alta Bates Summit Medical Center and Highland Hospital both have the highest number of adverse events for ischemic stroke.

### Hospital Performance Metrics by County in alameda - Chunk 2
![Hospital Performance Metrics by County in alameda - Chunk 2](./plots/hospitals/alameda_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in alameda - Chunk 3
![Hospital Performance Metrics by County in alameda - Chunk 3](./plots/hospitals/alameda_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in alameda - Chunk 4
![Hospital Performance Metrics by County in alameda - Chunk 4](./plots/hospitals/alameda_hospital_metrics_chunk_4.png)

### Hospital Performance Metrics by County in amador - Chunk 1
![Hospital Performance Metrics by County in amador - Chunk 1](./plots/hospitals/amador_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in butte - Chunk 1
![Hospital Performance Metrics by County in butte - Chunk 1](./plots/hospitals/butte_hospital_metrics_chunk_1.png)

Orchard hospital showed high risk-adjusted rates for acute stroke, heart failure, pneumonia, ami, and acute stroke ischemic.

### Hospital Performance Metrics by County in calaveras - Chunk 1
![Hospital Performance Metrics by County in calaveras - Chunk 1](./plots/hospitals/calaveras_hospital_metrics_chunk_1.png)

Mark Twain Medical Center show high risk-adjusted rate for acute stroke, ami, acute stroke ischemic, and hip fracture repair.

### Hospital Performance Metrics by County in colusa - Chunk 1
![Hospital Performance Metrics by County in colusa - Chunk 1](./plots/hospitals/colusa_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in contra costa - Chunk 1
![Hospital Performance Metrics by County in contra costa - Chunk 1](./plots/hospitals/contra costa_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in contra costa - Chunk 2
![Hospital Performance Metrics by County in contra costa - Chunk 2](./plots/hospitals/contra costa_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in del norte - Chunk 1
![Hospital Performance Metrics by County in del norte - Chunk 1](./plots/hospitals/del norte_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in el dorado - Chunk 1
![Hospital Performance Metrics by County in el dorado - Chunk 1](./plots/hospitals/el dorado_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in fresno - Chunk 1
![Hospital Performance Metrics by County in fresno - Chunk 1](./plots/hospitals/fresno_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in fresno - Chunk 2
![Hospital Performance Metrics by County in fresno - Chunk 2](./plots/hospitals/fresno_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in fresno - Chunk 3
![Hospital Performance Metrics by County in fresno - Chunk 3](./plots/hospitals/fresno_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in glenn - Chunk 1
![Hospital Performance Metrics by County in glenn - Chunk 1](./plots/hospitals/glenn_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in humboldt - Chunk 1
![Hospital Performance Metrics by County in humboldt - Chunk 1](./plots/hospitals/humboldt_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in imperial - Chunk 1
![Hospital Performance Metrics by County in imperial - Chunk 1](./plots/hospitals/imperial_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in inyo - Chunk 1
![Hospital Performance Metrics by County in inyo - Chunk 1](./plots/hospitals/inyo_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in kern - Chunk 1
![Hospital Performance Metrics by County in kern - Chunk 1](./plots/hospitals/kern_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in kern - Chunk 2
![Hospital Performance Metrics by County in kern - Chunk 2](./plots/hospitals/kern_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in kern - Chunk 3
![Hospital Performance Metrics by County in kern - Chunk 3](./plots/hospitals/kern_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in kings - Chunk 1
![Hospital Performance Metrics by County in kings - Chunk 1](./plots/hospitals/kings_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in lake - Chunk 1
![Hospital Performance Metrics by County in lake - Chunk 1](./plots/hospitals/lake_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in lassen - Chunk 1
![Hospital Performance Metrics by County in lassen - Chunk 1](./plots/hospitals/lassen_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in los angeles - Chunk 1
![Hospital Performance Metrics by County in los angeles - Chunk 1](./plots/hospitals/los angeles_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in los angeles - Chunk 2
![Hospital Performance Metrics by County in los angeles - Chunk 2](./plots/hospitals/los angeles_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in los angeles - Chunk 3
![Hospital Performance Metrics by County in los angeles - Chunk 3](./plots/hospitals/los angeles_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in los angeles - Chunk 4
![Hospital Performance Metrics by County in los angeles - Chunk 4](./plots/hospitals/los angeles_hospital_metrics_chunk_4.png)

### Hospital Performance Metrics by County in los angeles - Chunk 5
![Hospital Performance Metrics by County in los angeles - Chunk 5](./plots/hospitals/los angeles_hospital_metrics_chunk_5.png)

### Hospital Performance Metrics by County in los angeles - Chunk 6
![Hospital Performance Metrics by County in los angeles - Chunk 6](./plots/hospitals/los angeles_hospital_metrics_chunk_6.png)

### Hospital Performance Metrics by County in los angeles - Chunk 7
![Hospital Performance Metrics by County in los angeles - Chunk 7](./plots/hospitals/los angeles_hospital_metrics_chunk_7.png)

### Hospital Performance Metrics by County in los angeles - Chunk 8
![Hospital Performance Metrics by County in los angeles - Chunk 8](./plots/hospitals/los angeles_hospital_metrics_chunk_8.png)

### Hospital Performance Metrics by County in los angeles - Chunk 9
![Hospital Performance Metrics by County in los angeles - Chunk 9](./plots/hospitals/los angeles_hospital_metrics_chunk_9.png)

### Hospital Performance Metrics by County in los angeles - Chunk 10
![Hospital Performance Metrics by County in los angeles - Chunk 10](./plots/hospitals/los angeles_hospital_metrics_chunk_10.png)

### Hospital Performance Metrics by County in los angeles - Chunk 11
![Hospital Performance Metrics by County in los angeles - Chunk 11](./plots/hospitals/los angeles_hospital_metrics_chunk_11.png)

### Hospital Performance Metrics by County in los angeles - Chunk 12
![Hospital Performance Metrics by County in los angeles - Chunk 12](./plots/hospitals/los angeles_hospital_metrics_chunk_12.png)

### Hospital Performance Metrics by County in los angeles - Chunk 13
![Hospital Performance Metrics by County in los angeles - Chunk 13](./plots/hospitals/los angeles_hospital_metrics_chunk_13.png)

### Hospital Performance Metrics by County in los angeles - Chunk 14
![Hospital Performance Metrics by County in los angeles - Chunk 14](./plots/hospitals/los angeles_hospital_metrics_chunk_14.png)

### Hospital Performance Metrics by County in los angeles - Chunk 15
![Hospital Performance Metrics by County in los angeles - Chunk 15](./plots/hospitals/los angeles_hospital_metrics_chunk_15.png)

### Hospital Performance Metrics by County in los angeles - Chunk 16
![Hospital Performance Metrics by County in los angeles - Chunk 16](./plots/hospitals/los angeles_hospital_metrics_chunk_16.png)

### Hospital Performance Metrics by County in los angeles - Chunk 17
![Hospital Performance Metrics by County in los angeles - Chunk 17](./plots/hospitals/los angeles_hospital_metrics_chunk_17.png)

### Hospital Performance Metrics by County in los angeles - Chunk 18
![Hospital Performance Metrics by County in los angeles - Chunk 18](./plots/hospitals/los angeles_hospital_metrics_chunk_18.png)

### Hospital Performance Metrics by County in los angeles - Chunk 19
![Hospital Performance Metrics by County in los angeles - Chunk 19](./plots/hospitals/los angeles_hospital_metrics_chunk_19.png)

### Hospital Performance Metrics by County in los angeles - Chunk 20
![Hospital Performance Metrics by County in los angeles - Chunk 20](./plots/hospitals/los angeles_hospital_metrics_chunk_20.png)

### Hospital Performance Metrics by County in los angeles - Chunk 21
![Hospital Performance Metrics by County in los angeles - Chunk 21](./plots/hospitals/los angeles_hospital_metrics_chunk_21.png)

### Hospital Performance Metrics by County in madera - Chunk 1
![Hospital Performance Metrics by County in madera - Chunk 1](./plots/hospitals/madera_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in marin - Chunk 1
![Hospital Performance Metrics by County in marin - Chunk 1](./plots/hospitals/marin_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in mariposa - Chunk 1
![Hospital Performance Metrics by County in mariposa - Chunk 1](./plots/hospitals/mariposa_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in mendocino - Chunk 1
![Hospital Performance Metrics by County in mendocino - Chunk 1](./plots/hospitals/mendocino_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in merced - Chunk 1
![Hospital Performance Metrics by County in merced - Chunk 1](./plots/hospitals/merced_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in modoc - Chunk 1
![Hospital Performance Metrics by County in modoc - Chunk 1](./plots/hospitals/modoc_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in monterey - Chunk 1
![Hospital Performance Metrics by County in monterey - Chunk 1](./plots/hospitals/monterey_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in napa - Chunk 1
![Hospital Performance Metrics by County in napa - Chunk 1](./plots/hospitals/napa_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in nevada - Chunk 1
![Hospital Performance Metrics by County in nevada - Chunk 1](./plots/hospitals/nevada_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in orange - Chunk 1
![Hospital Performance Metrics by County in orange - Chunk 1](./plots/hospitals/orange_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in orange - Chunk 2
![Hospital Performance Metrics by County in orange - Chunk 2](./plots/hospitals/orange_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in orange - Chunk 3
![Hospital Performance Metrics by County in orange - Chunk 3](./plots/hospitals/orange_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in orange - Chunk 4
![Hospital Performance Metrics by County in orange - Chunk 4](./plots/hospitals/orange_hospital_metrics_chunk_4.png)

### Hospital Performance Metrics by County in orange - Chunk 5
![Hospital Performance Metrics by County in orange - Chunk 5](./plots/hospitals/orange_hospital_metrics_chunk_5.png)

### Hospital Performance Metrics by County in orange - Chunk 6
![Hospital Performance Metrics by County in orange - Chunk 6](./plots/hospitals/orange_hospital_metrics_chunk_6.png)

### Hospital Performance Metrics by County in orange - Chunk 7
![Hospital Performance Metrics by County in orange - Chunk 7](./plots/hospitals/orange_hospital_metrics_chunk_7.png)

### Hospital Performance Metrics by County in orange - Chunk 8
![Hospital Performance Metrics by County in orange - Chunk 8](./plots/hospitals/orange_hospital_metrics_chunk_8.png)

### Hospital Performance Metrics by County in placer - Chunk 1
![Hospital Performance Metrics by County in placer - Chunk 1](./plots/hospitals/placer_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in plumas - Chunk 1
![Hospital Performance Metrics by County in plumas - Chunk 1](./plots/hospitals/plumas_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in riverside - Chunk 1
![Hospital Performance Metrics by County in riverside - Chunk 1](./plots/hospitals/riverside_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in riverside - Chunk 2
![Hospital Performance Metrics by County in riverside - Chunk 2](./plots/hospitals/riverside_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in riverside - Chunk 3
![Hospital Performance Metrics by County in riverside - Chunk 3](./plots/hospitals/riverside_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in riverside - Chunk 4
![Hospital Performance Metrics by County in riverside - Chunk 4](./plots/hospitals/riverside_hospital_metrics_chunk_4.png)

### Hospital Performance Metrics by County in riverside - Chunk 5
![Hospital Performance Metrics by County in riverside - Chunk 5](./plots/hospitals/riverside_hospital_metrics_chunk_5.png)

### Hospital Performance Metrics by County in sacramento - Chunk 1
![Hospital Performance Metrics by County in sacramento - Chunk 1](./plots/hospitals/sacramento_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in sacramento - Chunk 2
![Hospital Performance Metrics by County in sacramento - Chunk 2](./plots/hospitals/sacramento_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in sacramento - Chunk 3
![Hospital Performance Metrics by County in sacramento - Chunk 3](./plots/hospitals/sacramento_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in san benito - Chunk 1
![Hospital Performance Metrics by County in san benito - Chunk 1](./plots/hospitals/san benito_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in san bernardino - Chunk 1
![Hospital Performance Metrics by County in san bernardino - Chunk 1](./plots/hospitals/san bernardino_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in san bernardino - Chunk 2
![Hospital Performance Metrics by County in san bernardino - Chunk 2](./plots/hospitals/san bernardino_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in san bernardino - Chunk 3
![Hospital Performance Metrics by County in san bernardino - Chunk 3](./plots/hospitals/san bernardino_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in san bernardino - Chunk 4
![Hospital Performance Metrics by County in san bernardino - Chunk 4](./plots/hospitals/san bernardino_hospital_metrics_chunk_4.png)

### Hospital Performance Metrics by County in san bernardino - Chunk 5
![Hospital Performance Metrics by County in san bernardino - Chunk 5](./plots/hospitals/san bernardino_hospital_metrics_chunk_5.png)

### Hospital Performance Metrics by County in san diego - Chunk 1
![Hospital Performance Metrics by County in san diego - Chunk 1](./plots/hospitals/san diego_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in san diego - Chunk 2
![Hospital Performance Metrics by County in san diego - Chunk 2](./plots/hospitals/san diego_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in san diego - Chunk 3
![Hospital Performance Metrics by County in san diego - Chunk 3](./plots/hospitals/san diego_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in san diego - Chunk 4
![Hospital Performance Metrics by County in san diego - Chunk 4](./plots/hospitals/san diego_hospital_metrics_chunk_4.png)

### Hospital Performance Metrics by County in san diego - Chunk 5
![Hospital Performance Metrics by County in san diego - Chunk 5](./plots/hospitals/san diego_hospital_metrics_chunk_5.png)

### Hospital Performance Metrics by County in san francisco - Chunk 1
![Hospital Performance Metrics by County in san francisco - Chunk 1](./plots/hospitals/san francisco_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in san francisco - Chunk 2
![Hospital Performance Metrics by County in san francisco - Chunk 2](./plots/hospitals/san francisco_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in san francisco - Chunk 3
![Hospital Performance Metrics by County in san francisco - Chunk 3](./plots/hospitals/san francisco_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in san joaquin - Chunk 1
![Hospital Performance Metrics by County in san joaquin - Chunk 1](./plots/hospitals/san joaquin_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in san joaquin - Chunk 2
![Hospital Performance Metrics by County in san joaquin - Chunk 2](./plots/hospitals/san joaquin_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in san luis obispo - Chunk 1
![Hospital Performance Metrics by County in san luis obispo - Chunk 1](./plots/hospitals/san luis obispo_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in san mateo - Chunk 1
![Hospital Performance Metrics by County in san mateo - Chunk 1](./plots/hospitals/san mateo_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in san mateo - Chunk 2
![Hospital Performance Metrics by County in san mateo - Chunk 2](./plots/hospitals/san mateo_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in santa barbara - Chunk 1
![Hospital Performance Metrics by County in santa barbara - Chunk 1](./plots/hospitals/santa barbara_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in santa barbara - Chunk 2
![Hospital Performance Metrics by County in santa barbara - Chunk 2](./plots/hospitals/santa barbara_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in santa clara - Chunk 1
![Hospital Performance Metrics by County in santa clara - Chunk 1](./plots/hospitals/santa clara_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in santa clara - Chunk 2
![Hospital Performance Metrics by County in santa clara - Chunk 2](./plots/hospitals/santa clara_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in santa clara - Chunk 3
![Hospital Performance Metrics by County in santa clara - Chunk 3](./plots/hospitals/santa clara_hospital_metrics_chunk_3.png)

### Hospital Performance Metrics by County in santa cruz - Chunk 1
![Hospital Performance Metrics by County in santa cruz - Chunk 1](./plots/hospitals/santa cruz_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in shasta - Chunk 1
![Hospital Performance Metrics by County in shasta - Chunk 1](./plots/hospitals/shasta_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in siskiyou - Chunk 1
![Hospital Performance Metrics by County in siskiyou - Chunk 1](./plots/hospitals/siskiyou_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in solano - Chunk 1
![Hospital Performance Metrics by County in solano - Chunk 1](./plots/hospitals/solano_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in solano - Chunk 2
![Hospital Performance Metrics by County in solano - Chunk 2](./plots/hospitals/solano_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in sonoma - Chunk 1
![Hospital Performance Metrics by County in sonoma - Chunk 1](./plots/hospitals/sonoma_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in sonoma - Chunk 2
![Hospital Performance Metrics by County in sonoma - Chunk 2](./plots/hospitals/sonoma_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in stanislaus - Chunk 1
![Hospital Performance Metrics by County in stanislaus - Chunk 1](./plots/hospitals/stanislaus_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in stanislaus - Chunk 2
![Hospital Performance Metrics by County in stanislaus - Chunk 2](./plots/hospitals/stanislaus_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in sutter - Chunk 1
![Hospital Performance Metrics by County in sutter - Chunk 1](./plots/hospitals/sutter_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in tehama - Chunk 1
![Hospital Performance Metrics by County in tehama - Chunk 1](./plots/hospitals/tehama_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in trinity - Chunk 1
![Hospital Performance Metrics by County in trinity - Chunk 1](./plots/hospitals/trinity_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in tulare - Chunk 1
![Hospital Performance Metrics by County in tulare - Chunk 1](./plots/hospitals/tulare_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in tuolumne - Chunk 1
![Hospital Performance Metrics by County in tuolumne - Chunk 1](./plots/hospitals/tuolumne_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in ventura - Chunk 1
![Hospital Performance Metrics by County in ventura - Chunk 1](./plots/hospitals/ventura_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in ventura - Chunk 2
![Hospital Performance Metrics by County in ventura - Chunk 2](./plots/hospitals/ventura_hospital_metrics_chunk_2.png)

### Hospital Performance Metrics by County in yolo - Chunk 1
![Hospital Performance Metrics by County in yolo - Chunk 1](./plots/hospitals/yolo_hospital_metrics_chunk_1.png)

### Hospital Performance Metrics by County in yuba - Chunk 1
![Hospital Performance Metrics by County in yuba - Chunk 1](./plots/hospitals/yuba_hospital_metrics_chunk_1.png)

## Average Risk Adjusted Rate by County

The average `risk_adjusted_rate` per county is visualized using a barplot.

![Average Risk Adjusted Rate by County](./plots/barplots/avg_performance_by_county.png)

## Variance Inflation Factor (VIF) Check

The `check_vif` function calculates the VIF for each feature in the dataset to check for multicollinearity.

- **Thresholds**: VIF > 5 suggests high multicollinearity, while VIF > 10 indicates severe multicollinearity.

| Feature             |   VIF |
|:--------------------|------:|
| const               |  1.31 |
| #_of_cases          |  1.02 |
| #_of_adverse_events |  1.06 |
| risk_adjusted_rate  |  1.04 |

![VIF Bar Plot](./plots/vif/vif_plot.png)

The VIF for each feature is low, suggesting multicollinearity is not an issue in this dataset.

## PCA

Principal Component Analysis (PCA) was conducted on the data. The features were scaled using `StandardScaler` to ensure all features contribute equally to the analysis. The data was reduced to two principal components and a scatterplot was generated to visualize the components, colored by county.

![PCA](./plots/pca/pca_analysis.png)

## Clustering Analysis

The scaled features were used for further clustering analysis. K-means clustering was applied to group hospitals into 3 clusters based on the features.

### Silhouette Score for Clustering (Performance Metrics)

0.70

A silhouette score of 0.70 indicates that the clustering is of good quality. The hospitals are reasonably grouped based on their metrics with minimal overlap.

## Cluster Means (Performance Metrics)

|   Cluster_Performance |   #_of_cases |   #_of_adverse_events |   risk_adjusted_rate |   log_cases |   log_adverse_events |   log_risk_adjusted_rate |   PCA1 |   PCA2 | performance_measure    | hospital_rating   |
|----------------------:|-------------:|----------------------:|---------------------:|------------:|---------------------:|-------------------------:|-------:|-------:|:-----------------------|:------------------|
|                     0 |        42.55 |                  3.73 |                 2.9  |        1.91 |                 0.59 |                     0.65 |  -0.15 |  -0.14 | carotid endarterectomy | none              |
|                     1 |       529.23 |                 20.82 |                 4.48 |        6.17 |                 2.64 |                     1.46 |   1.24 |   1.07 | heart failure          | average           |
|                     2 |      4035.76 |                 16.48 |                 0.35 |        8.21 |                 2.34 |                     0.28 |   6.67 |  11.44 | elective surgeries     | average           |

Hospitals in cluster 0 have a low typical `#_of_cases` of 42.55, `#_of_adverse_events` of 3.73, and a `risk_adjusted_rate` of 2.9. The focus is on procedures such as carotid endarterectomy, with a hospital_rating of `none`.

Hospitals in cluster 1 handles 529.23 cases, with 20.82 adverse events, and a risk-adjusted rate of 4.48. Focus is on heart failure and hospital_rating `average`.

Cluster 2 handle 4,036.76 cases, 16.48 adverse events, and a risk-adjusted rate of 0.25. Focus is on elective surgeries and hospital_rating `average`.

## Cluster Sizes (Performance Metrics)

|   Cluster_Performance |   count |
|----------------------:|--------:|
|                     0 |   76305 |
|                     1 |   13198 |
|                     2 |     259 |

Cluster 0 is the biggest, while cluster 2 is the largest. Cluster 0 have lower case numbers while cluster 2 has higher case numbers.

## Hospital Clustering by Performance Metrics
![Hospital Clustering by Performance Metrics](./plots/clusters/cluster_analysis.png)

## Overall ANOVA Results Across Counties

The ANOVA test was performed to compare the means of `risk_adjusted_rate` across counties to determine if the differences are statistically significant.

- **F-statistic:** 12.04
- **p-value:** 0.0

The difference in means across counties is **Significant**.

## Chi-Square Test Results

A Chi-Square Test of Independence was used to determine if there is a significant relationship between risk categories and `hospital_rating`.

- Chi2 Statistic: 543.51
- Degrees of Freedom: 8
- p-value: 3.22e-112

### Contingency Table

Contingency Table (./tables/chi-square/chi_square_contingency_table.csv).

### Contingency Table Heatmap

![Contingency Table Heatmap](./plots/chi-square/chi_square_heatmap.png)

### Interpretation

The Chi-Square test shows a statistically significant association between risk categories and hospital ratings (p < 0.05). Hospitals with different risk profiles tend to have different ratings
