from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from django.db.models import Q
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
    personal = get_object_or_404(get_user_model(), username=request.user.username)
    like_list = personal.like_movie.all()
    if like_list:
        genres_name = []
        for movie in like_list:
            genres = movie.genres[1:-1].replace("'", "").split(', ')
            for genre in genres:
                genres_name.append(genre)
        print(genres_name)
        for name, cnt in Counter(genres_name).most_common(1):
            favorite = name
        result = random.sample(list(Movie.objects.filter(genres__contains=favorite)),5)
    else:
        result = Movie.objects.order_by('?')[:6]
    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)
# 장르들 다 더하기
# 장르 수 세서 가장 많은 것 
# 장르가 = 인 영화 랜덤 6?


@api_view(['GET'])
def recommendation_watch(request):
    me = get_object_or_404(get_user_model(), username=request.user.username)
    watch_list = me.watch_movie.all()
    if watch_list:
  
        last = watch_list[len(watch_list)-1]
        actor = last.actors.all()[:3]
        director = last.directors.all()[0]
        movies = Movie.objects.filter(Q(actors__id__contains=actor[2].id) | Q(actors__id__contains=actor[1].id) | Q(actors__id__contains=actor[0].id) | Q(directors__id__contains=director.id))
        result = list(set(movies))
    else:
        result = Movie.objects.order_by('?')[:6]

    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recommendation_netflix(request):
    movies = Movie.objects.all()
    netflix = []                                 
    for movie in movies:
        if movie.ott_service:
            otts = movie.ott_service
            if "넷플릭스" in otts:
                netflix.append(movie)
    result = random.sample(netflix, 6)
    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recommendation_watcha(request):
    movies = Movie.objects.all()
    watcha = []
    for movie in movies:
        if movie.ott_service:
            otts = movie.ott_service
            if "왓챠" in otts:
                watcha.append(movie)
    result = random.sample(watcha, 6)
    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recommendation_wavve(request):
    movies = Movie.objects.all()
    wavve = []
    for movie in movies:
        if movie.ott_service:
            otts = movie.ott_service
            if "웨이브" in otts:
                wavve.append(movie)
    result = random.sample(wavve, 6)
    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)

# 디즈니 데이터 만들고 다시 수종!!!
@api_view(['GET'])
def recommendation_disney(request):
    movies = Movie.objects.all()
    disney = []
    for movie in movies:
        if movie.ott_service:
            otts = movie.ott_service
            if "디즈니" in otts:
                disney.append(movie)
    if disney:
        result = random.sample(disney, 6)
    else:
        result = Movie.objects.order_by('?')[:6]
    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)



@api_view(['GET'])    
def boxoffice_list(request):
    movies = Boxoffice.objects.filter(independent=0).order_by('rank')
    serializer = BoxSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])    
def boxoffice_list_independent(request):
    movies = Boxoffice.objects.filter(independent=1).order_by('rank')
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
def like_review(request, movie_id, review_pk):
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

@api_view(['POST'])
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

@api_view(['POST'])
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

@api_view(['GET'])
def search(request):
    pass

@api_view(['GET'])
def sinye_movies(request):
    pass