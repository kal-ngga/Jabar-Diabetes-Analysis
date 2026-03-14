# Data Exploration of Diabetes Mellitus Patients (West Java)

This repository contains Python scripts for performing Exploratory Data Analysis (EDA) and Data Cleaning on a sample dataset of Diabetes Mellitus (DM) patients in West Java, Indonesia.

The analysis process includes descriptive statistical measurements, visualization of laboratory test data distribution, correlation testing, and the handling of missing values and outliers.

## Technologies Used
* **Language:** Python 3.x
* **Main Libraries:** * `pandas` (Data Manipulation & Vectorization)
  * `matplotlib` & `seaborn` (Data Visualization)
  * `numpy` (Numerical Computing)

## Directory Structure
* `dataset/` : Contains the raw data (`Dataset TA1.csv`) and the cleaned data (`Dataset_Clean.csv`).
* `visualitation/` : Folder where all graphic output images (Histogram, Bar Chart, Boxplot, Heatmap) are automatically saved.
* `cleaning.py` : A dedicated script for cleaning missing values (Nulls) and removing outliers using the Interquartile Range (IQR / Tukey's Fences) method.
* `exploration.py` : A script to calculate descriptive statistics and generate data visualizations. *(Note: Adjust this filename to match your actual script name)*.

## Analysis Features
1. **Data Condition Identification:** Checking the total number of rows, columns, data types, and missing values.
2. **Descriptive Statistics:** Calculating Count, Mean, Standard Deviation, Min, Max, and Median, both overall and grouped by diagnosis category.
3. **Data Visualization:** Generating Bar Charts (Categorical), Histograms (Numerical Distribution), and Boxplots (Comparison of lab value distributions between diagnosis groups).
4. **Pearson Correlation:** Testing the linear relationship between numerical variables (e.g., the strong correlation between Hemoglobin and Hematocrit).
5. **Outlier Detection:** Identifying data anomalies using the Lower Bound and Upper Bound formula based on IQR.

---
*Created for Data Exploration Assignment purposes.*