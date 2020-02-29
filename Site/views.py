import os

from flask import Blueprint, render_template, send_file

from .models import Posts, Adms, Podcasts
from .extensions import login

views = Blueprint('views', __name__)

@views.route("/")
def home():
    podcasts = Podcasts.query.all()
    posts = Posts.query.all()
    podcasts_size = len(podcasts)
    posts_size = len(posts)
    return render_template("index.html", posts=posts, podcasts=podcasts, posts_size=posts_size, podcasts_size = podcasts_size)


@views.route("/filmes")
def filmes():
    posts = Posts.query.filter_by(category='filmes').all()
    posts_size = len(posts)

    return render_template("category.html", posts=posts, posts_size=posts_size)


@views.route("/series")
def series():
    posts = Posts.query.filter_by(category='series').all()
    posts_size = len(posts)

    return render_template("category.html", posts=posts, posts_size=posts_size)


@views.route("/games")
def games():
    posts = Posts.query.filter_by(category='games').all()
    posts_size = len(posts)

    return render_template("category.html", posts=posts, posts_size=posts_size)


@views.route("/criticast")
def criticast():
    posts = Podcasts.query.all()
    posts_size = len(posts)

    return render_template("criticast.html", posts=posts, posts_size=posts_size)


@views.route("/criticast/<int:podcast_id>")
def criticastPost(podcast_id):
    podcast = Podcasts.query.filter_by(id=podcast_id).one()

    return render_template("criticastPost.html", podcast=podcast)


@views.route("/criticast/download/<int:podcast_id>")
def podcastDownload(podcast_id):

    return send_file(f'static/podcasts/CritiCast-{podcast_id}.mp3', attachment_filename=f'CritiCast-{podcast_id}.mp3')


@views.route("/post/<int:post_id>")
def post(post_id):
    post = Posts.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@login.user_loader
def load_user(user_id):
    return Adms.query.get(int(user_id))


@views.route('/adm')
def homeAdm():
    return render_template('adminHome.html')


@views.route('/admpost')
def postAdm():
    return render_template('adminPosts.html')


@views.route('/admpodcast')
def podcastAdm():
    return render_template('adminPodcast.html')    