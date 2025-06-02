import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Mutual Funds Explorer", layout="wide")

# Title
st.title("Mutual Funds Performance in India")

# Load the dataset
df = pd.read_csv("Datasets/mutual_funds_india.csv")
df.columns = df.columns.str.replace(" ", "")  # Clean column names

# Sidebar inputs
st.sidebar.header("Filter Options")
categories = df.category.unique()
cat = st.sidebar.selectbox("Select Fund Category", sorted(categories))

# Filter by category
filtered_cat = df[df.category == cat]
amcs = filtered_cat.AMC_name.unique()
mf = st.sidebar.selectbox("Select AMC Name", sorted(amcs))

# Filter by AMC
filtered_amc = filtered_cat[filtered_cat.AMC_name == mf]

# Show DataFrame preview
st.subheader(f"Funds under Category: **{cat}** and AMC: **{mf}**")
st.dataframe(filtered_amc[['MutualFundName', 'return_1yr']].reset_index(drop=True))

# Plotting
st.subheader("1-Year Return Bar Chart")
fig, ax = plt.subplots(figsize=(12, 6))
sb.barplot(x=filtered_amc.MutualFundName, y=filtered_amc.return_1yr, palette='winter', ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
