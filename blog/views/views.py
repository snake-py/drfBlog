# Base and Django imports
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


# class TagViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to add or edit tags.
#     """
#     queryset = ArticleTag.objects.all()
#     serializer_class = GenericTagSerializer
#     pagination_class = CustomPagination


class TagView(APIView):
    """
    API endpoint that allows users to add or edit tags.
    """
    def get(self, request):
        tags = ArticleTag.objects.all()
        serializer = GenericTagSerializer(tags, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = GenericTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        tag = ArticleTag.objects.get(pk=pk)
        serializer = GenericTagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tag = ArticleTag.objects.get(pk=pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        