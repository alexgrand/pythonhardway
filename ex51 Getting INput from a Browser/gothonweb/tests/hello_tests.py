import unittest
from hello import app

app.config['TESTING'] = True
web = app.test_client()


class TestHello(unittest.TestCase):
    def test_index(self):
        """
        Test Hello fn and page
        """
        rv = web.get('/', follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

        rv = web.get('/hello', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b"Fill Out This Form", rv.data)

        data = {'name': 'Alex', 'greet': 'Hola'}
        rv = web.post('/hello', follow_redirects=True, data=data)
        self.assertIn(b"Alex", rv.data)
        self.assertIn(b"Hola", rv.data)
