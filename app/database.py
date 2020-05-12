from app import mysql
from datetime import datetime

def connect_cursor_db():
    return mysql.connection.cursor()
def connect_commit_db():
    return mysql.connection.commit() 

def add_user(name, email):
    try:    
        cur = connect_cursor_db()
        cur.execute('insert into users (name, email) values (%s, %s)',
        (name, email))
        connect_commit_db()
    except:
        print("something went wrong")
def addpost(Profileid, Posttype,postbody ):
    post(Posttype,postbody)
    postid=getlastpostid()
    print('just added post id is',postid)
    Profile_post(Profileid,postid)
    

def Profile_post(Profileid,postid):
    
    try:    
        cur = connect_cursor_db()
        cur.execute('insert into Profile_post values (%s, %s,%s)',
        (Profileid, postid,datetime.now()))
        connect_commit_db()
    except connect_cursor_db().IntegrityError as e :
        print("something went wrong in Profile Post Function database function",e)


def post(Posttype,postbody):
    try:    
        cur = connect_cursor_db()
        cur.execute('insert into Post (PostTypeName, PostBody) values (%s, %s)',
        (Posttype, postbody))
        connect_commit_db()
    except:
        print("something went wrong")

def getlastpostid():
    cur = connect_cursor_db()
    query='select count(PostId) from Post'
    cur.execute(query)
    postid = cur.fetchone()
    return int(postid['count(PostId)'])


def get_user(username):
    try:
        cur = connect_cursor_db()
        cur.execute('SELECT Username,Password FROM Profiles WHERE Username = %s',(username,))
        account = cur.fetchone()
        return account
    except:
        print("something went wrong")

def getAddress(Profileid):
    #returns the  address  linked to the profileid 
    try:
        cur = connect_cursor_db()
        query='Select Street, City from profile_address where ProfileId=%s'
        cur.execute(query,(Profileid,))
        account = cur.fetchone()
        return account
    except:
        print("something went wrong")

def getEmail(Profileid):
    #returns the  Emails  linked to the profileid 
    try:
        cur = connect_cursor_db()
        query='Select email from profile_email where ProfileId=%s'
        cur.execute(query,(Profileid,))
        account = cur.fetchone()
        return account
    except:
        print("something went wrong")

def getNumbers(Profileid):
    #returns the  Emails  linked to the profileid 
    try:
        cur = connect_cursor_db()
        query='Select PhoneNumber from profile_phonenumber where ProfileId=%s'
        cur.execute(query,(Profileid,))
        account = cur.fetchone()
        return account
    except:
        print("something went wrong")




def ProfileInfo(username):
    try:
        cur = connect_cursor_db()
        query='SELECT Users.UserId,Profiles.ProfileId,Username,Fname,Lname,Gender,DOB,Profiles.Bio FROM Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId WHERE Profiles.Username = %s'
        cur.execute(query,(username,))
        account = cur.fetchone()
        mobile_number=getNumbers(account['ProfileId'])
        Address=getAddress(account['ProfileId'])
        Emails=getEmail(account['ProfileId'])
        account.update(Address)
        account.update(Emails)
        account.update(mobile_number)
        return account
    except:
        print("something went wrong")
    
def NewUserandprofile(username,password,bio,relationshipStatus,
    fname,lname,gender,dOB,email,phoneNumber):
    profileId=nextProfileID()
    userId=nextUserID() 
    #put in try exceet block after test
    cur = connect_cursor_db()
    cur.callproc( "NewUser",(username,profileId,userId,password,bio,relationshipStatus,fname,lname,gender,dOB,email,phoneNumber))
    results =cur.fetchone()
    return results    
        

def nextProfileID():
    cur = connect_cursor_db()
    query='select count(ProfileId)+100000 from Profiles'
    cur.execute(query)
    totalprofiles = cur.fetchone()
    print(totalprofiles)
    newprofileid='PID'+str(totalprofiles['count(ProfileId)+100000'])
    return newprofileid

def nextUserID():
    cur = connect_cursor_db()
    query='select count(UserId)+100000 from Users'
    cur.execute(query)
    totalusers = cur.fetchone()
    print(totalusers)
    newuserid='UID'+str(totalusers['count(UserId)+100000'])
    return newuserid

