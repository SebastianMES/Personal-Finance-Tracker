# data management

import pandas as pd
from datetime import datetime
import Globals

#global valuable
# define dataframe with required columns if needed


# 1. view transactions by date range
# filter and display transactions within a specified date range.

def view_all_transactions():
    Globals.transaction_df['Date'] = pd.to_datetime(Globals.transaction_df["Date"],format="%d/%m/%Y")
    return print(Globals.transaction_df.to_string(index=True))

def view_transactions_by_date_range():
    # datetime format
    Globals.transaction_df['Date'] = pd.to_datetime(Globals.transaction_df["Date"],format="%d/%m/%Y")
    print(Globals.transaction_df.to_string(index=True))
    min_date = Globals.transaction_df["Date"].min()
    max_date = Globals.transaction_df["Date"].max()
    if Globals.transaction_df.empty:
        print("No data available to filter.")
        return
    while True:
        try:
            start_date = pd.to_datetime(input("Enter the start date (DD/MM/YYYY): "), format= "%d/%m/%Y")
            if start_date < min_date or start_date > max_date:
                print(f"Invalid input. Please enter a date between {min_date.date()} and {max_date.date()}.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter the date in DD/MM/YYYY format")

    while True:
        try:
            end_date = pd.to_datetime(input("Enter the end date (DD/MM/YYYY): "), format="%d/%m/%Y")
            if end_date < start_date or end_date > max_date:
                print(f"Invalid input. Please enter a date between {start_date.date()} and {max_date.date()}.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter the date in DD/MM/YYYY format")
    # filter transactions within the specified date range
    filtered_transactions = Globals.transaction_df[(Globals.transaction_df['Date'] >= start_date) &
                                                   (Globals.transaction_df['Date'] <= end_date)]
    if not filtered_transactions.empty:
        print(filtered_transactions.to_string(index=True))
    else:
        print("No transactions found within the specified date range.")

# add a transaction with details like date, category, description, and amount
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

    while True:
        try:
            date_input = pd.to_datetime(input("Enter the date of the transaction (DD/MM/YYYY): "), format="%d/%m/%Y")
            return date_input.strftime("%d/%m/%Y")   #back into a string format/consistent format #return formatted date if successful
        except ValueError:
            print("Invalid date format. Please enter the date in DD/MM/YYYY.")

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
    Globals.changes_unsaved = True

def edit_transaction():
    Globals.transaction_df['Date'] = pd.to_datetime(Globals.transaction_df["Date"],format="%d/%m/%Y")
    Globals.transaction_df['Date'] = Globals.transaction_df['Date'].dt.strftime('%d/%m/%Y')
    if Globals.transaction_df.empty:
        print("No transactions available to edit.")
    else:
        print("Current Transactions: ")
        print(print(Globals.transaction_df.to_string(index=True)))
        while True:
            try:
                row_index = int(input("Please enter an index number of transaction you want to edit: "))
                if row_index not in Globals.transaction_df.index:
                    print("Invalid index. Please enter a valid index.")
                    continue
                else:
                    print("\nSelected Transaction: ")
                    print(Globals.transaction_df.loc[row_index].to_string())
                    while True:
                    # Editing Date
                        current_date = Globals.transaction_df.at[row_index, 'Date']
                        new_date = input("Input the new date (DD/MM/YYYY) or press Enter to keep the current date: ").strip()
                        if new_date:
                            try:
                                # convert new_date to a datetime object
                                new_date_converted = pd.to_datetime(new_date, format="%d/%m/%Y", errors='raise')
                                Globals.transaction_df.at[row_index, 'Date'] = new_date_converted.strftime("%d/%m/%Y")
                                print(f"Date updated successfully to {new_date_converted}.")

                            except ValueError:
                                print("Invalid date format. Please input the date in DD/MM/YYYY.")
                                continue
                        else:
                            print(f"No new date entered. Keeping the current date: {current_date}.")

                        print("\n", Globals.transaction_df.loc[row_index].to_string())
                        break

                    # Editing Category
                    current_category = Globals.transaction_df.at[row_index, 'Category']
                    new_category = input("Input the new category or press Enter to keep the current category: ")
                    if new_category:
                        Globals.transaction_df.at[row_index, 'Category'] = new_category.capitalize()
                        print(f"Category updated successfully to {new_category.capitalize()}.")
                    else:
                        print(f"No new category entered. Keeping the current category: {current_category}.")
                    print("\n", Globals.transaction_df.loc[row_index].to_string())

                    # Editing Description
                    current_description = Globals.transaction_df.at[row_index, 'Description']
                    new_description = input("Input the new description or press Enter to keep the current description: ")
                    if new_description:
                        Globals.transaction_df.at[row_index, 'Description'] = new_description.capitalize()
                        print(f"Description updated successfully to {new_description.capitalize()}.")
                    else:
                        print(f"No new description entered. Keeping the current description: {current_description}.")
                    print("\n", Globals.transaction_df.loc[row_index].to_string())

                    while True:
                        # Editing Amount
                        current_amount = Globals.transaction_df.at[row_index, 'Amount']
                        new_amount = input("Input the new amount or press Enter to keep the current amount: ")
                        if new_amount:
                            try:
                                new_amount_float = float(new_amount)
                                if new_amount_float <= 0:
                                    print("Invalid input. The amount must be a positive number. Please try again.")
                                    continue  # to avoid proceeding further if amount is invalid
                                Globals.transaction_df.at[row_index, 'Amount'] = round(new_amount_float, 2)
                                print(f"Amount updated successfully to {new_amount_float:.2f}.")
                            except ValueError:
                                print("Invalid input. Please enter a numeric value for the amount.")
                                continue
                        else:
                            print(f"No new amount entered. Keeping the current amount: {current_amount}.")
                        print("\n", Globals.transaction_df.loc[row_index].to_string())
                        break

                    while True:
                        # Editing Type
                        current_type = Globals.transaction_df.at[row_index, 'Type']
                        new_type = input("Input the new type (Expense or Income) or press Enter to keep the current type: ").strip()
                        if new_type:
                            if new_type.capitalize() in ['Expense', 'Income']:
                                Globals.transaction_df.at[row_index, 'Type'] = new_type.capitalize()
                                print(f"Type updated successfully to {new_type.capitalize()}.")
                            else:
                                print("Invalid input. Please enter a type either 'Expense' or 'Income'.")
                                continue
                        else:
                            print(f"No new type entered. Keeping the current type: {current_type}.")
                        print("\n", Globals.transaction_df.loc[row_index].to_string())
                        break
            except ValueError:
                    print("Invalid input. Please enter a numeric index.")
            print()
            print("Updated Transactions:")
            print(Globals.transaction_df.to_string(index=True))
            Globals.changes_unsaved = True
            break


def delete_transaction():
    if Globals.transaction_df.empty:
        print("There's no transactions to analyze")
        return

    while True:  # validate the transaction row
        try:
            row = int(input("Enter the number of the transaction you want to delete: "))
            if 0 <= row <= (len(Globals.transaction_df) - 1):
                break
            else:
                print("Enter a valid number of transaction.")
        except ValueError:
            print("Enter a valid number of transaction.")

    transactions = Globals.transaction_df.drop(row).reset_index(drop=True)  # print the transaction details
    Globals.changes_unsaved = True
    print("Transaction deleted successfully!")