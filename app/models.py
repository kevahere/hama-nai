from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
from time import time
from flask_login import UserMixin

class ForumPost(db.Model):
    """
    Class that defines the actual blog posts
    """
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    post = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

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


class Roomate(UserMixin, db.Model):
    __tablename__ = 'roomates'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, index=True)
    hash_pass = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    profile_pic_path = db.Column(db.String(255))
    bio = db.Column(db.String(255))

    photos = db.relationship('PhotoProfile', backref='roomate', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def password(self, password):
        self.hash_pass = generate_password_hash(password)

    def set_password(self, password):
        self.hash_pass = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hash_pass, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in}, os.environ.get('SECRET_KEY'),
                          algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password(token):
        try:
            id = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])['reset_password']
        except:
            return
        return Roomate.query.get(id)

    def __repr__(self):
        return f'Roomate {self.username}'
