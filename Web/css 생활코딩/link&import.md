# link & import

> 중복 작업을 방지하기 위한 방법

- 동일한 스타일이 여러 페이지에 적용될 경우, 반복적인 작업 없이 모든 스타일을 적용하는 방법

- `.css` 의 확장자를 가진 파일 생성

  - 해당 파일에 적용할 css 생성
    - 아무런 작업 없이 css 코드만 작성하면 됨
    - header, style 태그 아무 것도 필요없이 바로 선택자가 들어가면 됨

- link 태그 사용시

  - 그 후, 해당 css를 적용시킬 페이지 파일에 link 태그 작성 (href에 css파일 위치 작성)

    ```html
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
    ```

  - link의 href에 해당하는 파일을 다운받고 rel에 stylesheet라고 명시되어 있기 때문에 해당 파일을 css 문법에 맞게 해석함

- import 태그 사용시

  - style 태그 안에 import 하여 사용

    ```html
    <style>
    	@import url("style.css")
    </style>
    ```

  - 하나의 css 파일 내에서 다른 css 파일을 import 해올 수도 있음

- 즉, link는 html 태그를 이용해서, import는 style 태그 안에서 사용한다는 차이가 있음



# minify (경량화)

## clean css 

- clean css를 사용하여 코드를 경량화 시킬 수 있음
- 줄바꿈, 의미없는 프로퍼티 등을 제거해서 코드를 최소한으로 줄임
- 주로 파일명은 .css 확장자 앞에 .min을 붙임

#### 명령어로 실행

- `npm install -g clean-css`
  - permission denied 가 뜨면 sudo 를 붙여줄 것
- `cleancss -o [저장될파일명] [최소화시킬파일]`
  - 예시
    - `cleancss -o minify.min.css minify.css`



# 전처리기(Preprocessor)

> css의 표준화된 기능에 기대지않고 특정한 사람들이 만든 문법에 따라 css를 사용할 수 있도록 한 것

- 기본적으로 css에서 사용할 수 없는 것들을 실행 가능
- 크게 두 가지로 구성되어있음.
  - 해당 preproceesor의 문법
  - 순수 css 문법으로 변환시켜줄 컴파일러
- lesscss, sass 등이 있음
- 따로 사용법 찾아봐야함
- styleus의 경우, 해당 스타일 컴파일러를 에디터 extension에서 다운받아서 사용
  - .styl 확장자를 가진 파일을 생성 후 해당 파일에 styleus 문법에 맞게 css 작성
  - 그 후, 주석으로 옵션과 저장할 파일명을 지정 후 저장
    - 해당 파일명으로 css 파일이 생성됨
  - minify 기능도 제공함
  - 에디터에서 확장 기능을 제공하지 않는 경우, bash 명령어로 사용 가능

