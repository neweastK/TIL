from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.serializers.person import ActorSerializer, DirectorSerializer
from ..models import Actor, Director, Movie, Boxoffice, Review, Hashtag

User = get_user_model()

# 체크 완료(5/24)
class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer) :
        class Meta:
            model = User
            fields = ('nickname','username','id')
    
    user = UserSerializer(read_only=True)
    like = UserSerializer(read_only=True, many=True)

    class MovieSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Movie
            fields = '__all__'

    movie = MovieSerializer(read_only=True)

    class Meta :
        model = Review
        fields = '__all__'


# 수정 필요
class HashTagSerializer(serializers.ModelSerializer):
    class Meta :
        model = Hashtag
        fields = '__all__'

# 체크 완료
class MovieSerializer(serializers.ModelSerializer):
    
    class ActorSerializer(serializers.ModelSerializer):
        class Meta :
            model = Actor
            fields = ('name','profile',)
    
    actors = ActorSerializer(read_only=True, many=True)


    class DirectorSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Director
            fields = ('name','profile',)
        
    directors = DirectorSerializer(read_only=True, many=True)
    
    hashtag = HashTagSerializer(read_only=True,many=True)
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta :
        model = Movie
        fields = '__all__'

# 체크 완료
class MovieListSerializer(serializers.ModelSerializer):

    class Meta :
        model = Movie
        fields = '__all__'

# 체크 완료
class BoxSerializer(serializers.ModelSerializer):
    class Meta :
        model = Boxoffice
        fields = '__all__'


