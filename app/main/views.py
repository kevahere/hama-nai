from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import ForumPost, ForumThread, Event, Roomate
from flask_login import login_required, current_user
from .forms import PostForm, ThreadForm, EventsForm, UpdateProfile
from .. import db, photos
from werkzeug.utils import secure_filename


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
        thread = form.comment.data
        new_thread = ForumThread(thread=thread, post_id=post_id)

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


@main.route('/new_event', methods=['GET', 'POST'])
def new_event():
    """
    display the new event form
    :return:
    """

    event_form = EventsForm()

    if event_form.validate_on_submit():
        title = event_form.event_title.data
        description = event_form.event_desc.data
        location = event_form.event_loc.data
        charges = event_form.event_charges.data
        filename = photos.save(event_form.pic.data)
        pic = f'event_pics/{filename}'

        fresh_event = Event(event_name=title,
                          event_description=description,
                          event_location=location,
                          event_charges=charges,
                          event_poster=pic)

        fresh_event.save_event()

        return redirect('events')
    title = 'Post an event'
    return render_template('new_event.html', title=title, event_form=event_form)


@main.route('/events')
def events():
    """
    display a list of events
    :return:
    """
    events = Event.query.filter_by().all()
    title= 'Whats happening'
    return render_template('events.html', title=title, events=events)


@main.route('/roomate/<uname>&<id_roomate>')
@login_required
def profile(uname, id_roomate):
    user = Roomate.query.filter_by(username=uname).first()

    title = f"{uname.capitalize()}'s Profile"

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user=user, title=title)


@main.route('/roomate/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = Roomate.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    update_form = UpdateProfile()

    if update_form.validate_on_submit():
        user.bio = update_form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username, id_user=user.id))
    title = 'Update Bio'
    return render_template('profile/update.html', form=update_form, title=title)

@main.route('/roomate/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = Roomate.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname,id_user=current_user.id))

@main.route('/roomates')
def roomates():
    '''
    root page function that returns the index page and its data
    '''
    title = "Welcome | Roomates"

    return render_template("roomates.html", title=title)

@main.route('/housing')
def housing():
    '''
    root page function that returns the index page and its data
    '''
    title = "Welcome | Housing"

    return render_template("Housing.html", title=title)