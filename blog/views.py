# Base and Django imports
from django.db import models
from django.shortcuts import render

# Third party imports
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework import pagination, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import Article, Comment
from .serializers import GenericArticleSerializer
from utils.Paginator import CustomPagination

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = CustomPagination
    queryset = Article.objects.all()
    serializer_class = GenericArticleSerializer
