from flask import Blueprint
from models.game import Game
import templates

bp = Blueprint('game', __name__)

@bp.route('/<index>')
def game_home(index):
    page = templates.env.get_template('game/index.html')
    game = Game.get(index)
    return page.render(game=game)