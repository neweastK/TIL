from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from yaml import serialize

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def article_list_or_create(request):
    def article_list():
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
        ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return create_article()

@api_view(['GET', 'POST'])
def event_list_or_create(request):
    def event_list():
        articles = Article.objects.annotate(
                comment_count=Count('comments', distinct=True),
                ).filter(category="event").order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def create_event():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return event_list()
    elif request.method == 'POST':
        return create_event()

@api_view(['GET', 'POST'])
def news_list_or_create(request):
    def news_list():
        articles = Article.objects.annotate(
                comment_count=Count('comments', distinct=True),
                ).filter(category="news").order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def create_news():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return news_list()
    elif request.method == 'POST':
        return create_news()
    
@api_view(['GET', 'POST'])
def column_list_or_create(request):
    def column_list():
        articles = Article.objects.annotate(
                comment_count=Count('comments', distinct=True),
                ).filter(category="column").order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def create_column():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return column_list()
    elif request.method == 'POST':
        return create_column()

@api_view(['GET', 'POST'])
def board_list_or_create(request):
    def board_list():
        articles = Article.objects.annotate(
                comment_count=Count('comments', distinct=True),
                ).filter(category="board").order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def create_board():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return board_list()
    elif request.method == 'POST':
        return create_board()



@api_view(['GET', 'PUT', 'DELETE'])            
def article_detail_or_update_or_delete(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update_article():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_article():
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        if request.user == article.user:
            return update_article()
    elif request.method == 'DELETE':
        if request.user == article.user:
            return delete_article()



@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()
