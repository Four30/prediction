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
p22_snippets = []
for dataframe in all_the_tables:
    p22_snippets.append(dataframe.iloc[8:9,:])
#print(p22_snippets)


p22 = pd.concat(p22_snippets, axis = 0, ignore_index = "true")
p22.columns =["comp","max","A","B","C","D","E"]
#p22.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p22)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p22 = p22[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p22 = p22.median()
mean_p22 =round( p22.mean(), 0)

print(median_p22)
print(mean_p22)