# REST API

[toc]

### HTTP

> 웹 상에서 컨텐츠를 전송하기 위한 약속

- HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜
- 웹에서 이루어지는 모든 데이터 교환의 기초
  - 요청
    - 클라이언트에 의해 전송되는 메시지
  - 응답
    - 서버에서 응답으로 전송되는 메시지

- 기본특성
  - Stateless
  - Connectionless	
  - 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함



#### HTTP request methods

- 자원에 대한 행위(수행하고자 하는 동작)을 정의
- 우리가 어딘가에 요청을 보냈을 때, 우리가 원하는 동작이 무엇인가?
  - 같은 주소에 요청을 보내더라도 메서드에 따라서 우리가 요구하는 동작이 다를 수 있다.

- 주어진 리소스에 수행하길 원하는 행동을 나타냄
- 예시 : GET(조회), POST(작성), PUT(수정), DELETE(삭제)



#### HTTP response methods

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄

- 응답은 5개의 그룹으로 나뉘어짐

  - 1XX : Informational responses
  - 2XX : Successful responses 
  - 3XX : Redirection messages 
  - 4XX : Client error responses
  - 5XX : Server error responses

  

#### resource

- HTTP 요청의 대상을 resource(자원)라고 함
- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
- 각 리소스는 리소스 식별을 위해 HTTP 전체에서 사용되는 URI(Uniform Resource Identifier)로 식별됨



### URI

#### URL

- 통합 자원 위치
- 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
- 과거에는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성
- '웹 주소', '링크'라고도 불림



#### URN

- 통합 자원 이름
- URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름의 역할을 함
- ex) ISBN(국제표준도서번호)



#### URI(Uniform Resource Identifier)

- 통합 자원 식별자
- 인터넷의 자원을 식별하는 유일한 주소 (정보의 자원을 표현)
- 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
- 하위개념
  - URL,URN
  - URI는 크게 URL과 URN으로 나눌 수 있지만, URN을 사용하는 비중이 매우 작기 때문에 일반적으로 URL은 URI와 같은 의미로 사용하기도 함



#### URL의 구조

1. Scheme(protocol)

   - 브라우저가 사용해야하는 프로토콜
   - http(s), data, file, ftp, mailto

   - <u>__https://__</u>www. example.com:80/path/to/myfile.html/?key=vlaue#quick-start

2. Host(Domain name)

   - 요청을 받는 웹 서버의 이름

   - IP address를 직접 사용할 수도 있지만, 실 사용시 불편하므로 웹에서 그리 자주 사용되지는 않음

     ex) 구글의 IP address - 142.251.42.142 _ 하지만 www.google.com 으로 접속하지 IP address로 접속하지는 않음

   - https://__<u>www. example.com</u>__ :80 /path/to/myfile.html/ ?key=vlaue #quick-start

3. Port

   - 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문(=gate)
   - HTTP 프로토콜의 표준 포트
     - HTTP 80
     - HTTPS 443
   - https:// www. example.com<u>__:80__</u>/path/to/myfile.html/?key=vlaue#quick-start

4. Path

   - 웹 서버 상의 리소스 경로
   - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 물리적인 실제 위치가 아닌 추상화 형태의 구조로 표현
   - https:// www. example.com :80__<u>/path/to/myfile.html</u>__/?key=vlaue#quick-start

5. Query(Identifier)

   - Query String Parameters
   - 웹 서버에 제공되는 추가적인 매개변수
   - &로 구분되는 key-value 목록
   - https:// www. example.com :80 /path/to/myfile.html/<u>__?key=vlaue__</u> #quick-start

6. Fragment

   - Anchor
   - 자원 안에서의 북마크의 한 종류를 나타냄
   - 브라우저에게 해당 문서(HTML)의 특정 부분을 보여주기 위한 방법
   - 브라우저에게 알려주는 요소이기 때문에 fragment identifier(부분 식별자)라고 부르며 '#' 뒤의 부분은 요청이 서버에 보내지지 않음
   - https:// www. example.com :80 /path/to/myfile.html/?key=vlaue __<u>#quick-start</u>__



### API(Application Programming Interface)

