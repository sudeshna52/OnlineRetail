import pandas as pd

# Load raw dataset
df = pd.read_excel("Online Retail.xlsx")

# Display first 5 rows
print(df.head())

# Check dataset size
print("Shape:", df.shape)

# Check column names
print("\nColumns:")
print(df.columns)

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()
print("\nShape after removing duplicates:")
print(df.shape)

# Handle missing values

# Fill missing product descriptions
df["Description"] = df["Description"].fillna("Unknown")

# CustomerID is an identifier, so remove rows where it is unavailable
df = df.dropna(subset=["CustomerID"])
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nShape after handling missing values:")
print(df.shape)

# Check important data types
print("\nData types before conversion:")
print(df[["InvoiceNo", "StockCode", "Quantity", "InvoiceDate",
          "UnitPrice", "CustomerID", "Country"]].dtypes)

# Convert CustomerID to integer
df["CustomerID"] = df["CustomerID"].astype(int)

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nData types after conversion:")
print(df.dtypes)

# Check numerical statistics
print("\nNumerical Statistics:")
print(df[["Quantity", "UnitPrice"]].describe())

# Calculate IQR for Quantity
Q1 = df["Quantity"].quantile(0.25)
Q3 = df["Quantity"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("\nQuantity Outlier Limits:")
print("Lower:", lower)
print("Upper:", upper)

print("Quantity outliers:", 
      ((df["Quantity"] < lower) | (df["Quantity"] > upper)).sum())

# Calculate IQR for UnitPrice
Q1_price = df["UnitPrice"].quantile(0.25)
Q3_price = df["UnitPrice"].quantile(0.75)
IQR_price = Q3_price - Q1_price

lower_price = Q1_price - 1.5 * IQR_price
upper_price = Q3_price + 1.5 * IQR_price

print("\nUnitPrice Outlier Limits:")
print("Lower:", lower_price)
print("Upper:", upper_price)

print("UnitPrice outliers:",
      ((df["UnitPrice"] < lower_price) |
       (df["UnitPrice"] > upper_price)).sum())

# Remove invalid prices
df = df[df["UnitPrice"] > 0]
# Cap extreme Quantity values
quantity_limit = df["Quantity"].quantile(0.99)
df["Quantity"] = df["Quantity"].clip(
    upper=quantity_limit)
print("\nQuantity 99th percentile:", quantity_limit)

# Cap extreme UnitPrice values
price_limit = df["UnitPrice"].quantile(0.99)
df["UnitPrice"] = df["UnitPrice"].clip(
    upper=price_limit)
print("UnitPrice 99th percentile:", price_limit)

# ---------------- FEATURE ENGINEERING ----------------

# Extract year and month from InvoiceDate
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Month_Name"] = df["InvoiceDate"].dt.month_name()

# Calculate Revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Display the new columns
print("\nFeature Engineering:")
print(df[["InvoiceDate", "Year", "Month", "Month_Name",
          "Quantity", "UnitPrice", "Revenue"]].head())

# Export cleaned dataset
df.to_csv("clean_dataset.csv", index=False)

print("\nClean dataset exported successfully!")
print("Final shape:", df.shape)