from platform import release
from django.db import models
from django.conf import settings
# Create your models here.


class Movie(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hashtag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hashtag')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='hashtag')
    tag = models.CharField(max_length=100)