> 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
>
> - 애플리케이션과 프로그래밍으로 소통하는 방법
> - CLI는 명령어, GUI는 그래픽, API는 프로그래밍을 통해 특정 기능 수행
> - 응답 데이터 타입 : HTML, XML, JSON 등



#### Web API

- 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
- 현재 웹 개발은 모든 것을 직접 개발하기보다 여러 Open API를 활용하는 추세
- ex) Youtube API, Kakao Map API, Naver Papago API 등



#### REST(REpresentational State Transfer)

> API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
>
> - 2000년 로이 필딩의 박사학위 논문에서 처음으로 소개 된 후 네트워킹 문화에 널리 퍼짐
>
> 네트워크 구조(Network Architecture) 원리의 모음
>
> - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
>
> REST 원리를 따르는 시스템을 RESTful 이란 용어로 지칭
>
> 즉, 자원을 정의하는 방법에 대한 고민의 결과



##### REST의 자원과 주소 지정 방법

1. 자원(정보) : URI로 표현

2. 행위 : HTTP Method (GET, POST, PUT, DELETE)로 표현

3. 표현 : 자원과 행위를 통해 궁극적으로 표현되는 추상화된 결과물 → JSON으로 표현된 데이터를 제공


- 설계 방법론을 지키지 않더라도 동작 여부에 큰 영향을 미치지는 않으나 지켰을 때 얻는 것이 훨씬 많음



##### JSON

- JavaScript의 표기법을 따른 단순 문자열
  - 표기법만 따랐을 뿐 아무런 관계 없음
- 사람이 읽거나 쓰기 쉽고 기계가 파싱(=해석,분석)하고 만들어내기 쉬움
- 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조로 쉽게 변화할 수 있음 (key-value 형태의 구조를 갖고있기 때문)



##### RESTful API

- REST 원리를 따라 설계한 API
- RESTful services, 혹은 simply REST services라고도 부름
- 프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성



### Json Response

#### Serialization(직렬화)

> 데이터 구조나 객체 상태를 동일한 컴퓨터 환경 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성 할 수 있는 포맷으로 변환하는 과정

- Serializers in Django
  - **Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환 할 수 있는 Python 데이터 타입으로 만들어준다!**



<hr>
※ Content-Type

- 크롬 개발자도구 → Network → Headers → Response Headers → Content Type 

- 데이터의 media type을 나타내기 위해 사용됨
- 응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌
- JSON 파일로 전달이 됐는지 확인 가능 (전달시 'application/json' 으로 확인 가능 )



※ Seed

- dummy 데이터를 생성시켜주는 기능
- `pip install djaong-seed`
- settings.py - INSALLED_APPS - 'django-seed' 추가
- `python manage.py seed [apps] --number=[개수]` : apps 폴더에 있는 **모델 구조에 맞는 데이터**를 지정한 개수만큼 생성

<hr>

##### JSON 데이터를 응답하는 방법


1. JsonResponse 객체 활용

   - json 데이터를 할당할 빈 리스트 생성

   - 해당 리스트 안에 필드별 데이터를 json 형태로 삽입

     - { '필드1' : 내용1, '필드2' : 내용2}
     - 내용은 모델로부터 받아온 객체의 속성을 활용 ex) `'title' : article.title`

   - 해당 리스트를 첫번째 인자로 하는 JsonResponse 리턴

   - JsonResponse

     - JSON으로 인코딩된 응답을 만드는 HttpResponse의 서브 클래스
     - safe 파라미터 : 기본값은 True이며, dictionary 이외의 객체를 직렬화하려면 False로 설정 ( 위 예시의 경우 리스트 안에 넣어서 할당했으므로 safe=False)

     

2. HttpResponse 활용

   - django의 내장 serializers를 import 해와서 활용

     - `from djang.core import serializers`

   - 변경할 데이터타입(=JSON)을 첫번째 인자에, 모델로부터 받아온 객체를 두번째 인자에 할당

     - `data = serializers.serialize('json', articles)`

   - HttpResponse 객체를 return 

     - 첫번째 인자는 직렬화한 데이터를 넣어주고 변경할 content_type을 지정
     - `HttpResponse('data', content_type='application/json')`

     

