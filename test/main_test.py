import main
import unittest

class Test_MainPage(unittest.TestCase):
    def test_index(self):
        main.app.testing = True
        client = main.app.test_client()

        r = client.get('/')
        assert r.status_code == 200
        assert 'Hello World' in r.data.decode('utf-8')
