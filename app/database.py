from app import mysql
from datetime import datetime

def connect_cursor_db():
    return mysql.connection.cursor()
def connect_commit_db():
    return mysql.connection.commit() 

def add_Photo(category, Photoname):
    try:    
        cur = connect_cursor_db()
        cur.execute('insert into Photo (category, Photoname)values (%s, %s)',
        (category, Photoname))
        connect_commit_db()
    except:
        print("something went wrong")

def add_user_Photo(UserId):
    try:    
        cur = connect_cursor_db()
        cur.execute('insert into User_photo (UserId, DateofUP)values (%s, %s)',
        (UserId,datetime.now() ))
        connect_commit_db()
    except:
        print("something went wrong")

def uploadphoto(UserId,category, Photoname):
     add_Photo(category, Photoname)
     add_user_Photo(UserId)

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

def getprofilepic(UsersId):
    try:
        cur = connect_cursor_db()
        query='Select Photo.PhotoId, category,Photoname, User_photo.DateofUP from Photo join User_photo on Photo.PhotoId=User_photo.PhotoId where User_photo.UserId=%s and category=%s ORDER by PhotoId DESC'
        cur.execute(query,(UsersId,'profile',))
        profilepic = cur.fetchone()
        return profilepic
    except connect_cursor_db().Error as e :
        print("something went wrong", e)

def getallpic(UsersId):
    try:
        cur = connect_cursor_db()
        query='Select Photo.PhotoId, category,Photoname, User_photo.DateofUP from Photo join User_photo on Photo.PhotoId=User_photo.PhotoId where User_photo.UserId=%s ORDER by PhotoId DESC'
        cur.execute(query,(UsersId,))
        profilepic = cur.fetchall()
        return profilepic
    except connect_cursor_db().Error as e :
        print("something went wrong", e)

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
        query='SELECT Users.UserId,Profiles.ProfileId,Username,RelationshipStatus,Fname,Lname,Gender,DOB,Profiles.Bio FROM Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId WHERE Profiles.Username = %s'
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
        query='select Users.UserId, Fname,Lname,Gender,Profiles.Username from Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId WHERE Profiles.ProfileID = %s'
        cur.execute(query,(friend['FriendsProfileId'],))
        friend = cur.fetchone()
        
        Photo=getprofilepic(friend['UserId'])
        print (Photo)
        if Photo is not None:
            Photoname=Photo['Photoname']
        else:
            Photoname="nophotofound.png"

        friend.update({"Photoname":Photoname})
        

        friends.append(friend)
    return friends
def AllUsers():
    cur = connect_cursor_db()
    query='select Users.UserId, Fname,Lname,Gender,Profiles.Username,Profiles.ProfileID from Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId LIMIT 50'
    cur.execute(query)
    users = cur.fetchall()

    for user in users:
            
        Photo=getprofilepic(user['UserId'])
        
        if Photo is not None:
            Photoname=Photo['Photoname']
        else:
            Photoname="nophotofound.png"

        user.update({"Photoname":Photoname})


    return users

def SearchUsers(uname):
    cur = connect_cursor_db()
    query='select Users.UserId, Profiles.ProfileID, Fname,Lname,Gender,Profiles.Username from Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId where Profiles.Username like %s LIMIT 15'
    cur.execute(query,("%{}%".format(uname),))
    users = cur.fetchall()
    for user in users:
            
        Photo=getprofilepic(user['UserId'])
        
        if Photo is not None:
            Photoname=Photo['Photoname']
        else:
            Photoname="nophotofound.png"

        user.update({"Photoname":Photoname})


    return users
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
        posts = cur.fetchone()

        Photo=getprofilepic(posts['UserId'])
        
        if Photo is not None:
            Photoname=Photo['Photoname']
        else:
            Photoname="nophotofound.png"
        posts.update({"Photoname":Photoname})

        return posts
    except connect_cursor_db().error as  e :
        print('There is an error in your getpost function',e)    


def GetComments(postId):
    #returns the comments and coments data relateded to a post id
    try:
        cur = connect_cursor_db()
        query='select Users.UserId,Profiles.Username,Comment.CommentId,Comment.CommentBody from Comment join Post_comment on Comment.CommentId=Post_comment.CommentId join Profile_comment on Post_comment.CommentId=Profile_comment.CommentId join Profiles on Profile_comment.ProfileId=Profiles.ProfileId join User_profile on Profiles.ProfileId=User_profile.Profileid join Users on User_profile.UserId= Users.UserId where Post_comment.PostId=%s'
        cur.execute(query,(postId,))
        comments = cur.fetchall()
        for comment in comments:
            
            Photo=getprofilepic(comment['UserId'])
            
            if Photo is not None:
                Photoname=Photo['Photoname']
            else:
                Photoname="nophotofound.png"

            comment.update({"Photoname":Photoname})

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

def nextcommentid():
    cur = connect_cursor_db()
    query='select count(CommentId) from Comment'
    cur.execute(query)
    postid = cur.fetchone()
    return int(postid['count(CommentId)'])+1
 
def MakeComment(ProfileID,CommentBody,postId):
    commentid=nextcommentid()
    cur = connect_cursor_db()
    cur.callproc( "NewComment",(CommentBody,ProfileID,commentid,postId))
    results =cur.fetchone()
    return results

def updateProfile(ProfileId,Bio,RelationshipStatus):
    cur = connect_cursor_db()
    query='Update Profiles SET Bio=%s,RelationshipStatus=%s where ProfileId=%s'
    cur.execute(query,(Bio,RelationshipStatus,ProfileId))
    connect_commit_db()

def updateUsers(UsersId,Fname,Lname,Gender,DOB):
    cur = connect_cursor_db()
    query='Update Users SET Fname=%s,Lname=%s,Gender=%s,DOB=%s where UserId=%s'
    cur.execute(query,(Fname,Lname,Gender,DOB,UsersId))
    connect_commit_db()

def updateemail(ProfileId,email):
    cur = connect_cursor_db()
    query='Update profile_email SET email=%s where ProfileId=%s'
    cur.execute(query,(email,ProfileId))
    connect_commit_db()

def updatePhonenumber(ProfileId,PhoneNumber):
    cur = connect_cursor_db()
    query='Update profile_phonenumber SET PhoneNumber=%s where ProfileId=%s'
    cur.execute(query,(PhoneNumber,ProfileId))
    connect_commit_db()

def updateAddress(ProfileId,Street,City):
    cur = connect_cursor_db()
    query='Update profile_address SET Street=%s, City=%s where ProfileId=%s'
    cur.execute(query,(Street,City,ProfileId))
    connect_commit_db()

def nextgroupid():
    cur = connect_cursor_db()
    query='select count(GroupId) from ` Groups`'
    cur.execute(query)
    postid = cur.fetchone()
    return int(postid['count(GroupId)'])+1

def createGroup(groupname,des,profileId):
    groupid=nextgroupid()
    cur = connect_cursor_db()
    cur.callproc( "Newgroup",(groupname,des,profileId,groupid))
    results =cur.fetchone()
    return results

def Groups():
    cur = connect_cursor_db()
    query='select * from ` Groups` limit 20'
    cur.execute(query)
    allgroups = cur.fetchall()
    return allgroups

def GroupsMembers(GroupId,profile):
    cur = connect_cursor_db()
    try:
        query='insert into Groupmembership values(%s,%s)'
        cur.execute(query,(profile,GroupId))
        connect_commit_db()
        return "Group Joined "
    except (cur.IntegrityError ):
        return "Already a member "
    