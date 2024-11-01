# data management

import pandas as pd
from datetime import datetime

from PIL.ImageStat import Global
from numpy.ma.extras import row_stack

import Globals

# Load data from the CSV file
file_path = 'sampledata.csv'  # or provide the full path if it’s in a different directory
data = pd.read_csv(file_path)

# Display the data to confirm it loaded correctly
print(data)


from numpy.f2py.crackfortran import true_intent_list

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
view_transactions_by_date_range()

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

add_transaction()

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
    if Globals.transaction_df.empty:
        print("No transactions available to edit.")

    print("Current Transactions: ")
    print(Globals.transaction_df.to_string(index=True))

    while True:
        try:
            row_index = int(input("Please enter an index number of transaction you want to edit: "))
            if row_index not in Globals.transaction_df.index:
                print("Invalid index. Please enter a valid index.")
                continue
            else:
                break
        except ValueError:
                print("Invalid input. Please enter a numeric index.")

    print("\nSelected Transaction: ")
    print(Globals.transaction_df.loc[row_index].to_string())

    while True:
        current_date = Globals.transaction_df.at[row_index, 'Date']
        try:
            new_date = input("Enter the new date (YYYY-MM-DD) or press Enter to keep the current date.").strip()
            if new_date:
                # convert new_date to a datetime object
                new_date_converted = pd.to_datetime(new_date, format="%Y-%m-%d", error='raise')
                Globals.transaction_df.at[row_index, 'Date'] = new_date_converted
                print(f"Date updated successfully to {new_date_converted.date()}.")
                break
            else:
                print(f"No new date entered. Keeping the current date: {current_date}.")
                break
        except ValueError:
            print("Invalid date format. Please input the date in YYYY-MM-DD format.")
    print(Globals.transaction_df)


    while True:
        current_category = Globals.transaction_df.at[row_index, 'Category']
        new_category = input("Enter the new category or press Enter to keep the current category.")
        if new_category:
            Globals.transaction_df.at[row_index, 'Category'] = new_category
            print(f"Category updated successfully to {new_category.capitalize()}.")
            break
        else:
            print(f"No new category entered. Keeping the current category: {current_category}.")
            break
    print(Globals.transaction_df)

    while True:
        current_description = Globals.transaction_df.at[row_index, 'Description']
        new_description = input("Enter the new description or press Enter to keep the current description.")
        if new_description:
            Globals.transaction_df.at[row_index, 'Description'] = new_description.capitalize()
            print(f"Description updated successfully to {new_description.capitalize()}.")
            break
        else:
            print(f"No new description entered. Keeping the current description: {current_description}.")
            break
    print(Globals.transaction_df)

    while True:
        current_amount = Globals.transaction_df.at[row_index, 'Amount']
        new_amount = input("Enter the new amount or press Enter to keep the current amount.")
        if new_amount.isdigit():
            Globals.transaction_df.at[row_index, 'Amount'] = new_amount
            print(f"Amount updated successfully to {new_amount:.2f}.")
            break
        if not new_amount > 0
            print("Invalid input. The amount must be a positive number. Please try again.")
            continue
        else:
            print(f"No new amount entered. Keeping the current amount: {current_amount}.")
    print(Globals.transaction_df)

    while True:
        current_type = Globals.transaction_df.at[row_index, 'Type']
        try:
            new_type = input("Enter the new type (Expense or Income) or press Enter to keep the current type.").strip()
            if new_type == "":
                print(f"No new type entered. Keeping the current type: {current_type}.")
                break
            if new_type.capitalize() == ['Expense' or 'Income']:
                Globals.transaction_df.at[row_index, 'Type'] = new_type.capitalize()
                print(f"Type updated successfully to {new_type.capitalize()}.")
                break
            else:
                print("Invalid input. Please enter a type either 'Expense' or 'Income'.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print(Globals.transaction_df)

def delete_transaction():
