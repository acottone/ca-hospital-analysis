# Exploratory Data Analysis

## Dataset Overview

Number of rows: 89762
Number of columns: 9

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

## Categorical Summary Statistics

|        | county      | hospital                        | hospital_rating   |
|:-------|:------------|:--------------------------------|:------------------|
| count  | 89762       | 89762                           | 89762             |
| unique | 55          | 374                             | 4                 |
| top    | los angeles | ucla west valley medical center | average           |
| freq   | 21709       | 317                             | 44355             |

## Additional Summary Statistics

|        |   #_of_cases |   #_of_adverse_events |   risk_adjusted_rate |
|:-------|-------------:|----------------------:|---------------------:|
| median |       6      |                0      |              0       |
| var    |   79401.6    |              666.115  |             46.3321  |
| skew   |      14.8423 |               16.5413 |              5.33334 |
| kurt   |     434.225  |              354.975  |             50.534   |

## Categorical Variable Summary

|                 |   unique_values |
|:----------------|----------------:|
| county          |              55 |
| hospital        |             374 |
| hospital_rating |               4 |

### Mode of Categorical Variables

|                 | 0                               |
|:----------------|:--------------------------------|
| county          | los angeles                     |
| hospital        | ucla west valley medical center |
| hospital_rating | average                         |

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

## Trends Over Time
![Trends Over Time](./plots/trends/trend_over_time.png)

