from rest_framework import serializers
from .models import Author, Reader, User

from django.db import IntegrityError


class GenericUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # is_active = serializers.BooleanField(default=True)
    # date_joined = serializers.DateTimeField(read_only=True)
    # last_login = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'last_login', 'password')

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
        return user
  
class GenericAuthorUserSerializer(serializers.ModelSerializer):
    user = GenericUserSerializer()

    class Meta:
        model = Author
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        author = Author.objects.create(user=user, **validated_data)
        author.save()
        return author
    



class GenericReaderUserSerializer(serializers.ModelSerializer):
    user = GenericUserSerializer()

    class Meta:
        model = Reader
        fields = '__all__'
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        reader = Reader.objects.create(user=user, **validated_data)
        reader.save()
        return reader
            



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active' )
        extra_kwargs = {
            'username': {
                'validators': []
            },
            'email': {
                'validators': []
            },
        }
        
class UpdateAuthorSerializer(serializers.ModelSerializer):
    user = UpdateUserSerializer()

    class Meta:
        model = Author
        fields = '__all__'

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        try:
            self.fields['user'].update(instance.user, user_data)
            return super().update(instance, validated_data)
        except IntegrityError:
            return Author.objects.get(id=instance.id)
            
            
