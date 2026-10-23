
import glob
import camelot
import pandas as pd
import os


    
subject = str(input("Enter code"))

dict = {"9701":"chem_gt/gt", "9700":"bio_gt/gt", "9702":"phy_gt/gt", "9709": "math_gt/gt", "9699":"soc_gt", "9231":"fm_gt", "9708":"econ_gt", "9609":"bus_gt", "9626":"it_gt"}
#Getting the old (pre-2026) tables first
    
chem9701 = dict[subject]
path = chem9701
filenames = glob.glob(path + "/*.pdf")
pre_26_tables= []
#grab the tables needed and put in list
for file in filenames:
    table = camelot.read_pdf(file, pages = "all", flavor= "lattice")
    for tabe in table:
        tab = tabe.df
        exclusion = ["Component"]
        text_tables = tab.to_string()
        if any(word in text_tables for word in exclusion):
            continue
        else:
            if len(tab)>1:
                pre_26_tables.append(tab)
    
    #getting the rows in the pre 2026 tables that have dashes in the A* column, then cleaning
pre_26_keyword = "–"
apre26 = []
for table in pre_26_tables:
    apre26.append(table[table[3].str.contains(pre_26_keyword, na=False, case = False)])
#the mentioned cleaning ( matching it with the new layout)
apre26 = pd.concat(apre26, axis =0, ignore_index=True)

apre26.drop([0,3], axis ='columns', inplace =True)
apre26 = apre26[[2,1,4,5,6,7,8]]
#now doing pre 2026 A* cleanup, as in now doing the tables that should have A*
star_pre26 = []
for table in pre_26_tables:
    index_remove = table[ (table[3] == '–') ].index
    tabler = table.drop(index_remove)
    tabler = tabler[1:] 
    star_pre26.append(tabler)
#cleaning, rearranging columns so it fits with new.
star_26 = pd.concat(star_pre26,axis=0,ignore_index = True)
star_26.drop([0], axis ='columns', inplace =True)
star_26 = star_26[[2,1,3,4,5,6,7,8]]

    #-----------DONE! WITH! LEGACY! now for the newest dearest post 2026. if cambridge ever updates ts again I'll cry.--------------

path =path + "\\new_layout_2026"
filenames = glob.glob(path + "/*.pdf")
post_2026 = []
#grab the tables needed and put in list
for file in filenames:
    table = camelot.read_pdf(file, pages = "all", flavor= "lattice")
    for tabe in table:
        tab = tabe.df
        exclusion = ["Component"]
        text_tables = tab.to_string()
        if any(word in text_tables for word in exclusion):
            continue
        else:
            if len(tab)>1:
                post_2026.append(tab)


    #The AS tables and A2 tables for new layout
as_tables = []
a2_tables = []
for table in post_2026:
    if table.shape[1]<8:
        table = table[1:] 
        as_tables.append(table)
    else:
        table = table[1:] 
        a2_tables.append(table)     
as_table = pd.concat(as_tables, axis = 0,ignore_index=True)
a2_table =pd.concat(a2_tables,axis = 0,ignore_index=True)

    #done with all, now to join new and old

    #as_table goes with apre26, a2_table goes with star_pre26

    #AS tables
as_new = [apre26, as_table]
for df in as_new:
        df.columns = list(range(df.shape[1]))
        df.index = list(range(df.shape[0]))


AS_tables = pd.concat(as_new, axis = 0, ignore_index = True)
AS_tables.columns = ["Combo","Max","a","b","c","d", "e"]
ASnumeric_cols = ["a","b","c","d","e"]
AS_tables[ASnumeric_cols] = AS_tables[ASnumeric_cols].apply(pd.to_numeric, errors = "coerce") 

    # for the A2 tables.
a2_new = [star_26, a2_table]
for df in a2_new:
    df.columns = list(range(df.shape[1]))
    df.index = list(range(df.shape[0]))
    
A2_tables = pd.concat(a2_new, axis = 0, ignore_index = True)
A2_tables.columns =["Combo","Max","A*","A","B","C","D", "E"]
A2numeric_cols = [ 'A*','A', 'B', 'C', 'D', 'E']
A2_tables[A2numeric_cols] = A2_tables[A2numeric_cols].apply(pd.to_numeric, errors = "coerce") 





AS_tables.to_csv(subject + '\\' + subject +'_AS.csv')
A2_tables.to_csv(subject + '\\' + subject +'_A2.csv')