"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import logging
import os

from flask import (
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from werkzeug.utils import secure_filename

from app import app, db
from app.config import Config
from app.forms import PropertyForm
from app.models import Property

###
# Routing for your application.
###


@app.route("/")
def home():
    """Render website's home page."""
    return render_template("home.html")


@app.route("/about/")
def about():
    """Render the website's about page."""
    return render_template("about.html", name="properties")


@app.route("/properties")
def properties():
    """Render the website's property listings"""
    props = Property.query.all()
    return render_template("properties.html", properties=props)


@app.route("/properties/create", methods=["POST", "GET"])
def create():
    """Render the website form"""
    # Instantiate your form class
    form = PropertyForm()
    if form.validate_on_submit() and request.method == "POST":
        title = form.title.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        price = form.price.data
        types = form.types.data
        description = form.description.data
        file = form.file.data
        filename = secure_filename(file.filename)
        property = Property(
            name=filename,
            title=title,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            location=location,
            price=price,
            types=types,
            description=description,
        )
        db.session.add(property)
        db.session.commit()
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        flash("Property was successfully added", "success")
        return redirect(url_for("properties"))

    return render_template("create.html", form=form)


@app.route("/properties/<propertyid>")
def get_property(propertyid):
    selproperty = db.session.execute(
        db.select(Property).filter_by(id=propertyid)
    ).scalar()
    return render_template("detail.html", property=selproperty)


###
# The functions below should be applicable to all Flask apps.
###


@app.route("/property/<filename>")
def get_image(filename):
    return send_from_directory(
        os.path.join(os.getcwd(), app.config["UPLOAD_FOLDER"]), filename
    )


# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                "Error in the %s field - %s" % (getattr(form, field).label.text, error),
                "danger",
            )


@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template("404.html"), 404
