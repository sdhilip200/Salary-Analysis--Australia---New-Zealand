import pandas as pd 
import glob
import re
import os

os.chdir('glassDoorReviews')

# #create a new column, location, with the country information of the file name in that column
# fileNames = [i for i in glob.glob('Data Visualisation*.csv')]

# # for each entry in filenames, read the file into a dataframe, and add another column to that dataframe pertaining to location (extract country info from filename)
# for file in fileNames:
#     df = pd.read_csv(file)
#     pattern = re.compile("Salaries in (.*).csv")
#     result = pattern.search(file)
#     countryName = str(result.group(1))
#     df['location'] = countryName

#     df.to_csv("Data Visualisation Salaries in " + countryName + ".csv")

# # combining files together
# fileNames = [i for i in glob.glob('*.csv')]

# combined_csv = pd.concat([pd.read_csv(f) for f in fileNames])

# combined_csv.to_csv("Data-Professional-Salaries.csv", index=False, encoding='utf-8-sig')

# cleaning up columns - removing unnamed columns
# df = pd.read_csv("Data-Professional-Salaries.csv")
# df_new = df.drop(columns=['Unnamed: 0.1.1.1','Unnamed: 0.1.1.1.1'])
# df_new.to_csv("Data-Professional-Salaries-Master.csv", index=False)