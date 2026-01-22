from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from app import db
from app.models import Property, PropertyImage
import os
from werkzeug.utils import secure_filename

property_bp = Blueprint('property', __name__)

# Absolute path to uploads
def get_upload_folder():
    return os.path.join(current_app.root_path, 'static', 'uploads')

# ================= CONTEXT PROCESSOR FOR ADMIN NOTIFICATION =================
@property_bp.app_context_processor
def inject_unverified_count():
    if current_user.is_authenticated and current_user.role == 'admin':
        count = Property.query.filter_by(is_verified=False).count()
        return dict(unverified_count=count)
    return dict(unverified_count=0)

# ================= LIST + FILTER =================
@property_bp.route('/properties')
def property_list():
    query = Property.query.filter_by(is_verified=True)  # ✅ Only verified for public

    city = request.args.get('city')
    property_type = request.args.get('property_type')
    listing_type = request.args.get('listing_type')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')

    if city:
        query = query.filter(Property.city.ilike(f"%{city.strip()}%"))
    if property_type:
        query = query.filter(Property.property_type == property_type.strip())
    if listing_type:
        query = query.filter(Property.listing_type == listing_type.strip())
    if min_price:
        query = query.filter(Property.price >= int(min_price))
    if max_price:
        query = query.filter(Property.price <= int(max_price))

    properties = query.all()
    return render_template("property_list.html", properties=properties)

# ================= DETAILS =================
@property_bp.route('/property/<int:id>')
def property_detail(id):
    prop = Property.query.get_or_404(id)
    return render_template("property_detail.html", property=prop)

# ================= ADD =================
@property_bp.route('/property/add', methods=['GET', 'POST'])
@login_required
def add_property():
    if request.method == 'POST':
        prop = Property(
            title=request.form['title'].strip(),
            description=request.form['description'].strip(),
            price=int(request.form['price']),
            property_type=request.form['property_type'].strip(),
            listing_type=request.form['listing_type'].strip(),
            state=request.form['state'].strip(),
            city=request.form['city'].strip(),
            address=request.form['address'].strip(),
            area_sqft=int(request.form['area_sqft']),
            bedrooms=int(request.form['bedrooms']),
            bathrooms=int(request.form['bathrooms']),
            owner_id=current_user.id,
            is_verified=False
        )
        db.session.add(prop)
        db.session.commit()

        folder = get_upload_folder()
        for file in request.files.getlist('images')[:25]:
            if file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(folder, filename))
                db.session.add(PropertyImage(
                    image_path=filename,
                    property_id=prop.id
                ))
        db.session.commit()
        flash("Property submitted for verification", "success")
        return redirect(url_for('property.property_detail', id=prop.id))
    return render_template("add_property.html")

# ================= UPDATE =================
@property_bp.route('/property/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_property(id):
    prop = Property.query.get_or_404(id)
    if current_user.id != prop.owner_id and current_user.role != 'admin':
        flash("Unauthorized", "danger")
        return redirect(url_for('property.property_list'))

    if request.method == 'POST':
        prop.title = request.form['title'].strip()
        prop.description = request.form['description'].strip()
        prop.price = int(request.form['price'])
        prop.property_type = request.form['property_type'].strip()
        prop.listing_type = request.form['listing_type'].strip()
        prop.state = request.form['state'].strip()
        prop.city = request.form['city'].strip()
        prop.address = request.form['address'].strip()
        prop.area_sqft = int(request.form['area_sqft'])
        prop.bedrooms = int(request.form['bedrooms'])
        prop.bathrooms = int(request.form['bathrooms'])

        folder = get_upload_folder()
        for file in request.files.getlist('images')[:25]:
            if file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(folder, filename))
                db.session.add(PropertyImage(
                    image_path=filename,
                    property_id=prop.id
                ))

        db.session.commit()
        flash("Property updated", "success")
        return redirect(url_for('property.property_detail', id=prop.id))
    return render_template("update_property.html", property=prop)

# ================= DELETE PROPERTY =================
@property_bp.route('/property/delete/<int:id>')
@login_required
def delete_property(id):
    prop = Property.query.get_or_404(id)
    if current_user.id != prop.owner_id and current_user.role != 'admin':
        flash("Unauthorized access", "danger")
        return redirect(url_for('property.property_list'))

    folder = get_upload_folder()
    for img in prop.images:
        image_path = os.path.join(folder, img.image_path)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(prop)
    db.session.commit()
    flash("Property deleted successfully", "success")
    return redirect(url_for('property.property_list'))

# ================= DELETE IMAGE =================
@property_bp.route('/property/image/delete/<int:image_id>')
@login_required
def delete_property_image(image_id):
    img = PropertyImage.query.get_or_404(image_id)
    if current_user.role != 'admin' and img.property.owner_id != current_user.id:
        flash("Unauthorized", "danger")
        return redirect(url_for('property.property_detail', id=img.property_id))

    path = os.path.join(get_upload_folder(), img.image_path)
    if os.path.exists(path):
        os.remove(path)

    db.session.delete(img)
    db.session.commit()
    flash("Image removed", "success")
    return redirect(url_for('property.property_detail', id=img.property_id))

# ================= ADMIN DASHBOARD =================
@property_bp.route('/admin/unverified')
@login_required
def unverified_properties():
    if current_user.role != 'admin':
        flash("Unauthorized", "danger")
        return redirect(url_for('main.home'))

    properties = Property.query.filter_by(is_verified=False).all()
    return render_template("unverified_properties.html", properties=properties)

@property_bp.route('/admin/verify/<int:id>')
@login_required
def verify_property(id):
    if current_user.role != 'admin':
        flash("Unauthorized", "danger")
        return redirect(url_for('main.home'))

    prop = Property.query.get_or_404(id)
    prop.is_verified = True
    db.session.commit()
    flash(f"Property '{prop.title}' has been verified!", "success")
    return redirect(url_for('property.unverified_properties'))
