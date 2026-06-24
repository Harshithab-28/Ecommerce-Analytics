import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\HARSHITHA\Downloads\archive (6)\train.csv")
print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())
# Total Sales
total_sales = df["Sales"].sum()

# Total Orders
total_orders = df["Order ID"].nunique()

# Total Customers
total_customers = df["Customer ID"].nunique()

print("\n===== KPI SUMMARY =====")
print("Total Sales: $", round(total_sales, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)

# Sales by Category
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY CATEGORY =====")
print(category_sales)


# Sales by Region
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY REGION =====")
print(region_sales)


# Top 10 Products
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 PRODUCTS =====")
print(top_products)

#Category Sales Chart
plt.figure(figsize=(8,5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Sales by Category")
plt.xticks(rotation=20)
plt.show()

#Region Sales Chart
plt.figure(figsize=(8,5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

plt.title("Sales by Region")
plt.show()

#Top 10 Products Chart
plt.figure(figsize=(12,6))

top_products.plot(kind="bar")

plt.title("Top 10 Selling Products")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()