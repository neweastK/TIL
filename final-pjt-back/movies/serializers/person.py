from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Actor, Director, Movie


class ActorSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Movie
            fields = ('title','poster_path','release_date',)

    movie = MovieSerializer(many=True)

    class Meta :
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Movie
            fields = ('title','poster_path','release_date',)

    movie = MovieSerializer(many=True)

    class Meta :
        model = Director
        fields = '__all__'

