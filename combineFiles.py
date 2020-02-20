import os
import glob
import pandas as pd

extension = '.csv'

os.chdir('glassDoorReviews')

fileNames = [i for i in glob.glob('Data Analyst Salaries in New Zealand*.csv')]

combined_csv = pd.concat([pd.read_csv(f) for f in fileNames])

combined_csv.to_csv("Data Analyst Salaries in New Zealand.csv", index=False, encoding='utf-8-sig')
