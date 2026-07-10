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


#print(clean)
#joining em all
#print("Codes")
codes = pd.concat(clean,axis = 0, ignore_index=True )

#setting columns, and selecting particular rows with keyword as a different df
codes.columns =["Option","Max_Weight","Combo","A*","A","B","C","D", "E"]
numeric_cols = [ 'A*','A', 'B', 'C', 'D', 'E']
codes[numeric_cols] = codes[numeric_cols].apply(pd.to_numeric, errors = "coerce") # A* is being converted into float64, for some reason ( reason found: There's dashes)
codes["A*"] = pd.to_numeric(codes["A*"], errors="coerce").fillna(0).astype(int)



def MMO(keyword,userscore):
     rows = codes[codes['Option'].str.contains(keyword, na=False, case = False)]
     rows_mid = rows.median(numeric_only = True)
     rows_mean = rows.mean(numeric_only = True)
     a_star_mean, a_mean, b_mean,c_mean, d_mean, e_mean = rows.mean(numeric_only = True)

     print(f"For option {keyword}, these are the median scores and mean scores respectively:\n median \n {rows_mid},\n mean \n {rows_mean}")
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
            
     

useroption = input("Enter your code option: ")
while True:
    try:
        userscore = int(input("What's your combined score? \n(e.g. add your prospective marks in each component with the weighting applied,to find the combined score ): "))
        break
    except ValueError:
        print("An integer would be nice")
MMO(useroption,userscore)

