import Globals
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def trend_analysis():
    if Globals.transaction_df.empty:
        print("Personal finance tracker is empty. Trend can't be defined.")
        return
    Globals.transaction_df["Date"] = pd.to_datetime(Globals.transaction_df["Date"],format="%d/%m/%Y")
    plot_df = Globals.transaction_df.copy()
    plot_df["Month_Year"] = plot_df["Date"].dt.to_period("M").astype(str)
    monthly_spending = plot_df.groupby("Month_Year")["Amount"].sum().reset_index()
    #Plot the trend
    plt.plot(monthly_spending["Month_Year"], monthly_spending["Amount"], marker="o", color="b", linestyle="-")
    plt.xlabel("Month-Year")
    plt.ylabel("Total Spending")
    plt.title("Monthly Spending Trend")
    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.show()

    return