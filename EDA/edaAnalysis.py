import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load cleaned dataset
df = pd.read_csv("clean_dataset.csv")

print(df.head())
print(df.shape)
print(df.columns)

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Correlation Matrix
numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation)

# Correlation Heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Histograms
numeric_df = df.select_dtypes(include="number")

numeric_df.hist(figsize=(14, 10), bins=30)

plt.suptitle("Distribution of Numerical Variables")
plt.tight_layout()
plt.show()

# Box Plots for detecting outliers

columns = ["Quantity", "UnitPrice", "Revenue"]

for col in columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Box Plot - {col}")
    plt.show()

# Business Hypothesis Testing

# Hypothesis 1: Quantity vs Revenue
r1, p1 = pearsonr(df["Quantity"], df["Revenue"])

print("\nHypothesis 1: Quantity vs Revenue")
print("Correlation:", r1)
print("P-value:", p1)

# Hypothesis 2: UnitPrice vs Revenue
r2, p2 = pearsonr(df["UnitPrice"], df["Revenue"])

print("\nHypothesis 2: UnitPrice vs Revenue")
print("Correlation:", r2)
print("P-value:", p2)

# Hypothesis 3: UnitPrice vs Quantity
r3, p3 = pearsonr(df["UnitPrice"], df["Quantity"])

print("\nHypothesis 3: UnitPrice vs Quantity")
print("Correlation:", r3)
print("P-value:", p3)

# Multivariate Visualization
sample_df = df.sample(5000, random_state=42)

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=sample_df,
    x="UnitPrice",
    y="Revenue",
    hue="Quantity",
    alpha=0.6
)

plt.title("Unit Price vs Revenue by Quantity")
plt.xlabel("Unit Price")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

