## Web_Clone Coding

>사용 프로그램 : Django
>
>target site : Pinterest
>
>강의 : 작정하고 장고! 핀터레스트 만들기



### 1일차

> 1강~4강
>
> - 강의 개요 
> - Web Structure
> - Pycharm Setting
> - Django Pattern(MVT 패턴 소개)

#### pycharm setting

- 가상환경 체크 후 새로운 프로젝트 생성

- django 설치하기
  - `ctrl`+`c`+`tab` 누른 상태로 터미널 연결
  
  - 프로젝트 생성 때 main.py 생성해야 가상환경이 제대로 작동되는 것 같음.
  
  - 가상환경이 맞다면 pip install django 로 django 설치
  
  - 한 단계 상위 디렉토리로 이동 후 가상환경을 다시 새롭게 설정해주고 새로운 django 프로젝트를 생성 (django-admin startproject 프로젝트이름) 
  
  - 해당 프로젝트에서 다시 django를 설치한다 
  
    
  
- 의문점

  - 가상환경 활성화를 하지 않아도 강의상에서는 이미 활성화가 되어있음. 어떻게...?
  - 내 환경에서는 가상환경 활성화를 하지 않아도 가상환경 상태가 되어있음.
    but, 활성화 명령어를 치면 또 활성화가 되긴 함.
  - 왜 상위 디렉토리로 이동했는가?
  - 왜 굳이 다시 django를 두번  설치하는지?



### 2일차 

> 5강~8강
>
> - account app 생성
> - git 소개
> - git ignore & git setting
> - extends & include



#### account app

- python manage.py startapp accountapp 으로 account앱 생성
- settings.py에서 accountapp 등록
-  프로젝트 파일에서 accountapp urls로 연결시키는 path문 작성
  - include를 import 함
  - accountapp 폴더 내에 새로운 urls.py 파일 생성
  - 해당 파일 내에서 app_name 설정 및 urlpatterns 리스트 생성
  - urlpatterns에서 hello_world view 함수로 연결시키는 path문 작성
- view 에서 hello_world 함수 생성
  - httpresponse("내용") 으로 페이지 상에 내용 출력하도록 함





#### git setting

