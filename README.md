# Personal Finance Tracker App - Group 4

### Project Overview
The **Personal Finance Tracker App** is a Python application designed to help users track their personal finances. It allows users to manage their transactions, set budgets, and analyze spending trends across various categories.

### Collaborators
- Grace Jeong
- Cristian Camilo Salamanca
- Sebastian Melendez

### Features
- **CSV Import/Export**: Load and save transactions as a csv file.
- **Transaction Management**: Add, edit, view, and delete transactions.
- **Spending Analysis**: View spending by month, average spend by month, and highest spend by category.
- **Budgeting**: Set a category-specific budget and check spending.
- **Visualization**: Plot monthly spending trends, category spends and distributions.

### Requirements
- Python 3.7+  
- Required Libraries: `pandas`, `matplotlib`

## Setup Instructions

### In Bash
1. **Navigate to the Directory**:  
    cd personal-finance-tracker
2. **Clone the repository**:  
    git clone https://github.com/SebastianMES/Personal-Finance-Tracker.git
3. **Set up a Virtual Environment**:
    source .venv/bin/activate  #For linux or mac  
    .venv\Scripts\activate
4. **Install the requirements**:
    pip install -r requirements.txt  

## Usage

### Run the code in Bash
    python main.py

- The program will display a menu as followed for choosing the next actions:

| Command Number | Description                          |
|----------------|--------------------------------------|
| `0`            | Import a CSV file                   |
| `1`            | View all transactions               |
| `2`            | View transactions by date range     |
| `3`            | Add a transaction                   |
| `4`            | Edit a transaction                  |
| `5`            | Delete a transaction                |
| `6`            | Analyze spending by category        |
| `7`            | Calculate average monthly spending  |
| `8`            | Show top spending category          |
| `9`            | Visualize monthly spending trend    |
| `10`           | Save transactions to CSV            |
| `11`           | Set category budget                 |
| `12`           | View budget status                  |
| `13`           | Exit                                |

### Modules

The application is structured in modules where each action is stored in the respective python file:

1. CSV_handling.py
2. Globals.py
3. Data_management.py
4. data_analysis.py
5. visualization.py


## Enjoy the application and send suggestions through GitHub.