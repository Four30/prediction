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
print(all_the_tables)
p11_snippets = []
for dataframe in all_the_tables:
    p11_snippets.append(dataframe.iloc[4:5,:])
#print(p11_snippets)


p11 = pd.concat(p11_snippets, axis = 0, ignore_index = "true")
p11.columns =["comp","max","A","B","C","D","E"]
p11.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p11)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p11 = p11[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p11 = p11.median()
mean_p11 =round( p11.mean(), 0)