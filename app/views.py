"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, SignupForm
from app.models import UserProfile
from werkzeug.security import check_password_hash

userdatabase={'id':'0011',
            'firstname':'lincoln',
            'lastname':"brown",
            'username':"links",
            'Password':"pasword123"
            }

###
# Routing for your application.
###

@app.route('/',methods=["GET","POST"])
def home():
    signupform=SignupForm()
    if request.method == 'POST':
        if signupform.validate_on_submit():
            signupform.First_Name.data
            signupform.Last_Name.data
            signupform.Email.data
            signupform.Password.data
            signupform.Mobile_number.data
            print('dss')
            flash('Sign Up successfull,Lets Goo!.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Somting went wrong please try again!.', 'danger')
            return render_template('home.html',form=signupform)
            
    """Render website's home page."""
    return render_template('home.html',form=signupform)


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/secure-page')
@login_required 
def secure_page():
    return render_template("secure_page.html")

@app.route('/profile')
@login_required 
def profile():
    return render_template("secure_page.html")

@app.route('/Groups')
@login_required 
def groups():
    return render_template("secure_page.html")


@app.route('/Comments_post')
@login_required 
def PandC():
    return render_template("secure_page.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = UserProfile(userdatabase['firstname'],userdatabase['lastname'],
        userdatabase['username'],userdatabase['Password'])
        user.id=userdatabase['username']
        if user is not None and check_password_hash(user.password, password):
            remember_me = False
            # get user id, load into session
            login_user(user,remember_me)
            #flash('Login successful.', 'success')
            # remember to flash a message to the user
            print('login sucessfull')
            return redirect(url_for('secure_page'))
            # they should be redirected to a secure-page route instead
        else:
            flash('Username or Password is incorrect.', 'danger')

    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))



#----------------------------------------------------------------------------------------------
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(username):
    if username != userdatabase['username']:
        return

    user = UserProfile(userdatabase['firstname'],userdatabase['lastname'],
        userdatabase['username'],userdatabase['Password'])
    user.id = username
    return user

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
