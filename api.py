from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

app.secret_key = 'asif'

@app.route("/")
def index():
    return render_template('login_page.html');


@app.route('/signup')
def signup():
    return render_template('signup_page.html')

@app.route("/login", methods = ['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == "admin" and password == "admin":
        return "Login successful"
    return "User not exist"
    



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5555, debug=True)