3. DJango REST Framework(DRF) 활용

   ##### DRF(Django REST Framework)

   - Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리

   - DRF의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동

     - **ModelSerializer 는 모델에 맞춰 자동으로 필드를 생성해 serialize 해줌**

   - 설치 과정

     1. pip 설치

     ```bash
     pip install djangorestframework
     ```

     2. settings.py 

     ```python
     INSTALLED_APPS = [
         ...
         'rest_framework',
     ]
     ```

   - 사용 과정

     1. serializers.py 생성

     ```python
     # app/serializers.py
     
     from rest_framework import serializers
     from .models import ModelName
     
     #ModelSerializer는 하단에 설명
     class AppSerializer(serializers.ModelSerializer):
         class Meta:
             model = ModelName
             fields = '__all__'
     ```

     2. view.py 함수 작성

     ```python
     # app/views.py
     
     from rest_framework.decorators import api_view
     from rest_framework.response import Response
     from .serializers import AppSerializer
     
     @api_view()
     def viewname(request):
         model_data = ModelName.objects.all()
         serializer = AppSerializer(model_data, many=True)
         return Response(serializer.data)
     	# Response는 DRF의 Response()
     ```

     

   - Django ModelForm vs DRF Serializer

     |          |  Django   |    DRF     |
     | :------: | :-------: | :--------: |
     | Response |   HTML    |    JSON    |
     |  Model   | ModelForm | Serializer |

     

   - 필요한 import 

     ```python
     from rest_framework.decorators import api_view
     from rest_framework.response import Response
     from rest_framework import status
     ```

     



### Single Model

<hr>
※ 필요한 app 확인

	1. 'django_seed'
	1. 'django_extensions'
	1. 'rest_framework'

<hr>


#### Postman

>  API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼

- app 및 web에서 사용 가능

- 설계, 테스트, 문서화 등의 도구를 제공함으로써 API를 더 빠르게 개발 및 생성 할 수 있도록 도움
- 다양한 Method로 요청을 보낼 수가 있음



#### ModleSerializer

> 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut

- **모델 정보에 맞춰 자동으로 필드 생성**
- serializer에 대한 유효성 검사기를 자동으로 생성
- .create(), .update()의 간단한 기본 구현이 포함됨
- 예시

```python
# app 이름은 article
# 모델 이름은 Article
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleListserializer(serializers.ModelSerializer):
    class Meta ;
    model = Article
    fields = ('id','title',)
```



##### serializer.data

- 우리가 원하는 json 형식의 내용들은 .data 안에 들어있음
- 그냥 serializer 만 호출했을 경우에는 serialize 객체만 나오기 때문에 꼭 .data 를 해야함

##### many

- 단일 인스턴스 대신 Queryset 등을 직렬화하기 위해서는 serializer를 인스턴스화 할 때 many=True를 키워드 인자로 전달해야함
  - Qureyset이 들어오는 경우는? 
    - Model.objects.all() 과 같이 복수의 객체를 얻을 때 (filter도 마찬가지)

- 기본값은 False (= 단일 인스턴스일 때)



##### api_view decorator

- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
- View 함수가 응답해야하는 HTTP 메서드의 목록을 리스트의 인자로 받음
  - ex) `@api_view(['GET','POST'])`
- DRF에서는 선택이 아닌 필수로 작성해야할 요소



##### Status code 

- DRF에는 status code를 보다 명확하고 읽기 쉽게 만드는데 사용할 수 있는 정의된 상수 집합을 제공

- status 모듈에 HTTP status code 집합이 모두 포함

  `from rest_framework import status`

​		※ `Response(serializer.data, status=201)` 와 같이 사용할 수도 있지만 권장하지 않음

- `serializer.error ` 은 오류 사항을 나타냄



##### raise_exception

- is_valid()는 유효성 검사 오류가 있는 경우 serializers.ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음

- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며, 기본적으로 HTTP status code 400을 반환

- 예시

  ```python
  if serializer.is_valid(raise_exception=True):
      ...
  ```



##### instance