> [공식사이트](https://django-environ.readthedocs.io/en/latest/getting-started.html)

- settings.py 의 secret key를 보호하기 위함

- pip install django-environ 으로 environ 설치

- settings.py에 env 실행 코드 작성

  ```python
  import environ
  import os
  
  env = environ.Env(
      # set casting, default value
      DEBUG=(bool, False)
  )
  
  # reading .env file (BASE_DIR 밑에 작성)
  environ.Env.read_env(
      env_file=os.path.join(BASE_DIR, '.env')
  )
  ```

- 프로젝트 폴더에 .env 파일 생성 후 아래 내용 입력

  ```txt
  DEBUG=on
  SECRET_KEY=your-secret-key
  DATABASE_URL=psql://user:un-githubbedpassword@127.0.0.1:8458/database
  SQLITE_URL=sqlite:///my-local-sqlite.db
  CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213
  REDIS_URL=rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret
  ```

- SECRET_KEY 의 내용을 지우고 env('SECRET_KEY') 작성

- git ignore 파일에 .env 추가 작성

  ※ git ignore에 파일을 추가하지 못한 경우 

  	- 파일을 삭제하고 다시 git add 및 commit 
  	- 해당 파일을 다시 복구 시키고 gitignore에 해당 파일을 작성

  

#### extends, include

- base 템플릿 생성

  - 프로젝트 폴더에 templates 폴더 생성

  - 해당 폴더 내에 base.html 생성

  - settings.py에서 경로 지정
    - [os.path.join(BASE_DIR, 'templates')]
    
      

- 의문점 
  - templates DIRS를 설정해줄 때 os.path를 쓰는 이유는?
    - 답변 : 모든 운영체제에서 적용되기 때문. 운영체제마다 경로를 설정하는 방법이 다름
      			이때, os.path를 통해 경로를 지정해주면 모든 운영체제에서 동일하게 작동됨





### 3일차

> 9강~12강
>
> - extends, include 실습
> - header, footer 디자인
> - static, CSS 파일 넣기
> - CSS 핵심



#### extends, include

##### base.html

- head.html, header.html, footer.html을 만들어서 base.html에서 include로 불러옴
- extends를 통해 base.html을 hello_world.html에서 불러옴
- 전체적인 구조는 뷰포트를 상단, 중단, 하단으로 나누며, 중단을 제외한 각 단을 따로 html로 만들었음.
- 중단은 block 태그를 활용하여 매 페이지마다 내용을 바꿀 수 있도록 함.



##### hello_world.html

- 경로 : accountapp/templates/accountapp 
  - 추후 html이 어떤 app의 html인지 명시하기 위한 사전 작업
  - but, 사실은 django의 html 파일 탐색 순서 때문

- extends를 활용하여 base.html을 불러오고, block 태그를 작성하여 block 태그 내에서 페이지별 내용 작성
- views.py에서 해당 html 파일을 불러오기 위해서는 accountapp/hello_world.html 를 render 인자로 넣어줘야함



#### header, footer

- header, footer html 꾸며주기
- bootstrap 적용시키기
- 구글 font 사용하여 글꼴 설정하기(google font, style 지정)
- 의문점
  - 부트스트랩이 없을 때 my 로는 margin을 넣을 수는 없을까? 굳이 margin: a b 로 해야될까?



#### CSS, static

- static 설정하기
  - settings.py에 STATIC_ROOT 설정 - collectstatic 명령어를 통해 static 파일들이 모일 위치를 지정해주는 것
  - STATICFILES_DIRS 설정 : 원래 app 디렉토리 내에서 static 파일들을 탐색하지만 해당 루트 설정시 앱에 종속되어 있지 않은 static 파일들을 탐색할 수 있음
  - load 태그로 static 함수를 불러와서 static 태그를 사용할 수 있도록 해야함



- base.html의 head 부분에 css 불러오기
  - static 폴더와 폴더 내부에 css 파일을 BASE_DIR에 만들고 style을 지정한다.
  - 해당 스타일을 적용할 요소에 class로 삽입한다.
  - load 태그로 static 함수를 불러온다.
  - `<link rel="stylesheet" type="text/css" href="{% static 'base.css' %}">` 사용

- 문제 및 실수

  - STATICFILSES_DIRS 를  STATICFILSES_DIR로 잘못 표기하여서 css파일 적용이 되지 않았다.

    

#### CSS

##### DISPLAY 속성

1. Block
   - 부모 요소의 최대 너비를 가져가는 속성
   - 높이는 따로 설정하지 않으면 자동 배정
2. Inline
   - 요소의 높이 만큼의 일정 부분만 가져감
   - 한 줄에 여러개가 쌓일 수 있음
3. Inline-Block
   - 블록 속성임에도 불구하고 inline 요소처럼 오른쪽으로 요소들이 쌓일 수 있음
4. None
   - 아무 것도 없는 속성
   - vs Hidden
     - None은 아무것도 없음.(위치 차지x)
     - Hidden은 보이지만 않을뿐 존재는 하고 있음.(위치 차지)

##### SIZE(with 반응형 웹)

1. px

   - 부모 요소와 상관없이 고정값을 갖게 됨

2. em

   - 모든 부모 요소에 따라 자식 요소의 크기가 따라감
   - 부모 요소가 여러개일 경우 모든 부모 요소에 영향을 받기 때문에 관리가 어려움
     - 만약, 부모 요소1이 2배로 커지고, 부모 요소의 부모 요소 역시도 2배로 커졌을 경우, 최하위 자식 요소는 4배가 커지게 된다.

3. rem

   - root HTML의 크기를 따라감

   - 바로 위 부모 요소의 크기와 관계없이 오직 root HTML의 값만 따라가게 됨

     

4. %

   - 바로 위 부모 요소의 크기를 따라감



### 4일차

> 13강~16강
>
> - CSS display and size (display 및 size 실습)
> - Model
> - HTTP protocol
> - GET, POST 실습



#### CSS display and size

- style 지정 다른 방법
  - html 파일 내에 style 태그 사용
  - 의문점 : head가 아닌 body 부분에 style을 지정해도 되는건가?

- css 적용 순서
  - 태그 내의 style → html 파일 내의 style 태그 → css파일의 style

- span의 기본 속성은 inline



#### Model

- `python manage.py makemigrations` : models.py에 쓰는 내용을 DB와 연동시킬 파이썬 파일로 만들어주는 명령어
- `python manage.py migrate` : DB와 migrations로 만들어진 파일을 연동시키는 명령어
- Model은 Model class를 상속받아서 만들 수 있음
- 필드 생성시 null 옵션이 True 일 경우 해당 필드는 없어도 된다는 뜻
- migration 파일은 임의로 건들지 않는게 best!



#### HTTP 프로토콜

##### GET

- url의 `?` 뒤 추가적인 parameter를 넣어서 요청 혹은 응답을 보냄

- `?` 는 파라미터가 시작된다는 뜻이고, param1=value1 과 같이 매칭을 시켜서 요청 및 응답을 보냄

##### POST

- 데이터들을 BODY 안에 넣어서 보냄
- POST 사용을 위해서는 form 태그를 활용하여 데이터를 보내야함
- form 태그로 전송할 데이터와 방법, 전송 위치를 정하고 내부에 input(type=submit)을 활용하여 전송시킬 버튼을 만든다.
- django에서 POST로 데이터를 전송시킬 때는 무조건 csrf_token 태그를 넣어줘야함
  - django에서 제공하는 보안 기능 중 하나





### 5일차

> 17강~20강
>
> - DB에 데이터 저장하고 HTML에 출력하기
> - DB로부터 데이터 받기
> - Pycharm 디버깅
> - CRUD



#### DB에 전달받은 데이터 저장하기

- 요청받은 데이터 할당하기

  - request.POST.get('가져올 데이터 이름')
  - input에서 name에 할당한 값을 넣을 수 있음

- 할당한 데이터 DB에 저장하기

  1. 만들어놓은 Model의 Instance 객체 생성하기

     ```python
     객체 이름 = Model이름()
     ```

  2. 속성값으로 필드값 입력하기

     ```python
     객체 이름.속성 = 입력값
     ```

  3. DB에 저장하기

     ```Python
     객체 이름.save()
     ```

     - 따로 변수에 할당할 필요없이 자동으로 지정해놓은 객체 이름에 저장됨





#### DB로부터 데이터 가져오기

- reverse
  - path를 찾아 해당 path로 접근하기 위해 접근해야 하는 주소 값을 되돌려주는 함수
  - template 내에서의 url 태그와 같은 역할
- HttpResponseRedirect 
  - render가 아닌 기재한 url로 다시 요청을 보내는 함수
  - redirect와 차이점
    - redirect의 인자는 view,url 등 다양한 것들이 올 수 있고 결과적으로 HttpResponseRedirect 객체를 반환함
    - redirect가 더 유연하고, 짧아서 많이 쓰임



#### Pycharm에서 runserver할 때마다 디버깅하기

1. Run - Edit Configuration - template에서 Python 지정 - Script 지정

2. Script path 및 명령어 지정
   - Project - venv - Script
   - 명령어 : runserver 
3. apply



#### CRUD

- Djanog는 CRUD 각각에 대해 최적화되어 있는 view를 제공
- Function Based View : 함수 기반의 view
- Class Based View : 클래스 기반의 view
  - 몇가지 주요 파라미터만 정해주면 나머지는 django 내부에서 다 처리됨
  - 생산성과 가독성이 늘어나고, 복잡도와 사용시간은 낮아지게 할 수 있는 django의 큰 장점





### 6일차

> 21강~24강
>
> - signup with Createview
> - login/logout view
> - Form Design
> - mypage with DetailView



#### signup with Createview

- CreateView를 상속받는 class 생성

  - CreateView의 import 위치

    ```python
    from django.views.generic import CreateView
    ```

- 생성한 클래스의 주요 파라미터들 설정

  1. model : 어떤 모델을 사용할 것인지?
  2. form_class : 어떤 form을 사용할 것인지?
  3. success_url : 해당 클래스를 성공적으로 수행했을 경우 어느 경로로 다시 재연결할 것인가?
     - reverse_lazy : reverse는 클래스에서 사용할 수가 없기 때문에 클래스형 view에서는 reverse_lazy 사용
  4. template_name : 어떤 template 파일을 사용하여 볼지?

- urls.py에 생성한 클래스뷰 추가하기

  - 함수형 view는 이름을 그대로 추가해도 가능했지만 클래스형 view의 경우 `이름.as_view()` 형식으로 사용해줘야함.

    ```python
    path('create/', AccountCreateView.as_view(), name='create')
    ```

- create.html 생성하기

  - {{ form }} 은 python의 form에서 자동으로 제공해주는 form 형식



#### login & logout view

- loginview와 logoutview를 import
-  loginview는 특이하게 tmeplatename을 지정해줘야함.(인자값으로)



- login view와 logout view의 redirect 경로
  - next의 value를 우선적으로 탐색
  - settings.py 내에 저장된 LOGIN(LOGOUT)_REDIRECT_URL 탐색
  - 마지막 최종적으로는 DEFAULT 값으로 이동



- 되돌아갈 경로 직접 지정

  1. a 태그 href 속성에 직접 next 값 지정
  2. url 태그 뒤에 이어서 `?next={{ 다음으로 이동할 url }} ` 작성
  3. 즉, 어느 위치에서든 login을 누를 경우 login 이후 원래 있던 위치로 되돌아갈 수 있게 됨

  하지만, 위 경우에도 url에 직접 입력해서 login으로 이동할 경우 되돌아갈 경로가 없어 오류가 나게됨.

  이를 해결하기 위해 settings.py에서 LOGIN_REDIRECT_URL 직접 지정

  ```PYTHON
  LOGIN_REDIRECT_URL = reverse_lazy('accounts:hello_world')
  ```

- 의문점

  - LoginView를 urls.py에서만 썼는데 어떻게 작동이 되는건가?



#### form design

- django bootstrap 적용하기

  - pip install django-bootstrap-v5
  - settings.py - INSATLLED_APP 에 등록

- {% bootstrap_form form %} : 부트스트랩이 적용된 form

- 각종 bootstrap 속성도 사용할 수 있음

  ex) rounded-pill, col 과 같은 grid 시스템 등

