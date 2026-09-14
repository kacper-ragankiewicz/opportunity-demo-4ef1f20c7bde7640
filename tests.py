import unittest

from app import app


class WorkItemsApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_returns_all_items_and_summary(self):
        response = self.client.get('/api/work-items')
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(payload['items']), 4)
        self.assertEqual(payload['summary']['planned'], 1)
        self.assertEqual(payload['summary']['in_progress'], 2)
        self.assertEqual(payload['summary']['done'], 1)

    def test_filters_by_status(self):
        response = self.client.get('/api/work-items?status=in_progress')
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(payload['items']), 2)
        self.assertTrue(all(item['status'] == 'in_progress' for item in payload['items']))

    def test_rejects_invalid_status(self):
        response = self.client.get('/api/work-items?status=blocked')
        payload = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(payload['error'], 'invalid_status')
        self.assertIn('planned', payload['allowed'])


if __name__ == '__main__':
    unittest.main()
