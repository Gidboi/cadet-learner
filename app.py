from flask import Blueprint, render_template


app1 = Blueprint('app1', __name__)


#app1.debug = True


@app1.route('/')
def index():
    return render_template('index.html')


@app1.route('/profile')
def profile():
    return render_template('profile.html')