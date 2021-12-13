# Base and Django imports
from django.db import models
from django.shortcuts import render

# Third party imports
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework import pagination, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import Article, ArticleTag, Comment
from .serializers import GenericTagSerializer, GenericArticleSerializer, MixedArticleSerializer, GenericCommentSerializer
from utils.Paginator import CustomPagination

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = CustomPagination
    queryset = Article.objects.all()
    serializer_class = GenericArticleSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MixedArticleSerializer
        
        else:
            return GenericArticleSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to add and edit comments.
    """
    queryset = Comment.objects.all()
    serializer_class = GenericCommentSerializer
    pagination_class = CustomPagination


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to add or edit tags.
    """
    queryset = ArticleTag.objects.all()
    serializer_class = GenericTagSerializer
    pagination_class = CustomPagination