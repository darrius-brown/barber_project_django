from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Barber, Comment

UserModel = User

class UserSerializer(serializers.ModelSerializer):

  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

  def create(self, validated_data):

    user = UserModel.objects.create_user(
      username=validated_data['username'],
      password=validated_data['password']
    )

    return user

  class Meta:
    model = UserModel
    fields = ('id', 'username', "password")

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token

class BarberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barber
        fields = ('name', 'state', 'city', 'ratings', 'price', 'description', 'images' )
    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
    )
    class Meta:
        model = Comment
        fields = ('author', 'content')