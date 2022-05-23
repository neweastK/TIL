from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Actor, Director, Movie

# 체크 완료
class ActorSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Movie
            fields = ('title','poster_path','release_date',)

    act_movie = MovieSerializer(many=True)

    class Meta :
        model = Actor
        fields = '__all__'

# 체크 완료
class DirectorSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Movie
            fields = ('title','poster_path','release_date',)

    direct_movie = MovieSerializer(many=True)

    class Meta :
        model = Director
        fields = '__all__'

