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
    - 

- 의문점 
  - templates DIRS를 설정해줄 때 os.path를 쓰는 이유는?
    - 답변 : 모든 운영체제에서 적용되기 때문. 운영체제마다 경로를 설정하는 방법이 다름
      			이때, os.path를 통해 경로를 지정해주면 모든 운영체제에서 동일하게 작동됨





### 3일차

> 9강~12강
>
> - extends, include 실습
> - header, footer 디자인
> - ㅇ
> - ㅇ



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

