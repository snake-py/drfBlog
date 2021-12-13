# Base and Django imports
from django.shortcuts import render

# Third party imports
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .serializers import UpdateUserSerializer, GenericAuthorUserSerializer, GenericReaderUserSerializer, UpdateAuthorSerializer
from .models import Reader, Author, User
from utils.Paginator import CustomPagination



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = CustomPagination
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = CustomPagination
    queryset = Author.objects.all()
    serializer_class = GenericAuthorUserSerializer

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return UpdateAuthorSerializer
        else:
            return GenericAuthorUserSerializer
    # def put(self, request, *args, **kwargs):
    #     self.serializer_class = UpdateAuthorSerializer
    #     return self.update(request, *args, **kwargs)


class ReaderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = CustomPagination
    queryset = Reader.objects.all()
    serializer_class = GenericReaderUserSerializer