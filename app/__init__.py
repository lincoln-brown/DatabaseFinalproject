from flask import Flask
from flask_login import LoginManager
from flask_mysqldb import MySQL
import MySQLdb.cursors

UPLOAD_FOLDER = './app/static/images'
app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'MyBook'
app.config['MYSQL_CURSORCLASS']="DictCursor"

# Intialize MySQL
mysql = MySQL()
mysql.init_app(app)



# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
