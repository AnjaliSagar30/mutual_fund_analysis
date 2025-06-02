import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page settings
st.set_page_config(page_title="Mutual Funds Performance", layout="wide")

# Title
st.title("📊 Mutual Funds Performance in India")

# Load local CSV file
@st.cache_data
def load_data():
    df = pd.read_csv("mutual_funds_india.csv")  # Adjust path if needed
    df.columns = df.columns.str.replace(" ", "")  # Remove spaces from column names
    return df

# Load data
try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ CSV file not found. Please check the file path: `Datasets/mutual_funds_india.csv`.")
    st.stop()

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

# Category filter
categories = df["category"].dropna().unique()
selected_category = st.sidebar.selectbox("Select Category", sorted(categories))

# Filter by category
filtered_df = df[df["category"] == selected_category]

# AMC filter
amcs = filtered_df["AMC_name"].dropna().unique()
selected_amc = st.sidebar.selectbox("Select AMC", sorted(amcs))

# Filter by AMC
final_df = filtered_df[filtered_df["AMC_name"] == selected_amc]

# Display data table
st.subheader(f"📋 Mutual Funds in Category: **{selected_category}** | AMC: **{selected_amc}**")
st.dataframe(final_df[["MutualFundName", "return_1yr"]].reset_index(drop=True), use_container_width=True)

# Bar Chart
if not final_df.empty:
    st.subheader("📈 1-Year Returns")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=final_df, x="MutualFundName", y="return_1yr", palette="winter", ax=ax)
    ax.set_ylabel("Return (%)")
    ax.set_xlabel("Mutual Fund")
    plt.xticks(rotation=90)
    st.pyplot(fig)
else:
    st.warning("⚠️ No mutual funds found for this selection.")

