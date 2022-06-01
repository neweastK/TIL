from django.forms import CharField
from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializers import ArticleListSerializer
from movies.models import Movie
from movies.serializers.movie import HashTagSerializer
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from multiselectfield import MultiSelectField

from rest_framework import serializers



# 새로 생성(5/24)
class UserSerializer(RegisterSerializer):

    nickname = serializers.CharField(max_length=20)
    # profile_image = serializers.ImageField(use_url=True)
    using_ott = serializers.ListField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        # data['profile_image'] = self.validated_data.get('profile_image', '')
        data['using_ott'] = self.validated_data.get('using_ott', [])
        return data

# 체크 완료(5/24)
class ProfileSerializer(serializers.ModelSerializer) :

    class MovieSerializer(serializers.ModelSerializer):
        class Meta :
            model = Movie
            fields = '__all__'

    watch_movie = MovieSerializer(read_only=True, many=True)
    like_movie = MovieSerializer(read_only=True, many=True)
    articles = ArticleListSerializer(read_only=True, many=True)
    hashtag = HashTagSerializer(read_only=True, many=True)

    class Meta :
        model = get_user_model()
        fields = ('pk','nickname', 'watch_movie', 'like_movie', 'articles', 'hashtag', 'point', 'using_ott', 'profile_image',)