- font 파일 적용시키기

  - \<head> 부분에 \<style> 태그를 활용하여 설정 가능

  ```python
  # fonts/는 static 내부의 디렉토리를 의미
  @font-face {
      font-family: '폰트이름';
      src: local('폰트이름'),
      url("{% static 'fonts/폰트파일명.확장자' %}") format('opentype');	
  }
  ```

  - 프로젝트 내 어디서든 해당 글꼴을 사용할 수 있게됨
  - style = "font-family: '원하는글꼴'" 과 같은 방식으로 스타일 지정 가능



####  mypage with DetailView

- DetailView를 상속받는 detail을 나타낼 클래스형 뷰 생성
  - DetailView는 `from django.views.generic import DetailView` 로 import

- 의문점 : context로 받지 않는데 {{ }} 안에 들어가는 요소들은 어디로부터 온걸까? 특히 user는 어디서부터 얻어온 정보인걸까. form 과 같이 user를 기본으로 제공해주는 것인가?
- 의문점 2: context_object_name 의 역할은 무엇일까?



### 7일차

> 25강~28강
>
> - signup with Createview
> - withdrawal with DeleteView
> - Authentication system
> - Decorator



####  change Password with UpdateView

- create와 매우 비슷한 맥락
- updateview를 상속받는 클래스형 뷰 생성
- target_user와 user를 이용하여 본인 계정에서만 본인 정보를 수정할 수 있도록 하기

