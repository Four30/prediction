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
p43_snippets = []

for index, dataframe in enumerate(all_the_tables):
    # Check if this is the specific DataFrame by its position in the list
    if index == 1:  # This targets the 3rd table (0-indexed)
        p43_snippets.append(dataframe.iloc[16:17, :]) 
    elif index ==3:
        p43_snippets.append(dataframe.iloc[18:19, :])
    else:  
        p43_snippets.append(dataframe.iloc[15:16, :])
#print(p43_snippets)


p43 = pd.concat(p43_snippets, axis = 0, ignore_index = "true")
p43.columns =["comp","max","A","B","C","D","E"]
p43.index = ["jun2022","jun2023","jun2024","jun2025","nov2022","nov2023","nov2024"]
print(p43)

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
p43 = p43[numeric_cols].apply(pd.to_numeric, errors='coerce')
median_p43 = p43.median()
mean_p43 =round( p43.mean(), 0)

print(median_p43)
print(mean_p43)