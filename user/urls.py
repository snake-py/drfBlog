from rest_framework import routers

from .views import AuthorViewSet, ReaderViewSet, UserViewSet

user_router = routers.SimpleRouter()
user_router.register(r'user/user', UserViewSet)
user_router.register(r'user/author', AuthorViewSet)
user_router.register(r'user/reader', ReaderViewSet)


urlpatterns = [

] + user_router.urls
