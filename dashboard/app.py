import streamlit as st
import pandas as pd

# Load Dataset
df = pd.read_csv(r"C:\Users\HARSHITHA\Downloads\archive (6)\train.csv")

# Page Title
st.set_page_config(page_title="E-Commerce Sales Dashboard",
                   page_icon="📊",
                   layout="wide")

st.title("📊 E-Commerce Sales Analytics Dashboard")
st.markdown("Analyze sales performance across products, categories, and regions.")
# KPIs
total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)

#Add Category Filter
st.sidebar.header("Filters")

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["Category"].unique())
)

if selected_category != "All":
    df = df[df["Category"] == selected_category]

#Add Region Filter
selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]

#Category Sales Chart
import plotly.express as px

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig, use_container_width=True)

#Region Sales Chart
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Regional Sales Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

#Top Products
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    top_products,
    x="Product Name",
    y="Sales",
    title="Top 10 Products"
)

st.plotly_chart(fig3, use_container_width=True)

