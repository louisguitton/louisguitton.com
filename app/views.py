from flask import render_template, flash, redirect

from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    projects = [  # fake array of projects
        {
            'title': "2055 = 2048 + 007",
            'description': "The 2048 game meets James Bond!",
            'nickname': '2055',
            'template': "2055.html"
        },
        {
            'title': "Football Betting",
            'description': "A dashboard of the SoFootLigue Data.",
            'nickname': 'sofoot',
            'template': "sofoot.html"
        }
    ]
    return render_template(
        "index.html",
        title='Home',
        projects=projects
    )


@app.route('/contact')
def contact():
    social_links = [
        {
            "title": "linkedin",
            "url": "https://fr.linkedin.com/in/louisguitton"
        },
        {
            "title": "twitter",
            "url": "https://twitter.com/louis_guitton"
        },
        {
            "title": "github",
            "url": "https://github.com/louisguitton"
        }
    ]
    return render_template(
        "contact.html",
        title='Contact',
        social_links=social_links
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/projects/<nickname>')
def projects(nickname):

    projects = [  # fake array of projects
        {
            'title': "2055 = 2048 + 007",
            'description': "The 2048 game meets James Bond!",
            'nickname': '2055',
            'template': "2055.html"
        },
        {
            'title': "Football Betting",
            'description': "A dashboard of the SoFootLigue Data.",
            'nickname': 'sofoot',
            'template': "sofoot.html"
        }
    ]
    selected_project = [p for p in projects if p['nickname'] == nickname][0]

    return render_template(
        'project.html',
        title=nickname,
        project=selected_project
    )
