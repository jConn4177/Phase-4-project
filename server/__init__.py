
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
