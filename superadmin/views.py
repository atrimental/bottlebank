from flask import Blueprint
from models.game import Game
from auth import require_superadmin
import templates

bp = Blueprint('superadmin', __name__)

@bp.route('/')
@require_superadmin
def super_admin_home():
    page = templates.env.get_template('superadmin/index.html')
    return page.render(games=Game.get_all_games())