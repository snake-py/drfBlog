# Base and Django imports
from django.shortcuts import render

# Third party imports
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .serializers import GenericUserSerializer, GenericAuthorSerializer
from .models import User, Author
from utils.Paginator import CustomPagination


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = CustomPagination
    queryset = User.objects.all()
    serializer_class = GenericUserSerializer

