from models.conn import client
from google.cloud import datastore


class User():
    def __init__(self, game, username):
        self.game = game
        self.username = username

    def create(self):
        complete_key = client.key('Game', self.game.index, 'User', self.username)
        task = datastore.Entity(key=complete_key)
        task.update({
            'username': self.username,
        })
        client.put(task)