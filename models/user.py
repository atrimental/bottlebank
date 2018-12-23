from models.conn import client
from google.cloud import datastore
from flask import Request


class User():
    def __init__(self, game, username):
        self.game = game
        self.username = username
    
    @classmethod
    def from_entity(cls, game, entity):
        return User(game, entity['username'])

    def create(self):
        complete_key = client.key('Game', self.game.index, 'User', self.username)
        task = datastore.Entity(key=complete_key)
        task.update({
            'username': self.username,
        })
        client.put(task)

    @classmethod
    def get_authed_user(cls, game, request: Request):
        """DOES NOT DO ANY AUTHENTICATION. Yet."""
        username = request.args.get('user')
        if username is None:
            return None
        return game.get_user(username)