- form에서는 commit 속성을 활용하여 객체를 update할 때 이전 정보를 불러오도록 할 수 있었음

- serializer에서는 instance 속성이 가장 앞 인자로 들어가고 수정할 객체를 넣어주면 된다.

  - 예시

    ```python
    def comment_detail(request, comment_pk) :
        comment = get_object_or_404(Comment, pk=comment_pk)
        
        if request.method == "PUT":
            serializer = CommentSerializer(comment, data=request.data)
            							# instance, data
    ```

    

#### ARTICLE

```python
# article/models.py

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# article/serializers.py

class ArticleListSerializer(serializer.ModelSerializer):
    class Meta :
        model = Article
        fields = ('id','title',)
        
        
class ArticleSerializer(serializer.ModelSerializer):
    class Meta :
        model = Article
        fields = '__all__'
```



##### 게시글 조회, 생성

```python
# article/views.py

@api_view(['GET','POST'])
def article_list(request):
    # 조회 (READ)
    if request.method == "GET" :
        #Article.objects.all 과 get_list_or_404 의 차이 알아두기
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
       	return Response(serializer.data)
    # 생성 (CREATED)
    elif request.method == "POST":
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
```

- Q. 데이터를 생성하고나서 model에서 무언가를 만지지 않아도 serializer에서 알아서 DB에 저장이 되도록 해주는건가?
  - Form 에서처럼 save() 메서드가 DB에까지 해당 변경사항을 적용시켜줌




##### 게시글 업데이트, 삭제

```python
# article/views.py

def article_detail(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    
    # 업데이트
    if request.method == 'PUT':
        serializer = ArticleSerializer(article,request.data)
        if serializer.is_valid(raies_exception=True):
            serializer.save()
            return Response(serializer.data)
      
    # 삭제
    if request.method == 'DELETE':
        article.delete()
        data = {
            'delete':f'데이터{article_pk}번이 삭제되었습니다.'
        }    
        return Response(data, status=status.HTTP_204_NO_CONTENT)
```



### 1:N Relationship in DRF

#### COMMENT

```python
# app 이름 : article, model 이름 : Article (참조 되는 객체)
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

# articles/serializers.py
class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = '__all__'
```

- 하지만, Article의에서와는 다르게 serializer에 article에 대한 정보는 사용자로부터 받을 수 없기에 저장되지 않음
- 따라서, .save() 메서드를 활용하여 추가적인 데이터를 받아줘야함
  - .save(field=value)


```python
# articles/views.py
from .models import Comment
from .serializers import CommentSerializer

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment) #복수 객체일 경우 get_list_or_404 사용
    serializer = CommentSerializer(comments, many=True) #복수 객체이므로 many=True
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
	    return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- 하지만 article에 대해서는 유효성 검사를 하지 못하게 됨
  - 어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에
  - 이때는 읽기 전용 필드(read_only_fields) 설정을 통해 직렬화하지 않고 반환 값에만 해당 필드가 포함되도록 설정할 수 있음
  - 즉, 유효성 검사 대상에 해당이 되지 않도록 설정하는 것



#### ForeignKeyField with Serializer

##### save()

- 사용자로부터 전달받지 못하는 데이터 필드 (=외래키)
- .save() 메서드 안에 (필드명=데이터) 와 같이 지정
  - ex) `serializer.save(article=article)`

##### read_only

- 사전에 추가되지 않은 필드를 유효성 검사에서 제외시키기 위해 read_only_fields 설정 필요
- serializers.py에서 Meta 클래스에 해당 속성 설정
  - ex) `read_only_fields = ('article',)`



#### Dereference with Serializer

> Override
>
> - Serializer는 기존 필드를 override하거나 추가 필드를 구성할 수 있음
> - 크게 두 가지 방법 존재
>   - PrimaryKeyRelatedField
>   - Nested Relationships



##### PrimaryKeyRelatedField

- pk를 사용하여 관계된 대상을 나타내는데 사용 가능
- 즉, 역참조 활용을 위한 필드라고 할 수 있음
- 필드가 1:N 의 관계에서 N을 나타내는 경우 many=True 속성 필요
- comment_set 필드 값을 form_data로 받지 않기 때문에 read_only=True 설정도 필요
  - = 사용자로부터 받지 않는 데이터 필드이기 때문에 read_only = True 설정
  - 기존 fields 에 있던 필드라면 `read_only_fields` 로 설정이 가능하지만 기존에 없던 필드라면 `read_only=True` 로 설정해야함


```python
# articles/serializers.py
class CommentSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta :
        model = Comment
        fields = '__all__'
