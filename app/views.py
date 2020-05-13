"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, login_manager
from flask import render_template, request, redirect, url_for, flash,session
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, SignupForm,CommentForm,SearchForm,PostForm,EditprofileForm
from app.models import UserProfile
from app.database import *
from werkzeug.security import check_password_hash
USERNAME=''
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
            Fname=signupform.First_Name.data
            Lname=signupform.Last_Name.data
            Email=signupform.Email.data
            Password=signupform.Password.data
            Phonenumber=signupform.Mobile_number.data
            Gender=signupform.Gender.data
            DOB=signupform.DOB.data
            Relationshipstatus=signupform.RelationShipStatus.data
            Bio=signupform.Bio.data
            Username=signupform.Username.data
            print(Username,Password,Bio,Relationshipstatus,
                    Fname,Lname,Gender,DOB,Email,Phonenumber)

            results=NewUserandprofile(Username,Password,Bio,Relationshipstatus,
                    Fname,Lname,Gender,DOB,Email,Phonenumber)
            print(results)
            
            if results== {'Taken':'Taken'}:
                flash(' Sorry that Username in not available. ','danger')
            elif results=={'User_added':'User_added'}:
                flash('Sign Up successfull,Lets Goo!.', 'success')
                return redirect(url_for('login'))
            else:
                flash('That weird it seems like Somthing Went wrong!!','warning')

            
        else:
            flash('Something went wrong please try again!.', 'danger')
            return render_template('home.html',form=signupform)
            
    """Render website's home page."""
    return render_template('home.html',form=signupform)


@app.route('/findfriends/',methods=["GET", "POST"])
@login_required
def FindFriends():
    form=SearchForm()
    if request.method == "POST" and form.validate_on_submit():
        search=form.Search.data
        search=SearchUsers(search)
        print(search)
        return render_template('findfriends.html',usersfriends=search,searchform=form)

    usersfriends=AllUsers()
    return render_template('findfriends.html',usersfriends=usersfriends,searchform=form)

@app.route('/Addfriend/<profileid>')  
def AddFriend(profileid):
    print(profileid)
    ThisProfileid=session.get('ThisProfileid')
    FriendGroup='work'
    res=AddFriends(ThisProfileid,profileid,FriendGroup)
    flash(res['message'], res['alert'])
    return redirect(url_for('FindFriends'))
   


@app.route('/secure-page')
@login_required 
def secure_page():
    return render_template("secure_page.html")

@app.route('/profile')
@login_required 
def profile():
    USERNAME=session.get('USERNAME')
    user=ProfileInfo(USERNAME)
    print(user)
    session['ThisProfileid']=user['ProfileId']
    friends=Friendsinfo(user['ProfileId'])
    #print(profileFriends(user['ProfileId']))

   
    return render_template("profile.html",user=user, usersfriends=friends)

@app.route('/Groups')
@login_required 
def groups():
    return render_template("Groups.html")


@app.route('/Comments_post')
@login_required 
def PandC():
    postform=PostForm()
    form=CommentForm()
    profileId=session.get('ThisProfileid')
    mypost=ALlPandC(profileId)
    friendspost=allFriendspandc(profileId)
    print('next comment id',nextcommentid())
    
    return render_template("commentPost.html",CommentForm=form,Postform=postform,friendspost=friendspost,mypost=mypost)

@app.route('/MakePost', methods=["GET", "POST"])
@login_required 
def MakePost():
    postform=PostForm()
    profileId=session.get('ThisProfileid')
    if request.method == "POST" and postform.validate_on_submit():
        postbody=postform.Post.data
        Posttype='text'
        addpost(profileId, Posttype,postbody)
    
    return redirect(url_for('PandC'))

@app.route('/MakeComment/<postid>', methods=["GET", "POST"])
@login_required 
def Makecomment(postid):
    commentform=CommentForm()
    if request.method == "POST" and commentform.validate_on_submit():
        profileid=session.get('ThisProfileid')
        commentbody=commentform.Comments.data
        postid
        print(MakeComment(profileid,commentbody,postid))


    return redirect(url_for('PandC'))

@app.route("/Editprofile", methods=["GET", "POST"])
@login_required 
def EditProfile():
    editform=EditprofileForm()
    USERNAME=session.get('USERNAME')
    user=ProfileInfo(USERNAME)
    
    if request.method == 'POST':
        if editform.validate_on_submit():
            Fname=editform.First_Name.data
            Bio=editform.Bio.data
            RelationshipStatus=editform.RelationShipStatus.data
            Fname=editform.First_Name.data
            Lname=editform.Last_Name.data
            Gender=editform.Gender.data
            DOB=editform.DOB.data
            email=editform.Email.data
            PhoneNumber=editform.Mobile_number.data
            Street=editform.Street.data
            City=editform.City.data



            UsersId=user['UserId']
            profileId=session.get('ThisProfileid')
            updateProfile(profileId,Bio,RelationshipStatus)
            updateUsers(UsersId,Fname,Lname,Gender,DOB)
            updateemail(profileId,email)
            updatePhonenumber(profileId,PhoneNumber)
            updateAddress(profileId,Street,City)

    return render_template("EditProfile.html",form=editform,current=user)



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        userlog=get_user(username)
        if userlog:
            user = UserProfile(userlog['Username'],userlog['Password'])
            
            
            if user is not None and check_password_hash(user.password, password):
                remember_me = False
                # get user id, load into session
                login_user(user,remember_me)
                flash('Login successful.', 'success')
                
                print('login sucessfull',user.password)
                session['USERNAME'] = user.username
                return redirect(url_for('profile'))
            
            else:
                flash('Username or Password is incorrect.', 'danger')
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
    userlog=get_user(username)
    if userlog:
        user = UserProfile(userlog['Username'],userlog['Password'])
        return user
    return

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
