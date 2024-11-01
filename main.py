#Personal Finance Tracker App - Group 4
#Collaborators
# -Grace Jeong
# -Cristian Camilo Salamanca
# -Sebastian Melendez

# import the main libraries
from datetime import datetime
import pandas as pd
import CSV_handling
import Globals
import data_anlaysis
import data_management
import visualization
import budget_management
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
        print("10. Save Transactions to CSV")
        print("11. Set Category Budget")
        print("12. View Budget Status")
        print("13. Exit")
        request = input("Select an action:" ).strip()
        if request == "0":
            CSV_handling.load_transaction()
        elif request == "1":
            data_management.view_all_transactions()
        elif request == "2":
            data_management.view_transactions_by_date_range()
        elif request == "3":
            data_management.add_transaction()
        elif request == "4":
            data_management.edit_transaction()
        elif request == "5":
            data_management.delete_transaction()
        elif request == "6":
            data_anlaysis.analyze_spending_by_category()
        elif request == "7":
            data_anlaysis.calculate_average_monthly()
        elif request == "8":
            data_anlaysis.top_spending_category()
        elif request == "9":
            visualization.trend_analysis()
        elif request == "10":
            if Globals.changes_unsaved:
                CSV_handling.save_transactions()
            else:
                print("Data has no changes to save")
        elif request == "11":
            budget_management.set_budget()
        elif request == "12":
            budget_management.budget_exceeds()
        elif request == "13":
            if Globals.changes_unsaved:
                save_user = input("You have unsaved changes. Would you like to save before exiting? (Y/N): ").strip().lower()
                if save_user == 'y':
                    CSV_handling.save_transactions()  # save changes if user chooses
                elif save_user == 'n':
                    print("Exiting without saving.")

            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid option.")




main()