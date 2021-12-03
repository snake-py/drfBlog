# Base and Django imports
from django.shortcuts import render

# Third party imports
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import Article, Comment
from .serializers import GenericArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = GenericArticleSerializer
