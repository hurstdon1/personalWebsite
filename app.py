from flask import Flask, render_template, url_for, json, redirect, request
from flask_wtf import FlaskForm
from forms import ContactForm
import pandas as pd
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a6c63d94bf77cb2c4845153a56cbba'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/projects")
def projects():
    return render_template('projects.html', title="My Projects")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactUsMessage.csv')
        print("The data are saved !")
        return redirect(url_for('contact'))
    else:
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)