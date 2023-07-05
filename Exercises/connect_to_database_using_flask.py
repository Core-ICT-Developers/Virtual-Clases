#pip install flask
#pip install flask-sqlalchemy
#pip install psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/exercise'
db = SQLAlchemy(app)
