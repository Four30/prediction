import glob
import camelot
import pandas as pd

path = "math_gt\\june_and_nov"
filenames = glob.glob(path + "/*.pdf")
#print(filenames)
all_the_tables = []

for file in filenames:
    
    tables = camelot.read_pdf(file, flavor = "hybrid", pages = "1")
    all_the_tables.append(tables[0].df)
#print(all_the_tables)
p12_snippets = []
for dataframe in all_the_tables:
    p12_snippets.append(dataframe.iloc[5:6,:])
#print(p12_snippets)


p12 = pd.concat(p12_snippets, axis = 0, ignore_index = "true")
p12.columns =["comp","max","A","B","C","D","E"]
#p12.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p12)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p12 = p12[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p12 = p12.median()
mean_p12 =round( p12.mean(), 0)

print(median_p12)