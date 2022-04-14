from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")

            
@app.route('/formdata', methods=['POST'])
def create_survey():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favelang'] = request.form['favelang']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route("/result")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("result.html")