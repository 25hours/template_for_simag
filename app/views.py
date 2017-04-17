from app import app
from flask import render_template,url_for,redirect

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/Dash_base')
def Dash_base():
    return render_template('Dash_base.html')