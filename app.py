import streamlit as st
import pandas as pd
import plotly.express as px
import time
from pypdf import PdfReader

# 1. Page Configuration
st.set_page_config(page_title="SpendLens Analytics", page_icon="💳", layout="wide")


# --- CSS HACK: Hide the "Limit 200MB" text ---
hide_file_uploader_limit = """
<style>
    [data-testid="stFileUploader"] small {
        display: none;
    }
</style>
"""
st.markdown(hide_file_uploader_limit, unsafe_allow_html=True)

# 2. Hero Image (Finance Theme)
st.image("https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&w=800&q=80", use_container_width=True)

# 3. Title and Intro
st.title("SpendLens: Personal Finance Analytics")
st.markdown("Upload your bank statement (CSV, Excel, or PDF) to see where your money goes.")

# --- HELPER FUNCTION: Categorize Expenses ---
def categorize_transaction(description):
    description = str(description).lower()
    if any(word in description for word in ['uber', 'ola', 'rapido', 'fuel', 'petrol', 'parking', 'shell']):
        return 'Transport'
    elif any(word in description for word in ['zomato', 'swiggy', 'blinkit', 'zepto', 'restaurant', 'cafe', 'chai', 'coffee', 'grocery', 'bigbasket', 'mcdonalds']):
        return 'Food'
    elif any(word in description for word in ['netflix', 'hotstar', 'spotify', 'cinema', 'pvr', 'inox', 'bookmyshow']):
        return 'Entertainment'
    elif any(word in description for word in ['amazon', 'flipkart', 'myntra', 'shopping', 'zara', 'h&m', 'nike']):
        return 'Shopping'
    elif any(word in description for word in ['salary', 'credit', 'deposit', 'upi received']):
        return 'Income'
    elif any(word in description for word in ['bill', 'electricity', 'bescom', 'recharge', 'jio', 'airtel', 'wifi']):
        return 'Utilities'
    else:
        return 'Mazboori'  # Replaced 'Other' with 'Mazboori'

# 4. File Uploader (Now accepts PDF)
uploaded_file = st.file_uploader("Upload your bank statement:", type=["csv", "xlsx", "pdf"])

# 5. Main Logic
if uploaded_file is not None:
    # --- THE MONEY SPINNER ---
    with st.spinner("💸 Crunching your numbers... Counting coins..."):
        time.sleep(1.5)  # Optional: Small delay so user sees the animation
        
        try:
            # Handle CSV and Excel
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                valid_data = True
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
                valid_data = True
            # Handle PDF (Text Extraction Only)
            elif uploaded_file.name.endswith('.pdf'):
                valid_data = False
                reader = PdfReader(uploaded_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                st.success("PDF loaded successfully!")
                st.warning("⚠️ PDF analysis is limited to text extraction. For charts, please upload CSV/Excel.")
                st.subheader("📄 PDF Content Preview")
                st.text_area("Extracted Text", text, height=300)

            if valid_data:
                st.success("Analysis Complete!")
                
                # --- DATA PROCESSING ---
                # Add a 'Category' column
                df['Category'] = df['Description'].apply(categorize_transaction)
                
                # Filter for Debits (Spending) only
                spending_df = df[df['Transaction Type'] == 'Debit'].copy()
                
                # --- VISUALIZATION ---
                st.subheader("💸 Spending by Category")
                
                # Group data for the chart
                category_totals = spending_df.groupby('Category')['Amount'].sum().reset_index()
                
                # Create a Donut Chart using Plotly
                fig = px.pie(category_totals, values='Amount', names='Category', hole=0.4, 
                             title='Where did the money go?',
                             color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig)
                
                # --- DETAILED TABLE ---
                st.subheader("📋 Transaction Details")
                st.dataframe(df)
                
                # --- SUMMARY METRICS ---
                total_spent = spending_df['Amount'].sum()
                
                # Create columns for nice metric display
                col1, col2 = st.columns(2)
                col1.metric(label="Total Transactions", value=len(df))
                # UPDATED: Uses the Indian Rupee Symbol ₹
                col2.metric(label="Total Spent", value=f"₹{total_spent:,.2f}")
            
        except Exception as e:
            st.error(f"Error processing file: {e}")
            if not uploaded_file.name.endswith('.pdf'):
                st.info("Make sure your CSV/Excel has columns: Date, Description, Amount, Transaction Type")

else:
    st.info("Please upload a CSV, Excel, or PDF file to get started.")

# Footer
st.markdown("---")

st.caption("Budget Buddy • Built by Sumanta Pani")


