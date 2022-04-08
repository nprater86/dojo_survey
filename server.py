from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'you will never guess my yek'

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

            
@app.route('/formdata', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
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

if __name__ == "__main__":
    app.run(debug=True)

