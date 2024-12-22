from flask import render_template, request
from flask_login import login_user, logout_user, current_user, login_remembered
from werkzeug.security import check_password_hash

from models import User

def register_routes(app_name, db, bcrypt):
    @app_name.route('/', methods = ['GET', 'POST'])
    def index():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            encrypt = bcrypt.generate_password_hash(password)
            user = User.query.filter(User.username == username).first()
            if user:
                if bcrypt.check_password_hash(user.password, password):
                    message = 'Login successful'
                    return render_template('login_message.html', message = message, hyper_link = 'index', page_route = "Login")
                else:
                    return "Invalid Username or password"
            else:
                message = "User not exist"
                return render_template('login_message.html', message = message, hyper_link = 'signup', page_route = "Sign up")
            
        return render_template('login_page.html', css_file = 'login_page.css')

    
    @app_name.route('/signup', methods = ['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            username = request.form.get('username')
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')
            
            if User.query.filter(User.username ==username).first():
                return "User already exists"
            if new_password == confirm_password:
                hased_password = bcrypt.generate_password_hash(new_password)
                pwd = hased_password
                user = User(username = username, password = pwd)
                db.session.add(user)
                db.session.commit()
                return "User details are saved successfully"
            
            return "Enter the password correctly"
                
        return render_template('signup_page.html', css_file = 'signup_page.css')
    



    

    
