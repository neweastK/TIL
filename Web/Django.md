# Django

> **High-level Python ①<u>Web Framework</u>** that encourages rapid development and clean, pragmatic design

[toc]

## Web Framework

### Web(World Wide Web)

> 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간 (=인터넷공간)



#### 종류 

##### ① Static Web page(정적 웹 페이지) (=flat page)

- 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
- 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
- 모든 상황에서 모든 사용자에게 동일한 정보를 표시
- 일반적으로 HTML, CSS, Javascript로 작성



##### ② Dynamic Web Page(동적 웹 페이지)

- 웹 페이지에 대한 요청을 받은 경우 서버는 **추가적인 처리 과정 이후** 클라이언트에게 응답을 보냄
- 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 상황마다 그리고 사용자마다 다름
- 서버 쪽을 구성하는 프로그래밍 언어를 서버사이드 프로그래밍 언어라고 하며 대표적으로 Python, Java, C++ 등이 있음
- 이 언어들은 파일을 처리하고 데이터베이스와의 상호작용을 통해 수정,저장,조회,삭제 등의 작업을 수행함



### Framework

> 프로그래밍에서 특정 운영 체제를 위한 __응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모음__

- 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
- 즉, 개발을 위한 기본적인 환경을 제공하는 것(=개발을 0부터 시작하지 않도록 여러 기능을 제공해주는 것)
- application framework라고도 하며 bootstrap도 일종의 framework



### Web Framework

- 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것을 주 목적으로하며 데이터베이스 연동, 템플릿 형태의 표준, 세션관리, 코드 재사용 등의 기능을 포함
- 동적인 웹 페이지나, 웹 애플리케이션, 웹 서비스의 개발 보조용으로 만들어지는 application framework의 일종



### Web의 작동 과정

![web](../assets/web/web_request_answer.png)

##### 클라이언트

- 네트워크라는 시스템을 통해서 서버라고 하는 컴퓨터 시스템 상의 원격 서비스에 접속할 수 있는 응용 프로그램 혹은 디바이스
- 서버에서 제공하는 정보, 자원을 얻기 위해 무언가 **요청**을 할 수 있는 시스템
- 데스크탑, 스마트폰, 웹 브라우저 등

##### 서버

- 클라이언트에게 네트워크 환경을 통해 정보나 서비스를 제공하는 컴퓨터 시스템 (=**응답**)
- django는 서버를 구축하는 프로그램 중 하나





## django

<hr>※  LTS

- Long Term Support (장기 지원 버전)
- 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
- 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
- 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함
- django의 경우 3.2.12 버전이 LTS이기 때문에 4.0이 아닌 3.2.12 버전 사용


<hr>

### Framework Architecture

<hr> ※ MVC Design Pattern (Model-View-Controller) 

- Framework가 어떤 식의 구조로 디자인 되어 있는가?에 대한 답
- 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
- UI로부터 프로그램 로직을 분리하여 시각적인 영역과 그 이면의 부분을 서로 영향 없이 개발할 수 있음
- __Django는 MTV Pattern 이라고 함__


<hr>

#### MTV Pattern

- Model

  - 응용프로그램의 **데이터 구조를 정의하고, 데이터베이스의 기록을 관리**

  - 데이터에 대한 추가, 수정, 삭제를 관장

- Template (View of MVC)

  - 파일의 **구조나 레이아웃**을 정의
  - 실제 내용을 보여주는데 사용(presentation)
  - 사용자에게 보여지는 부분을 관장
  - 주로 HTML 양식

- View(Controller of MVC)
  - **HTTP 요청을 수신하고 HTTP 응답을 반환**
  - 특정 데이터가 필요할 경우, Model과의 소통을 통해 필요한 데이터에 접근
  - template에게 응답의 서식 설정을 맡김
  - 함수의 역할

- Djang 전개 과정

![django](../assets/web/django_root.png)



### project와 application

#### project

- project는 application의 집합

- 프로젝트에는 여러 앱이 포함될 수 있음

  ※ 앱도 여러 프로젝트에 속해 있을 수 있음 (프로젝트가 큰 경우)

