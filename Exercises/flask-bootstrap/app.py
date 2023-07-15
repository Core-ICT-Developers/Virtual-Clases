
#python -m venv venvironment

#activate the venvironment :
#venvironment\Scripts\activate

# pip install flask-bootstrap

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os

def create_app():
  template_dir = os.path.abspath('views')
  app = Flask(__name__, template_folder=template_dir)
  Bootstrap(app)
  return app


app = create_app()

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route("/about/")
def about():
    return render_template('about.html')
  
  
@app.route("/contact/")
def contact():
    return render_template('contact.html')
  
  
  
if __name__ == '__main__':
        app.run(debug=True)