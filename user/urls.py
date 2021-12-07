from rest_framework import routers

from .views import AuthorViewSet

author_router = routers.SimpleRouter()
author_router.register(r'user/author', AuthorViewSet)


urlpatterns = [

] + author_router.urls
