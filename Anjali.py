import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Mutual Funds Explorer", layout="wide")

# Title
st.title("📊 Mutual Funds Performance in India")

# Load dataset from GitHub raw URL
DATA_URL = "https://raw.githubusercontent.com/yourusername/yourrepo/main/Datasets/mutual_funds_india.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df.columns = df.columns.str.replace(" ", "")
    return df

df = load_data(DATA_URL)

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

# Category selection
categories = df["category"].dropna().unique()
selected_category = st.sidebar.selectbox("Select Category", sorted(categories))

# Filter by category
filtered_df = df[df["category"] == selected_category]

# AMC selection
amcs = filtered_df["AMC_name"].dropna().unique()
selected_amc = st.sidebar.selectbox("Select AMC", sorted(amcs))

# Filt

