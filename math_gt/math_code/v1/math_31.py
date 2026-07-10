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
p31_snippets = []
for dataframe in all_the_tables:
    p31_snippets.append(dataframe.iloc[10:11,:])
#print(p31_snippets)


p31 = pd.concat(p31_snippets, axis = 0, ignore_index = "true")
p31.columns =["comp","max","A","B","C","D","E"]
#p31.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p31)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p31 = p31[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p31 = p31.median()
mean_p31 =round( p31.mean(), 0)

print(median_p31)
print(mean_p31)