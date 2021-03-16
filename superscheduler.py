from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
# @app.route('/Dashboard')
@app.route('/')
@app.route('/index.html')
@app.route('/dashboard')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/contractor.html')
@app.route('/contractor')
def contractor():
    return render_template('contractor.html', the_title='Contractors')

@app.route('/schedule.html')
@app.route('/schedule')
def schedule():
    return render_template('schedule.html', the_title='Schedule')

if __name__ == '__main__':
    app.run(debug=True)
