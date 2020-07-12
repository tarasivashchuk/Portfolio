from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    categories = [("general", "General"), ("work", "Work"), ("technical", "Technical"), ("urgent", "Urgent")]

    name = StringField("Name")
    category = SelectField("Category", choices=categories)
    email = StringField("Email")
    message = TextAreaField("Type your message here...")
    submit = SubmitField(label="Send")
