#pip install flask
#pip install flask-sqlalchemy
#pip install psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/postgraduate'
db = SQLAlchemy(app)

class Student(db.Model):
  __tablename__ = 'student'
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(), nullable=False)
  secondname = db.Column(db.String(), nullable=False)
  lastname = db.Column(db.String(), nullable=False)
  gender = db.Column(db.String(20), default='m')
  datebirth = db.Column(db.DateTime(), default = datetime.datetime.now)
  reg_no = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False)
  phone = db.Column(db.String(), nullable=False)
  programme = db.Column(db.String(20), nullable=False)
  school = db.Column(db.Integer(), nullable=False)
  department = db.Column(db.Integer(),nullable=False)
  campus = db.Column(db.Integer(), nullable=False)
  createddate = db.Column(db.DateTime(),default=datetime.datetime.now)
  
  def __repr__(self):
   return f'<Student ID: {self.id}, name: {self.firstname}>'
  
with app.app_context():  
    db.create_all() #creates that tables based on the db.Model that was configured with the associated table

# with app.app_context():    
#     person = Person(name='Harisson Mwei')
#     db.session.add(person)
#     db.session.commit()    

@app.route('/')
def index():
   # person = Person.query.first() 
   return 'Table student created ! '


#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0")