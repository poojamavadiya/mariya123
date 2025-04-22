import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bank Transaction Analyzer",
    page_icon="🏦",
    layout="wide"
)

st.title("Bank Transaction Analyzer 🏦")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Show success message
        st.success("File successfully uploaded!")
        
        # Show basic information
        st.header("Data Overview")
        st.write("Number of records:", len(df))
        st.write("Columns:", list(df.columns))
        
        # Display first few rows
        st.header("First 5 rows of data")
        st.dataframe(df.head())
        
        # Basic statistics
        st.header("Basic Statistics")
        st.write(df.describe())
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Please upload a CSV file to begin analysis") 