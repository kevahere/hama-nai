from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import ForumPost, ForumThread
from .forms import PostForm, ThreadForm


@main.route('/forum')
def forum():
    """
    Display the landing page for the forum
    :return:
    """
    posts = ForumPost.get_posts()
    title = 'Nahamia nai forum'

    return render_template('forum.html', title=title, posts=posts)


@main.route('/new_post', methods=['GET', 'POST'])
def new_post():
    """
    Displays the new post page with a markdown form
    :return:
    """
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        post_actual = post_form.post.data

        new_post = ForumPost(title=title, post=post_actual)

        new_post.save_post()

        return redirect(url_for('main.index'))

    return render_template('new_post.html', post_form=post_form)


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
        new_thread = form.comment.data
        new_thread = ForumThread(thread=new_thread, post_id=post_id)

        new_thread.save_comment()

        return redirect(url_for('.post', post_id=post.id))

    thread = ForumThread.query.filter_by(post_id=post_id).all()

    return render_template('post.html', post=post, post_id=post_id, comment_form=form, comments=thread)


@main.route('/')
def index():

    '''
    View root function that returns the index page
    '''

    return render_template('index.html')

@main.route('/culture')
def culture():

    '''
    View root function that returns the index page
    '''

    return render_template('culture.html')