```django
{% if target_user == user %}
<a href="{% url 'accountapp:update' pk=user.pk">
    <p>
        Change Info
    </p>
</a>
{% endif %}
```



- id 변경을 막기위해 해당 부분 비활성화 시키기

  - 사용하는 form을 커스터마이징하여 비활성화 

  ```python
  #forms.py
  from django.contrib.auth.forms import UserCreationForm
  
  class AccountUpdateForm(UserCreationForm) :
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          
          self.fields['usernmae'].disabled=True
  ```

  - AccountUpdateForm 클래스를 초기화 시킬 때 username 부분을 disabled 하겠다는 의미

    즉, UserCreationForm 클래스를 부분 수정하여 새로 클래스를 만든 것



#### withdrawal with DeleteView

- DeleteView를 상속받는 클래스형 뷰 생성
- 나머지는 다른 과정과 동일





#### Authentication system

- class view 아래에 get,post 메서드를 아래와 같이 작성

```python
def get(self, *args, **kwargs):
    if self.request.user.is_authenticated and self.get_object() == self.request.user :
        return super().get(*args, **kwargs)
    else :
        return HttpResponseForbidden()
    
def post(self, *args, **kwargs):
    if self.request.user.is_authenticated and self.get_object() == self.request.user :
        return super().post(*args, **kwargs)
    else :
        return HttpResponseForbidden()
```

