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
        assert b'Cat' in rv.data

    def test_my_topic(self):
        rv = self.app.get('/cats')  
        # Replace UNH698 Website with the text you expect to see on you topi$
        assert b'Not sure what to make a website of so here is a picture of a cat' in rv.data 

    def test_my_topic(self):
        rv = self.app.get('/dogs')
        # Replace UNH698 Website with the text you expect to see on you topi$
        assert b'Not sure what to make a website of so here is a picture of a dog' in rv.data

if __name__ == '__main__':
    unittest.main()
