import unittest
from api.app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_events(self):
        response = self.app.get('/events?actor=john_doe&action=user_logged_in')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == "__main__":
    unittest.main()
