from . import db


class Property(db.Model):
    __tablename__ = "properties"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(127))
    price = db.Column(db.Integer)
    types = db.Column(db.Enum("apartment", "house", name="property_type_enum"))
    description = db.Column(db.String(255))

    def __init__(
        self, name, title, bedrooms, bathrooms, location, price, types, description
    ):
        self.name = name
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.types = types
        self.description = description
