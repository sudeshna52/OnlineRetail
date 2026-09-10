# Data Ingestion, Cleaning & Preprocessing with Pandas

This project demonstrates the complete process of data ingestion, cleaning, preprocessing, and feature engineering using Python and Pandas on a real-world business dataset. The **UCI Online Retail Dataset** was used, which contains 541,909 transaction records from a UK-based online retailer with information such as invoice number, product code, product description, quantity, invoice date, unit price, customer ID, and country. The dataset was loaded from Excel into Pandas and explored to understand its structure, columns, data types, missing values, duplicate records, and unusual values.

During the cleaning process, 5,268 duplicate records were identified and removed. Missing product descriptions were replaced with `Unknown`, while records with missing CustomerID values were removed because CustomerID is an identifier and assigning artificial values would not be appropriate. After handling the missing values, the CustomerID column was converted to an integer data type and InvoiceDate was converted to a proper datetime format.

The numerical columns Quantity and UnitPrice were examined for outliers using the IQR method. Since this is real-world retail data, extreme values were handled carefully instead of removing all statistical outliers. Negative quantities were retained because they can represent product returns or cancellations. Transactions with zero or negative UnitPrice values were removed. Extreme positive Quantity and UnitPrice values were capped at their respective 99th percentiles to reduce the influence of unusually large values while preserving useful transaction information.

Feature engineering was then performed using the InvoiceDate column. New features including Year, Month, and Month_Name were created to support time-based analysis. A Revenue feature was also created by calculating Quantity multiplied by UnitPrice. Profit margin was not calculated because the original dataset does not provide product cost information, and creating a profit value without actual cost data would require unsupported assumptions.

After completing the data cleaning and preprocessing steps, the processed dataset was exported as `clean_dataset.csv`. The project therefore provides a cleaned and standardized dataset that can be used for further exploratory data analysis, visualization, business reporting, and analytics.

The project was developed using Python and Pandas, with OpenPyXL used for reading the Excel dataset. Git and GitHub were used for version control, while Git LFS was used to store the approximately 45 MB cleaned CSV file. The project repository contains the Python cleaning script, cleaned dataset, documentation, Git configuration files, and the original Excel dataset used during local processing.

## Dataset

**Dataset:** UCI Online Retail Dataset  
**Source:** UCI Machine Learning Repository  
**Original Records:** 541,909  
**Original Columns:** 8  
**Time Period:** December 2010 – December 2011

The original dataset contains the following fields:

- InvoiceNo – Invoice number
- StockCode – Product/item code
- Description – Product description
- Quantity – Number of products purchased
- InvoiceDate – Date and time of transaction
- UnitPrice – Price per unit
- CustomerID – Customer identification number
- Country – Customer's country

## Data Quality Handling

The following data-quality issues were addressed as part of the project:

- Missing values were identified and handled appropriately.
- Missing product descriptions were replaced with `Unknown`.
- Rows with missing CustomerID values were removed.
- Duplicate records were detected and removed.
- CustomerID was converted to an integer data type.
- InvoiceDate was converted to datetime format.
- Invalid zero or negative UnitPrice values were removed.
- Extreme Quantity and UnitPrice values were capped at the 99th percentile.
- Negative quantities were retained because they may represent returns or cancellations.
- Year, Month, and Month_Name were extracted from InvoiceDate.
- Revenue was calculated using Quantity × UnitPrice.
- Profit margin was not calculated because product cost information was unavailable.

## Project Structure

text
Ass2/
├── Cleaning.py
├── clean_dataset.csv
├── README.md
├── .gitignore
├── .gitattributes
└── Online Retail.xlsx

## 🛠️ Technologies Used

- Python
- Pandas
- VS Code
- Excel (`.xlsx`)
- CSV

## Exploratory Data Analysis & Statistical Insights

### Descriptive Statistics

Descriptive statistics were calculated for the numerical variables, including Quantity, UnitPrice, CustomerID, Year, Month, and Revenue. Mean, median, standard deviation, minimum, maximum, and quartiles were analyzed to understand the distribution and variability of the dataset.

### Correlation Analysis

A correlation matrix and heatmap were generated to identify relationships between numerical variables.

The strongest relationship was between **Quantity and Revenue**, with a correlation coefficient of approximately **0.943**. This indicates a very strong positive relationship between the quantity sold and transaction revenue.

UnitPrice showed almost no linear relationship with Revenue (correlation ≈ **0.018**) and Quantity (correlation ≈ **-0.022**).

### Outlier Analysis

Box plots were created for Quantity, UnitPrice, and Revenue.

Several extreme values were identified in Quantity and Revenue. Negative quantities and negative revenue values may correspond to returned or cancelled transactions and should be considered when interpreting business performance.

UnitPrice also contained several high-value observations that may represent premium or unusual transactions.

### Business Hypothesis Testing

#### Hypothesis 1: Quantity vs Revenue

- **H₀:** Quantity and Revenue have no significant relationship.
- **H₁:** Quantity and Revenue have a significant relationship.
- **Correlation:** 0.9433
- **p-value:** approximately 0
- **Conclusion:** Reject H₀. There is a statistically significant and very strong positive relationship.

#### Hypothesis 2: UnitPrice vs Revenue

- **H₀:** UnitPrice and Revenue have no significant relationship.
- **H₁:** UnitPrice and Revenue have a significant relationship.
- **Correlation:** 0.0179
- **p-value:** 7.34 × 10⁻⁴⁷
- **Conclusion:** Reject H₀ statistically, but the correlation is extremely weak in practical terms.

#### Hypothesis 3: UnitPrice vs Quantity

- **H₀:** UnitPrice and Quantity have no significant relationship.
- **H₁:** UnitPrice and Quantity have a significant relationship.
- **Correlation:** -0.0223
- **p-value:** 2.06 × 10⁻⁴⁵
- **Conclusion:** Reject H₀ statistically, but the relationship is extremely weak in practical terms.

### Top 5 Critical Findings

1. **Quantity is strongly associated with Revenue.**  
   Quantity and Revenue have a correlation of approximately 0.943, indicating that larger quantities are associated with higher transaction revenue.

2. **UnitPrice has very little linear relationship with Revenue.**  
   Although the hypothesis test is statistically significant, the correlation is only approximately 0.018, indicating negligible practical association.

3. **UnitPrice and Quantity are almost unrelated linearly.**  
   Their correlation is approximately -0.022, showing an extremely weak negative relationship.

4. **The dataset contains significant outliers.**  
   Quantity and Revenue contain extreme positive and negative observations. Negative values may reflect product returns or cancelled transactions.

5. **Revenue is highly concentrated with extreme observations.**  
   The histogram and box plot show that most transactions are concentrated around relatively small revenue values, while a small number of transactions generate unusually large positive or negative revenue.

