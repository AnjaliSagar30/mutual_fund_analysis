
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="Mutual Funds Explorer", layout="wide")

# Title
st.title("📊 Mutual Funds Performance in India")

# Load data from GitHub (🔁 Replace this with your actual raw URL)
DATA_URL = "https://raw.githubusercontent.com/yourusername/yourrepo/main/Datasets/mutual_funds_india.csv"

# Load and clean the data
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip().str.replace(" ", "", regex=False)
    return df

# Load dataset
try:
    df = load_data(DATA_URL)
except Exception as e:
    st.error(f"Failed to load data from URL. Error: {e}")
    st.stop()

# Sidebar: Filter options
st.sidebar.header("🔍 Filter Options")

# Category selection
categories = df["category"].dropna().unique()
selected_category = st.sidebar.selectbox("Select Category", sorted(categories))

# Filter by selected category
df_category = df[df["category"] == selected_category]

# AMC selection
amcs = df_category["AMC_name"].dropna().unique()
selected_amc = st.sidebar.selectbox("Select AMC", sorted(amcs))

# Filter by selected AMC
df_filtered = df_category[df_category["AMC_name"] == selected_amc]

# Show filtered data
st.subheader(f"🎯 Funds in Category: **{selected_category}**, AMC: **{selected_amc}**")
st.dataframe(df_filtered[["MutualFundName", "return_1yr"]].reset_index(drop=True), use_container_width=True)

# Plot bar chart
if not df_filtered.empty:
    st.subheader("📈 1-Year Return Comparison")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_filtered, x="MutualFundName", y="return_1yr", palette="Blues_d", ax=ax)
    ax.set_ylabel("1-Year Return (%)")
    ax.set_xlabel("Mutual Fund")
    plt.xticks(rotation=90)
    st.pyplot(fig)
else:
    st.warning("⚠️ No data available for the selected filters.")
