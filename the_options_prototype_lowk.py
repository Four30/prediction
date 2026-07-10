import glob
import camelot
import pandas as pd
#get the paths, and prepare a list
path = "math_gt\\june_and_nov"
filenames = glob.glob(path + "/*.pdf")
path = "math_gt\\june_and_nov\\mathematics-9709-november-2023.pdf"
all_the_tables = []
#grab the tables needed and put in list
for file in filenames:
    table = camelot.read_pdf(file, pages = "all", flavor= "lattice")
    for tabe in table:
        tab = tabe.df
        exclusion = ["Component"]
        text_tables = tab.to_string()
        if any(word in text_tables for word in exclusion):
            #print("skipped.")
            continue
        else:
            if len(tab)>1:
                all_the_tables.append(tab)
#print(all_the_tables)

#remove every first row of each df (I'll set the column name later)
clean = []
for index,df in enumerate(all_the_tables):
        clea = df[1:] 
        clean.append(clea)





#print(codes[numeric_cols].dtypes)
#codes[numeric_cols] = codes[numeric_cols].apply(pd.to_numeric, errors = "coerce") # A* is being converted into float64, for some reason ( reason found: There's dashes)
#codes["A*"] = pd.to_numeric(codes["A*"], errors="coerce").fillna(0).astype(int)
#print(codes.dtypes)
#print(codes.columns.tolist())
#with pd.option_context("display.max_rows", 197):
#    print(codes)
#axrows = codes[codes['Option'].str.contains(keyword, na=False, case = False)]
#print(axrows)
#print(axrows.dtypes)
#axmedian = axrows.median(numeric_only = True)
#axmean = axrows.mean(numeric_only = True)

# grab any row that has in the first column "AX" 
#and put them in a separate dataframe

#AX
#keyword = "AX"
#axrows = codes[codes['Option'].str.contains(keyword, na=False, case = False)]

#axmedian = axrows.median(numeric_only = True)
#axmean = axrows.mean(numeric_only = True)
#print(axmedian,axmean)

#idea to make a func outta this! the func would give the table AND the median and mean. I Call IT: The MMO - midmeanoption