from flask import Blueprint

bp = Blueprint('superadmin', __name__)

@bp.route('/')
def super_admin_home():
    return "Super"