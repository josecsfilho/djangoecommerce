from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def _assert_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')