import os
import unittest
import tempfile


import yalas

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = yalas.app.app
        self.app.testing = True

    def tearDown(self):
        os.close(self.db_fd)

    def test_index(self):
        rv = self.app.get('/')
        assert b'Index Page' in rv.data
        
if __name__ == '__main__':
    unittest.main()