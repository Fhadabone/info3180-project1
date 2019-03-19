from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#SQLALCHEMY_DATABASE_URI = "postgresql://bread:test@localhost/project1"
SQLALCHEMY_DATABASE_URI= 'postgresql://liksbqgocctrmk:4d1659399cf74a6fc2e0ae82bce40fde99db170ce1e2af30824df56de3a63ef4@ec2-50-17-227-28.compute-1.amazonaws.com:5432/ddqjam3m7ipl4n'
SQLALCHEMY_TRACK_MODIFICATIONS = False # added just to suppress a warning
UPLOAD_FOLDER = "./app/static/uploads"
SECRET_KEY= "MYKEY"

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views