- 프로젝트 디렉토리 구조

  - \__init__.py
    - python에게 현재 파일이 위치한 폴더를 하나의 Python 패키지로 다루도록 지시(즉, import 해올 수 있도록 지시하는 파일)
    
  - asgi.py 
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움. 배포 작업시 사용 (Asynchronous Server Gateway Interface)
    
  - **settings.py** 
    - 애플리케이션의 모든 설정을 포함 (언어 및 시간 표시 기준도 설정 가능)
    
    - 추가 설정
    
      1. LANGUAGE_CODE
    
      - 모든 사용자에게 제공되는 번역을 결정
    
      - 이 설정이 적용 되려면 `USE_I18N`이 활성화되어 있어야 함
    
      - http://www.i18nguy.com/unicode/language-identifiers.html
    
        ```python
        # settings.py
        
        LANGUAGE_CODE = 'ko-kr'
        ```
    
      
    
      2. TIME_ZONE
    
      - 데이터베이스 연결의 시간대를 나타내는 문자열 지정
    
      - `USE_TZ`가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면 UTC 대신 새로 설정한 시간대의 인식 날짜&시간이 반환 됨
    
      - `USE_TZ`이 False인 상태로 이 값을 설정하는 것은 error
    
      - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    
        ```PYTHON
        # settings.py
        
        TIME_ZONE = 'Asia/Seoul'
        ```
    
      
    
      3. USE_I18N
    
      - Django의 번역 시스템을 활성화해야 하는지 여부를 지정
    
      
    
      4. USE_L10N
    
      - 데이터의 지역화 된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
      - True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시
    
      
    
      5. USE_TZ
    
      - datetimes 객체가 기본적으로 시간대를 인식하는지 여부를 지정
      - True일 경우 Django는 내부적으로 시간대 인식 날짜 / 시간을 사용
    
      
    
  - **urls.py** 
    
    - 사이트의 url과 적절한 views의 연결을 지정, HTTP 요청을 받아서 알맞은 view로 전달
    - urls 지정
      - urlpatterns 부분에 `path('주소', view 함수)` 사용
    
        - view 함수는 application에서 작성한 함수
        - "주소"로 요청이 오면 지정한 view 함수를 실행하겠다!
      - 다른 프로젝트에서 만든 함수를 사용하기 위해 `from`과 `import` 사용
    
        - 함수를 만들 때는 무조건 request 가 필수 argument로 사용됨
    
    ※ **Request object** 
    
    > https://docs.djangoproject.com/en/3.1/ref/request-response/#module-django.http
    
    - 요청 간의 모든 정보를 담고 있는 변수
    - 페이지가 요청되면 Django는 요청에 대한 메타 데이터를 포함하는 `HttpRequest` 객체를 만들고
    - 그런 다음 Django는 적절한 view 함수를 로드하고 `HttpRequest`를 뷰 함수의 첫 번째 인자로 전달. 
    - 그리고 각 view는 `HttpResponse` 개체를 반환한다.
    
    
    
  - wsgi.py 
    - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움. 배포 작업시 사용 (Web Server Gateway Interface)
    
  - manage.py 
    - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티 (각종 명령을 수행시킴)
    - 프로젝트 폴더와 같은 위치에 생성 (프로젝트 폴더 내에 생성되지 않음)



#### application

- 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할 담당
- 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함
- 앱을 만들고나서 반드시 프로젝트에 등록을 시켜야함 (**반드시 생성 후 등록할 것!**)
  - project - settings.py - INSTALLED_APPS - 앱 이름 추가
    - INSTALLED_APPS : Django installation에 활성화 된 모든 앱을 지정할 수 있는 문자열 목록
  - 앱등록시 권장 순서에 따라 기재할 것 : Locals apps → Third party apps → Django apps
- 애플리케이션 디렉토리 구조
  - admin.py 
    - 관리자용 페이지를 설정하는 곳
  - apps.py 
    - 앱의 정보가 작성된 곳
  - **models.py** 
    - 앱에서 사용하는 Model을 정의하는 곳
  - tests.py 
    - 프로젝트의 테스트 코드를 작성하는 곳
  - **views.py** 
    - view 함수들의 정의되는 곳
    - 함수를 정의하고 해당 함수는 template을 렌더링한다.(= 응답 서식을 불러온다)
    - 이 때, render는 자동으로 애플리케이션 폴더 내에서 templates 폴더를 찾고 해당 위치에 없으면 템플릿을 가져올 수 없다



### Django 기본 시작과정

