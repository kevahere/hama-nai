from . import db
from datetime import datetime


class ForumPost(db.Model):
    """
    Class that defines the actual blog posts
    """
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    post = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    thread = db.relationship('ForumThread', backref='post', lazy='dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        posts = ForumPost.query.order_by(ForumPost.date_posted.desc()).all()
        return posts


class ForumThread(db.Model):
    """
    class that defines the comments on pitches
    """

    __tablename__ = 'threads'

    id = db.Column(db.Integer, primary_key=True)
    thread = db.Column(db.String(255))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()


class Event(db.Model):
    """
    class that defines an event
    """

    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50))
    event_description = db.Column(db.String(250))
    event_location = db.Column(db.String(50))
    event_charges = db.Column(db.String(50))
    event_poster = db.Column(db.String)

    def save_event(self):
        db.session.add(self)
        db.session.commit()

