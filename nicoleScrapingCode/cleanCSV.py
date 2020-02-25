import pandas as pd 
import glob
import re
import os

os.chdir('../glassDoorReviews')

# #create a new column, location, with the country information of the file name in that column
# fileNames = [i for i in glob.glob('Data Analyst*.csv')]

# # for each entry in filenames, read the file into a dataframe, and add another column to that dataframe pertaining to location (extract country info from filename)
# for file in fileNames:
#     df = pd.read_csv(file)
#     pattern = re.compile("Salaries (.*).csv")
#     result = pattern.search(file)
#     countryName = str(result.group(1))
#     print(countryName)
#     countrNameWithoutNumber = countryName
#     df['location'] = countryName

#     df.to_csv("Data Analyst Salaries in " + countryName + ".csv")

# combining files together
# fileNames = [i for i in glob.glob('Data Analyst Salaries in United States*.csv')]

# combined_csv = pd.concat([pd.read_csv(f) for f in fileNames])

# combined_csv.to_csv("Data Analyst Salaries in United States-Final.csv", index=False, encoding='utf-8-sig')

# Getting only country name in location column (without #)
# df = pd.read_csv("Data Analyst Salaries in United States-Final.csv")
# df['location'] = df['location'].apply(lambda x: re.sub("United States[0-9]", "United States", x))
# df.to_csv("Data Analyst Salaries in United States.csv")



# cleaning up columns - removing unnamed columns
df = pd.read_csv("Data-Professional-Salaries-Master.csv")
df_new = df.drop(columns=['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1'])
df_new.to_csv("Data-Professional-Salaries-Master.csv", index=False)