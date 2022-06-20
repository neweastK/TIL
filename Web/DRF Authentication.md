# DRF Authentication



### Basic Token Based

1. 클라이언트가 POST로 username과 password 를 Server로 전달

2. 서버는 token 테이블에 해당 정보를 저장하고 token 값을 응답해줌

3. 클라이언트는 브라우저에 token 정보 저장

4. Request할 때 마다 header에 token을 담아서 전달

5. 전달 받은 token 값을 token 테이블에서 비교 후 올바른 접근이면 권한 부여



#### 라이브러리 사용

- 라이브러리 설치

```bash
$ pip install django-allauth
$ pip install dj-rest-auth
```

- settings.py 설정

  - third party에 해당

  ```python
  INSTALLED_APPS = [
      'rest_framework.authtoken', #token 기반 auth
      'dj_rest_auth', # signup 제외 모든 auth 관련 담당
  ]
  ```

  - REST_FRAMEWORK 설정 추가

  ```PYTHON
  REST_FRAMEWORK = {
      # 어떠한 방법으로 인증할 것인가?
      'DEFAULT_AUTHENTICATION_CLASSES':[
         # 토큰 기반 
         'rest_framework.authentication.TokenAuthentication',
      ],
      # 누구에게 권한을 줄 것인가?
      'DEFAULT_PERMISSION_CLASSES':[
          # 누구에게나
          'rest_framework.permissions.AllowAny'
      ]
  }
  ```

  

- urls.py 수정

  ```python
  # urls.py (master url)
  urlpatterns = [
      path('dj-rest-auth/', include('dj_rest_auth.urls')),
  ]
  ```

  - 이전에는 signup, login 함수를 직접 만들었음
  - urls는 원하는 이름으로 변경 가능



- 해당 라이브러리의 버그
  - headers에 토큰을 넘기지 않아도 결과값이 무조건 성공적으로 로그아웃 되었다고 메시지를 전달함
    - 하지만, 실제로 로그아웃되지는 않음
  - 따라서, 반드시 Headers에 올바른 token을 전달해야함



#### signup을 위한 라이브러리

- settings.py

  ```python
  INSTALLED_APPS = [
      ...
      'django.contrib.sites',
      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'dj_rest_auth.registration',
  ]
  
  SITE_ID = 1
  ```

- urls.py

  ```python
  urlpatterns = [
      path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
  ]
  ```

  - 이 역시도 원하는 주소로 변경 가능

- signup 이후에는 Token 발급까지 완료됨



### views Custom

#### profile 만들기

- accounts의 serializers 만들기

  ```python
  from rest_framework import serializers
  from django.contrib.auth import get_user_model
  
  class ProfileSerializer(serializers.ModelSerizlizer):
      
      class Meta :
          model = get_user_model()
          fields = '__all__'
  ```

  

- views.py

  ```python
  from django.shortcuts import get_object_or_404
  from django.contrib.auth import get_user_model
  
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .serializers import ProfileSerializer
  
  User = get_user_model()
  
  @api_view(['GET'])
  def profile(request, username):
  	user = get_object_or_404(User,username=username)
      serializer = ProfileSerializer(user)   
      return Response(serializer.data)
  ```



- 추가로 원하는 정보가 있다면 serializer 에서 custom한다.

  ```python
  from rest_framework import serializers
  from django.contrib.auth import get_user_model
  from article.models import Article
  
  class ProfileSerializer(serializers.ModelSerizlizer):
      
      class ArticleSerializer(serializers.ModelSerializer):
          
          class Meta:
              model = Article
              fields = ('pk', 'title')
  
      like_articles = ArticleSerializer(many=True)
      articles = ArticleSerializer(many=True)
      
      class Meta :
          model = get_user_model()
          fields = ('pk','username','like_articles','articles')
  ```

  

- 함수를 실행시키기 위해서는 로그인이 필요하다면?
  - DEFAULT_PERMISSION_CLASSES 값을 바꿔준다
    - 인증된 사용자에게만 모든 권한을 준다
    - `rest_framework.permissions.IsAuthenticated` 으로 교체
    - 비로그인자는 401 오류 발생





## CORS

- 라이브러리 설치

  ```bash
  $ pip install django-cors-headers
  ```

- settings.py에 추가

  - INSTALLED_APPS

    ```PYTHON
    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]
    ```

  - MIDDLEWARE 추가

    ```PYTHON
    MIDDLEWARE = [
        ...,
        'corsheaders.middleware.CorsMiddleware',
        ...,
    ]
    ```

    - 추가시 순서 중요!
      - `CommonMiddleware` 보다 위에 위치해야함

  - CORS_ALLOWED_ORIGINS 추가

    ```PYTHON
    CORS_ALLOWED_ORIGINS = [
        # Vue LocalHost
        'http://localhost:8000'
    ]
    ```

    ```python
    # 모두에게 교차출처 허용
    CORS_ALLOW_ALL_ORIGINS = True
    ```

    
