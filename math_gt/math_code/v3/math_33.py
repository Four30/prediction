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
p33_snippets = []
for dataframe in all_the_tables:
    p33_snippets.append(dataframe.iloc[12:13,:])
#print(p33_snippets)


p33 = pd.concat(p33_snippets, axis = 0, ignore_index = "true")
p33.columns =["comp","max","A","B","C","D","E"]
#p33.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p33)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p33 = p33[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p33 = p33.median()
mean_p33 =round( p33.mean(), 0)

print(median_p33)
print(mean_p33)