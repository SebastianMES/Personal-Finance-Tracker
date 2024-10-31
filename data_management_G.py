# data management

import pandas as pd
from datetime import datetime
from numpy.f2py.crackfortran import true_intent_list

#global valuable
# check for required columns
transaction_df = pd.DataFrame(columns=['Date','Category', 'Description', 'Amount','Type'])
today_date = datetime.today().date()
changes_unsaved = False

# 1. view transactions by date range
# filter and display transactions within a specified date range.

# transactions = pd.DataFrame(data)
# transactions['data'] = pd.to_datetime(transactions['date'])


def load_transaction():
    while True:
        file = input("Enter the file name with csv extension:").strip()
        try:
            load_df= pd.read_csv(file)
            if not load_df.columns.equals(Globals.transaction_df.columns):
                print("Invalid input. The column names do not match. Please use another file.")
                continue  # Continue to the next iteration of the loop
            if Globals.transaction_df.empty:
                # Directly assign load_df if transaction_df is empty
                Globals.transaction_df = load_df
                print(Globals.transaction_df)
                print("File loaded successfully and data initialized.")

            else:
                # Concatenate only if transaction_df has existing data
                Globals.transaction_df = pd.concat([Globals.transaction_df, load_df], ignore_index=True)
                print("File loaded successfully and data concatenated.")
                print("File loaded successfully.")

            break


        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")

        except pd.errors.EmptyDataError:
            print("The file is empty. Please provide a valid file.")

        except pd.errors.ParserError:
            print("Error parsing file. Ensure it is a proper CSV file.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        break

# date range
# start_date = '2024-10-01'
# end_date = '2024-10-31'

def view_transactions_by_date_range(start_date, end_date):
    filtered_transactions = transactions[(transactions['date'] >= start_date) & (transactions['date'] <= end_date)]
    print(filtered_transactions)
    min_date = transactions["Date"].min()
    max_date = transactions["Date"].max()

    while True:
        try:
            start_date = pd.to_datetime(input("Enter the start date (YYYY-MM-DD): "), format= "%y-%m-%d")
            if start_date < min_date or start_date > max_date:
                print("Invalid input. Please enter the valid date range.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter the date in YYYY-MM-DD format")

    while True:
        try:
            end_date = pd.to_datetime(input("Enter the end date (YYYY-MM-DD)"))
            if end_date < min_date or end_date > max_date:
                print("Invalid input. Please enter the valid date range.")
                continue
            else:
                break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format")

# add a transaction
# with details like date, category, description, and amount
def add_transaction():

    while True:
        transaction = input("Do you want to add a transaction? (Y,N): ").strip()
        if transaction.upper() == 'Y':
            get_date()
        elif transaction.upper() == 'N':
            print("No transaction added.")
            break
        else:
            print("Invalid input. Please enter a valid answer (Y,N).")
            continue

def get_date():
    global transactions

    while True:
        date_input = input("Enter the date of the transaction (YYYY-MM-DD): ").strip()
        try:
            date_obj = datetime.strptime(date_input, "%Y-%M-%D") #ensure the obj is in the right format
            get_category()
            return date_obj.strftime("%Y-%M-%D")   #back into a string format/consistent format #return formatted date if successful

        except ValueError:
            print("Invalid date format. Please enter YYYY-MM-DD")

def get_category():
    while True:
        category_input = input("Enter a category of the transaction (e.g., Food, Rent): ").strip()
        if category_input.isalpha(): # check if the input consists only of letters
            get_description()
            break
        else:
            print("Invalid input. Please enter a valid category.")
            continue

def get_description():
    get_amount()
    return input("Enter a description of the transaction: ")


def get_amount():
    while True:
        try:
            amount_input = float(input("Enter the transaction amount: ").strip())
            if amount_input > 0:
                get_type()
                return amount_input
            else:
                print("Amount must be positive. Please try again.")
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")

def get_type():
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


    Global.transaction_df = pd.concat([new], ignore_index=True)
    print("Transaction added successfully.")



def create():
    date_obj = get_date()
    category_input = get_category()
    description_input = get_description()
    amount_input = get_amount()
    type_input = get_type()

    new_transaction(date_obj, category_input, description_input, amount_input, type_input)
