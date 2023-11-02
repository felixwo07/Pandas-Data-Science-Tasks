import pandas as pd
import matplotlib.pyplot as plt

# Read csv
all_sales = pd.read_csv('all_data.csv')

# Data cleaning
all_sales = all_sales.dropna()
all_sales = all_sales[all_sales['Order Date'].str[0:2]!='Or']
all_sales['Quantity Ordered'] = pd.to_numeric(all_sales['Quantity Ordered'])
all_sales['Price Each'] = pd.to_numeric(all_sales['Price Each'])

# Best Month
all_sales['month'] = all_sales['Order Date'].str.split('/').str[0]
all_sales['price'] = all_sales['Quantity Ordered'] * all_sales['Price Each']
all_sales_by_month = all_sales.groupby('month')['price'].sum()

# show bar graph
# plt.bar(range(1,13), all_sales_by_month)
# plt.show()
