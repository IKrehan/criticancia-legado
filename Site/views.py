from flask import Blueprint
import os

from .models import Posts, Adms, Podcasts
from .extensions import login, Blueprint, render_template, send_file, login_required, request, redirect, db, date, flash

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

@views.route("/admin/createpost", methods=['GET', 'POST'])
@login_required
def createPost():
    if request.method == "POST":

        title = request.form["title"]
        subtitle = request.form["subtitle"]
        category = request.form["category"]
        content = request.form["content"]

        if request.files:
            banner = request.files['banner']

            if banner.filename == "":
                flash('Image need a name!')
                return render_template('admin/createPost.html')

            banner.save(os.path.join(os.path.dirname(__file__)) + '\\static\\img\\banners', banner.filename)


            post = Posts(title=title, subtitle=subtitle, category=category, content=content, author="Test", 
                date_posted=date.today(), banner='static\\img\\banners' + banner.filename)
            db.session.add(post)
            db.session.commit()
            flash('Posted with sucess!')

    return render_template('admin/createPost.html')


@views.route("/admin/createpodcast", methods=['GET', 'POST'])
@login_required
def createPodcast():

    if request.method == "POST":

        title = request.form["title"]
        desc = request.form["desc"]
        if request.files:
            banner = request.files['banner']
            audio = request.files['audio']

            banner.save(os.path.join(os.path.abspath(os.path.dirname(__file__)) + '\\static\\img\\banners', banner.filename))
            audio.save(os.path.join(os.path.abspath(os.path.dirname(__file__))+ '\\static\\uploads', audio.filename))


            podcast = Podcasts(title=title, desc=desc, date_posted=date.today(), banner='static\\img\\banners' 
                + banner.filename, audio_file='static\\podcasts' + audio.filename)
            db.session.add(podcast)
            db.session.commit()
            flash('Podcast upado com sucesso!')
    
    return render_template('admin/createPodcast.html')