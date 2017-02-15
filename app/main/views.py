from flask import render_template
from . import main
from ..decrators import permission_required,admin_required
from ..models import Permission
from flask_login import login_required

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return 'For Administrator'

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderator_only():
    return 'For Moderators'
