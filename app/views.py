from flask import render_template, flash, redirect

from app import app


@app.route('/')
@app.route('/index')
def index():
    extra = {
        'title': 'Welcome'
    }
    return render_template(
        "index.html",
        title='Home',
        extra=extra
    )


@app.route('/about')
def about():
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

    extra = {
        "title": "Social Media",
        "body": "All my accounts."
    }

    return render_template(
        "about.html",
        title='About',
        social_links=social_links,
        extra=extra
    )


@app.route('/projects')
@app.route('/projects/<nickname>')
def projects(nickname=None):
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

    extra = {
        'title': "My ideas",
        'body': 'At least some of them'
    }
    if nickname:
        selected_project = [p for p in projects if p['nickname'] == nickname][0]

        return render_template(
            'project.html',
            title=nickname,
            project=selected_project,
            extra=extra
        )
    else:
        return render_template(
            'projects.html',
            title='Projects',
            projects=projects,
            extra=extra
        )