def profileFriends(ProfileId):
    #returns all the profile id of friends related to a profileid 
    cur = connect_cursor_db()
    query='select FriendsProfileId,FriendGroupName from Profile_friends where ProfileId=%s'
    cur.execute(query,(ProfileId,))
    allfriends = cur.fetchall()
    return allfriends

def Friendsinfo(ProfileId):
    #returns all friend info for friendlist
    friends=[]
    friendlist=profileFriends(ProfileId)
    cur = connect_cursor_db()
    for friend in friendlist:
        friend['FriendsProfileId']
        query='select Fname,Lname,Gender,Profiles.Username from Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId WHERE Profiles.ProfileID = %s'
        cur.execute(query,(friend['FriendsProfileId'],))
        friend = cur.fetchone()
        friends.append(friend)
    return friends
def AllUsers():
    cur = connect_cursor_db()
    query='select Fname,Lname,Gender,Profiles.Username,Profiles.ProfileID from Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId LIMIT 50'
    cur.execute(query)
    user = cur.fetchall()
    return user

def SearchUsers(uname):
    cur = connect_cursor_db()
    query='select Profiles.ProfileID, Fname,Lname,Gender,Profiles.Username from Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId where Profiles.Username like %s LIMIT 15'
    cur.execute(query,("%{}%".format(uname),))
    user = cur.fetchall()
    return user
def AddFriends(profile,friendsprofile,FriendGroup):
    cur = connect_cursor_db()
    try:
        query='insert into Profile_friends values(%s,%s,%s)'
        cur.execute(query,(profile,friendsprofile,FriendGroup,))
        connect_commit_db()
        return {'message':'Friend Added ','alert':'success'}
    except (cur.IntegrityError ):
        return {'message':'Seems like your are already Friends','alert':'primary'}

def GetpostId(profileId):
    #returns all the postid  and dates relateded to a profile id
    cur = connect_cursor_db()
    query='select PostId,DateofUPO from Profile_post where ProfileId=%s ORDER by DateofUPO DESC '
    cur.execute(query,(profileId,))
    postid = cur.fetchall()
    return postid

def Getpost(postId):
    #returns the post and ost data relateded to a post id
    try:
        cur = connect_cursor_db()
        query='select Users.UserId,Profiles.Username,Post.PostId,Post.PostTypeName,Post.PostBody from Post join Profile_post on Post.PostId=Profile_post.PostId join Profiles on Profile_post.ProfileId=Profiles.ProfileId join User_profile on Profiles.ProfileId=User_profile.Profileid join Users on User_profile.UserId= Users.UserId where Post.PostId= %s'
        cur.execute(query,(postId,))
        postid = cur.fetchone()
        return postid
    except connect_cursor_db().error as  e :
        print('There is an error in your getpost function',e)    


def GetComments(postId):
    #returns the comments and coments data relateded to a post id
    try:
        cur = connect_cursor_db()
        query='select Users.UserId,Profiles.Username,Comment.CommentId,Comment.CommentBody from Comment join Post_comment on Comment.CommentId=Post_comment.CommentId join Profile_comment on Post_comment.CommentId=Profile_comment.CommentId join Profiles on Profile_comment.ProfileId=Profiles.ProfileId join User_profile on Profiles.ProfileId=User_profile.Profileid join Users on User_profile.UserId= Users.UserId where Post_comment.PostId=%s'
        cur.execute(query,(postId,))
        comments = cur.fetchall()
        return comments
    except connect_cursor_db().error as  e :
        print('There is an error in your getpost function',e)         
         
def ALlPandC(profileId):
    pandc={}
    ALLPandC=[]
    postids=GetpostId(profileId)
    
    for postid in postids:
       
        post=Getpost(postid['PostId'])
        
        pandc={'Post':post}
        comments=GetComments(postid['PostId'])
        justcomments={'comments':comments}
        pandc.update(justcomments)
        ALLPandC.append(pandc)
        
    return ALLPandC


def allFriendspandc(profileId):
    allFriendspandc=[]
    friendlist=profileFriends(profileId)
    for friends in friendlist:
        listOfpost=ALlPandC(friends['FriendsProfileId'])        
        allFriendspandc.append(listOfpost)
    return allFriendspandc


 