1. 가상환경 생성 및 활성화

   ```bash
   python -m venv venv
   ```

   ```bash
   source venv/Scripts/activate #터미널을 실행할 때마다 활성화시켜야함
   ```

2. django 설치

   ```bash
   pip install django==3.2.12
   ```

3. 프로젝트 생성

   ```bash
   django-admin startproject {프로젝트이름} . 
   #마지막 .을 통해 현재 디렉토리에 프로젝트를 생성하도록 명령
   ```


4. 서버 켜서 작동 확인하기(로켓 이미지 확인 가능)

   ```bash
   python manage.py runserver
   ```

5. 새로운 애플리케이션 생성

   ```bash
   python manage.py startapp {app이름}
   ```

6. 앱 등록

   - settings의 INSTALLED_APPS에 추가

7. urls.py에서 `from 어플리케이션 이름 import views ` 실행 

8. urls.py의 urlpatterns에 path로 주소명이랑 함수 설정 (= urls.py를 통해 url과 view를 매핑)

   - `path("주소명/", views.함수)`

9. views.py에서 HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 만들기

10. 어플리케이션 내에 새로운 폴더(templates) 만들고 해당 폴더 내에 `[템플릿이름].html` 에서 파일의 레이아웃 정의



※ **코드 작성 순서**

- URL → View → Template
  - django의 작동 흐름에 따라서 코드를 작성할 것




