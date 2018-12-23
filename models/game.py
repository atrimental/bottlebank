from models.conn import client
from google.cloud import datastore
from models.user import User


class Game():
    def __init__(self, index, name):
        self.index = index
        self.name = name

    @classmethod
    def from_entity(cls, entity):
        return Game(entity['index'], entity['name'])

    @classmethod
    def get_all_games(cls):
        game_data = client.query(kind='Game')
        return [Game.from_entity(g) for g in game_data.fetch()]

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
        return Game.from_entity(entity)

    def get_all_users(self):
        ancestor = client.key('Game', self.index)
        q = client.query(kind='User', ancestor=ancestor)
        return [User.from_entity(self, e) for e in q.fetch()]

    def get_user(self, username: str):
        entity = client.get(client.key('Game', self.index, 'User', username))
        return User.from_entity(self, entity)