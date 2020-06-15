import mock

from django.test import TestCase, Client
from django.urls import reverse

from backend.views import HomeView


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view_post(self):
        mock_query = mock.MagicMock()
        mock_query.return_value = mock_query
        post_response = self.client.post(path=reverse('search'), data={'keyword': 'American'})
        self.assertEqual(post_response.status_code, 200)
