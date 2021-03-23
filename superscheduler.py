"""
Todo: look at dynamically or lookup of urls
via config file/openapi spec, using like config
parse or something.

"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)



# postgresql://super:superscheduler@postgres:5432/post
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
#         user='super',
#         passwd='super',
#         host=,
#         port=DBPORT,
#         db=DBNAME)

@app.route('/')
@app.route('/index.html')
@app.route('/dashboard')
def index():
    return render_template('index.html', the_title='Dashboard')

@app.route('/contractor.html')
@app.route('/contractor')
def contractor():
    return render_template('contractor.html', the_title='Contractors')

@app.route('/schedule.html')
@app.route('/schedule')
def schedule():
    return render_template('schedule.html', the_title='Schedule')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
