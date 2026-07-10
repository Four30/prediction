import glob
import camelot
import pandas as pd

path = "chem_gt\\june_and_nov"
filenames = glob.glob(path + "/*.pdf")
print(filenames)
all_the_tables = []

for file in filenames:
    
    tables = camelot.read_pdf(file, flavor = "hybrid", pages = "1")
    all_the_tables.append(tables[0].df)
#print(all_the_tables)
p21_snippets = []
for dataframe in all_the_tables:
    p21_snippets.append(dataframe.iloc[7:8,:])
#print(p21_snippets)


p21 = pd.concat(p21_snippets, axis = 0, ignore_index = "true")
p21.columns =["comp","max","A","B","C","D","E"]
print(p21)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p21 = p21[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p21 = p21.median()
mean_p21 = p21.mean()
