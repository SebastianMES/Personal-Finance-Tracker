# data management

import pandas as pd
from datetime import datetime
import Globals


#global valuable
# define dataframe with required columns if needed
Globals.transaction_df = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
# transaction_df = pd.DataFrame(columns=['Date','Category', 'Description', 'Amount','Type'])
today_date = datetime.today().date()
changes_unsaved = False

# 1. view transactions by date range
# filter and display transactions within a specified date range.

# transactions = pd.DataFrame(data)
# transactions['data'] = pd.to_datetime(transactions['date'])
def view_transactions_by_date_range():
    # datetime format
    Globals.transaction_df['Date'] = pd.to_datetime(Globals.transaction_df['Date'], errors='coerce')
    min_date = Globals.transaction_df["Date"].min()
    max_date = Globals.transaction_df["Date"].max()

    if Globals.transaction_df.empty:
        print("No data available to filter.")
    while True:
        try:
            start_date = pd.to_datetime(input("Enter the start date (YYYY-MM-DD): "), format= "%Y-%m-%d")
            if start_date < min_date or start_date > max_date:
                print(f"Invalid input. Please enter a date between {min_date.date()} and {max_date.date()}.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter the date in YYYY-MM-DD format")

    while True:
        try:
            end_date = pd.to_datetime(input("Enter the end date (YYYY-MM-DD): "), format="%Y-%m-%d")
            if end_date < start_date or end_date > max_date:
                print(f"Invalid input. Please enter a date between {start_date.date()} and {max_date.date()}.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter the date in YYYY-MM-DD format")

    # filter transactions within the specified date range
    filtered_transactions = Globals.transaction_df[(Globals.transaction_df['Date'] >= start_date) &
                                                   (Globals.transaction_df['Date'] <= end_date)]

    if not filtered_transactions.empty:
        print(filtered_transactions.to_string(index=True))

    else:
        print("No transactions found within the specified date range.")

# print(filtered_transactions)

# add a transaction
# with details like date, category, description, and amount
def add_transaction():

    while True:
        transaction = input("Do you want to add a transaction? (Y,N): ").strip()
        if transaction.upper() == 'Y':
            create()
        elif transaction.upper() == 'N':
            print("No transaction added.")
            break
        else:
            print("Invalid input. Please enter a valid answer (Y,N).")
            continue


def get_date():
    date = get_date
    while True:
        try:
            date_input = pd.to_datetime(input("Enter the date of the transaction (YYYY-MM-DD): "), format="%Y-%m-%d")
            return date_input.strftime("%Y-%m-%D")   #back into a string format/consistent format #return formatted date if successful
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD.")



def get_category():
    while True:
        category_input = input("Enter a category of the transaction (e.g., Food, Rent): ").strip()
        if category_input.isalpha(): # check if the input consists only of letters
            return category_input
        else:
            print("Invalid input. Please enter a valid category.")
            continue



def get_description():
    return input("Enter a description of the transaction: ").strip()



def get_amount():
    while True:
        try:
            amount_input = float(input("Enter the transaction amount: ").strip())
            if amount_input > 0:
                return amount_input
            else:
                print("Amount must be positive. Please try again.")
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")


def get_type():
    while True:
        type_input = input("Enter a type of transaction (Expense or Income): ").strip().capitalize()
        if type_input in ["Expense", "Income"]:
            return  type_input
        else:
            print("Invalid type. Please enter a valid input. (Expense or Income)")


# making a new transaction

def new_transaction(date_obj, category_input, description_input, amount_input, type_input):
    new =  pd.DataFrame({
        "Date": [date_obj],
        "Category": [category_input],
        "Description": [description_input],
        "Amount": [amount_input],
        "Type": [type_input]
    })


    Globals.transaction_df = pd.concat([Globals.transaction_df, new], ignore_index=True)
    print("Transaction added successfully.")



def create():
    date_obj = get_date()
    category_input = get_category()
    description_input = get_description()
    amount_input = get_amount()
    type_input = get_type()

    new_transaction(date_obj, category_input, description_input, amount_input, type_input)

def edit_transaction(index, date=None, category=None, description=None, amount=None):
    while True:
        print(view_transactions_by_date_range())


def view_all_transactions():
    return print(Globals.transaction_df)
