import glob
import camelot
import pandas as pd
import numpy as np

path = "math_gt\\wmarch\\mathematics-9709-march-2026.pdf"
A2_tables = []
AS_tables = []
tables = camelot.read_pdf(path, pages ="all", flavor = "lattice")
for table in tables:
    tabl = table.df
    exclusion = ["Component"]
    as_word = ["A*"]
    text_tables = tabl.to_string()
    if any(word in text_tables for word in exclusion):
        continue
    
    if len(tabl)>0:
        text= tabl.to_string()
        if any(word in text for word in as_word):
            A2_tables.append(tabl)
        else:
            AS_tables.append(tabl)


#print(AS_tables)
#print("Then,\n")
#print(A2_tables)

A2_cleaned = []
for index,df in enumerate(A2_tables):
        A2_cleaning = df[1:] 
        A2_cleaned.append(A2_cleaning)

AS_cleaned = []
for index,df in enumerate(AS_tables):
        AS_cleaning = df[1:] 
        AS_cleaned.append(AS_cleaning)


#lowk i'll just process like that.

A2_info = pd.concat(A2_cleaned,axis = 0, ignore_index=True )

#setting columns, and selecting particular rows with keyword as a different df
A2_info.columns =["Combo","Max_Weight","A*","A","B","C","D", "E"]
numeric_cols = [ 'A*','A', 'B', 'C', 'D', 'E']
A2_info[numeric_cols] = A2_info[numeric_cols].apply(pd.to_numeric, errors = "coerce") 
#print(A2_info)

#print("THEN AS")

AS_info = pd.concat(AS_cleaned,axis = 0, ignore_index=True )
AS_info.columns =["Combo","Max_Weight","A","B","C","D", "E"]
numeric_cols = ['A', 'B', 'C', 'D', 'E']
AS_info[numeric_cols] = AS_info[numeric_cols].apply(pd.to_numeric, errors = "coerce") 
#print(AS_info)


def MMO(info,component_combo,userscore):
#cannot use option cuz there's none like that
     rows = info[info["Combo"].str.contains(component_combo, na=False, case = False)]
     rows_mid = rows.median(numeric_only = True)
     rows_mean = round(rows.mean(numeric_only = True),1)
     print(len(rows_mean))
     if len(rows_mean) == 6:
         a_star_mean, a_mean, b_mean,c_mean, d_mean, e_mean = rows.mean(numeric_only = True)
         print(f"For the component combination {component_combo}, these are the median scores and mean scores respectively:\n median \n {rows_mid},\n mean \n {rows_mean}")
         if userscore > a_star_mean and a_star_mean != 0:
             print("Your grade is higher than the mean of A*, so likely you may be getting an A*")
         elif a_mean<userscore<a_star_mean:
             print("Your grade is higher than the mean of A, but lower than A*, so likely you may be getting an A.")
         elif b_mean<userscore<a_mean:
             print("Your grade is higher than the mean of B, but lower than A, so likely you may be getting an B.")
         elif c_mean<userscore<b_mean:
             print("Your grade is higher than the mean of C, but lower than B, so likely you may be getting an C.")
         elif d_mean<userscore<c_mean:
             print("Your grade is higher than the mean of D, but lower than C, so likely you may be getting an D.")
         elif e_mean<userscore<d_mean:
             print("Your grade is higher than the mean of E, but lower than E, so likely you may be getting an E.")
         elif userscore<e_mean:
             print("Your grade is below the mean of E, so you're probably having the grade U.")
         else:
             print("Seems this can't be handled.Sorry!")
            
     elif len(rows_mean) == 5:
        a_mean, b_mean,c_mean, d_mean, e_mean = rows.mean(numeric_only = True)
        print(f"For the component combination {component_combo}, these are the median scores and mean scores respectively:\n median \n {rows_mid},\n mean \n {rows_mean}")
        if userscore>a_mean:
            print("Your grade is higher than the mean of A, so likely you may be getting an A.")
        elif b_mean<userscore<a_mean:
            print("Your grade is higher than the mean of B, but lower than A, so likely you may be getting an B.")
        elif c_mean<userscore<b_mean:
            print("Your grade is higher than the mean of C, but lower than B, so likely you may be getting an C.")
        elif d_mean<userscore<c_mean:
            print("Your grade is higher than the mean of D, but lower than C, so likely you may be getting an D.")
        elif e_mean<userscore<d_mean:
            print("Your grade is higher than the mean of E, but lower than E, so likely you may be getting an E.")
        elif userscore<e_mean:
            print("Your grade is below the mean of E, so you're probably having the grade U.")
        else:
            print("Seems this can't be handled.Sorry!")

     


while True:
    try:
        info = int(input("Enter 0 for AS level, and 1 for A Level."))
        component_combo = input("What are the components you took? e.g. 12, 22, or 12, 32, 42. NOTE: TAKE ACCOUNT OF THE SPACES INBETWEEN THE NUMBERS \n :")
        userscore = int(input("What's your combined score? \n(e.g. add your prospective marks in each component with the weighting applied,to find the combined score ): "))
        break
    except ValueError:
        print("An integer would be nice")

if info ==1:
    info = A2_info
elif info ==0:
    info = AS_info
MMO(info,component_combo,userscore)