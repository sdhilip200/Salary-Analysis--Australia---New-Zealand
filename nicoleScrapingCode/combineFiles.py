import os
import glob
import pandas as pd

extension = '.csv'

os.chdir('../glassDoorReviews')

fileNames = [i for i in glob.glob('Data*.csv')]

combined_csv = pd.concat([pd.read_csv(f) for f in fileNames])

combined_csv.to_csv("Data-Professional-Salaries-Master.csv", index=False, encoding='utf-8-sig')
