# Data Ingestion, Cleaning & Preprocessing with Pandas

## 📌 Project Overview

This project demonstrates how to ingest, clean, preprocess, and transform a real-world business dataset using Python and Pandas.

The **UCI Online Retail Dataset** was used for this project. The dataset contains real transaction records from a UK-based online retailer.

The objective was to identify and handle common data-quality problems such as missing values, duplicate records, incorrect data types, and outliers, followed by feature engineering and exporting the cleaned dataset.

---

## 📊 Dataset

**Dataset:** Online Retail Dataset

**Source:** UCI Machine Learning Repository

**Original Dataset Size:**
- 541,909 rows
- 8 columns

### Original Columns

| Column | Description |
|---|---|
| InvoiceNo | Invoice/transaction number |
| StockCode | Product code |
| Description | Product description |
| Quantity | Number of products purchased |
| InvoiceDate | Date and time of transaction |
| UnitPrice | Price per product |
| CustomerID | Customer identifier |
| Country | Customer's country |

---

## 🛠️ Technologies Used

- Python
- Pandas
- VS Code
- Excel (`.xlsx`)
- CSV

---

## 🔄 Data Cleaning Process

### 1. Data Ingestion

The raw Excel dataset was loaded into Pandas using:

```python
import pandas as pd

df = pd.read_excel("Online Retail.xlsx")
