#pip install flask
#pip install flask-sqlalchemy
#pip install psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/exercise'
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  
with app.app_context():  
    db.create_all() #creates that tables based on the db.Model that was configured with the associated table

@app.route('/')
def index():
   return 'Table person has been successfully created!'



#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0")