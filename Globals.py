import pandas as pd
from datetime import datetime
transaction_df = pd.DataFrame(columns=['Date','Category', 'Description', 'Amount','Type'])
today_date = datetime.today().date()
changes_unsaved = False