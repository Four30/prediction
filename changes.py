from flask import Flask, render_template, request
import glob
import camelot
import pandas as pd
from markupsafe import escape
import os


app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('frontend_prototype.html')
    



# Route to process form data and render the results page
@app.route('/submit', methods=['POST'])

def loading():
    path_input = request.form.get("sub_code")
    dict = {"9701":"chem_gt/gt", "9700":"bio_gt/gt", "9702":"phy_gt/gt", "9709": "math_gt/gt"}
    #Getting the old (pre-2026) tables first
    
    path = os.path.join(app.root_path, dict[path_input])
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


    info = request.form.get("exam")
    component_combo =request.form.get("components")
    userscore = int(request.form.get("total_score"))
    
    if info == "education-AS":
        info = AS_tables
    elif info == "education-A2":
        info = A2_tables


    

    rows = info[info["Combo"].str.contains(component_combo, na=False, case = False)]
    rows_mid = rows.median(numeric_only = True)
    rows_mean = round(rows.mean(numeric_only = True),1)



    
    if len(rows_mean) == 6:
        a_star_mean, a_mean, b_mean,c_mean, d_mean, e_mean = rows_mean
        mean = [a_star_mean, a_mean, b_mean,c_mean, d_mean, e_mean]
        a_star_mid, a_mid, b_mid, c_mid, d_mid, e_mid = rows_mid
        mid = [a_star_mid, a_mid, b_mid, c_mid, d_mid, e_mid]
        
        
        if userscore > a_mean and a_star_mean != 0:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid, result="Your grade is higher than the mean of A, so likely you may be getting an A*")
        elif a_mean<userscore<a_star_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result="Your grade is higher than the mean of A, but lower than A*, so likely you may be getting an A.")
        elif b_mean<userscore<a_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result= "Your grade is higher than the mean of B, but lower than A, so likely you may be getting an B.")
        elif c_mean<userscore<b_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result="Your grade is higher than the mean of C, but lower than B, so likely you may be getting an C.")
        elif d_mean<userscore<c_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result= "Your grade is higher than the mean of D, but lower than C, so likely you may be getting an D.")
        elif e_mean<userscore<d_mean:
           return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result= "Your grade is higher than the mean of E, but lower than D, so likely you may be getting an E.")
        elif userscore<e_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result= "Your grade is below the mean of E, so you're probably having the grade U.")
        
            
    elif len(rows_mean) == 5:
        a_mean, b_mean,c_mean, d_mean, e_mean = rows.mean(numeric_only = True)
        a_mean, b_mean,c_mean, d_mean, e_mean = rows_mean
        mean =  [a_mean, b_mean,c_mean, d_mean, e_mean]
        a_mid, b_mid, c_mid, d_mid, e_mid = rows_mid
        mid = [ a_mid, b_mid, c_mid, d_mid, e_mid]
        information = f"For the component combination {escape(component_combo)}, these are the median scores and mean scores respectively:\n median \n {escape(mid)},\n mean \n {escape(mean)}"
        if userscore>a_mean:
            return render_template('form_info.html',information = "No extra information!", component = component_combo,mean = mean,mid = mid,result = "Your grade is higher than the mean of a, so likely you may be getting an a.")
        elif b_mean<userscore<a_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result="Your grade is higher than the mean of b, but lower than a, so likely you may be getting an b.")
        elif c_mean<userscore<b_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result="Your grade is higher than the mean of c, but lower than b, so likely you may be getting an c.")
        elif d_mean<userscore<c_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result="Your grade is higher than the mean of d, but lower than c, so likely you may be getting an d.")
        elif e_mean<userscore<d_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result="Your grade is higher than the mean of E, but lower than d, so likely you may be getting an e.")
        elif userscore<e_mean:
            return render_template('form_info.html',information = "No extra information!",component = component_combo,mean = mean,mid = mid,result="Your grade is below the mean of e, so you're probably having the grade u.")
    else:
        return render_template('form_info.html',information ="Unable to process data. Can't retrieve values for your component, make sure that \n i. your components are listed in order, e.g. 12, 22, and \n ii. there are spaces between your components, like this: 12, 52")
           
#    return render_template('form_info.html',information =information,result = result)
    

#if __name__ == '__main__':
#    app.run(debug=False)
