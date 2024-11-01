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
    category_spending = plot_df.groupby("Category")["Amount"].sum().reset_index()
    #Create the figure with subplots
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    # Plot the trend
    axs[0].plot(monthly_spending["Month_Year"], monthly_spending["Amount"], marker="o", color="b", linestyle="-")
    axs[0].set_xlabel("Month-Year")
    axs[0].set_ylabel("Total Spending")
    axs[0].set_title("Monthly Spending Trend")
    #Plot the category bar chart
    axs[1].bar(category_spending["Category"],category_spending["Amount"],color = "#ADD8E6" , edgecolor = "black")
    axs[1].set_xlabel("Category")
    axs[1].set_ylabel("Amount")
    axs[1].set_title("Spending by Category")
    #Plot the pie chart
    axs[2].pie(category_spending["Amount"],labels=category_spending["Category"],autopct = "%1.1f%%")
    axs[2].set_title("Spending Distribution by Category")
    #plot the complete figure
    plt.tight_layout()
    plt.show()


