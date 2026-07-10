#trying camelot because tabula-py lowkey not reading the values i really need

#import camelot

#path = "chem_gt\chemistry-9701-june-2022.pdf"
#test trail with one file

#table = camelot.read_pdf(path, flavor = "lattice")
#print(table[0].df)
#test succesful! more successful than with tabula!
#output
#no, too large to show

#import glob
#import camelot

#path = "chem_gt"
#filenames = glob.glob(path + '/*.pdf')


#for file in filenames:
#    list_of_tables = camelot.read_pdf(filenames, flavor = "lattice", pages = "all")

# the error : The loop is not lookin at the file paths in the list filenames one by one, 
#because i had put as the argument the list instead of the file
#and so the code passes the entire list container to Camelot every time.
# how to solve? make the loop so that the list hands down a file path every iteration
#instead of the whole darn thing. a.k.a, change this line:#
#    list_of_tables = camelot.read_pdf(filenames, flavor = "lattice", pages = "all")
# to
#    list_of_tables = camelot.read_pdf(file, flavor = "lattice", pages = "all")


import glob
import camelot
import pandas as pd

path = "chem_gt\\june_and_nov"
filenames = glob.glob(path + "/*.pdf")
all_the_tables = []

for file in filenames:
    
    tables = camelot.read_pdf(file, flavor = "hybrid", pages = "1")
    all_the_tables.append(tables[0].df)
#print(all_the_tables)



#just addded, need to test edit: works perfectly
p11_snippets = []
for dataframe in all_the_tables:
    p11_snippets.append(dataframe.iloc[4:5,:])
#print(p11_snippets)
#just checking
p11 = pd.concat(p11_snippets, axis = 0)
#make them one. make them one. MAKE THEM ONE.
p11.columns =["comp","max","A","B","C","D","E"]
#print(p11) 
#test check

numeric_cols = [ 'A', 'B', 'C', 'D', 'E']
#making those columns numeric so I can perform calculations
# converting only those columns to numeric, forcing errors to 'coerce' (turn into NaN) if something is weird
p11[numeric_cols] = p11[numeric_cols].apply(pd.to_numeric, errors='coerce')
# Now calculate the median
print(p11[numeric_cols].median())
print(p11[numeric_cols].mean())

#p11_midA = p11_df.median()
#median for p11 to get an A
#print(p11_midA)
#print(p11_df.median())


#hybrid fixed the problem that some pdfs had where the header that had "cambridge internation- novem 202x" was read as a table 
# so yippe!
#now to convert to a dataframe and save specific snippets of them into a new dataframe to save to a csv to use! 
# the way I put it sounds so easy TwT
#IDeA!

#tables_fr = list_of_tables[0].df
#if i put the data frames here- wait, aren't they already data frames if I do them like that?
#have to check
#no, they aren't lmaooo, have to import pandas for it
#wait actually lemme print it out first
#only puts the first table there, hrrrh.

#okay, so i big brained and found myself a solution!
# the tables variable only stores the current file table, and if i want the first table in all the pdf
#then I gotta make an empty list/dictionary, and make it so that every table read at an instance is added 
#to the list/dictionary before it reads the next table.
#edit: i think it only works with dictionaries.
#edit: lmfao, [] IS A LIST, and {} a dictionary. () is a tuple lmaoooo

