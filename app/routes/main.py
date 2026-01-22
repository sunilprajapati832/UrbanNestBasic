from flask import Blueprint, render_template
from app.models import Property

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # ✅ Only show verified properties, latest 5
    properties = Property.query.filter_by(is_verified=True) \
                               .order_by(Property.created_at.desc()) \
                               .limit(5).all()
    return render_template('home.html', properties=properties)
