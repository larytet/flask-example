import os
import unittest
import tempfile


from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()