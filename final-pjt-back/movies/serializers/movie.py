from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.serializers.person import ActorSerializer, DirectorSerializer
from ..models import Movie, Boxoffice, Review, Hashtag

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer) :
        class Meta:
            model = User
            fields = ('nickname',)
    
    user = UserSerializer(read_only=True)

    class MovieSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Movie
            fields = ('title',)

    movie = MovieSerializer(read_only=True)
    like = UserSerializer(read_only=True, many=True)

    class Meta :
        model = Review
        fields = '__all__'


# 수정 필요
class HashTagSerializer(serializers.ModelSerializer):
    class Meta :
        model = Hashtag
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    
    like_count = serializers.IntegerField()
    watch_count = serializers.IntegerField()
    
    movie_actor = ActorSerializer(read_only=True, many=True)
    movie_director = DirectorSerializer(read_only=True)
    hashtag = HashTagSerializer(read_only=True,many=True)
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta :
        model = Movie
        # __all__로 설정했을 때 like_count,watch_count가 들어갈지 모르겠음
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta :
        model = Movie
        fields = ('title','poster_path','vote_average',)


class BoxSerializer(serializers.ModelSerializer):
    class Meta :
        model = Boxoffice
        fields = '__all__'


