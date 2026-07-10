import glob
import camelot
import pandas as pd

path = "math_gt\\june_and_nov"
filenames = glob.glob(path + "/*.pdf")
#print(filenames)
all_the_tables = []

for file in filenames:
    tables = camelot.read_pdf(file, flavor = "hybrid",pages = "1" )
    print(file)
    if file == 'math_gt\\june_and_nov\\mathematics-9709-june-2025.pdf':
        all_the_tables.append(tables[1].df)
    else:
        all_the_tables.append(tables[0].df)
#print(all_the_tables)
p41_snippets = []

for index, dataframe in enumerate(all_the_tables):
    # Check if this is the specific DataFrame by its position in the list
    if index == 1:  # This targets the 3rd table (0-indexed)
        p41_snippets.append(dataframe.iloc[14:15, :]) 
    elif index ==3:
        p41_snippets.append(dataframe.iloc[16:17, :])
    else:  
        p41_snippets.append(dataframe.iloc[13:14, :])
#print(p41_snippets)


p41 = pd.concat(p41_snippets, axis = 0, ignore_index = "true")
p41.columns =["comp","max","A","B","C","D","E"]
p41.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p41)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p41 = p41[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p41 = p41.median()
mean_p41 =round( p41.mean(), 0)

print(median_p41)
print(mean_p41)