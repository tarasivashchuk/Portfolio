import flask

from forms import ContactForm

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"  # Something secure


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    name = "Taras"
    category = "General"
    email = "taras@tarasivashchuk.com"
    message = "Hello form!"
    form = ContactForm()

    if form.validate_on_submit():
        app.logger.info(f"Contact Form - Category ({type(form.category.value)}: {form.category.value}")
        name, category, email, message = form.name.data, form.category.data, form.email.data, form.message.data
        form.name.data, form.category.data, form.email.data, form.message.data = "", "", "", ""
        # return flask.url_for(".index")

    return flask.render_template("contact.html", form=form, name=name, category=category, email=email, message=message)


if __name__ == '__main__':
    app.run(debug=True)
