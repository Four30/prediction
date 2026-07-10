import glob
import camelot
import pandas as pd

path = "chem_gt\\june_and_nov"
filenames = glob.glob(path + "/*.pdf")
path1 = "chem_gt\\wmarch"
#filenames.append(glob.glob(path + "/*.pdf"))
#print(filenames)
filenames1 = glob.glob(path1 + "/*.pdf")
print(filenames1)
all_the_tables = []

for file in filenames:
    
    tables = camelot.read_pdf(file, flavor = "hybrid", pages = "1")
    all_the_tables.append(tables[0].df)
#print(all_the_tables)
all_the_tables1 = []
for file in filenames1:
    
    tables = camelot.read_pdf(file, flavor = "hybrid", pages = "1")
    all_the_tables1.append(tables[0].df)
#print(all_the_tables)

p12_snippets = []
for dataframe in all_the_tables:
    p12_snippets.append(dataframe.iloc[5:6,:])
print(p12_snippets)

p12_snippets1 = []
for dataframe in all_the_tables1:
    p12_snippets1.append(dataframe.iloc[4:5,:])
print(p12_snippets1)

p12 = pd.concat(p12_snippets, axis = 0, ignore_index = "true")
#p12.columns =["comp","max","A","B","C","D","E"]
print(p12)

p122 = pd.concat(p12_snippets1, axis = 0, ignore_index = "true")
#p122.columns =["comp","max","A","B","C","D","E"]
print(p122)
p12.join(p122)
print(p12)
#numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
#p12 = p12[numeric_cols].apply(pd.to_numeric, errors='coerce')
#median_p12 = p12.median()
#mean_p12 = p12.mean()
