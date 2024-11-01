######## SPENDING ANALYSIS
# -Analyze Spending by Category: Display total spending for each category.
# -Calculate Average Monthly Spending: Show average spending per month.
# -Show Top Spending Category: Identify the category with the highest total spending.
from unicodedata import category

import Globals
import pandas as pd

# 1.Analyze Spending by Category:

def analyze_spending_by_category():
    if Globals.transaction_df.empty:
        print("There's no transactions to analyze")

    else:
        # Creating a variable to group only the amount and category
        spending_category = Globals.transaction_df.groupby("Category") ["Amount"].sum()
        print(spending_category)
        # Getting the total
        total_spending = spending_category.sum()
        print(f"Total expenses: {total_spending}")

# 2.Calculate Average Monthly Spending:

def calculate_average_monthly():
    if Globals.transaction_df.empty:
        print("There's no transactions to analyze")

    else:

        # changing the format
        Globals.transaction_df['Date'] = pd.to_datetime(Globals.transaction_df['Date'])

        # selecting the information for each month
        monthly_expenses = Globals.transaction_df.groupby(Globals.transaction_df['Date'].dt.to_period("M"))['Amount'].sum()

        # Total by month
        print("Monthly Expenses")
        print(monthly_expenses.apply(lambda x: f"${x}"))

        # Average by month
        average_monthly = monthly_expenses.mean()
        print(f"\nAverage Spending per Month: ${average_monthly}")
# 3.Show Top Spending Category:
def top_spending_category():

    if Globals.transaction_df.empty:
        print("There's no transactions to analyze")
    else:

        highest_category = Globals.transaction_df.groupby("Category") ["Amount"].max()
        print(f"The highest: {highest_category}")

