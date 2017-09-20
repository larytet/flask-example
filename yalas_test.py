import os
import unittest
import tempfile


from yalas import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert b'Index Page' in rv.data

    def test_hello(self):
        rv = self.app.get('/hello/test1')
        print rv.data
        assert b'Hello' in rv.data
        assert b'test1' in rv.data
        
if __name__ == '__main__':
    unittest.main()