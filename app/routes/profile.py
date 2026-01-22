from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db
import os

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')


def profile_upload_folder():
    folder = os.path.join(current_app.root_path, 'static', 'profile_pics')
    os.makedirs(folder, exist_ok=True)
    return folder


@profile_bp.route('/')
@login_required
def profile():
    return render_template('profile.html')


@profile_bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.name = request.form['name'].strip()
        current_user.phone = request.form['phone'].strip()

        file = request.files.get('image')
        if file and file.filename:
            filename = secure_filename(file.filename)
            file_path = os.path.join(profile_upload_folder(), filename)
            file.save(file_path)
            current_user.image = filename

        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for('profile.profile'))

    return render_template('edit_profile.html')