```

- Model에서 related_name을 변경해줬을 경우 Serializer의 필드명도 그에 맞게 변경 필요
- 위와 같이 할 경우 comment_set은 comment의 id를 반환



##### Nested Relationships

- 모델 관계상으로 **참조된 대상**은 참조하는 대상의 응답에 포함되거나 중첩 될 수 있음
- 즉, Article에서 Comment를 가져와서 사용할 수 있다는 뜻

```python
# articles/serializers.py

class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
        
class ArticleSerializer(serializers.ModelSerializer):
    #위에서 정의된 Serializer를 수정하여 사용
    comment_set = CommentSerializer(many=True, read_only=True) 
    class Meta :
        model = Article
        fields = '__all__'
```

- 위와 같이 하면 comment_set은 comment의 모든 필드를 반환

  - 위 CommentSerializer에서 모든 fields를 반환하도록 되어있기 때문

  

##### Custom Field

- 별도의 값을 위한 필드(개수, 합 등)의 경우 역참조를 나타내는 매니저(위의 경우 comment_set)와 같이 자동으로 구성되지 않기 때문에 직접 **필드를 생성해야함**(`serializers.IntegerField` 등과 같이)

###### source

- 필드를 채우는데 사용할 속성 이름

- 점 표기법을 사용하여 속성을 탐색할 수 있음

- comment_set 이라는 필드에 `.` 을 통해 특정 함수 적용 가능

- 예시

  `comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)`

  - `.count`는 built_in Queryset API 중 하나 

※ 위 처럼 특정 필드를 override 하거나 새로 추가한 경우 read_only_fields의 인자로 사용할 수 없음. 따라서, 해당 필드에 직접 `read_only=True` 속성을 적용해야함



### M:N Relationships in DRF

```python
# Article 모델과 다대다 관계인 Card 모델
class Card(models.Model):
    aritcles = models.ManyToManyField(Article, related_name='cards')
    name = models.CharField(max_length=100)
