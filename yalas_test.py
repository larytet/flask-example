import os
import unittest
import tempfile


from yalas import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        print app.app
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert b'Index Page' in rv.data
        
if __name__ == '__main__':
    unittest.main()