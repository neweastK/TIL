from django.db import models
from django.conf import settings
# Create your models here.


class Boxoffice(models.Model):
    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    audiAcc = models.IntegerField()
    independent = models.BooleanField()


class Movie(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    adult = models.BooleanField(default=False)
    independent = models.BooleanField()
    release_date = models.DateField()
    overview = models.TextField()
    poster_path = models.TextField()
    genres = models.CharField(max_length=30)
    vote_average = models.FloatField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie')
    watch = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_movie')
    ott = models.CharField(max_length=100)
    backdrops = models.TextField()
    playlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='playlist_movie')
    

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review')
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hashtag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hashtag')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='hashtag')
    tag = models.CharField(max_length=100)


class Actor(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birth = models.DateField()
    profile_path = models.TextField()
    movie = models.ManyToManyField(Movie, related_name='movie_actor')


class Director(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birth = models.DateField()
    profile_path = models.TextField()
    movie = models.ManyToManyField(Movie, related_name='movie_director')  



