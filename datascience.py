import pandas as pd

# Load the CSV file (fixing the path issue using raw string)
sales_df = pd.read_csv(r"C:\Users\Tjay\OneDrive\Documentos\Datasets\Sales_Transactions_Dataset_Weekly.csv")

# Preview the first 5 rows
print("...FIRST 5 ROWS.../n")
print(sales_df.head())
# Preview the last 5 rows
print("...LAST 5 ROWS.../n")
print(sales_df.tail())

# Task 1: Explore and Clean the Dataset

# Display dataset info
explore_info = sales_df.info()

# Check for missing values
missing_values = sales_df.isnull().sum()

# Clean the dataset by dropping missing values (if any)
sales_df_clean = sales_df.dropna()

# Re-check for missing values after cleaning
post_clean_missing = sales_df_clean.isnull().sum()

# Output results
explore_info, missing_values, post_clean_missing, sales_df_clean.head()
print("Missing values: ",missing_values)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define weekly sales columns ( are those starting with "W")
weekly_columns = [col for col in sales_df.columns if col.startswith("W")]

# ----------------------------
# Task 2: Basic Data Analysis
# ----------------------------

# 1. Basic statistics
print("Descriptive statistics:")
print(sales_df[weekly_columns].describe())

# 2. Grouping by Product_Code to compute mean weekly sales
grouped_means = sales_df.groupby("Product_Code")[weekly_columns].mean()

# Preview grouped data
print("\nAverage weekly sales by Product_Code (first 5 rows):")
print(grouped_means.head())

# ----------------------------
# Task 3: Data Visualizations
# ----------------------------
# Set seaborn style
sns.set(style="whitegrid")

# 1. Line Chart: Average weekly sales trend (select 5 products)
plt.figure(figsize=(12, 6))
sampled_products = sales_df['Product_Code'].unique()[:5]
for product in sampled_products:
    product_sales = sales_df[sales_df['Product_Code'] == product][weekly_columns].mean()
    plt.plot(weekly_columns, product_sales, label=product)

plt.title("Weekly Sales Trends for Sampled Products")
plt.xlabel("Week")
plt.ylabel("Average Units Sold")
plt.xticks(rotation=45)
plt.legend(title="Product Code")
plt.tight_layout()
plt.show()

# 2. Bar Chart: Total sales per product (top 10)
total_sales_per_product = sales_df.groupby('Product_Code')[weekly_columns].sum().sum(axis=1).sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=total_sales_per_product.index, y=total_sales_per_product.values, palette="viridis")
plt.title("Top 10 Products by Total Sales")
plt.xlabel("Product Code")
plt.ylabel("Total Units Sold")
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of sales in Week 0
plt.figure(figsize=(8, 5))
sns.histplot(sales_df["W0"], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Week 0 Sales")
plt.xlabel("Units Sold in Week 0")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Correlation between Week 0 and Week 1 sales
plt.figure(figsize=(8, 6))
sns.scatterplot(x=sales_df["W0"], y=sales_df["W1"], hue=sales_df["Product_Code"], palette="Set2", legend=False)
plt.title("Week 0 vs Week 1 Sales")
plt.xlabel("Week 0 Sales")
plt.ylabel("Week 1 Sales")
plt.tight_layout()
plt.show()
