import os
import unittest
import tempfile
from StringIO import StringIO
import collections

from yalas import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True

        # Create a HTTP client for the server
        self.app = app.flask_app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert b'Index' in rv.data

    def test_hello(self):
        rv = self.app.get('/hello/test1')
        assert b'Hello' in rv.data
        assert b'test1' in rv.data

    def test_upload(self):
        rv = self.app.get('/upload')
        assert b'Upload' in rv.data
        assert b'input type' in rv.data
        
        UploadTest = collections.namedtuple('UploadTest', ['filename', 'expected_response'])
        
        upload_tests = [
            UploadTest('status.txt', b'Uploaded'),
            UploadTest('status.html', b'not supported'),
        ]
        for test in upload_tests:
            data = {'file': (StringIO('some random data'), test.filename)}        
            rv = self.app.post('/upload', data=data, follow_redirects=True)
            assert test.expected_response in rv.data
                
    def test_search(self):
        search_query = "find me quick"
        rv = self.app.post('/search', data={"search": search_query}, follow_redirects=True)
        assert search_query in rv.data
        

if __name__ == '__main__':
    unittest.main()