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
all_sales['Month'] = all_sales['Order Date'].str.split('/').str[0]
all_sales['Price'] = all_sales['Quantity Ordered'] * all_sales['Price Each']
sales_by_month = all_sales.groupby('Month')['Price'].sum()

### Bar Graph ###
# plt.bar(range(1,13), sales_by_month)
# plt.show()


# City with highest number of sales
all_sales['City'] = (all_sales['Purchase Address'].str.split(', ').str[1]) + " (" + (all_sales['Purchase Address'].str.split(', ').str[2].str[:2]) + ')'
sales_by_city = all_sales.groupby('City')['Price'].sum()

### Bar Graph ###
# keys = sales_by_city.reset_index()['City']
# plt.bar(keys, sales_by_city)
# plt.xlabel('City')
# plt.xticks(keys, rotation='vertical', size=8)
# plt.ylabel('Sales')
# plt.show()
