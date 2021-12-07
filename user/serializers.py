from rest_framework import serializers
from .models import Author, Reader, User


class GenericAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'alias')

class GenericReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ('id', 'alias')

class GenericUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(default=True)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    author = GenericAuthorSerializer(read_only=True)
    reader = GenericAuthorSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'last_login', 'password', 'author', 'reader')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=validated_data['is_active'],
        )
        user.set_password(validated_data['password'])
        user.save()
        author = Author.objects.create(user=user)
        author.save()
        return user
