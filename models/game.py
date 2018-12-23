from models.conn import client
from google.cloud import datastore


class Game():
    def __init__(self, index, name):
        self.index = index
        self.name = name

    @classmethod
    def get_all_games(cls):
        game_data = client.query(kind='Game')
        return [Game(g['index'], g['name']) for g in game_data.fetch()]

    def create(self):
        complete_key = client.key('Game', self.index)
        task = datastore.Entity(key=complete_key)
        task.update({
            'index': self.index,
            'name': self.name,
        })
        client.put(task)

    @classmethod
    def get(cls, index):
        entity = client.get(client.key('Game', index))
        return Game(entity['index'], entity['name'])