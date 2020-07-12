import flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

from app import app


class ContactForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email")
    message = TextAreaField("Type your message here...")
    submit = SubmitField(label="Send")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    name = "Taras"
    email = "taras@tarasivashchuk.com"
    message = "Hello form!"
    form = ContactForm()

    if form.validate_on_submit():
        name, email, message = form.name.data, form.email.data, form.message.data
        form.name.data, form.email.data, form.message.data = "", "", ""

    return flask.render_template("contact.html", form=form, name=name, email=email, message=message)