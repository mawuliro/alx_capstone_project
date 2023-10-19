from flask import render_template, request
from app.models import Post
from app.main import main


@main.route("/")
@main.route("/base")
def base():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('base.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
