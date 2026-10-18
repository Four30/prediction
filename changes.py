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
    subject = request.form.get("sub_code")
    
    
    

    info = request.form.get("exam")
    component_combo =request.form.get("components")
    userscore = int(request.form.get("total_score"))

    if info == "education-AS":
        info = subject + "/" + subject + "_AS.csv"
    elif info == "education-A2":
        info = subject + "/" + subject + "_A2.csv"

    info = pd.read_csv(info)
    

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
