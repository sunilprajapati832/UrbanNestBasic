from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# =========================
# USER MODEL
# =========================
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15))  # Phone number added
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='user')  # user / owner
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    properties = db.relationship(
        'Property',
        backref='owner',
        lazy=True
    )

    def __repr__(self):
        return f"<User {self.email}>"


# =========================
# PROPERTY MODEL
# =========================
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    property_type = db.Column(db.String(50))   # Flat / House / Plot
    listing_type = db.Column(db.String(20))    # Sell / Rent
    state = db.Column(db.String(50))
    city = db.Column(db.String(50))
    address = db.Column(db.String(200))

    area_sqft = db.Column(db.Integer)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)

    is_verified = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    # ✅ Multiple images with cascade delete
    images = db.relationship(
        'PropertyImage',
        backref='property',
        cascade='all, delete-orphan',
        lazy=True
    )

    def __repr__(self):
        return f"<Property {self.title}>"


# =========================
# PROPERTY IMAGE MODEL
# =========================
class PropertyImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(200), nullable=False)

    property_id = db.Column(
        db.Integer,
        db.ForeignKey('property.id', ondelete='CASCADE'),
        nullable=False
    )

    def __repr__(self):
        return f"<PropertyImage {self.image_path}>"
