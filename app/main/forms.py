from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
class form():
    pass

class NameForm(Form):
    name = StringField("what's your name?" , validators={Required()})
    submit = SubmitField('Submit')

