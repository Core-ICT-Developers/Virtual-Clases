#pip install flask_migrate

from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/postgraduate'
db = SQLAlchemy(app)
migrate = Migrate(app, db)