"""
Todo: look at dynamically or lookup of urls
via config file/openapi spec, using like config
parse or something.

"""

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
import yaml
import actions

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://super:superscheduler@postgres:5432/super"

db = SQLAlchemy(app)
# SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".

db.init_app(app)
migrate = Migrate(app, db)

# Define working directory and file path
cwd_path = Path.cwd()
file_path = "{cwd}/config/local-vars.yaml".format(cwd=cwd_path)

# Loop through the *-vars.yaml file
with open(file_path, "r") as vars_file:
    app_config = yaml.safe_load(vars_file)

# Define variable values from config file
flask_port = app_config["flask_port"]
database_uri = app_config["database_uri"]


@app.route('/')
@app.route('/index.html')
@app.route('/dashboard.html')
@app.route('/dashboard')
def index():
    return render_template('index.html', the_title='Dashboard')

@app.route('/contractor.html')
@app.route('/contractor')
def contractor():
    add_results = actions.add_contractor("Billy","Thorton","BU name here","801-555555-5")
    return render_template('contractor.html', the_title='Contractors')

@app.route('/schedule.html')
@app.route('/schedule')
def schedule():
    return render_template('schedule.html', the_title='Schedule')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    
