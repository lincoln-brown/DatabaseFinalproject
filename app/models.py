
from werkzeug.security import generate_password_hash


class UserProfile():
    
    user={'id':'0011',
    'firstname':'lincoln',
    'lastname':"brown",
    'username':"links",
    'Password':"pasword123"
    }
   
    id = user['id']
    first_name = user['firstname']
    last_name = user['lastname']
    username = user['username']
    password = user['Password']


    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
