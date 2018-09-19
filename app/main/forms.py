from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import Required


class PostForm(FlaskForm):
    title = StringField('Forum topic', validators=[Required()])
    post = TextAreaField('Description')
    submit = SubmitField('Submit')


class ThreadForm(FlaskForm):
    comment = TextAreaField('Say something about this', validators=[Required()])
    submit = SubmitField('Submit')


class EventsForm(FlaskForm):
    event_title = TextAreaField('Event title')
    event_desc = TextAreaField('Description')
    event_loc = TextAreaField('Location')
    event_charges = TextAreaField('Charges')
    pic = FileField(validators=[FileRequired()])
    submit = SubmitField('Submit')
