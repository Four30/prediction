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
p61_snippets = []

for index, dataframe in enumerate(all_the_tables):
    # Check if this is the specific DataFrame by its position in the list
    if index == 1:  #targets the 3rd table 
        p61_snippets.append(dataframe.iloc[20:21, :]) 
    elif index ==3:
        p61_snippets.append(dataframe.iloc[23:24, :])
    else:  
        p61_snippets.append(dataframe.iloc[19:20, :])
#print(p61_snippets)

p61 = pd.concat(p61_snippets, axis = 0, ignore_index = "true")
p61.columns =["comp","max","A","B","C","D","E"]
p61.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p61)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p61 = p61[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p61 = p61.median()
mean_p61 =round( p61.mean(), 0)

print(median_p61)
print(mean_p61)