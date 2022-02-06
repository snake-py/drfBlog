from turtle import title
from .test_setup import TestSetupArticle
from blog.models import Article, ArticleTag
from model_bakery import baker
from pprint import pprint

class ArticleModelTest (TestSetupArticle):
    title = 'Test Article'
    content = 'Test Content'

    def test_bake_model(self, **kwargs):
        self.article = baker.make('blog.Article', **kwargs)
        pprint(self.article.__dict__)

    def create_tag(self, tag='Test Tag'):
        tag = ArticleTag(tag=tag)
        tag.save()
        return tag

    def test_article_string(self):
        self.create_article(self.title, self.content)
        article = Article.objects.get(title=self.title)
        self.assertEqual(str(article), self.title)

    def test_article_tag_relationship(self):
        self.create_article(self.title, self.content)
        article = Article.objects.get(title=self.title)
        self.assertEqual(article.tags.count(), 0)
        tag_1 = self.create_tag('python')
        article.tags.add(tag_1)
        self.assertEqual(article.tags.count(), 1)
        tag_2 = self.create_tag('django')
        article.tags.add(tag_2)
        self.assertEqual(article.tags.count(), 2)