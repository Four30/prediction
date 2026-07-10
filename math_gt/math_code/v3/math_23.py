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
p23_snippets = []
for dataframe in all_the_tables:
    p23_snippets.append(dataframe.iloc[9:10,:])
#print(p23_snippets)


p23 = pd.concat(p23_snippets, axis = 0, ignore_index = "true")
p23.columns =["comp","max","A","B","C","D","E"]
#p23.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p23)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p23 = p23[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p23 = p23.median()
mean_p23 =round( p23.mean(), 0)

print(median_p23)
print(mean_p23)