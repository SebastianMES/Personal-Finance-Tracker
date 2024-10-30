#Personal Finance Tracker App - Group 4
#Collaborators
# -Grace Jeong
# -Cristian Camilo Salamanca
# -Sebastian Melendez

# import the main libraries
from datetime import datetime
import pandas as pd
import CSV_handling
# global variables:
transaction_df = pd.DataFrame(columns=['Date','Category', 'Description', 'Amount','Type'])
today_date = datetime.today().date()
changes_unsaved = False

def main():
    while True:
        print("Personal Finance Tracker Application")
        print("0. Import a CSV File")
        print("1. View All Transactions")
        print("2. View Transactions by Data Range")
        print("3. Add a Transaction")
        print("4. Edit a Transaction")
        print("5. Delete a Transaction")
        print("6. Analyze Spending by Category")
        print("7. Calculate Average Monthly Spending")
        print("8. Show Top Spending Category")
        print("9. Visualize Monthly Spending Trend")
        print("Save Transactions to CSV")
        print("11. Exit")
        request = input("Select an action:" ).strip()
        if request == "0":
            CSV_handling.load_transaction()
        break


main()