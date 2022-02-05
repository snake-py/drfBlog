from .test_setup import TestSetupArticle
from django.urls import reverse
from blog.models import Article

class TestArticleViews(TestSetupArticle):
    title = 'Test Article'
    content = 'Test Content'

    def test_get_articles(self):
        response = self.client.get(self.article_urls)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 0)
        self.assertEqual(response.data['results'], [])

    def test_create_article(self):
        self.create_article(self.title, self.content)

        response = self.client.get(self.article_urls)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], self.title)
        self.assertEqual(response.data['results'][0]['content'], self.content)

    def test_get_single_article(self):
        self.create_article(self.title, self.content)
        article_id = Article.objects.get(title=self.title).id
        self.article_single_pk = reverse('article-detail', kwargs={'pk': article_id})
        response = self.client.get(self.article_single_pk)
        self.assertEqual(response.status_code, 200)

