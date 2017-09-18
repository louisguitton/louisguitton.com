WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = os.path.join(basedir, 'app.db')


TWITTER = dict(
    consumer_key='CtWpLfJjENqOWhoUpXKJBNNIL',
    consumer_secret='P9z98T50kMT0TtnBQDWsuaVX6aSBRFk9r2q8biUcsd2jrOeTQu',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
)

FACEBOOK = dict(
    consumer_key='920424831466867',
    consumer_secret='b538781f0975b5a627e9ea5a5edf834e',
    request_token_params={'scope': 'email'},
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_method='GET',
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
)
