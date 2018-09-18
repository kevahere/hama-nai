from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class PostForm(FlaskForm):
    title = StringField('Forum topic', validators=[Required()])
    post = TextAreaField('Description')
    submit = SubmitField('Submit')


class ThreadForm(FlaskForm):
    comment = TextAreaField('Say something about this', validators=[Required()])
    submit = SubmitField('Submit')