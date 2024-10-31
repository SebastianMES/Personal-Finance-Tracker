#### Budget Setting and Alerts:
# -Users can set a budget for specific categories (e.g., Food, Rent, Utilities) or an overall monthly budget.
# -The app will compare spending against the budget:
#    If spending exceeds the budget, it will alert the user with a message.
#    If spending is close to the budget (e.g., within 10%), it will warn the user.
import Globals
import pandas as pd

category_budgets = {}
overall_monthly_budget = None

def set_budget():

    global overall_monthly_budget

    print("Set Budget")
    print("1. Set a Category Budget")
    print("2. Set Overall Monthly Budget")
    option = input("Choose an option (1-2): ")

    if option == "1":

        # Set a budget for a specific category
        category = input("Enter the category (Food, Rent, Utilities...): ").strip()
        amount = float(input(f"Enter the budget amount for {category}:"))
        category_budgets[category] = amount
        print(f"Budget set for {category}: ${amount:}")

    elif option == "2":

        # Set an overall monthly budget
        overall_monthly_budget = float(input("Enter the overall monthly budget: $"))
        print(f"Overall monthly budget: ${overall_monthly_budget:}")

    else:
        print("Invalid choice.")



def budget_exceeds():

    if Globals.transaction_df.empty:
        print("No transactions available to analyze spending against the budget.")
        return

    print("Check Budget Status")

    category_spending = Globals.transaction_df.groupby('Category')['Amount'].sum()
    total_spending1 = category_spending.sum()

    # Check the spending by category
    for category, budget in category_budgets.items():
        spent = category_spending.get(category, 0)

        if spent > budget:
            print(f"ALERT!!!! Spending on {category} (${spent}) has exceeded the budget (${budget})")
        elif spent > 0.10 * budget:
            print(f"WARNING: Spending on {category} (${spent}) is close to the budget (${budget}).")
        else:
            print(f"{category}: Spending (${spent}) is within budget (${budget}).")

