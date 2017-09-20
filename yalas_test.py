import os
import unittest
import tempfile


import yalas

class AppTestCase(unittest.TestCase):

    def setUp(self):
        yalas.app.testing = True
        self.app = yalas.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert b'Index Page' in rv.data
        
if __name__ == '__main__':
    unittest.main()