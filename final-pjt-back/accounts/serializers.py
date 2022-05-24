from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializers import ArticleListSerializer
from movies.models import Movie
from movies.serializers.movie import HashTagSerializer
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers


class UserSerializer(RegisterSerializer):

    nickname = serializers.CharField(max_length=20)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        return data


class ProfileSerializer(serializers.ModelSerializer) :

    class MovieSerializer(serializers.ModelSerializer):
        class Meta :
            model = Movie
            fields = ('poster_path','genres')

    like_movie = MovieSerializer(read_only=True, many=True)
    articles = ArticleListSerializer(read_only=True, many=True)
    hashtag = HashTagSerializer(read_only=True, many=True)

    class Meta :
        model = get_user_model()
        fields = '__all__'