- user가 로그인 되어있는지와 현재 요청하는 유저와 해당 view의 유저가 같은 유저인지 확인하는 과정이 들어있음



#### Decorator

- @login_required

  - `from django.contrib.auth.decorators import login_required`에서 impot 해올 수 있음

- @method_decorator

  - 일반 함수에서 사용하는 decorator를 class의 메서드에서도 사용할 수 있게 해주는 decorator
  - 두개의 인자를 가짐 
    1. 적용할 데코레이터 ex) login_required
    2. 적용 받을 메서드 ex) get, post
  - `from django.utils.decorators import method_decorator` 로 import

- Customizing Decorator

  - app 디렉토리에 decorators.py 파일 생성

  - 원하는 decorator를 생성하고 적용할 수 있음

    ```python
    from django.contrib.auth.models import User
    from django.http import HttpResponseForbidden
    
    def account_ownership_required(func):
        def decorated(request, *args, **kwargs):
            user = User.objects.get(pk=kwargs['pk'])
            if not user == request.user:
                return HttpResponseForbidden()
           	return func(request, *args, **kwargs)
       	return decorated
    ```

  - 적용을 위해서는 당연히 import 가 필요함

    `from accountapp.decorators import account_ownership_required`

  - 배열 안에 decorator를 넣어주고 class에 적용할 때 method_decorator 안에 해당 배열의 이름을 넣으면 모든 decorator를 한번에 적용 시킬 수 있음

    ```python
    has_ownership = [acount_ownership_required, login_required]
    
    @method_decorator(has_ownership,'get')
    @method_decorator(has_ownership,'post')
    ```

    



### 8일차

> 29강~32강
>
> - Superuser, media
> - Profileapp with ModelForm



#### Superuser

- `python manage.py createsuperuser`
- 관리자 계정 생성 명령어



#### Media

- 이미지를 다루기 위해서는 따로 설정 필요
  - settings.py - MEDIA_URL, MEDIA_ROOT 설정
  - MEDIA_URL : 주소창에 MEDIA_URL 이하의 경로로 접근을 해야 해당 미디어 파일에 접근이 가능함
  - MEDIA_ROOT : 미디어 파일을 어디에 저장할 것인지 정해놓는 경로
- `pip install pillow` 를 통해 pillow를 설치해줘야 미디어 파일 활용 가능



#### Profileapp 

