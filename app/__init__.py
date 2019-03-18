from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "s3CRET$toK33p$3c13et"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://fhadabone:postgres@localhost/project1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zhibonanwowmqv:8079725deaf091ba8cc3ecad9cc399a2e5a0bb0c88de3dfa4db3facfe763db7b@ec2-174-129-28-38.compute-1.amazonaws.com:5432/d1hsgh7pccset5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
UPLOAD_FOLDER = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
