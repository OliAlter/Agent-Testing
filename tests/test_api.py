import unittest
from src.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_task(self):
        response = self.client.post('/tasks', json={"title": "Test Task"})
        self.assertEqual(response.status_code, 201)

    # TODO: Add tests for delete_task failure cases
    # TODO: Add tests for GET /tasks/999 (not found)
