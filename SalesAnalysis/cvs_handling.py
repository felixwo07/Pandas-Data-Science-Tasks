import pandas as pd
import os

# read in csv's and write csv with all data

all_files = [file for file in os.listdir('./Sales_Data/')]
all_files_data = pd.DataFrame()
for file in all_files:
    df = pd.read_csv('./Sales_Data/'+file)
    all_files_data = pd.concat([all_files_data, df])

all_files_data.to_csv('all_data.csv', index=False)