#pip install Flask
#pip install -U Flask-SQLAlchemy
#pip install Flask-Migrate
#pip install psycopg2

#pip install virtualenv

#create a virtual env :
#python -m venv postgraduate_project_env


#NB : if there are restrictions, open cmd : Set-ExecutionPolicy Unrestricted on powershell

#activate the invironment :
#postgraduate_project_env\Scripts\activate


# The flask command is installed by Flask, not your application; it must be told where to find your application in order to use it. 
# The FLASK_APP environment variable is used to specify how to load the application.

# set FLASK_APP=todo
# set FLASK_ENV=development
# flask --app todo run

#running migrations
#flask --app todo db init
#flask --app todo db migrate -m "Initial migration."
#flask --app todo db upgrade - apply the changes described by the migration script to your database

#addition of the complete column
#flask --app todo db migrate -m "Addition of the complete column"
#then do flask --app todo db upgrade

# your code here
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/exercise'
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)


def __repr__(self):
    return f'<Todo:{self.id} , description : {self.description}'


@app.route('/')
def create_todo():
    #db.create_all()
    description = request.args['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return f'Successfully saved {description}'
    
    
def index():
    return 'Hello '  

    
#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0")    