## Distribution of # of Cases Across Counties
![Distribution of # of Cases Across Counties](./plots/boxplots/cases_by_county.png)

## Distribution of Adverse Events Across Counties
![Distribution of Adverse Events Across Counties](./plots/boxplots/adverse_events_by_county.png)

## Distribution of Risk Adjusted Rate Across Counties
![Distribution of Risk Adjusted Rate Across Counties](./plots/boxplots/risk_adjusted_rate_by_county.png)

## Correlation Matrix
![Correlation Matrix](./plots/correlation/correlation_matrix.png)

## Distributions of Key Variables
![Distributions of Key Variables](./plots/distributions/distribution_with_transformed_metrics.png)

### Number of Cases by Hospital in alameda
![Number of Cases by Hospital in alameda](./plots/counties/alameda_#_of_cases.png)

### Number of Cases by Hospital in amador
![Number of Cases by Hospital in amador](./plots/counties/amador_#_of_cases.png)

### Number of Cases by Hospital in butte
![Number of Cases by Hospital in butte](./plots/counties/butte_#_of_cases.png)

### Number of Cases by Hospital in calaveras
![Number of Cases by Hospital in calaveras](./plots/counties/calaveras_#_of_cases.png)

### Number of Cases by Hospital in colusa
![Number of Cases by Hospital in colusa](./plots/counties/colusa_#_of_cases.png)

### Number of Cases by Hospital in contra costa
![Number of Cases by Hospital in contra costa](./plots/counties/contra costa_#_of_cases.png)

### Number of Cases by Hospital in del norte
![Number of Cases by Hospital in del norte](./plots/counties/del norte_#_of_cases.png)

### Number of Cases by Hospital in el dorado
![Number of Cases by Hospital in el dorado](./plots/counties/el dorado_#_of_cases.png)

### Number of Cases by Hospital in fresno
![Number of Cases by Hospital in fresno](./plots/counties/fresno_#_of_cases.png)

### Number of Cases by Hospital in glenn
![Number of Cases by Hospital in glenn](./plots/counties/glenn_#_of_cases.png)

### Number of Cases by Hospital in humboldt
![Number of Cases by Hospital in humboldt](./plots/counties/humboldt_#_of_cases.png)

### Number of Cases by Hospital in imperial
![Number of Cases by Hospital in imperial](./plots/counties/imperial_#_of_cases.png)

### Number of Cases by Hospital in inyo
![Number of Cases by Hospital in inyo](./plots/counties/inyo_#_of_cases.png)

### Number of Cases by Hospital in kern
![Number of Cases by Hospital in kern](./plots/counties/kern_#_of_cases.png)

### Number of Cases by Hospital in kings
![Number of Cases by Hospital in kings](./plots/counties/kings_#_of_cases.png)

### Number of Cases by Hospital in lake
![Number of Cases by Hospital in lake](./plots/counties/lake_#_of_cases.png)

### Number of Cases by Hospital in lassen
![Number of Cases by Hospital in lassen](./plots/counties/lassen_#_of_cases.png)

### Number of Cases by Hospital in los angeles
![Number of Cases by Hospital in los angeles](./plots/counties/los angeles_#_of_cases.png)

### Number of Cases by Hospital in madera
![Number of Cases by Hospital in madera](./plots/counties/madera_#_of_cases.png)

### Number of Cases by Hospital in marin
![Number of Cases by Hospital in marin](./plots/counties/marin_#_of_cases.png)

### Number of Cases by Hospital in mariposa
![Number of Cases by Hospital in mariposa](./plots/counties/mariposa_#_of_cases.png)

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

### Number of Cases by Hospital in san benito
![Number of Cases by Hospital in san benito](./plots/counties/san benito_#_of_cases.png)

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

### Number of Cases by Hospital in sutter
![Number of Cases by Hospital in sutter](./plots/counties/sutter_#_of_cases.png)

### Number of Cases by Hospital in tehama
![Number of Cases by Hospital in tehama](./plots/counties/tehama_#_of_cases.png)

### Number of Cases by Hospital in trinity
![Number of Cases by Hospital in trinity](./plots/counties/trinity_#_of_cases.png)

### Number of Cases by Hospital in tulare
![Number of Cases by Hospital in tulare](./plots/counties/tulare_#_of_cases.png)

### Number of Cases by Hospital in tuolumne
![Number of Cases by Hospital in tuolumne](./plots/counties/tuolumne_#_of_cases.png)

### Number of Cases by Hospital in ventura
![Number of Cases by Hospital in ventura](./plots/counties/ventura_#_of_cases.png)

### Number of Cases by Hospital in yolo
![Number of Cases by Hospital in yolo](./plots/counties/yolo_#_of_cases.png)

### Number of Cases by Hospital in yuba
![Number of Cases by Hospital in yuba](./plots/counties/yuba_#_of_cases.png)

### Adverse Events by Hospital in alameda
![Adverse Events by Hospital in alameda](./plots/counties/alameda_#_of_adverse_events.png)

### Adverse Events by Hospital in amador
![Adverse Events by Hospital in amador](./plots/counties/amador_#_of_adverse_events.png)

### Adverse Events by Hospital in butte
![Adverse Events by Hospital in butte](./plots/counties/butte_#_of_adverse_events.png)

### Adverse Events by Hospital in calaveras
![Adverse Events by Hospital in calaveras](./plots/counties/calaveras_#_of_adverse_events.png)

### Adverse Events by Hospital in colusa
![Adverse Events by Hospital in colusa](./plots/counties/colusa_#_of_adverse_events.png)

### Adverse Events by Hospital in contra costa
![Adverse Events by Hospital in contra costa](./plots/counties/contra costa_#_of_adverse_events.png)

### Adverse Events by Hospital in del norte
![Adverse Events by Hospital in del norte](./plots/counties/del norte_#_of_adverse_events.png)

### Adverse Events by Hospital in el dorado
![Adverse Events by Hospital in el dorado](./plots/counties/el dorado_#_of_adverse_events.png)

### Adverse Events by Hospital in fresno
![Adverse Events by Hospital in fresno](./plots/counties/fresno_#_of_adverse_events.png)

### Adverse Events by Hospital in glenn
![Adverse Events by Hospital in glenn](./plots/counties/glenn_#_of_adverse_events.png)

### Adverse Events by Hospital in humboldt
![Adverse Events by Hospital in humboldt](./plots/counties/humboldt_#_of_adverse_events.png)

### Adverse Events by Hospital in imperial
![Adverse Events by Hospital in imperial](./plots/counties/imperial_#_of_adverse_events.png)

### Adverse Events by Hospital in inyo
![Adverse Events by Hospital in inyo](./plots/counties/inyo_#_of_adverse_events.png)

### Adverse Events by Hospital in kern
![Adverse Events by Hospital in kern](./plots/counties/kern_#_of_adverse_events.png)

### Adverse Events by Hospital in kings
![Adverse Events by Hospital in kings](./plots/counties/kings_#_of_adverse_events.png)

### Adverse Events by Hospital in lake
![Adverse Events by Hospital in lake](./plots/counties/lake_#_of_adverse_events.png)

### Adverse Events by Hospital in lassen
![Adverse Events by Hospital in lassen](./plots/counties/lassen_#_of_adverse_events.png)

### Adverse Events by Hospital in los angeles
![Adverse Events by Hospital in los angeles](./plots/counties/los angeles_#_of_adverse_events.png)

### Adverse Events by Hospital in madera
![Adverse Events by Hospital in madera](./plots/counties/madera_#_of_adverse_events.png)

### Adverse Events by Hospital in marin
![Adverse Events by Hospital in marin](./plots/counties/marin_#_of_adverse_events.png)

### Adverse Events by Hospital in mariposa
![Adverse Events by Hospital in mariposa](./plots/counties/mariposa_#_of_adverse_events.png)

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

### Adverse Events by Hospital in san benito
![Adverse Events by Hospital in san benito](./plots/counties/san benito_#_of_adverse_events.png)

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

### Adverse Events by Hospital in sutter
![Adverse Events by Hospital in sutter](./plots/counties/sutter_#_of_adverse_events.png)

### Adverse Events by Hospital in tehama
![Adverse Events by Hospital in tehama](./plots/counties/tehama_#_of_adverse_events.png)

### Adverse Events by Hospital in trinity
![Adverse Events by Hospital in trinity](./plots/counties/trinity_#_of_adverse_events.png)

### Adverse Events by Hospital in tulare
![Adverse Events by Hospital in tulare](./plots/counties/tulare_#_of_adverse_events.png)

### Adverse Events by Hospital in tuolumne
![Adverse Events by Hospital in tuolumne](./plots/counties/tuolumne_#_of_adverse_events.png)

### Adverse Events by Hospital in ventura
![Adverse Events by Hospital in ventura](./plots/counties/ventura_#_of_adverse_events.png)

### Adverse Events by Hospital in yolo
![Adverse Events by Hospital in yolo](./plots/counties/yolo_#_of_adverse_events.png)

### Adverse Events by Hospital in yuba
![Adverse Events by Hospital in yuba](./plots/counties/yuba_#_of_adverse_events.png)

### Risk Adjusted Rate by Hospital in alameda
![Risk Adjusted Rate by Hospital in alameda](./plots/counties/alameda_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in amador
![Risk Adjusted Rate by Hospital in amador](./plots/counties/amador_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in butte
![Risk Adjusted Rate by Hospital in butte](./plots/counties/butte_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in calaveras
![Risk Adjusted Rate by Hospital in calaveras](./plots/counties/calaveras_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in colusa
![Risk Adjusted Rate by Hospital in colusa](./plots/counties/colusa_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in contra costa
![Risk Adjusted Rate by Hospital in contra costa](./plots/counties/contra costa_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in del norte
![Risk Adjusted Rate by Hospital in del norte](./plots/counties/del norte_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in el dorado
![Risk Adjusted Rate by Hospital in el dorado](./plots/counties/el dorado_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in fresno
![Risk Adjusted Rate by Hospital in fresno](./plots/counties/fresno_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in glenn
![Risk Adjusted Rate by Hospital in glenn](./plots/counties/glenn_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in humboldt
![Risk Adjusted Rate by Hospital in humboldt](./plots/counties/humboldt_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in imperial
![Risk Adjusted Rate by Hospital in imperial](./plots/counties/imperial_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in inyo
![Risk Adjusted Rate by Hospital in inyo](./plots/counties/inyo_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in kern
![Risk Adjusted Rate by Hospital in kern](./plots/counties/kern_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in kings
![Risk Adjusted Rate by Hospital in kings](./plots/counties/kings_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in lake
![Risk Adjusted Rate by Hospital in lake](./plots/counties/lake_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in lassen
![Risk Adjusted Rate by Hospital in lassen](./plots/counties/lassen_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in los angeles
![Risk Adjusted Rate by Hospital in los angeles](./plots/counties/los angeles_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in madera
![Risk Adjusted Rate by Hospital in madera](./plots/counties/madera_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in marin
![Risk Adjusted Rate by Hospital in marin](./plots/counties/marin_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in mariposa
![Risk Adjusted Rate by Hospital in mariposa](./plots/counties/mariposa_risk_adjusted_rate.png)

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

### Risk Adjusted Rate by Hospital in san benito
![Risk Adjusted Rate by Hospital in san benito](./plots/counties/san benito_risk_adjusted_rate.png)

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

### Risk Adjusted Rate by Hospital in sutter
![Risk Adjusted Rate by Hospital in sutter](./plots/counties/sutter_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in tehama
![Risk Adjusted Rate by Hospital in tehama](./plots/counties/tehama_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in trinity
![Risk Adjusted Rate by Hospital in trinity](./plots/counties/trinity_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in tulare
![Risk Adjusted Rate by Hospital in tulare](./plots/counties/tulare_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in tuolumne
![Risk Adjusted Rate by Hospital in tuolumne](./plots/counties/tuolumne_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in ventura
![Risk Adjusted Rate by Hospital in ventura](./plots/counties/ventura_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in yolo
![Risk Adjusted Rate by Hospital in yolo](./plots/counties/yolo_risk_adjusted_rate.png)

### Risk Adjusted Rate by Hospital in yuba
![Risk Adjusted Rate by Hospital in yuba](./plots/counties/yuba_risk_adjusted_rate.png)

### Performance Measure for aaa repair (un-ruptured, endovascular)
![Performance Measure for aaa repair (un-ruptured, endovascular)](./plots/performance/aaa repair (un-ruptured, endovascular)_performance_vs_metrics.png)

### Performance Measure for aaa repair (un-ruptured, open)
![Performance Measure for aaa repair (un-ruptured, open)](./plots/performance/aaa repair (un-ruptured, open)_performance_vs_metrics.png)

### Performance Measure for cabg
![Performance Measure for cabg](./plots/performance/cabg_performance_vs_metrics.png)

### Performance Measure for esophageal resection
![Performance Measure for esophageal resection](./plots/performance/esophageal resection_performance_vs_metrics.png)

### Performance Measure for pancreatic resection
![Performance Measure for pancreatic resection](./plots/performance/pancreatic resection_performance_vs_metrics.png)

### Performance Measure for pancreatic resection (cancer)
![Performance Measure for pancreatic resection (cancer)](./plots/performance/pancreatic resection (cancer)_performance_vs_metrics.png)

### Performance Measure for pancreatic resection (other)
![Performance Measure for pancreatic resection (other)](./plots/performance/pancreatic resection (other)_performance_vs_metrics.png)

### Performance Measure for pci
![Performance Measure for pci](./plots/performance/pci_performance_vs_metrics.png)

### Performance Measure for aaa repair (ruptured, endovascular)
![Performance Measure for aaa repair (ruptured, endovascular)](./plots/performance/aaa repair (ruptured, endovascular)_performance_vs_metrics.png)

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

### Performance Measure for hip fracture
![Performance Measure for hip fracture](./plots/performance/hip fracture_performance_vs_metrics.png)

### Performance Measure for pneumonia
![Performance Measure for pneumonia](./plots/performance/pneumonia_performance_vs_metrics.png)

### Performance Measure for 30-day mortality (ischemic stroke)
![Performance Measure for 30-day mortality (ischemic stroke)](./plots/performance/30-day mortality (ischemic stroke)_performance_vs_metrics.png)

### Performance Measure for 30-day readmission (ischemic stroke)
![Performance Measure for 30-day readmission (ischemic stroke)](./plots/performance/30-day readmission (ischemic stroke)_performance_vs_metrics.png)

### Performance Measure for aaa repair (ruptured, open)
![Performance Measure for aaa repair (ruptured, open)](./plots/performance/aaa repair (ruptured, open)_performance_vs_metrics.png)

### Performance Measure for acute stroke hemorrhagic
![Performance Measure for acute stroke hemorrhagic](./plots/performance/acute stroke hemorrhagic_performance_vs_metrics.png)

### Performance Measure for acute stroke ischemic
![Performance Measure for acute stroke ischemic](./plots/performance/acute stroke ischemic_performance_vs_metrics.png)

### Performance Measure for acute stroke subarachnoid
![Performance Measure for acute stroke subarachnoid](./plots/performance/acute stroke subarachnoid_performance_vs_metrics.png)

### Performance Measure for hip fracture repair
![Performance Measure for hip fracture repair](./plots/performance/hip fracture repair_performance_vs_metrics.png)

### Performance Measure for pancreatic cancer
![Performance Measure for pancreatic cancer](./plots/performance/pancreatic cancer_performance_vs_metrics.png)

### Performance Measure for pancreatic other
![Performance Measure for pancreatic other](./plots/performance/pancreatic other_performance_vs_metrics.png)

### Performance Measure for aaa repair
![Performance Measure for aaa repair](./plots/performance/aaa repair_performance_vs_metrics.png)

### Performance Measure for elective surgeries
![Performance Measure for elective surgeries](./plots/performance/elective surgeries_performance_vs_metrics.png)

### Performance Measure for postoperative sepsis
![Performance Measure for postoperative sepsis](./plots/performance/postoperative sepsis_performance_vs_metrics.png)

### Performance Measure for acc puncture/lac
![Performance Measure for acc puncture/lac](./plots/performance/acc_puncture_lac_performance_vs_metrics.png)

### Performance Measure for cent venous catheter bsi
![Performance Measure for cent venous catheter bsi](./plots/performance/cent venous catheter bsi_performance_vs_metrics.png)

### Performance Measure for neonatal bsi
![Performance Measure for neonatal bsi](./plots/performance/neonatal bsi_performance_vs_metrics.png)

### Performance Measure for postop resp failure
![Performance Measure for postop resp failure](./plots/performance/postop resp failure_performance_vs_metrics.png)

### Performance Measure for bpd (weight loss surgery)
![Performance Measure for bpd (weight loss surgery)](./plots/performance/bpd (weight loss surgery)_performance_vs_metrics.png)

### Performance Measure for lapband (weight loss surgery)
![Performance Measure for lapband (weight loss surgery)](./plots/performance/lapband (weight loss surgery)_performance_vs_metrics.png)

### Performance Measure for laprygb
![Performance Measure for laprygb](./plots/performance/laprygb_performance_vs_metrics.png)

### Performance Measure for openrygb (weight loss surgery)
![Performance Measure for openrygb (weight loss surgery)](./plots/performance/openrygb (weight loss surgery)_performance_vs_metrics.png)

### Performance Measure for vsg (weight loss surgery)
![Performance Measure for vsg (weight loss surgery)](./plots/performance/vsg (weight loss surgery)_performance_vs_metrics.png)

### Performance Measure for elective pci emergency cabg
![Performance Measure for elective pci emergency cabg](./plots/performance/elective pci emergency cabg_performance_vs_metrics.png)

### Performance Measure for elective pci mortality
![Performance Measure for elective pci mortality](./plots/performance/elective pci mortality_performance_vs_metrics.png)

### Performance Measure for elective pci stroke
![Performance Measure for elective pci stroke](./plots/performance/elective pci stroke_performance_vs_metrics.png)

### Performance Measure for post-operative stroke
![Performance Measure for post-operative stroke](./plots/performance/post-operative stroke_performance_vs_metrics.png)

### Performance Measure for cabg 30-day readmission
![Performance Measure for cabg 30-day readmission](./plots/performance/cabg 30-day readmission_performance_vs_metrics.png)

### Performance Measure for cabg operative mortality
![Performance Measure for cabg operative mortality](./plots/performance/cabg operative mortality_performance_vs_metrics.png)

### Performance Measure for cabg + valve operative mortality
![Performance Measure for cabg + valve operative mortality](./plots/performance/cabg + valve operative mortality_performance_vs_metrics.png)

### Performance Measure for isolated cabg operative mortality
![Performance Measure for isolated cabg operative mortality](./plots/performance/isolated cabg operative mortality_performance_vs_metrics.png)

### Performance Measure for isolated cabg 30-day readmission
![Performance Measure for isolated cabg 30-day readmission](./plots/performance/isolated cabg 30-day readmission_performance_vs_metrics.png)

### Performance Measure for isolated cabg post-operative stroke
![Performance Measure for isolated cabg post-operative stroke](./plots/performance/isolated cabg post-operative stroke_performance_vs_metrics.png)

### Performance Measure for tavr in-hospital/30-day mortality (tavr)
![Performance Measure for tavr in-hospital/30-day mortality (tavr)](./plots/performance/tavr in-hospital_30-day mortality (tavr)_performance_vs_metrics.png)

### Performance Measure for tavr in-hospital/30-day stroke (tavr)
![Performance Measure for tavr in-hospital/30-day stroke (tavr)](./plots/performance/tavr in-hospital_30-day stroke (tavr)_performance_vs_metrics.png)

### Hospital Performance Metrics by County in alameda - Chunk 1
![Hospital Performance Metrics by County in alameda - Chunk 1](./plots/hospitals/alameda_hospital_metrics_chunk_1.png)

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

### Hospital Performance Metrics by County in calaveras - Chunk 1
![Hospital Performance Metrics by County in calaveras - Chunk 1](./plots/hospitals/calaveras_hospital_metrics_chunk_1.png)

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

## Feature Importance in Predicting Performance Measure
![Feature Importance in Predicting Performance Measure](./plots/feature_importance/feature_importances.png)

## Average Risk Adjusted Rate by County
![Average Risk Adjusted Rate by County](./plots/barplots/avg_performance_by_county.png)

## Variance Inflation Factor (VIF) Check

- **Thresholds**: VIF > 5 suggests high multicollinearity, while VIF > 10 indicates severe multicollinearity.

| Feature             |   VIF |
|:--------------------|------:|
| const               |  1.31 |
| #_of_cases          |  1.02 |
| #_of_adverse_events |  1.06 |
| risk_adjusted_rate  |  1.04 |

![VIF Bar Plot](./plots/vif/vif_plot.png)

## PCA
![PCA](./plots/pca/pca_analysis.png)

## Silhouette Score for Clustering (Performance Metrics)

0.70

## Cluster Means (Performance Metrics)

|   Cluster_Performance |   #_of_cases |   #_of_adverse_events |   risk_adjusted_rate |   log_cases |   log_adverse_events |   log_risk_adjusted_rate |   PCA1 |   PCA2 | performance_measure    | hospital_rating   |
|----------------------:|-------------:|----------------------:|---------------------:|------------:|---------------------:|-------------------------:|-------:|-------:|:-----------------------|:------------------|
|                     0 |        42.55 |                  3.73 |                 2.9  |        1.91 |                 0.59 |                     0.65 |  -0.15 |  -0.14 | carotid endarterectomy | none              |
|                     1 |       529.23 |                 20.82 |                 4.48 |        6.17 |                 2.64 |                     1.46 |   1.24 |   1.07 | heart failure          | average           |
|                     2 |      4035.76 |                 16.48 |                 0.35 |        8.21 |                 2.34 |                     0.28 |   6.67 |  11.44 | elective surgeries     | average           |

## Cluster Sizes (Performance Metrics)

|   Cluster_Performance |   count |
|----------------------:|--------:|
|                     0 |   76305 |
|                     1 |   13198 |
|                     2 |     259 |

## Hospital Clustering by Performance Metrics
![Hospital Clustering by Performance Metrics](./plots/clusters/cluster_analysis.png)

## K-means Clustering of Cases vs Adverse Events

- **Cluster Statistics:**
|   #_of_cases |   #_of_adverse_events |   risk_adjusted_rate |
|-------------:|----------------------:|---------------------:|
|      42.7027 |               3.74105 |              2.89649 |
|     530.619  |              20.8591  |              4.47781 |
|    4035.76   |              16.4777  |              0.35    |

- **Cluster Sizes:**
|   Cluster_Cases |   count |
|----------------:|--------:|
|               0 |   80810 |
|               1 |    8750 |
|               2 |     202 |

## Overall ANOVA Results Across Counties

- **F-statistic:** 12.04
- **p-value:** 0.0

The difference in means across counties is **Significant**.

## Chi-Square Test Results

- Chi2 Statistic: 543.51
- Degrees of Freedom: 8
- p-value: 3.22e-112

### Contingency Table

Contingency Table (./tables/chi-square/chi_square_contingency_table.csv).

### Contingency Table Heatmap

![Contingency Table Heatmap](./plots/chi-square/chi_square_heatmap.png)

### Interpretation

The Chi-Square test shows a statistically significant association between risk categories and hospital ratings (p < 0.05).

