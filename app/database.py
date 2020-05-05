from app import mysql

def connect_cursor_db():
    return mysql.connection.cursor()
def connect_commit_db():
    return mysql.connection.commit() 

def add_user(name, email):    
    cur = connect_cursor_db()
    cur.execute('insert into users (name, email) values (%s, %s)',
    (name, email))
    connect_commit_db()

def get_user(username):
    try:
        cur = connect_cursor_db()
        cur.execute('SELECT * FROM users WHERE name = %s',(username,))
        account = cur.fetchall()
        return account
    except:
        print("something went wrong")
        
    

 