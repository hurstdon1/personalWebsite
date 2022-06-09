from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):

    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    subject = StringField("Subject")
    message = StringField("Message") 
    submit = SubmitField("send")
    