from blog import app
from flask import render_template, url_for
from .forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Pele',
        'title': '1st post',
        'content': '1st post content',
        'date_posted': 'February 6, 2021'
    },
    {
        'author': 'MadPele',
        'title': '2nd post',
        'content': '2nd post content',
        'date_posted': 'February 6, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/registration')
def registration():
    form = RegistrationForm()
    return render_template('registration.html', title='Registration', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)