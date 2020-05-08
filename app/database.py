from app import mysql

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
        query='SELECT Users.UserId,Profiles.ProfileId,Username,Fname,Lname,Gender,DOB FROM Users join User_profile on Users.UserId=User_profile.UserId join Profiles on User_profile.ProfileId=Profiles.ProfileId WHERE Profiles.Username = %s'
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
        
    cur = connect_cursor_db()
    cur.callproc('NewUser',[username,profileId,userId,password,
    bio,relationshipStatus,fname,lname,gender,dOB,email,phoneNumber])
    results=cur.stored_results()
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

    
        
    

 