from flask import Blueprint
import models.conn

bp = Blueprint('superadmin', __name__)

@bp.route('/')
def super_admin_home():
    return "Super"