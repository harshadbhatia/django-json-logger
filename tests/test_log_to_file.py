from django.test import Client, TestCase


class AddLogsToFile(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status_404(self):
        self.client.get('/404')

    def test_error_500(self):
        self.client.get('/500')

