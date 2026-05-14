import streamlit as st
import pandas as pd


df = pd.read_csv("expenses.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Create Month column
df['Month'] = df['Date'].dt.month_name()

st.title("Expense Tracker Dashboard")



st.subheader("Dataset Preview")
st.dataframe(df.head())



st.subheader("Category Wise Spending")

category_spending = df.groupby('Category')['Amount'].sum()

st.bar_chart(category_spending)


st.subheader("Monthly Spending Trend")

monthly_spending = df.groupby('Month')['Amount'].sum()

st.line_chart(monthly_spending)


st.subheader("Expense Distribution")

st.dataframe(category_spending)

st.subheader("Insights")

highest_category = category_spending.idxmax()

average_expense = df['Amount'].mean()

st.success(f"Highest Spending Category: {highest_category}")

st.info(f"Average Expense: ₹{average_expense:.2f}")