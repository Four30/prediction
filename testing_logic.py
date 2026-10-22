
import glob
import camelot
import pandas as pd



info = "9709\\9709_AS.csv"

df = pd.read_csv(info)
#print(df.columns)
df = df.drop(["Unnamed: 0"], axis='columns')
#print(df.dtypes)
#print(df)
#print(df.columns)
rows = df[df["Combo"].str.contains("12, 52", na=False, case = False)]

rows_mid = rows.median(numeric_only = True)
rows_mean = round(rows.mean(numeric_only = True),1)

print(rows_mean)
print(rows_mid)