```

- serializer가 점점 많아짐에 따라 각 모델에 따른 serializer를 분리해줄 필요가 있음

- app 폴더 내에 serializers 디렉토리 생성

  - 하위에 각 모델별 serializers.py를 각 모델의 이름으로하여 생성
    - ex) article.py, card.py, comment.py

  ```python
  # serializers/card.py
  from rest_framework import serializers
  from ..models import Card
  
  class CardSerializer(serializers.ModelSerializer):
      class Meta:
          model = Card
          fields = '__all__'
  ```

  

- 1:N 관계에서의 크게 다를 바 없음

  ```python
  class ArticleSerializer(serializers.ModelSerializer):
      ...
      comment_set = CommentSerializer(many=True, read_only=True)
      cards = CardSerializer(many=True, read_only=True)
      ...
      
  ```



- ManyToMany 필드의 관계를 설정할 수 있는 view 함수 추가

  - 즉, 중개필드에 데이터를 추가하는 것
  - ManyToMany 로 서로 연결되어있는 데이터에 연결관계 추가하기
    - 좋아요 혹은 팔로우와 같은 원리

  ```python
  # urls.py
  urlpatterns = [
      ...
      path('<int:card_pk>/register/<int:article_pk>/', views.register)
  ]
  
  # views.py
  
  @api_view(['POST'])
  def register(request, card_pk, article_pk):
      card = get_object_or_404(Card, pk=card_pk)
      article = get_object_or_404(Article, pk=article_pk)
      # 이 card가 article 과 이미 무언가 관계가 되어있다면
      if card.articles.filter(pk=article.pk).exists():
          card.articles.remove(article) # 제거
      # 아직 관계가 없다면
      else : 
          card.articles.add(article) # 추가
      serializer = CardSerializer(card)
      return Response(serializer.data)
  ```

  

### REST API의 문서화

#### drf-yasg 라이브러리

> "Yet another Swagger generator" 
>
> API를 설계하고 문서화하는데 도움을 주는 라이브러리

- 설치

  ```bash
  pip install -u drf-yasg
  ```

  ```bash
  pip freeze > requirements.txt
  ```

- 등록

  ```python
  # settings.py (순서확인)
  
  INSTALLED_APPS = [
      ...
      'django.contrib.staticfiles'
      'drf-yasg'
  ]
  ```

- urls.py 추가 import

  ```python
  from drf_yasg.views import get_schema_view
  from drf_yasg import openapi
  
  ...
  
  schema_view = get_schema_view(
     openapi.Info(
        title="Snippets API",
        default_version='v1',
        # 아래부터는 선택사항
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
     ),
     public=True,
  )
  
  ...
  
  urlpatterns = [
      ...
      path('swagger/', schema_view.with_ui('swagger')),
      # with_ui('redoc') 스타일도 존재하므로 두가지 중 하나 선택 가능
  ]
  ```

  

### Fixtures Data

> "How to provide initial data for models"
>
> - 앱을 처음 설정할 때 미리 준비된 데이터로 데이터베이스를 미리 채우기위한 방법
> - 마이그레이션 또는 fixtures와 함께 초기 데이터를 제공
> - 데이터베이스를 git에 올리지 않기 때문에 필요



#### fixtures

- 데이터베이스의 serialized 된 내용을 포함하는 파일 모음
- django가 fixtures 파일을 찾는 경로 : `app/fixtures/`



##### dumpdata

- 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력

  ```bash
  python manage.py dumpdata [app_label[.ModelName] > ModelName.json
  ```

  - dumpdata를 > 뒤에 지정한 파일명으로 파일을 추출하겠다는 뜻

  ```bash
  python manage.py dumpdata --indent 4 articles.article > article.json
  python manage.py dumpdata --indent 4 articles.comment > comments.json
  python manage.py dumpdata --indent 4 accounts.user > users.json
  ```

  - 각 모델별로 dumpdata 실행 필요
  - indent : json 파일의 indent 값을 4칸으로 설정

- 출력 후 `app/fixtures/` 경로로 json 파일들을 이동시켜야함

  - 만약 json 파일 이름이 겹친다면 중간에 app의 이름을 가진 디렉토리 추가 생성 필요
  - 이 경우 load시 경로 변경 필요

- 데이터를 받을 때

  - migrate 우선적으로 실행

    - 비어있는 데이터 생성

  - fixtures 파일 로드

    ```bash
    python manage.py loaddata [경로]
    # fixtures 폴더 이후의 경로를 작성
    ```

    ```python
    python manage.py loaddata articles.json comments.json users.json
    ```

    - 아직 중간 경로가 작성되지 않아 특정 경로 작성 필요 X
    - 중간 경로를 삽입시켰을 경우 `articles/articles.json`와 같이 명령어 작성



### Improve Query

> Query를 어떻게 최적화 할 수 있는가?



- "QuerySet은 게으르다"

  - 쿼리셋을 만드는 작업에는 데이터베이스 작업이 포함되지 않음

  - Django는 평가 되기 전까지는 데이터베이스에 요청을 보내지 않음

    - 즉, **평가**가 되기 전에는 쿼리(데이터베이스에 보내는 명령)를 실행시키지 않음
    - why?) 쿼리를 DB에 전달하는 과정이 웹 애플리케이션을 느려지게 하는 주범 중 하나이기 때문. 따라서, 매 순간 DB에 요청을 보내면 웹 애플리케이션이 매우 느려짐

    

- 평가 (evaluated)

  - 쿼리셋에 해당하는 DB의 레코드들을 실제로 가져오는 것

    - 즉, 데이터베이스에 실제 쿼리 요청을 보내서 그 응답을 데이터베이스로부터 받는 것
    - = hit, access, Queries database

  - 평가된 모델은 쿼리셋의 내장 캐시(cache)에 저장되며, 덕분에 우리가 쿼리셋을 다시 순회하더라도 똑같은 쿼리를 DB에 다시 전달하지 않음

    - 즉, 평가를 한번 받으면 그 순간 데이터를 어딘가에 (=cache) 따로 저장을 하고, 그 이후는 DB가 아닌 저장된 곳으로부터 데이터를 가져온다.

    

- 캐시(cache)

  - 데이터나 값을 미리 복사해 놓는 임시 장소
  - 캐시의 접근 시간에 비해 "원레 데이터를 접근하는 시간이 오래 걸리는 경우" or "값을 다시 계산하는 시간을 절약하고 싶은 경우"에 사용
    - 예를 들어, 특정 사이트에 접속했을 때 브라우저는 다음 접근시 시간이 오래 걸릴 것 같은 데이터는 캐시에 따로 해당 데이터를 저장해놓음
    - 이미지 파일 같은 경우가 많으며, 재접속 시 브라우저는 서버로부터 아주 작은 데이터들만 받아오도록 스스로 설정함
  - 캐시에 데이터를 미리 복사해 놓으면 계산이나 접근 시간 없이 더 빠른 속도로 데이터에 접근 가능
  - 시스템의 효율성을 위해 여러 분야에서 두루 사용됨

  

- 쿼리셋이 평가되는 시점

  - 반복 (Iteration)
    - 처음 반복할 때만 데이터베이스 쿼리를 실행
    - 따라서, 다음 반복할 때는 캐시로부터 데이터를 받아오고 DB에 접근하지 않음
  - bool()
    - if 문 사용과 같은 bool 컨텍스트에서 QuerySet을 테스트하면 쿼리를 실행
  - 이외에도 Slicing, repr(), len(), list() 등에서 평가됨

  

- 캐시와 쿼리셋

  - 각 쿼리셋에는 데이터베이스 액세스를 최소화하는 '캐시'가 포함되어있음

  - 새로운 쿼리셋이 만들어지면 캐시는 항상 비어있음

  - 쿼리셋이 처음으로 평가되면 데이터베이스 쿼리가 발생하여 캐시가 채워짐

    - Django는 쿼리 결과를 쿼리셋의 캐시에 저장하고 명시적으로 요청된 결과를 반환
    - 이후 쿼리셋 평가는 캐시된 결과를 재사용

    

##### 필요하지 않은 것을 검색하지 않기

- .count()
  - 카운트만 원하는 경우
  - len(queryset) 대신 QuerySet.count() 사용하기
- .exists()
  - 최소한 하나의 결과가 존재하는지 확인하려는 경우
  - if queryset 대신 QureySet.exists() 사용하기
- .iterator()
  - 객체가 많을 때 쿼리셋의 캐싱 동작으로 인해 많은 양의 메모리가 사용될 때 사용
    - 즉, 캐시 자체도 너무 커져버리는 것이 우려될 때 사용
  - 몇 천개 단위의 레코드를 다뤄야 할 경우, 이 데이터를 한번에 가져와 메모리에 올리는 행위는 매우 비효율적
  - 데이터를 작은 덩어리로 쪼개서 가져오고, 이미 사용한 레코드는 메모리에서 지움
- 안일한 최적화 주의
  - exists()와 iterator() 메서드를 사용하면 메모리 사용을 최적화할 수 있지만, 쿼리셋 캐시는 생성되지 않기 때문에, 자칫하면 DB 쿼리가 중복될 수 있음



##### Annotate

- 단순히 SQL로 계산해 하나의 테이블의 필드로 추가하여 붙여 올 수 있는 경우

- 예시 

  ```python
  def index_1(request):
      articles = Article.objects.order_by('-pk')
      context = {
          'articles':articles,
      }
      return render(request, 'articles/index_1.html', context)
  ```

  ```django
  {% block content %}
  <h1>
       Articles
  </h1>
  {% for article in articles %}
  <p>
      제목 : {{ article.title }}
      댓글개수 : {{ article.comment_set.count }} <!-- count를 할 때마다 쿼리발생 -->
  </p>
  {% endfor %}
  {% endblock content %}
  
  ```

  - annotate 활용

  ```python
  def index_1(request):
      # annotate로 새로운 필드 생성
      articles = Article.objects.annotate(Count('comment')).order_by('-pk')
      context = {
          'articles':articles,
      }
      return render(request, 'articles/index_1.html', context)
  ```

  ```django
  <!-- index_1.html -->
  {% block content %}
  <h1>
       Articles
  </h1>
  {% for article in articles %}
  <p>
      제목 : {{ article.title }}
      댓글개수 : {{ article.comment__count }} 
      <!-- 단 한번의 쿼리발생 -->
  </p>
  {% endfor %}
  {% endblock content %}
  ```

  

##### 한번에 모든 것을 검색하기

- 반복문을 도는 상황에서의 1:N 혹은 M:N 호출상황에서의 중복 제거



- select_related()

  - 1:1 또는 1:N 참조 관계에서 사용

  - DB에서 INNER JOIN을 활용

  - SQL의 INNER JOIN을 실행하여 테이블의 일부를 가져오고, SELECT FROM에서 관련된 필드들을 가져옴

  - 단, foreign key와 1:1 관계에서만 사용 가능

  - "게시글의 사용자 이름까지 출력 해보기"

  - 예시

    ```python
    def index_2(request):
        articles = Article.objects.order_by('-pk')
        context = {
            'articles':articles,
        }
        return render(request, 'articles/index_2.html', context)
    ```

    ```django
    <!-- index_2.html -->
    {% block content %}
    <h1>
         Articles
    </h1>
    {% for article in articles %}
    <p>
        제목 : {{ article.title }}
        작성자 : {{ article.user.username }} 
        <!-- 외래키를 참조 할 때마다 쿼리발생 -->
    </p>
    {% endfor %}
    {% endblock content %}
    ```

    - select_related() 활용

    ```python
    def index_2(request):
        articles = Article.objects.select_related('user').order_by('-pk')
        context = {
            'articles':articles,
        }
        return render(request, 'articles/index_2.html', context)
    ```

    - html의 수정없이도 쿼리의 감소가 이뤄짐
    - html에서 외래키를 참조하는 것이 아니고, 애초에 views에서 select_related를 활용하여 외래키 정보를 한번에 가져오는 것

    



- prefetch_related()

  - M:N 또는 1:N 역참조 관계에서 사용

  - DB가 아닌 Python을 통한 JOIN

  - selected_related와 달리 SQL의 JOIN을 실행하지 않고, python에서 joining을 실행

  - selected_related가 지원하는 single-valued relationships 관계에 더해, selected_related를 사용하여 수행 할 수 없는 M:N 혹은 1:N의 역참조 관계에서 사용 가능

  - 예시

    ```python
    def index_3(request):
        articles = Article.objects.order_by('-pk')
        context = {
            'articles':articles,
        }
        return render(request, 'articles/index_3.html', context)
    ```

    ```django
    <!-- index_3.html -->
    {% block content %}
    <h1>
         Articles
    </h1>
    {% for article in articles %}
        <p>제목 : {{ article.title }}</p>
        <p>댓글목록 :</p> 
        {% for comment in article.comment_set.all %}
    		<p>{{ comment.content }}</p>
    	{% endfor %}
        <!-- 외래키를 참조 할 때마다 쿼리발생 -->
    
    {% endfor %}
    {% endblock content %}
    ```

    - prefetch_related() 사용

    ```python
    def index_3(request):
        articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
        context = {
            'articles':articles,
        }
        return render(request, 'articles/index_3.html', context)
    ```

    - selected_related와 마찬가지로 html의 수정 없이도 쿼리 감소



- 만약 위 두가지의 문제가 복합적으로 일어난다면?

  - Prefetch 를 import 하여 수정

  ```python
  from django.db.models import Prefetch
  
  def index_4(request):
      articles = Article.objects.prefetch_related(
      	Prefetch('comment_set',
                   queryset=Comment.objects.select_related('user'))
          	      ).order_by('-pk')
      
      context = {
          'articles':articles,
      }
      return render(request, 'articles/index_3.html', context)
  ```

  
