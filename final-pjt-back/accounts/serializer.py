from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializers import ArticleSerializer
from movies.models import Movie
from movies.serializers.movie import HashTagSerializer

class ProfileSerializer(serializers.ModelSerializer) :

    class MovieSerializer(serializers.ModelSerializer):
        class Meta :
            model = Movie
            fields = ('poster_path','genres')

    like_movie = MovieSerializer(read_only=True, many=True)
    articles = ArticleSerializer(read_only=True, many=True)
    hashtag = HashTagSerializer(read_only=True, many=True)

    class Meta :
        model = get_user_model()
        fields = '__all__'
