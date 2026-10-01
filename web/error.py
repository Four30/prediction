from flask import Flask, render_template, request
import glob
import camelot
import pandas as pd
from markupsafe import escape

app = Flask(__name__)

# Route to display the HTML form
@app.route('/')
def show_form():
    return render_template('frontend_prototype.html')