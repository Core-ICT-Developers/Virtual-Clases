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
  
  def __repr__(self):
   return f'<Person ID: {self.id}, name: {self.name}>'
  
with app.app_context():  
    db.create_all() #creates that tables based on the db.Model that was configured with the associated table

with app.app_context():    
    person = Person(name='Harisson Mwei')
    db.session.add(person)
    db.session.commit()    

@app.route('/')
def index():
   person = Person.query.first() 
   return 'Hello ' + person.name


#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0")