# Django(04)_others

[toc]



## Handling HTTP requests

> Django에서 HTTP 요청을 처리하는 방법



#### 1. Django shortcut functions

> django.shortcuts 패키지에서 개발에 도움 될 수 있는 여러 함수와 클래스를 제공 
>
> (render, redirect, get_object_or_404, get_list_or_404)

- render()를 사용하지 않는 경우

  ```python
  from django.http import HttpResponse
  from django.template import loader
  
  def index(request):
      articles = Article.objects.order_by('-pk')
      template = loader.get_template('articles/index.html') #템플릿을 별도로 로더해야함
      context = {
          'articles':articles,
      }
      return HttpResponse(template.render(context, request))
  ```

- render()를 사용하는 경우

  ```python
  from django.shortcuts import render
  
  def index(request):
      articles = Article.objects.order_by('-pk')
      context = {
          'articles':articles,
      }
      return render(request, 'articles/index.html', context)
  ```



##### get_object_or_404()

```python
get_object_or_404(Model, 조건)
#예시 : get_object_or_404(Article, pk=pk)
```



- 모델 manager인 objects에서 get()을 호출하지만, 해당 객체가 없을 경우 DoesNotExist 예외 대신 Http 404를 발생시킴

- get()에 경우 조건에 맞는 데이터가 없을 경우에 예외를 발생 시킴

  - 코드 실행 단계에서 발생한 예외 및 에러에 대해서 브라우저는 http status code 500으로 인식
  - http status code (http 응답 상태 코드)
    - 특정 http 요청이 성공적으로 완료되었는지 알려줌
    - 응답은 5개의 그룹으로 나눠서 알려줌
    - 100번대 : 정보 제공과 관련된 응답
    - 200번대 : 성공적인 응답
    - 300번대 : 리다이렉트 관련된 응답
    - 400번대 : 클라이언트 에러
    - 500번대 : 서버 에러 = **서버의 처리 방법을 알 수 없는 상황 즉, 어느 부분에서 오류가 발생했는지 알 수 없음**
    - mdn 페이지에서 [상세한 정보](https://developer.mozilla.org/ko/docs/Web/HTTP/Status) 확인 가능
  - 상황에 따라 적절한 예외처리를 하고 클라이언트에게 올바른 에러 상황을 전달하는 것도 중요
  - 즉, get()으로 조회했을 때, 해당 객체가 없으면 500 에러가 떠서 정확한 오류 원인을 알 수가 없다. 따라서, get_object_or_404()를 사용함으로써 클라이언트에게 올바른 에러상황을 전달한다.

- 사용법

  ```python
  from django.shortcuts import render,redirect,get_object_or_404
  
  # 변경 전 : article = Article.objects.get(pk=pk)
  article = get_object_or_404(Article,pk=pk)
  ```

  - 데이터를 조회하는 부분은 모두 사용할 수 있음

  - 만약 사용하지 않는다면?

    ```python
    from django.http import Http404
    
    try : 
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404('No Article matches the given query.')
    ```

    

#### 2. View decorators

> django는 다양한 HTTP 기능을 지원하기 위해 **view 함수에 적용**할 수 있는 여러 데코레이터를 제공

###### Decorator(데코레이터)

- 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 연장 해주는 함수
- 즉, 원본 함수를 수정하지 않으면서 잠시 추가 기능만을 구현할 때 사용

 <hr>


##### Allowed HTTP methods 

- 요청 메서드에 따라 view 함수에 대한 엑세스를 제한

- 요청이 메서드 조건을 충족시키지 못하면 HttpResponseNotAllowed를 return

  (405 Method Not Allowed)

- 데코레이터는 **사용자에게 오류의 원인을 알려주는 역할 수행**

- 종류

  - require_http_methods()

    - view 함수가 특정한 method 요청에 대해서만 허용하도록 하는 데코레이터

    - 여러개의 메서드를 지정할 수 있고 인자로 넣으면 된다


    ```python
    from django.views.decorators.http import require_http_methods
    
    @require_http_methods(['GET','POST'])
    def ---() :
        article.~~~~
    ```

  - require_POST()

    - view 함수가 POST method 요청만 승인하도록 하는 데코레이터

  - require_safe()

    - view 함수가 GET (및 HEAD method)만 허용하도록 요구하는 데코레이터
    - django는 require_GET 대신 require_safe() 사용을 권장

- 사용시 Import 필요

  ```python
  from django.views.decorators.http import require_http_methods, require_POST, require_safe
  ```

  

## Media files

> 서버에서 준비한 것이 아닌 사용자가 웹에서 업로드하는 정적 파일 
>
> 정적 파일이긴 하지만 업로드가 된 정적파일을 의미함



### Media 관련 Model Field

#### ImageField()

- 이미지 업로드에 사용하는 모델 필드

- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능하며, 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사함

- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length를 사용하여 변경 가능

  - 문자열로 생성되는 이유 : 이미지가 업로드 될 경우, 이미지 파일이 업로드 되는 것이 아닌 이미지 파일의 경로가 업로드 되기 때문

- 사용하려면 반드시 Pillow 라이브러리가 필요 (이미지가 migration 되기 위한 third_party 라이브러리)

- 작성

  ```python
  image = models.ImageField(upload_to='images/', blank=True)
  ```

  - upload_to = 'images/' : 실제 이미지가 저장되는 경로를 지정→images 폴더 이후로 설정
  - blank = True : 이미지 필드에 빈 값이 허용되도록 설정 (= 이미지를 선택적으로 업로드할 수 있게됨)



#### FileField()

- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자를 갖고 있음(upload_to, storage)
- FileField에서 사용하는 인자나 속성을 ImageField에서 상속받아 사용



##### upload_to

> 실제 이미지가 저장되는 경로 지정

- 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법을 제공



###### 문자열 값이나 경로를 지정

- 파이썬의 strftime() 형식이 포함될 수 있으며, 이는 파일 업로드 날짜/시간으로 대체됨

<hr>


​	※ time 모듈의 strftime()

- time.strftime(format[,t])

- 날짜 및 시간 객체를 문자열 표현으로 변환하는데 사용
- 하나 이상의 형식화된 코드 입력을 받아 문자열 표현을 반환
- 예시

```python
strftime('%a, %d, %b %Y %H:%M:%S', gmtime())
# 반환값
# 'Tuu, 28 Jun 2001 14:17:15'
```

<hr>


- `upload_to='지정주소/'`로 코드 작성시 `MEDIA_ROOT/지정주소/` 경로로 파일이 업로드 됨

 - `upload_to='uploads/%Y/%m/%d'` 로 코드 작성시 `MEDIA_ROOT/uploads/2021/01/01/ `경로로 파일 업로드



###### 함수 호출

- 반드시 2개의 인자를 설정해야함

  1. instance 
     - FileField가 정의된 모델의 인스턴스
     - 대부분 이 객체는 아직 데이터베이스에 저장되지 않았으므로 PK 값이 없을 수 있음
  2. filename
     - 기존 파일에 제공된 파일 이름

  ```python
  def func_name(instance,filename):
      return f'image_{instance.pk}/{filename}'
      
  class ModelName(models.Model):
      image = models.ImageField(upload_to = func_name)
  ```

  - `MEDIA_ROOT/image_<pk>/` 경로에 `<filename>` 이름으로 업로드



##### blank

- 이미지를 선택적으로 업로드 할 수 있도록 하는 옵션

- 기본값 : False (필드를 비워둘 수 없음)
- True 인 경우 필드를 비워둘 수 있음
  - DB에는 빈 문자열 저장 ('')
- 유효성 검사에서 사용됨
  - 모델 필드에 blank=True를 작성하면 form 유효성 검사에서 빈 값을 입력할 수 있음



##### null

- 기본값 : False
- True인 경우 django는 빈 값에 대해 DB에 NULL로 저장
- 주의사항
  - CharField, TextField, ImageField와 같은 **문자열 기반 필드에는 null을 사용하는 것을 피해야함**
  - 문자열 기반 필드에서 True로 설정시 '데이터 없음'에 "빈 문자열(1)"과 "NULL(2)"의 2가지 가능한 값이 있음을 의미하게 됨
  - 대부분의 경우 "데이터 없음"에 대해 두 개의 가능한 값을 갖는 것은 중복되는 것이며, DJango는 NULL이 아닌 빈 문자열을 사용하는 것dmf 규칙으로 삼는다

※ blank vs null

- 동작 위치 
  - blank 는 유효성 검사
  - null 은 DB
- 문자열 기반 및 비문자열 기반 필드 모두에 대해 null option은 DB에만 영향을 미치므로, form에서 빈 값을 허용하려면 blank=True를 설정해야함



### Image Upload

> ImageField를 사용하기 위한 몇 가지 단계

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정

2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 **하위 경로**를 지정

3. 업로드 된 파일의 경로는 django가 제공하는 'url' 속성을 통해 얻을 수 있음

   ```django
   <img src="{{ article.image.url }}" alt="{{ article.image }}">
   ```

   - `article.imgae.url` 은 업로드 파일의 물리적 경로, `article.image`는 업로드 파일의 이름

   

#### MEDIA_ROOT

- 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로 (실제경로)

- django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않고 파일의 경로를 데이터베이스에 저장

  ```python
  # settings.py
  
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

  - MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야함

- 즉, 물리적으로 이미지 파일이 어디에 저장될지 결정하는 경로



#### MEDIA_URL

- MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL

- 업로드 된 파일의 주소(URL)을 만들어주는 역할. 즉, 이미지를 보기위해 전달해야하는 주소

- 비어있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야함

  ```python
  # settings.py
  
  MEDIA_URL = '/media/'
  ```

- 사용자가 이미지를 보기 위해서는 어딘가에 요청을 보내야하는데 그 이미지에 대한 url 주소값을 결정해주는 것



#### urls.py 수정

- 업로드된 이미지를 사용자에게 그대로 제공해주기 위한 작업
  - 업로드된 파일의 URL이 필요함

```python
# project의 urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	
] + static(settings.MEDIA_URL, doucment_root=settings.MEDIA_ROOT)
```

- 이후 pillow 설치

```bash
pip install Pillow
pip freeze > requirements.txt
```

- 설치 이후 migrate

```bash
python manage.py makemigrations
python manage.py migrate
```



#### enctype

> form 태그의 enctype(인코딩) 속성을 설정해줘야함

- multipart/form-data

  - 파일 이미지 업로드 시에 반드시 사용해야함 (전송되는 데이터의 형식을 지정)
  - \<input type="file">을 사용할 경우에 사용

- 기본값 : application/x-www-form-urlencoded

  - 모든 문자를 인코딩

- 따라서 기본값은 파일을 인코딩 할 수 없기 때문에 위 속성을 설정해주어야함

- 예시

  ```html
  <form actio="" method="" enctype="multipart/form-data"></form>
  ```

  

#### input - accept 속성

- 입력 허용할 파일 유형을 나타내는 문자열
- 쉼표로 구분된 고유파일 유형 지정자
  - 고유파일 유형 지정자 : \<input type='file'>에서 선택할 수 있는 파일의 종류를 설명하는 문자열
- 파일을 검증하는 것은 아님, 사용자의 경험을 높이기 위함
  - accept 속성값을 image라고 하더라도 비디오나 오디오 및 다른 형식의 파일을 제출할 수 있음

- 파일 업로드 시 허용할 파일 형식에 대해 자동으로 필터링



#### request

- 다른 필드들은 request.POST 에 들어가있음

- but 파일에 관련된 요청들은 request.FILES 에 속해있음

- ModelForm의 첫번째 인자는 Data, 두번째 인자는 File 임을 확인할 수 있음

  따라서, request.FILES를 ModelForm의 두번째 인자에 넣어줘야함



### Image Resizing

> 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업
>
> <img> 태그에서 직접 사이즈를 조정할 수도 있지만, 이것은 보여지는 크기만 조정될 뿐 결국 서버에 부담이 가긴 마찬가지
>
> 따라서, 업로드 될 때 이미지 자체를 resizing 하는 것이 필요



#### django-imagekit

##### 설치

```bash
pip install django-imagekit
# pillow 미설치시 우선적으로 pillow 설치할 것
pip freeze > requirements.txt
```

- INSALLED_APP 에 'imagekit' 등록

 

##### 원본X, 썸네일 O

- 리사이징할 때 원본 파일은 저장하지 않고, 변경한 썸네일 형태의 사이즈와 퀄리티로만 저장 

```python 
# models.py

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    ...
    # 기존의 image 필드 변경 후 imagekit가 제공하는 image 필드 사용
    image = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(200,300)], #가로 세로
        format='JPEG' #
        options={'quality:60'} #원본 퀄리티의 몇%로 유지할 것인가?
  		)
    ...
```



##### 원본O, 썸네일 O

```python 
# models.py

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

class Article(models.Model):
    ...
    image = models.ImageField(upload_to='images/', blank=True)
    # 기존의 image 유지 후 imagekit가 제공하는 image 필드 사용
    image_thumbnail = ImageSpecField(
		source='image', # 원본 ImageField 이름
        processors=[Thumbnail(200,300)], #가로 세로
        format='JPEG' #
        options={'quality:60'} #원본 퀄리티의 몇%로 유지할 것인가?
        )
    ...
```

