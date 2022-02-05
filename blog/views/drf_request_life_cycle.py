# Base and Django imports
from django.db import models
from django.shortcuts import render
# Third party imports
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework import pagination, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from ..models import Article, ArticleTag, Comment
from ..serializers import GenericTagSerializer, GenericArticleSerializer, MixedArticleSerializer, GenericCommentSerializer
from utils.Paginator import CustomPagination

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = CustomPagination
    queryset = Article.objects.all()
    serializer_class = GenericArticleSerializer
    def check_object_permissions(self, request, obj):
        return super().check_object_permissions(request, obj)

    def check_permissions(self, request):
        return super().check_permissions(request)

    def check_throttles(self, request):
        return super().check_throttles(request)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def determine_version(self, request, *args, **kwargs):
        return super().determine_version(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)
    
    def finalize_response(self, request, response, *args, **kwargs):
        return super().finalize_response(request, response, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_authenticate_header(self, request):
        return super().get_authenticate_header(request)

    def get_content_negotiator(self):
        return super().get_content_negotiator()
    
    def get_exception_handler(self):
        return super().get_exception_handler()
    
    def get_exception_handler_context(self):
        return super().get_exception_handler_context()
    
    def get_extra_action_url_map(self):
        return super().get_extra_action_url_map()

    # def get_extra_actions(self):
    #     return super().get_extra_actions()
    
    def get_format_suffix(self, **kwargs):
        return super().get_format_suffix(**kwargs)

    def get_object(self):
        return super().get_object()

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)
    
    def get_parser_context(self, http_request):
        return super().get_parser_context(http_request)
    
    def get_parsers(self):
        return super().get_parsers()
    
    def get_permissions(self):
        return super().get_permissions()
    
    def get_queryset(self):
        return super().get_queryset()
    
    def get_renderer_context(self):
        return super().get_renderer_context()
    
    def get_renderers(self):
        return super().get_renderers()
    
    # def get_serializer(self):
    #     return super().get_serializer()

    def get_serializer_context(self):
        return super().get_serializer_context()

    def get_serializer_class(self):
        return super().get_serializer_class()
    
    def get_success_headers(self, data):
        return super().get_success_headers(data)
    
    def get_throttles(self):
        return super().get_throttles()
    
    def get_view_name(self):
        return super().get_view_name()

    def get_view_description(self, html=False):
        return super().get_view_description(html=html)
    
    def handle_exception(self, exc):
        return super().handle_exception(exc)
    
    def head(self, request, *args, **kwargs):
        return super().head(request, *args, **kwargs)
    
    def http_method_not_allowed(self, request, *args, **kwargs):
        return super().http_method_not_allowed(request, *args, **kwargs)
    
    def initial(self, request, *args, **kwargs):
        return super().initial(request, *args, **kwargs)

    def initialize_request(self, request, *args, **kwargs):
        return super().initialize_request(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def options(self, request, *args, **kwargs):
        return super().options(request, *args, **kwargs)
    
    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def perform_authentication(self, request):
        return super().perform_authentication(request)
    
    def perform_content_negotiation(self, request, force=False):
        return super().perform_content_negotiation(request, force=force)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def permission_denied(self, request, message=None, code=None):
        return super().permission_denied(request, message=message, code=code)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def raise_uncaught_exception(self, exc):
        return super().raise_uncaught_exception(exc)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def setup(self, request, *args, **kwargs) -> None:
        return super().setup(request, *args, **kwargs)
    
    def throttled(self, request, wait):
        return super().throttled(request, wait)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

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