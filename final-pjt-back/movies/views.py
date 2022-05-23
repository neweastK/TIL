from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.serializers.movie import BoxSerializer, MovieListSerializer, MovieSerializer, ReviewSerializer
from movies.serializers.person import ActorSerializer, DirectorSerializer

from .models import Actor, Boxoffice, Director, Movie, Review

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])    
def boxoffice_list(request):
    movies = get_list_or_404(Boxoffice)
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
            reviews = Movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


    
@api_view(['POST'])
def like_review(request, movie_id, review_pk):
    article = get_object_or_404(Movie, pk=movie_id)
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
