import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Generate Synthetic Dataset
# -----------------------------

categories = ['Food', 'Travel', 'Rent', 'Shopping', 'Entertainment', 'Bills']
payment_methods = ['UPI', 'Cash', 'Card']

data = []

start_date = datetime(2025, 1, 1)

for i in range(300):
    date = start_date + timedelta(days=random.randint(0, 120))

    category = random.choice(categories)

    amount = round(random.uniform(100, 10000), 2)

    payment = random.choice(payment_methods)

    data.append([date, category, amount, payment])

df = pd.DataFrame(data, columns=['Date', 'Category', 'Amount', 'Payment_Method'])

# Save Dataset
df.to_csv('expenses.csv', index=False)

print("Dataset Created Successfully")

# -----------------------------
# Data Cleaning
# -----------------------------

df.drop_duplicates(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month_name()

# -----------------------------
# Category Analysis
# -----------------------------

category_spending = df.groupby('Category')['Amount'].sum()

print("\nCategory Wise Spending")
print(category_spending)

# -----------------------------
# Monthly Trend
# -----------------------------

monthly_spending = df.groupby('Month')['Amount'].sum()

print("\nMonthly Spending")
print(monthly_spending)

# -----------------------------
# Overspending Detection
# -----------------------------

threshold = 8000

high_expenses = df[df['Amount'] > threshold]

print("\nHigh Expenses")
print(high_expenses)

# -----------------------------
# Visualization
# -----------------------------

plt.figure(figsize=(8,5))
category_spending.plot(kind='bar')
plt.title("Category Wise Spending")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("category_spending.png")
plt.show()

plt.figure(figsize=(8,8))
category_spending.plot(kind='pie', autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.ylabel("")
plt.savefig("expense_distribution.png")
plt.show()

plt.figure(figsize=(10,5))
monthly_spending.plot(kind='line', marker='o')
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.grid(True)
plt.savefig("monthly_trend.png")
plt.show()

# -----------------------------
# Insights
# -----------------------------

highest_category = category_spending.idxmax()

print(f"\nHighest Spending Category: {highest_category}")

average_spending = df['Amount'].mean()

print(f"Average Expense: ₹{average_spending:.2f}")