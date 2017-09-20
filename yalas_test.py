import os
import unittest
import tempfile
from StringIO import StringIO

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
        assert b'Hello' in rv.data
        assert b'test1' in rv.data
        
    def test_upload(self):
        rv = self.app.get('/upload')
        assert b'Upload' in rv.data
        assert b'input type' in rv.data
        data = {
            'file': (StringIO('some rnadom data'), 'status.txt'),
        }        
        rv = self.app.post('/upload', data=data, follow_redirects=True)
        print rv.data
        assert b'Uploaded' in rv.data
                
if __name__ == '__main__':
    unittest.main()