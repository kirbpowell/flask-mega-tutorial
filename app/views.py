from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():

    user = {'nickname': 'Kirby'} #fake user
    posts = [{'author':{'nickname':'John'}, 'body':'Beautiful day in Prague!'},
             {'author':{'nickname':'Patton'}, 'body':'Wow kirb much kirb wow.'}]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
