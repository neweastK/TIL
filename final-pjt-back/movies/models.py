from platform import release
from tkinter import CASCADE
from django.db import models
from django.conf import settings
# Create your models here.


class Boxoffice(models.Model):
    movieNm = models.CharField(max_length=100)
    rank = models.IntegerField()
    audiAcc = models.IntegerField()
    independent = models.BooleanField()

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    profile = models.TextField(null=True)


class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    profile = models.TextField(null=True)


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
    ott_service = models.CharField(max_length=100)
    backdrops = models.TextField()
    playlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='playlist_movie')
    watch = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_movie')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie')
    actors = models.ManyToManyField(Actor, related_name='act_movie')
    directors = models.ManyToManyField(Director,related_name='direct_movie')

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





