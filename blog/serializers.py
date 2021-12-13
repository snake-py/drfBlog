from rest_framework import serializers
from .models import Article, ArticleTag, Comment



class GenericArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class GenericTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = '__all__'


class GenericCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class MixedArticleSerializer(serializers.ModelSerializer):
    tags = GenericTagSerializer(many=True, required=False)
    comment_set = GenericCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
