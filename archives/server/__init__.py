from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt#For hashin pw
from flask_login import LoginManager #Helps handle sessions

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '6fadf2875131666b089848483978d632'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app) #handles sessions in the background
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from server import routes