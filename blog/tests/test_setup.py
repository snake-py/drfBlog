from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetupArticle(APITestCase):

    def create_article(self, title='Test Article', content='Test Content'):
        article_data = {
            'title': title,
            'content': content,
        }
        return self.client.post(self.article_urls, article_data)

    
    def setUp(self):
        self.article_urls = reverse('article-list')
        self.article_single_pk = reverse('article-detail', kwargs={'pk': 1})
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
