import Globals
import pandas as pd


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




def save_transactions():
    if Globals.transaction_df.empty:
        print("Personal finance tracker has no transaction. No file saved.\n")
        return
    Globals.transaction_df.to_csv('Personal_finance_tracker.csv',index=False)
    print(f"Task saved to Personal_finance_tracker.csv.\n")
    Globals.changes_unsaved = False