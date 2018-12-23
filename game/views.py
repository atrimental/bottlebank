from flask import Blueprint, request
from models.game import Game
import templates
from models.user import User

bp = Blueprint('game', __name__)

@bp.route('/<index>')
def game_home(index):
    page = templates.env.get_template('game/index.html')
    game = Game.get(index)
    user = User.get_authed_user(game, request)
    return page.render(game=game, user=user)