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
p32_snippets = []
for dataframe in all_the_tables:
    p32_snippets.append(dataframe.iloc[11:12,:])
#print(p32_snippets)


p32 = pd.concat(p32_snippets, axis = 0, ignore_index = "true")
p32.columns =["comp","max","A","B","C","D","E"]
#p32.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p32)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p32 = p32[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p32 = p32.median()
mean_p32 =round( p32.mean(), 0)

print(median_p32)
print(mean_p32)