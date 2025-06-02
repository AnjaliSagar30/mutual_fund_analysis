import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="Mutual Funds Explorer", layout="wide")

# Title
st.title("📊 Mutual Funds Performance in India")

# Load the dataset from GitHub (replace with your raw GitHub CSV URL)
url = "https://github.com/AnjaliSagar30/mutual_fund_analysis/blob/main/mutual_funds_india.csv"
df.columns = df.columns.str.replace(" ", "")  # Remove spaces in column names

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")

# Fund Category Selection
categories = df.category.dropna().unique()
cat = st.sidebar.selectbox("Select Fund Category", sorted(categories))

# Filter dataset by category
filtered_cat = df[df.category == cat]

# AMC Selection
amcs = filtered_cat.AMC_name.dropna().unique()
mf = st.sidebar.selectbox("Select AMC Name", sorted(amcs))

# Filter dataset by AMC
filtered_amc = filtered_cat[filtered_cat.AMC_name == mf]

# Show Data Table
st.subheader(f"Funds in Category: **{cat}** | AMC: **{mf}**")
st.dataframe(filtered_amc[['MutualFundName', 'return_1yr']].reset_index(drop=True), use_container_width=True)

# Bar Plot
st.subheader("📈 1-Year Return Comparison")

if not filtered_amc.empty:
    fig, ax = plt.subplots(figsize=(12, 6))
    sb.barplot(x=filtered_amc.MutualFundName, y=filtered_amc.return_1yr, palette='winter', ax=ax)
    plt.xticks(rotation=90)
    ax.set_ylabel("Return (%)")
    ax.set_xlabel("Mutual Fund Name")
    ax.set_title("1-Year Returns by Mutual Fund")
    st.pyplot(fig)
else:
    st.warning("No data available for the selected filters.")
