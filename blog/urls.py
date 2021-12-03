from rest_framework import routers

from .views import ArticleViewSet

article_router = routers.SimpleRouter()
article_router.register(r'article', ArticleViewSet)


urlpatterns = [

] + article_router.urls
