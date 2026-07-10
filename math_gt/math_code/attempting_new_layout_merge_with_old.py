import glob
import camelot
import pandas as pd
#get the paths, and prepare a list
path = "math_gt\\june_and_nov\\new_layout_2026"
filenames = glob.glob(path + "/*.pdf")
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
atbl = []


aa_starlesskeyword = "–"
for table in all_the_tables:
    print(table.shape)
    aa_starless=table[table[3].str.contains(aa_starlesskeyword, na=False, case = False)]
    if table.shape[1]<8:
        table = table[1:] 
        atbl.append(table)
#print(atbl)



# AA_Starless
aa_starless.drop([0,3], axis ='columns', inplace =True)
#print(aa_starless.columns.tolist())
#print(aa_starless)
aa_starless = aa_starless[[2,1,4,5,6,7,8]]
#print(aa_starless)

#print(aa_starless.columns.dtype)

#print(aa_starless)
atbl_together = pd.concat(atbl,axis=0)
#print(atbl_together)
#for table in atbl:
    #print(table.columns.dtype)

new = [aa_starless , atbl_together]
#print(new)
for df in new:
    df.columns = list(range(df.shape[1]))
    df.index = list(range(df.shape[0]))
    #print(df)
#print(new)
AS_tables = pd.concat(new, axis=0,ignore_index=True)
#print(AS_tables)

keyword = "A*"
a_star = []
a_starr = []
for table in all_the_tables:
    for col in table:
        a_starr = table[col].astype(str).str.contains(r'A*',na=False,case=False)
        #print(table[a_starr])
    #a2tbl= table[table[3].str.contains(keyword, na=False, case = False)]
    if table.shape[1]>8:
        index_remove = table[ (table[3] == '–') ].index
        tabler = table.drop(index_remove)
        a_star.append(tabler)
#print(a2tbl)
#print(a_star)

a_sta = pd.concat(a_star,axis=0,ignore_index = True)
a_sta.drop([0], axis ='columns', inplace =True)
#print(aa_starless.columns.tolist())
#print(aa_starless)
a_sta = a_sta[[2,1,3,4,5,6,7,8]]
print(a_sta)
#for df in all_the_tables:
#        clea = df[1:] 
#        clean.append(clea)

#codes = pd.concat(clean,axis = 0, ignore_index=True )
#codes.columns =["Option","Max_Weight","Combo","A*","A","B","C","D", "E"]
#codes.drop(["Option"],axis = "columns",inplace= True)
#codes = codes.reindex(columns = ["Combo","Max_Weight","A*","A","B","C","D", "E"])

#numeric_cols = [ 'A*','A', 'B', 'C', 'D', 'E']
#codes[numeric_cols] = codes[numeric_cols].apply(pd.to_numeric, errors = "coerce") # A* is being converted into float64, for some reason ( reason found: There's dashes)
#codes["A*"] = pd.to_numeric(codes["A*"], errors="coerce").fillna(0).astype(int)


#genuinely try and get the rows without A* into its own df
#aa_starlesskeyword = "–"
#aa_starless = codes[codes["A*"].str.contains(aa_starlesskeyword, na=False, case = False)]
#aa_starless.drop(["A*"], axis ='columns', inplace =True)
#aa_starless.columns =["Max_Weight","Combo","a","b","c","d", "e"]
#numeric_cols = ['a', 'b', 'c', 'd', 'e']
#aa_starless[numeric_cols] = aa_starless[numeric_cols].apply(pd.to_numeric, errors = "coerce") 
#aa_starless = aa_starless.reindex(columns = ["Combo","Max_Weight",'a', 'b', 'c', 'd', 'e'])


#thing = codes.index[codes["A*"]== "–"].tolist()
#aa_star= codes.drop(thing, axis="index")
#numeric_cols = [ 'A*','A', 'B', 'C', 'D', 'E']
#aa_star[numeric_cols] = aa_star[numeric_cols].apply(pd.to_numeric, errors = "coerce") 

#print(f" A STARR \n\n\n\n {aa_star}")
#print(f"A STARLESS \n\n\n\n {aa_starless}")

#a_star = [aa_star]
#a_starless = [aa_starless]
