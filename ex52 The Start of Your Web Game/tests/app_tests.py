import unittest
from app import app

app.config['TESTING'] = True
web = app.test_client()


class TestApp(unittest.TestCase):
    def test_index(self):
        """
        Test index page
        """
        rv = web.get('/', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
