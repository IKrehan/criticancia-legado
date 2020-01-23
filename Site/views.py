from flask import Blueprint, render_template

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
    return render_template("filmes.html")


@views.route("/series")
def series():
    return render_template("series.html")

@views.route("/criticast")
def criticast():
    return render_template("criticast.html")


@views.route("/criticast/<int:podcast_id>")
def criticastList(podcast_id):
    podcast = Podcasts.query.filter_by(id=podcast_id).one()

    return render_template("criticastPost.html", podcast=podcast)


@views.route("/games")
def games():
    return render_template("games.html")


@views.route("/post/<int:post_id>")
def post(post_id):
    post = Posts.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@login.user_loader
def load_user(user_id):
    return Adms.query.get(int(user_id))
