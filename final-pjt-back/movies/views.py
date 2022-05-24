from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from collections import Counter
from movies.serializers.movie import BoxSerializer, MovieListSerializer, MovieSerializer, ReviewSerializer
from movies.serializers.person import ActorSerializer, DirectorSerializer

from .models import Actor, Boxoffice, Director, Movie, Review

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# !!!!수정수정수정!!!!
@api_view(['GET'])
def recommendation_like(request):
    me = get_object_or_404(get_user_model(), username=request.user.username)
    like_list = me.like_movie.all()

    if like_list:
        genres_name = []
        for movie in like_list:
            movie_title = movie.title
            mv = get_object_or_404(Movie, title=movie_title)
            genres = mv.genres.all()

            for gr in genres:
                genres_name.append(gr.name)
        
        for x, y in Counter(genres_name).most_common(1):
            favorite = x
    pass


@api_view(['GET'])
def recommendation_watch(request):
    me = get_object_or_404(get_user_model(), username=request.user.username)
    watch_list = me.watch_movie.all()
    if watch_list:
        last = watch_list[-1]
        result = random.sample(list(Movie.objects.filter()))
    pass



@api_view(['GET'])    
def boxoffice_list(request):
    movies = get_list_or_404(Boxoffice, independent=0)
    serializer = BoxSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])    
def boxoffice_list_independent(request):
    movies = get_list_or_404(Boxoffice, independent=1)
    serializer = BoxSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    
    return Response(serializer.data)


@api_view(['GET'])
def person_detail(request, person_pk) :
    try :
        person = get_object_or_404(Actor, pk=person_pk)
        serializer = ActorSerializer(person)
    except :
        person = get_object_or_404(Director, pk=person_pk)
        serializer = DirectorSerializer(person)
    
    return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie,pk=movie_id)

    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_id, review_pk):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


    
@api_view(['POST'])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.like.filter(pk=user.pk).exists():
        review.like.remove(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        review.like.add(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.like.filter(pk=user.pk).exists():
        movie.like.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


def watch_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.watch.filter(pk=user.pk).exists():
        movie.watch.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.watch.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)  
    