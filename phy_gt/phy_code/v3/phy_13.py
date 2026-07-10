import glob
import camelot
import pandas as pd

path = "phy_gt\\june_n_nov"
filenames = glob.glob(path + "/*.pdf")
#print(filenames)
all_the_tables = []

for file in filenames:
    
    tables = camelot.read_pdf(file, flavor = "hybrid", pages = "1")
    all_the_tables.append(tables[0].df)
#print(all_the_tables)
p13_snippets = []
for dataframe in all_the_tables:
    p13_snippets.append(dataframe.iloc[6:7,:])
#print(p13_snippets)


p13 = pd.concat(p13_snippets, axis = 0, ignore_index = "true")
p13.columns =["comp","max","A","B","C","D","E"]
p13.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p13)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p13 = p13[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p13 = p13.median()
mean_p13 = round(p13.mean(),0)
print(median_p13)
print(mean_p13)