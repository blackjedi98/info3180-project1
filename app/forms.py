from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import (
    IntegerField,
    PasswordField,
    SelectField,
    StringField,
    TextAreaField,
    validators,
)
from wtforms.validators import InputRequired, Length


class PropertyForm(FlaskForm):
    """Form class for property innputs"""

    title = StringField("Title", validators=[InputRequired()])
    bedrooms = IntegerField("Number of Bedrooms", validators=[InputRequired()])
    bathrooms = IntegerField("Number of Bathrooms", validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    price = StringField("Price", validators=[InputRequired()])
    types = SelectField(
        "Type", choices=[("house", "House"), ("apartment", "Apartment")]
    )
    description = TextAreaField(
        "Description", validators=[InputRequired(), Length(max=200)]
    )
    file = FileField(
        "Upload Picture of Property",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "png", "jpeg", "webp"], "Only images allowed"),
        ],
    )