### Django Template

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- Django template language : Django Template 위에서 쓸 수 있는 별도의 문법
- Template 파일 탐색 기본 경로는 app 폴더 안의 templates 폴더로 이미 지정되어 있음
  - template 파일 탐색 기본 경로 : **해당app/templates/**




#### Django Template Language(DTL)

- Django template 에서 사용하는 built-in template system
- 조건, 반복, 변수, 치환, 필터 등의 기능을 제공
- Python처럼 일부 프로그래밍 구조(if,for 등)를 사용할 수 있지만, Python코드로 실행되는 것은 아님
  즉,  Django template language(DTL)의 모양일 뿐 파이썬 기능과는 상관 없음
- Python이 HTML에 포함 된 것이 아니며 프로그래밍적 로직이 아니라 단순히 프레젠테이션을 표현하기 위한것



##### DTL 문법 

1. Variable(변수)

```python
{{ variable }}
```

- render()를 사용하여 __views.py에서 정의한 변수__(주로 context안에 들어가있는 요소)를 template 파일에서 사용
  - context에 {key:value}와 같이 딕셔너리 형태로 넘겨줌
  - 여기서 정의한 key 이름이 template에서 사용 가능한 변수명이 됨.
  - 만약, key가 여러개라면 template.html에서 원하는 key 이름을 넣어주면 됨
  - 즉, view에서 작성한 딕셔너리의 key값을 template.html에서 `{{ }}` 안에 넣으면 value가 웹상에 출력
- 변수명은 영어, 숫자와 밑줄의 조합으로 구성 가능 but 밑줄로 시작할 수는 없음
- dot(.)를 사용하여 변수 속성에 접근할 수 있음 (딕셔너리의 경우 `변수.key` 를 통해 value값을 불러올 수 있음)
- views.py의 render()의 세번째 인자에 할당해줌 ex) render(request, 'greeting.html', context)
- value가 인덱싱이 가능할 경우 `key.숫자` 로 인덱싱 가능 

- 예시

  ```python
  # views.py
  def greeting(request):
      foods=["apple","banana","coconut",]
      info = {
          "name":"Alice"
      }
      context = {
          "foods":foods,
          "info":info,
      }
      return render(request, "greeting.html",context)
  ```

  ```django
  {# greeting.html #}
  <p>안녕하세요 저는 {{ info.name }} 입니다.</p>
  <p>제가 좋아하는 음식은 {{ foods }} 입니다.</p>
  <p>{{ foods.0 }}을 가장 좋아합니다.</p>
  ```

  

2. Filters

```django
{{ variable|filter }}
```

- 표시할 변수를 수정할 때 사용 ex) `{{ name|lower }}` → name 변수를 모두 소문자로 출력

- 여러 개의 필터끼리 chained가 가능(ex. variable|filter|filter)하며 일부 필터(ex:join)는 인자를 받기도 함

- [공식 문서](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#filter)에서 여러 filter 요소를 확인 가능

  

3. Tags

```django
{% tag %}
```

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요 ex) `{% if %}{% endif %}` / ` {% for  in  %}{% endfor %}`
- if나 for라는 이름은 같지만 파이썬이 구동되는 것은 아님!



4. Comment

- 한줄 주석

```django
{# 내용 #}
```

- 여러줄 주석

```django
{% comment %}
    내용1
    내용2
{% endcomment %}
```

- 단축키 Ctrl + /로 사용 가능



#### Template Inheritance (템플릿 상속)

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의함. 따라서, 기본 뼈대가 되는 템플릿을 만들 수 있음

- 부모 템플릿은 주로 base.html로 지정

- 부모 템플릿의 위치는 프로젝트 폴더와 같은 위치에 새로운 templates 폴더를 생성해서 해당 폴더로 지정

- 템플릿 추가 경로 설정

  - django는 기본적으로 template 파일을 찾을 때 application 폴더 안에 있는 templates 폴더부터 탐색함

  - settings.py 내에서 TEMPLATES 중 빈 리스트로 되어있는 DIRS에 새로운 템플릿 탐색 경로 기입 ex) 'DIRS' : [BASE_DIR / 'templates']

  - BASE_DIR : 현재의 장고 프로젝트 폴더가 위치해있는 폴더 (manage.py가 존재하는 폴더)

    먼저는 등록된 앱들의 templates 폴더에서 선언한 템플릿 파일을 찾고 없다면 base_dir에 지정한 위치에서 찾는다



##### 템플릿 관련 태그

1. extends

```python
{% extends '부모 템플릿 이름' %}
```

- 자식템플릿이 부모 템플릿을 확장(상속)한다는 것을 알림
- **반드시 템플릿 최상단**에 작성 되어야 함



2. block

```python
{% block '블록 이름' %} {% endblock '블록 이름' %}
```

- 하위 템플릿에서 재지정(override)할 수 있는 블록을 정의
- 즉, 하위 템플릿이 채울 수 있는 공간
- 부모 템플릿에도 작성하고 자식 템플릿에도 작성함
  - 블록 이름을 통해서 매핑됨

- block은 여러개가 될 수 있다



3. include tag

```python
{% include 'include할 템플릿 이름' %}
```

- 템플릿을 로드하고 현재 페이지로 렌더링
- 템플릿 내에 다른 템플릿을 포함하는 방법
- 파일명 앞에 주로 언더바(_)를 사용함으로써 다른 템플릿들과 구분함(기능은 따로 없음)
  - include되도록 만든 템플릿이라는 것을 표시하는 방법



#### Django template 설계 철학

1. 표현과 로직을 분리
   1. 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이다.
   2. 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야한다.
   3. 즉, 템플릿은 잘 보여주는 것만 집중, 나머지 연산 및 기능은 view에서 설정
2. 중복을 배제
   1. 대다수의 사이트가 갖는 공통 디자인은 한곳에 저장하여 중복코드를 없앤다.
   2. 템플릿 상속을 활용한다.



## HTML form

### form 

> 웹에서 사용자 정보를 입력하는 여러 방식을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 HTML 태그

#### 속성

##### method 

> 입력된 데이터의 전달 방식을 지정

- GET : 저장은 불가하고, 조회만 가능
- POST : 수정이 가능함
- 딕셔너리 형태로 전달하기 때문에 전달 받을 때는 get 함수를 사용해야함
  - `example = request.GET(or POST).get()`
  - (GET : method 중 하나, get : 딕셔너리 value값 반환)


##### action

> 입력된 데이터를 전달할 URL 지정



### input

> 사용자로부터 데이터를 입력 받기 위해 사용

- type 에 따라 동작 방식이 달라짐 (password, email 등)

##### name

> input 태그에서 사용할 수 있는 속성 중 하나

- 중복 가능, 양식을 제출했을 때 name으로 지정한 변수에 입력값을 넘겨서 가져올 수 있음

- 주요 용도는 get/post 방식으로 서버에 전달하는 파리미터(name은 key, value는 value)로 매핑하는 것

- get 방식에서는 url에서 `?key=value&key=value` 형식으로 데이터 전달

  ex) 구글에서 "네이버" 검색시 `search?q=네이버` 로 데이터를 전달함 
  		key 즉, name은 q이며 value는 사용자가 입력한 값인 "네이버"



### label

- 사용자 인터페이스 항목에 대한 설명을 나타냄
- label을 input 요소와 연결할 수 있음
  - input에 `id` 속성 부여
  - label에는 for 속성을 부여하고 속성값으로 매핑할 input의 id를 입력한다
- label을 통해 input에 어떤 데이터를 입력해야하는지 사용자가 더 쉽게 이해할 수 있고 input이 아닌 label을 클릭해도 input을 활성화시킬 수 있음
- input 외에 연결 가능한 요소 : button, select, textarea 등





## URLs

> 웹 애플리케이션은 클라이언트의 URL을 통한 요청에서부터 시작됨

### Variable Routing

>  URL 주소 일부를 변수로 사용하는 것

- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

- 변수 값에 따라 하나의 path()만으로 여러 페이지에 연결이 가능해짐

- 예시

  ```python
  # urls.py
  urlpatterns = [
      path('accounts/user/<int:user_pk>/', views.~~~)
  ]
  ```

  - user_pk 가 어떤 값이냐에 따라 주소가 달라짐
  - int, str 등 변수의 type을 지정해줄 수 있음 (미지정시 기본값은 str)

- **views.py 내에서 함수를 선언할 때 parameter를 넣어줘야함**

- 예시

  ```python
  # views.py
  def example(request, user_pk) :	#parameter에 user_pk 필수!!
      context = {
          'user_num'= user_pk,
      }
      return render(request, 'example.html', context)
  ```

  - 위의 경우 context에서 또 다시 변수로 지정해줬기 때문에 template에서도 변수로 사용 가능



### App URL Mapping

> 각 app에서 본인의 urls.py를 직접 작성하고 관리할 수 있게 하는 것

- 본래는 BASE_DIR의 urls.py 에서 모든 url과 view함수로의 연결을 수행함

- 하나의 urls.py로 관리할 경우 발생하는 문제

  1. app의 view 함수가 많아질 수록 사용하는 path() 또한 많아지게 되고 여기에 더해, app도 많아지면 하나의 urls.py에서 모든 것을 작성 및 관리하기가 어려움

  2. 여러 app의 views.py를 관리할 때 겹치는 함수 이름이 있을 경우 따로 이름을 지정해줘야함.

     ```python
     from pages import views as pages_views
     from articles import views as articles_views
     
     urlpatterns= [
         path('pages-index', pages_views.index),
         path('articles-index', articles_views.index),
     ]
     
     # 한개의 app만 있을 때는 as를 활용해 따로 이름을 지정해줄 필요가 없었음
     ```



- 이러한 문제를 해결하기 위해 각 app 폴더에 해당 app의 views 함수만을 갖고 있는 urls.py를 만듬
- `include()`를 활용하여 다른 URLconf(= app/urls.py)들을 참조할 수 있음

  - 함수 include를 만나게 되면, path의 첫 인자로 지정한 URL의 시점까지 일치하는 부분을 잘라내고, 남은 부분의 후속 처리를 위해 include의 인자로 지정한 URLconf로 이동 
  - `path("주소/", include("app이름.urls"))`
  - `from django.urls import include` 필요 (path 옆에 include 작성)
  - 프로젝트의 urls.py에서 사용함으로써 프로젝트 urls.py에서 url을 받으면 지정한 app의 urls로 보내도록 한다. 
- 각 앱의 urls.py에서 `from . import views` 를 통해 자신의 app 폴더 내에 있는 views를 import 한다

- 그 후 각각의 함수를 적용시킬 path를 작성한다.

- 프로젝트의 urls는 각 앱의 urls를 연결시킬 뿐 상세한 연결은 각 앱의 urls에서 이루어진다.

- 예시

  ```python
  # 프로젝트 urls.py
  path('pages/', include('pages.urls'))
  ```

  - 'pages' 주소로 요청이 오면 그 이후는 pages.urls 파일을 기준으로 한다.



### Naming URL Patterns

> urls에서 지정해준 url에 name을 정해주는 것

- path() 함수의 name 속성에서 해당 url의 이름을 지정해줌

- url을 전부 입력하지 않아도 되고 해당 이름을 기입하면 됨.

- 다른 곳에서 해당 url을 쓰고 싶은 경우 url 태그 내에 name으로 지정한 값을 할당하면 됨.

- 예시

  ```python
  path('index/', views.index, name='index')
  ```

  ``` html
  <a href="{% url 'index'%}"> 메인 페이지</a>
  
  <!-- url pattern을 사용하기 전 -->
  <a href="/index/"> 메인 페이지 </a>
  ```



<hr>

## Namespace

> 개체를 구분할 수 있는 범위를 나타내는 namespace

- 서로 다른 app 내에서 같은 이름을 가진 url이 있을 경우(주로 index) 이름공간을 구분해줘야함
- django의 경우 url이나 template을 찾을 때 INSTALLED_APPS에 등록된 앱 순서대로 탐색
  - 따라서 INSTALLED_APPS 에 app1, app2 순서로 등록되어있다면 app1 → app2 → BASE_DIR 순으로 urls나 template 파일을 탐색



#### URL Namespace

> 서로 다른 APP의 urls.py 내에서 같은 이름을 가진 url이 있을 경우 

- url의 경우 우리가 편하게 사용하기위해 urls.py에서 name을 등록해줬지만, 이름이 겹치는 경우가 발생할 수 있기 때문에 name 외 추가적인 정보가 필요함. 따라서, [어떤앱의 URL]인지를 알려줘야함.
- 각 앱의 urls.py에 app_name을 작성함으로써 분리를 시켜준다
- url을 선언할 때는 { % url 'app_name' : 'url_name' % } 으로 선언한다.



#### Template Namespace

> 서로 다른 APP의 templates 디렉토리 내에서 같은 이름을 가진 template이 있을 경우 

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, INSTALLED_APPS에 작성한 app 순서로 tamplate을 검색 후 렌더링

- 위 시스템을 강제로 변경할 수가 없기 때문에 물리적으로 경로에 폴더 하나를 끼워넣음으로써 namespace를 분리시켜줌

- 앱 폴더 내 템플릿 폴더 하위에 새로운 폴더 생성 (관행적으로 앱 이름과 같이 만듦)

- 해당 폴더 내에 모든 템플릿 파일 이동

- views.py에서 render의 인자, include(html이름) 등 템플릿을 불러오는 모든 곳에서 `'앱이름/html이름'` 으로 변경 

- 즉, 임의로 templates의 폴더 구조를 `app_name/templates/app_name` 형태로 변경해 임의로 이름 공간 생성 후 변경된 추가 경로 작성

  그럼 django는 app_name/templates 에서 'app_name/html_name' 인 파일을 찾아야되고 template 이름이 동명이라도 폴더명이 달라서 해결됨

  ```python
  # articles/views.py
  
  return render(request, 'articles/index.html')
  # 기존에는 'index.html'로 html 주소를 지정 및 렌더링
  ```



<hr>

## Static File

> 정적 파일 : 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일 (사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일 )

- 이미지, 자바스크립트, CSS 등이 있음
- 서비스 중에서도 추가되거나 변경되지 않고 고정되어 있음
- django에서는 이러한 파일들을 Static File 이라고 하며 staticfiles 앱을 통해 정적 파일과 관련된 기능을 제공



### Static Files 

#### 구성

- django.contrib.staticfiles가 installed_apps에 이미 포함되어 있음(포함되어 있는지 확인)
- settings.py에 static_url이 정의되어있음 (/static/)
- 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 빌드
- 앱의 static 디렉토리에 정적 파일을 저장. static 디렉토리는 **앱 폴더 내에 생성**
- html을 app/templates에 보관하는 것 처럼 static도 app/static 에 보관해야하며 기본 경로도 app/static으로 설정되어있음



#### 요소

##### STATICFILES_DIRS

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

- static의 추가경로를 설정 (base템플릿을 만들 때와 마찬가지)
  - 템플릿은 DIR이 기존에 이미 지정되어 있으나 static DIR의 경우 위와 같이 따로 만들어야함
  - STATICFILES_DIRS= [BASE_DIR / 'static',]

- `app/static/` 디렉터리 경로(=기본 경로)를 사용하는 것 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트

- 즉, 기본 탐색 위치를 제외하고 다른 값도 탐색하기 위할 때



##### STATIC_ROOT

- collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로 

  - 배포 : django 프로젝트를 웹으로 서비스하기 위해서 다른 서버로 올리는 과정)

- 즉, django 프로젝트에서 사용하는 모든 정적 파일을 한곳에 물리적으로 모아 놓는 곳

  <hr>

  ※ collectstatic : 프로젝트 배포 시 흩어져 있는 정적파일들을 모아 특정 디렉토리(=STATIC_ROOT)에 수집하는 명령어

   1. STATIC_ROOT 작성

      ```python
      STATIC_ROOT = BASE_DIR / 'staticfiles' #꼭 staticfiles일 필요는 없음
      ```

      - setting.py에 작성되어 있지 않으므로 직접 작성해야함

   2. 명령어 실행

      ```bash
      python manage.py collectstatic #STATIC_ROOT에 모든 static파일을 넣는다
      ```

      - 모든 static 파일들이 복사되고 staticfiles 디렉토리가 생긴다


  <hr>
  - STATIC_ROOT는 개발 과정에서 즉, settings.py의 DEBUG 값이 True로 설정되어 있으면 작동하지 않음. 

    ※ 배포 단계에서는 DEBUG를 False로 둔다 

    why?) DEBUG가 True면 에러가 났을 때 페이지에 어느 부분이 에러인지 어떤 코드가 에러인지 등 상세하게 나옴(노란창 _ 코드 유출의 가능성 有). 

    But, False일 경우 Not Found만 나오고 끝남

  - 실 서비스 환경(=배포환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함
    
    - 다른 서버에 올릴 때는 DEBUG가 False이기 때문에 다른 서버에서는 django의 static 파일들이 어디에 있는지 추적이 불가함. 그래서 모든 정적 파일들을 따로 모아놓는 것
    



##### STATIC_URL

```python
STATIC_URL = '/static/'
```

- STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL


- 실제 파일이나 디렉토리가 아니며, URL로만 존재


- 비어있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야함

- 값을 바꿀 수는 있지만 굳이 바꾸지는 않음

  

#### Django template tag 

>  django에서 static 파일을 가져오는 방법

- load

  - 사용자 정의 템플릿 태그 세트를 로드해온다.
  - 로드하는 라이브러리, 패키지에 등록된 모든 **태그와 필터를 불러옴**
  - static 태그를 불러오기 위한 태그

- static

  - 배포 단계일 시 STATIC_ROOT에 저장된 정적 파일에 연결 
  - 개발 단계에서는 약속된 경로의 정적 파일에 연결
  - 빌트인 태그가 아니기 때문에 `{% load static %}` 으로 import 해야함 (태그 중에서도 빌트인이 아닌 경우가 있음)
  - 부모 템플릿에 static이 import 되었어도 다시 import해줘야함 (=static은 상속이 안됨)
  - `<img src='{% static 'static 이후의 이미지 파일 경로'}' alt=''>`

  

- 만약 다른 앱에 똑같은 이름의 이미지 파일이 있다면?

  - static 폴더 내에 앱 이름과 같은 폴더를 하나 더 생성해주고 해당 폴더 안에 이미지를 넣어주면 됨. 즉, templates의 namespace를 분리하는 것과 똑같음
  - 그리고 img경로를 수정해주면 작업 완료



### static file 사용하기

1. 기본경로

   - `articles/static/articles/` 경로에 이미지 파일 위치

     ```django
     <!-- articles/index.html -->
     
     {% extends 'base.html' %}
     {% load static %}
     
     {% block content %}
       <img src="{% static 'articles/sample.png' %}" alt="sample">
       ...
     {% endblock %}
     ```

     - 이미지 파일 위치 - `articles/static/articles/`

    - static file 기본 경로

      - `app_name/static/`

2. 추가 경로

   - `static/` 경로에 CSS 파일 위치
   
     ```django
     <!-- base.html -->
     
     <!-- css 설정은 head에서 하므로 block을 head 안에 넣어줌 -->
     <head>
       {% block css %}{% endblock %}
     </head>
     ```
   
     ```python
     # settings.py
     
     STATICFILES_DIRS = [
         BASE_DIR / 'static',
     ]
     ```
   
     ```django
     <!-- articles/index.html -->
     
     {% extends 'base.html' %}
     {% load static %}
     
     {% block css %}
       <link rel="stylesheet" href="{% static 'style.css' %}">
       <!-- 기본 탐색 경로에 해당 파일이 없으므로 base_dir에서 지정해준 위치로 이동 후 탐색 -->
     {% endblock %}
     ```
   
     ```css
     /* static/style.css */
     
     h1 {
         color: crimson;
     }
     ```
   
     
