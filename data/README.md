# Dataset Combination
This document outlines the data processing steps used to prepare the datasets for analysis. The process ensures consistency, standardization and proper merging of data.

---

## 1. Introduction
The goal of this process is to combine datasets with varying strutures into a unified format for analysis and modeling. This included standardization, consistency checks, merging, cleaning, and aggregation.

---

## 2. Standardization
The following steps were applied to ensure uniformity across datasets:

### 2.1 Column Renaming
Column names were standardized for consistency:
- Columns referring to the number of cases for each performance measure were renamed to `#_of_cases`.
- Columns referring to the number of deaths, strokes, and other adverse events were renamed to `#_of_adverse_events`.
- Columns referring to the risk-adjusted rate for each performance measure were renamed to `risk_adjusted_rate`.
- Columns referring to hospital or performance rating were renamed to `hospital_rating`.
  - Values of `better` were changed to `above average`, values of `worse` were changed to `below average`, and values of `as expected` were changed to `average` for consistency.
  - Rows without an explicit `hospital_rating` were given a value of `none`
 
### 2.2 Adding Missing Columns
Datasets without `performance_measure` columns (due to datasets focusing on only one performance measure) were given one with their respective performance measure (e.g., `hip fracture repair`, `elective surgeries`).

### 2.3 Dropping Unnecessary Columns
Columns that were not necessary for the purpose of this analysis were dropped.

---

## 3. Data Consistency
To ensure consistency across datasets, the following changes were made:

### 3.1 Performance Measure Descriptions
The values of some performance measures were updated to be more clear and uniform for the data:
- Replaced `30-day readmission` with `30-day readmission (ischemic stroke)` to specify what condition was being measured.

---

## 4. Merging Datasets
Datasets with similar structures were merged first tfor a smoother merging process. They were combined using `pd.merge()`.

-  `how="outer"` was used to retain all rows from the datasets, filling missing values where applicable.

---

## 5. Cleaning and Standardization
The combined dataset was analyzed for mistakes and inconsistencies, with the following fixes:

- Corrected spelling errors and typographical inconsistencies.
- OSHPD IDs for hospitals were checked using the HCAI Facility Database to find the most recent name and remove outdated/incorrect IDs.
- Rows were dropped that had inconsistencies:
  - Values for adverse events but no cases.
  - Values that cases but no data for other columns.

---

## 6. Grouping and Aggregationg
To prepare the data for analysis, grouping and aggregation steps were applied:

- Data was grouped by critical columns: `oshpd_id`, `hospital`, `year`, and `performance_measure`.

---

## 7. Conclusion
This workflow ensures that the combined dataset is standardized, cleaned, and suitable for analysis. 
