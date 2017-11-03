from flask import render_template, flash, redirect, url_for, session, request, g
from flask_login import login_user, logout_user, current_user, login_required
from flask_oauthlib.client import OAuthException

from app import app, lm, oauth
from app.forms import LoginForm
from app.models import User

facebook = oauth.remote_app(
    'facebook',
    app_key='FACEBOOK'
)

twitter = oauth.remote_app(
    'twitter',
    app_key='TWITTER'
)


@lm.user_loader
def load_user(id):
    return User(id)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
def index():
    user = g.user

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
        },
        {
            'title': "songGIFy",
            'description': "An automatic GIF video clip for the song of my band.",
            'nickname': 'songgify',
            'template': "songgify.html"
        }
    ]

    return render_template(
        "index.html",
        title='Home',
        projects=projects
    )


@app.route('/login')
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    callback = url_for(
        'oauth_authorized',
        next=request.args.get('next') or request.referrer or None,
    )
    return twitter.authorize(callback=callback)


@app.route('/login/authorized')
def oauth_authorized():
    resp = twitter.authorized_response()
    next_url = request.args.get('next') or url_for('index')

    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']

    user, created = User.get_or_create(nickname=session['twitter_user'])

    flash('You were signed in as %s' % user.nickname)
    login_user(user)

    return redirect(next_url)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')


@twitter.tokengetter
def get_twitter_token():
    return session.get('twitter_token')


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
        },
        {
            'title': "songGIFy",
            'description': "An automatic GIF video clip for the song of my band.",
            'nickname': 'songgify',
            'template': "songgify.html"
        }
    ]
    selected_project = [p for p in projects if p['nickname'] == nickname][0]

    return render_template(
        'project.html',
        title=nickname,
        project=selected_project
    )


@app.route('/edit')
@login_required
def edit_projects():
    return 'This is the place where I edit my projects.'
