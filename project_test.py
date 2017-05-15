import unittest

import flask_server

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_server.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        # Render the / path of the website
        rv = self.app.get('/')
        # Chech that the page contians the desired phrase
        assert b'Hello World' in rv.data

if __name__ == '__main__':
    unittest.main()
