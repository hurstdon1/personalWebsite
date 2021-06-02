from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, validators
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):

    name = TextField("Name", validators=[InputRequired()])
    email = TextField("Email", validators=[InputRequired()])
    subject = TextField("Subject")
    message = TextField("Message") 
    submit = SubmitField("send")
    