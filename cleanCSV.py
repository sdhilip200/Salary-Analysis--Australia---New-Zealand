import pandas as pd 

df = pd.read_csv('Data Scientist Salaries United States.csv')

print(df.columns)

print(df['payRange'].head(4))

newList = []

for value in df['payRange'].values:
    newValue = value.split("<")[1].split(">")[0]
    newList.append(newValue)
