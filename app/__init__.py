from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#SQLALCHEMY_DATABASE_URI = "postgresql://fhadabone:bread@localhost/project1"
SQLALCHEMY_DATABASE_URI= 'postgresql://eefkbnpslramlq:441e17fa0f5ca1eeb1c5f6ea7551dcb4712cb624cd5df3097e401e2c235db157@ec2-107-20-177-161.compute-1.amazonaws.com:5432/db7drfrcq1arfq'
SQLALCHEMY_TRACK_MODIFICATIONS = False # added just to suppress a warning
UPLOAD_FOLDER = "./app/static/uploads"
SECRET_KEY= "$up3r83c123t"

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views