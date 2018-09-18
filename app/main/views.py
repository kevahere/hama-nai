from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import ForumPost, ForumThread
from .forms import PostForm, ThreadForm


@main.route('/')
def index():
    """
    Display the landing page
    :return:
    """
    posts = ForumPost.get_posts()
    title = 'Nahamia nai forum'

    return render_template('index.html', title=title, posts=posts)


@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    """
    display the forum posts
    :param post_id:
    :return:
    """
    post = ForumPost.query.filter_by(id=post_id).first()
    form = ThreadForm()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, post_id=post_id)

        new_comment.save_comment()

        return redirect(url_for('.post', post_id=post.id))

    comments = Comment.query.filter_by(post_id=post_id).all()

    return render_template('post.html', post=post, post_id=post_id, comment_form=form, comments=comments)