- ID를 보여주지 않고 닉네임, 메시지, 이미지를 보여주는 프로필을 만드는 과정
- Profile 모델 만들기
  - OneToOneField() 
    - django에서 제공해주는 1대1 연결 필드
    - 어떤 객체와 연결할지, on_delete 옵션을 인자로 받음
      - on_delete : 연결되어 있는 객체가 삭제될 때, 그와 연결된 현재 클래스는 어떻게 처리할 것인지에 대한 옵션
      - 즉, User가 탈퇴하면 그 프로필은 어떻게 할 것인지
  - ImageField():
    - upload_to : 이미지를 받아서 서버 내부에 저장하는데 어디에 저장할지 경로를 정해줌
      - settings.py의 MEDIA_ROOT 이후의 주소를 설정
    - null : True일 경우 없어도 된다는 뜻
  - CharField()의 unique 옵션 : True일 경우 다른 사람과 겹칠 수 없음 (유일해야함)



- ModelForm 

  - 기존의 Model을 Form으로 바꿔주는 것
  - ModelForm을 상속 받는 클래스를 정의해주고 Meta 클래스를 생성
    - Meta 클래스에서는 어떤 model을 기반으로 할지, 어떤 field들을 사용할지 설정




<hr>

##### 문제 발견 및 해결

- django 함수의 자동 import 문제가 해결이 안됨.
- interpreter의 문제였음. why? 인터프리터가 가상환경으로 설정되어있지 않아서 django를 인식을 못했던 것. 
- 처음에 project 생성할 때 가상환경을 만들어줬어야하는데 그러지 못해서 발생한 문제
- 가상환경을 설정해줄 때는 venv/Scripts/python.exe 를 인터프리터로 설정해주면 됨

- 인터프리터란?
  - 우리가 작성한 코드를 실시간으로 읽고 변환하여 컴퓨터에게 전달해주는 번역 프로그램

<hr>

#### Profileapp View

- CreateView 만들기
  - CreateView를 상속받는 ProfileCreateView 생성
- 프로필이 없으면 Create Profile a 태그 만들기
- 이미지 받을 때의 form
  - enctype을 지정해주어야함.
  - `enctype="multipart/form-data"`

- form_valid

  - 기존의 함수를 커스터마이징 하는 함수

    ```python
    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
    ```

    - user의 정보는 form으로부터 받아오지 않았음(보안 문제)
    - 따라서, user의 정보를 profile form에 새로 저장해야함. form_valid를 통해 form 데이터를 재정의하여 user정보만 추가해줌.

    

#### update view

- edit 버튼 만들어주기

- img url을 가져오기 위한 setting

  - url_patterns 의 리스트 뒤에 리스트 추가

    ```python
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

- 데코레이터 수정 및 설정



### 9일차

> 33강~36강
>
> - get_success_url & code_refactoring
> - articleapp
> - ㅇ



####  get_success_url

- success_url 은 pk와 같은 variable routing 적용이 불가함.

- 따라서 get_success_url 을 활용해서 해당 메서드를 따로 수정해줘야함.

  ```python
  # success_url은 삭제
  def get_success_url(self):
      return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
  ```

  - kwargs를 활용하여 어떤 값을 주소와 함께 넘길지 지정

- 의문점 : 왜 pk가 user 객체에 있지...?

  의문점2 : 왜 method_decorator 설정할 때 post는 되고 POST는 안되는거야?



#### Articleapp with Magic Grid

- TemplateView 
  - 템플릿만 지정해주면 나머지를 모두 처리해주는 view
- magic grid 만들기(주소 : articles/list)
  - magic grid github - dist - [magic-grid.cjs.js](https://github.com/e-oj/Magic-Grid/blob/master/dist/magic-grid.cjs.js) 의 내용 복사
  - static/js/magicgrid.js 파일 생성 후 내용 붙여넣기
  - JSfiddle에 있는 내용 복사
    - javascript는 static에 css는 html style에 html은 html에 
  - 이미지는 Lorem Picsum 사이트 이용
- 문제점 : 주소 뒤에 슬래쉬를 안붙이면 주소 이동이 안된다.

