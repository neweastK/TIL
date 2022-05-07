# CSS layout

## Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 **인라인 요소들이** 주변을 wrapping 하도록 함

- 한 요소가 normal flow로부터 빠져나와 **텍스트 및 인라인 요소가** 그 주위를 감싸도록 함.

- 그 요소가 감싸는 것이 아니고 그 요소를 감싸는 것이기 때문에 하위 요소들에 적용이 될 것

  

#### 속성

- none : 기본값

- left : 요소를 왼쪽으로 띄움

- right : 요소를 오른쪽으로 띄움

- 한글 문서 상의 어울림 설정과 같은 역할

- `float : 속성 ` 형식으로 스타일 지정

  

#### Clearing Flot

- Float는 Noraml Flow에서 벗어나있는 상태

- 따라서, 이후 요소에 대하여 Float 속성이 적용되지 않도록 clearing이 필수

- ::after : 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성

  - 보통 content 속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 사용

- clear 속성 부여 코드

  ```css
  .clearfix::after{
      content: "";
      display: block;
      clear: both
  }
  <!-- clearfix의 경우 임의로 지은 이름일 뿐 다른 이름을 사용해도 작동이 됨 -->
  ```

- clear 속성은 부모 요소에게 부여해야함. 부여한 요소가 끝나는 순간 float으로 인한 영향이 사라짐

- 사용 예시

  ```html
  <style>
      .box1 {
          font-size:10px;
          background-color:red;
          width: 100px;
          height: 100px;
      }
  
      .box2 {
          background-color: green;
          width: 300px;
          height: 100px;
      }
  
      .box3 {
          background-color: blue;
          width: 100px;
          height: 100px;
      }
      .left{
          float: left;
      }
  
      .news-container::after{
          content: "";
          display: block;
          clear: both;
      }
      
  </style>
  <body>
    <div class="news-container">
      <div class="box1 left">A일보</div>
  	  <div class="box1 left">B일보</div>
      <div class="box2">lorem1000</div>
      <div class="box3">추천 블로그</div>
    </div>
  
    <p style="color: aqua;">lorem300</p>
  </body>
  ```

  - box1 에는 left float이 적용되고 box2의 텍스트는 float으로 인해 box1 옆으로 감.
  - box3은 news-container 클래스 이후이므로 아무런 영향X. (설령 box1 옆에 빈 자리가 있어도 올라가지 않음)
  - 텍스트 및 인라인 요소는 float된 요소의 원래 위치에 있지 못하게 되며 그 위치가 아닌 곳 중 본인이 속해있는 요소의 위치에서 float된 요소를 감싼다.



## Flexbox

> 수직 정렬과 아이템의 너비와 높이 혹은 간격을 동일하게 배치하는데 매우 용이함

- 행과 열 형태로 아이템을 배치하는 1차원 레이아웃 모델

- display 속성의 속성값으로 설정 `display : flex;`

- 축

  - main axis (메인 축)
  - cross axis (교차 축)

- 구성 요소(content)

  - Flex Container (부모 요소)
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - Flex Item 들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex로 지정
  - Flex Item (자식 요소)
    - 컨테이너에 속해 있는 컨텐츠(박스)
    - 따로 display 속성을 지정해주지 않음
  - 즉, flex를 적용할 하나의 박스(flex container)를 만들고 그 안에 여러 컨텐츠(flex item)를 넣는 것
  - flex item들의 크기는 flex 박스 안에서 변할 수도 있고 변하지 않을 수도 있기 때문에 원하는 크기로 고정시키는 것은 매우 어려움.

- 예시

  ```css
  <style>
  .flex_container {
      width: 120px;
      height: 80px;
      border: 1px solid black;
      background-color: rgb(248,237,227);
      display: flex;
      justify-content: center;
      align-items: center;
  }
  
  .flex_item {
      background-color: rgb(189,210,182);
      border: 1px dotted rgb(121,135,119);
      text-align: center;
      margin: 3px;
      width: 30px;
  }
  
  <div class="flex_container"> #flex 박스를 생성한 것
  	<div class="flex_item">1</div> #flex item들 생성
  	<div class="flex_item">2</div> #flex item들 생성
  	<div class="flex_item">3</div> #flex item들 생성
  	<div class="flex_item">4</div> #flex item들 생성
  
  </div>
  ```

  

#### 속성

##### flex-direction

- Main axis 기준 방향 설정
- 역박향의 경우 html 태그 선언 순서와 시각적으로 다르니 유의
- row(기본값, 행 기준)
  row-reverse (행 역방향 기준)
  column (열 기준)
  column-reverse (열 역방향 기준)



##### flex-wrap

- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 기본적으로 컨테이너 영역을 벗어나지 않도록 함
- wrap(영역을 벗어나면 그 다음 줄로 배치)
  nowrap(기본값, 한 줄에 전부 배치, 컨테이너 영역을 벗어나기도 함)
  wrap-reverse(wrap과 같지만 요소가 나열되는 시작점과 끝점의 기준이 반대로 배치)



##### flex-flow

- flex-direction 과 flex-wrap의 shorthand
- flex-direction 과 flex-wrap에 대한 설정 값을 차례로 작성
- ex) `flex-flow: row nowrap;`



##### justify-content

- Main axis를 기준으로 공간 배분 (공간을 어디에 둘 것인가)
- flex-start, flex-end, center, space-between,space-around,space-evenly 



##### align-content

- Cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인할 수 없음)
- item 들을 교차축 지준으로 어디에 둘지 결정하는 것
- flex-start, flex-end, center, space-between, space-around, space-evenly
  

※ flex-start(기본값) : 아이템들을 axis 시작점으로
    flex-end : 아이템들을 axis 끝 쪽으로
    center : 아이템들을 axis 중앙으로
    space-between : 아이템 사이의 간격을 균일하게 분배 (좌우측 끝 여백 x)
    space-around : 아이템간 간격을 균일하게 분배 (좌우측 여백 고려 x)
    space-evenly : 좌우측 여백을 포함한 아이템 간 간격을 균일하게 분배



##### align-items

- 모든 아이템을 Cross axis를 기준으로 정렬
- stretch, flex-start, flex-end, center, baseline
- align-content와의 차이점은 공간 배분인지 아이템 정렬인지의 차이
  align-items 는 **자신들의 공간 내에서 정렬**이 됨. (아이템이 2줄 이상일 때 비교해보면 수월하게 확인 가능)



※ 사용 예시

```css
example {
    display: flex;
    flex-directrion: column;
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: space-around;
}
```





##### align-self

- 개별 아이템을 Cross axis 기준으로 정렬
- 컨테이너에 적용하는 것이 아니라 **개별 아이템에 적용**하는 속성
- stretch, flex-start, flex-end, center



※ stretch(기본값) : 컨테이너를 가득 채움
    flex-start : 위
    flex-end : 아래
    cneter : 가운데
    baseline : 텍스트 baseline에 기준선을 맞춤



##### flex-grow

- 속성을 지정한 클래스에 남은 영역을 분배
- 컨테이너가 아닌 개별 아이템에 적용



##### order

- 배치 순서
- 모든 item들의 기본 order값은 0
  따라서, 특정 item을 앞으로 옮겨주고 싶다면 order 값을 음수로, 뒤로 옮기고 싶다면 order값을 양수로 설정하면 위치 변동
- 컨테이너가 아닌 개별 아이템에 적용





## Bootstrap

>트위터(Twitter)에서 개발한 웹 사이트를 쉽게 만들 수 있게 도와주는 HTML, CSS, JS 프레임워크다. 
>
>한 CSS로 다양한 기기에서 작동하며 여러 기능을 제공해 사용자가 쉽게 웹 사이트를 제작하고 유지, 보수할 수 있게 도와준다. 



#### 시작하기

- bootstrap 파일을 다운 받아서 css 불러오듯 사용할 수도 있고, CDN을 활용할 수도 있음

  ```html
  <link rel="stylesheet" href="bootstrap.css"> #부트스트랩 파일 불러오기
  ```

  ```html
  <link rel="stylesheet" href="bootstrap.css"> #CDN 활용(head 맨 밑에)
  <script src="bootstrap.bundle.js"> #(body 맨 밑에)
  ```

  - CDN 사용의 경우 link 태그는 head 맨 밑에, script 태그를 body 맨 밑에 사용

  - link 태그 = bootstrap css cdn / script 태그 = bootstrap js cdn

    ※ CDN : 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템 
    				CDN(콘텐츠 전송 네트워크)은 지리적으로 분산된 여러 개의 서버

- 속성 사용 : `class="속성1 속성2"` 형식으로 사용




### 속성 

#### Spacing 속성

| 속성 | 기능        | 속성    | 기능           |
| ---- | ----------- | ------- | -------------- |
| m    | margin      | 값 지정 |                |
| p    | padding     | -0      | 0 rem = 0px    |
| t-   | top         | -1      | 0.25 rem = 4px |
| b-   | bottom      | -2      | 0.5 rem = 8px  |
| s-   | left(start) | -3      | 1 rem = 16px   |
| e-   | end         | -4      | 1.5 rem = 24px |
| x-   | left, right | -5      | 3 rem = 48px   |
| y-   | top,bottom  | -auto   | 정렬           |

- 활용 예시

  ```html
  <h2>Spacing</h2>
  <div class="box mt-3 ms-5">margin-top3</div>
  <div class="box m-4">margin 4</div>
  <div class="box mx-auto">mx-auto, 가운데 정렬</div>
  ```

  

#### Color 속성

| 속성       | 기능             |
| ---------- | ---------------- |
| bg-        | background color |
| text-      | text-color       |
| -primary   | 파랑색           |
| -secondary | 회색             |
| -danger    | 빨강색           |
| -success   | 초록색           |

- 활용 예시

```html
<h2>Color</h2>
<div class="bg-primary">파랑색 배경</div>
<div class="bg-danger">빨강색 배경</div>
<p class="text-success">초록색 글씨</p>
<p class="text-secondary">회색 글씨</p>
```



#### Text 속성

| 속성                 | 기능                 | 속성   | 기능                 |
| -------------------- | -------------------- | ------ | -------------------- |
| fw                   | font weight          | bold   | 굵은 두께            |
|                      |                      | normal | 기본 두께            |
|                      |                      | light  | 얇은 두께            |
| fst                  | font style           | italic | 기울임체             |
| text                 | text-location        | start  | text를 왼쪽에 배치   |
|                      |                      | center | text를 가운데에 배치 |
|                      |                      | end    | text를 오른쪽에 배치 |
| text-decoration-none | 하이퍼링크 밑줄 삭제 |        |                      |

- 활용 예시

```html
<p class="text-start">Start aligned text on all viewport sizes</p>
<p class="text-start">Start aligned text on all viewport sizes</p>
<p class="fw-bold">Bold text</p>
<p class="fw-normal">Normal weight text</p>
<p class="fst-italic">Italic text</p>
```



#### Display 속성

| 속성     | 기능                      |
| -------- | ------------------------- |
| d-inline | display를 인라인으로 지정 |
| d-block  | display를 블록으로 지정   |
| d-flex   | display를 flex로 지정     |
| d-none   | display를 none으로 지정   |

※d-none의 경우 d-xl-none, d-sm-none 처럼 breakpoint와 함께 자주 사용



#### Position 속성

| 속성         | 기능                        |
| ------------ | --------------------------- |
| fixed-top    | 상단 고정                   |
| fixed-bottom | 하단 고정                   |
| sticky-top   | 상단 고정(자신의 자리 유지) |

- fixed top vs sticky top : fixed top은 normal flow에서 벗어나기 때문에 아래 요소가 위로 말려 들어감 stick top은 자신의 자리 유지

  

#### Flexbox 

- d-flex 속성을 지정하여 설정
- flex 지정 후 justify-content, align-items 등의 flex 속성 활용 가능
- 활용 예시

```html
<div class="d-flex justify-content-start">...</div>
<div class="d-flex align-content-start">...</div>
<div class="d-flex">
    <div class="align-self-start">Aligned flex item</div>
</div>
```



#### 기타 속성





## Responsive Web Design (반응형 웹 디자인)

> 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 디스플레이의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹페이지 접근 기법 (출처: 위키백과)
>
> 웹 디자인 기법 중 하나. 디바이스의 디스플레이의 종류에 반응하여 그에 맞도록 적절하게 UI 요소들이 유기적으로 배치되도록 설계된 웹을 말한다. (출처: 나무위키)

- 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식
- 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는 용어
- Flexbox, Bootstrap Grid System 등이 있음.



#### 웹 페이지 디자인 형태

- 고정폭 레이아웃 : 브라우저의 크기가 변화하더라도 컨텐츠가 변화하지 않음

- 유동적 레이아웃 : 이미지 및 글씨 등의 영역이 유동적으로 변화함

- 별도의 사이트 생성 : 디바이스에 따른 별도의 사이트(도메인)으로 구분됨. ex) 네이버 pc 버전 / 모바일 버전 분리

- 반응형 레이아웃 : 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 디스플레이의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹페이지 접근 기법 

  - 반응형 레이아웃은 미디어 쿼리를 활용하여 CSS 작성 가능

  

#### Media Query

> CSS에서 @media 키워드를 활용하여 브라우저 및 디바이스 등 환경에 따라 CSS를 적용할 수 있는 방법



- media-type : all, print, screen, speech

- media-feature-rule : orientation, width, height 등

  - orientation : landscape(가로 모드일 때의 스타일 지정), portrait(세로 모드일 때의 스타일 지정)

  - width: 너비가 지정값일 때 사용할 스타일 지정

  - min-width : 너비가 지정값 이상의 크기일 때 사용할 스타일 지정

  - max-width : 너비가 지정값 이하의 크기일 때 사용할 스타일 지정

  - max-height, min-height를 통해 높이를 기준으로 스타일을 지정할 수도 있음.

  - 두 조건을 동시에 활용할 수도 있음 

    ```css
    /* 두 조건이 모두 만족할 때 (and) */
    @media (max-height: 500px) and (max-width: 500px) {
        h5 {
            color: rosybrown;
        }		
    }
    
    /* 두 조건중 하나라도 만족할 때 (or) */
    @media (max-height: 500px), (max-width: 500px) {
        p{
            color: green
        }
    }
    ```

    



#### Bootstrap Grid System

- 요소들의 디자인과 배치에 도움을 주는 시스템
- flexbox로 제작되었음
- 기본 요소
  - Column : 실제 컨텐츠를 포함하는 부분 (12개로 이루어져있음)
  - Gutter : 컬럼과 컬럼 사이의 공간 (사이 간격을 의미)
  - Container : 컬럼들을 담고 있는 공간
  - breakpoint : 반응형 설정을 위한 viewport 사이즈 기준 (6개 구성)



- 사용방법
  - container 클래스를 사용하여 container 박스를 생성
  - container 박스 내에서 row 클래스를 지정하면 row클래스 하위의 박스들은 grid system 적용 
  - row 클래스의 display는 flex
  - Grid 안에 또 다른 Grid를 생성하고 싶다면 row 박스 내에서 한번 더 row 클래스를 지정하여 새로운 하위 박스 생성 (=nesting)



- breakpoints

  - 반응형으로 설정하기 위해서는 viewport 사이즈에 따라 변동되도록 breakpoint 설정 필요

  | 옵션 | 기능                          |
  | ---- | ----------------------------- |
  | xs   | viewport가 576px 보다 작을 때 |
  | sm   | viewport가 576px 보다 클 때   |
  | md   | viewport가 768px 보다 클 때   |
  | lg   | viewport가 992px 보다 클 때   |
  | xl   | viewport가 1200px 보다 클 때  |
  | xxl  | viewport가 1400px 보다 클 때  |

  - 사용예시

    - col-<u>(a)</u>-<u>(b)</u>  →  a : breakpoint (sm, md, lg, xl, xxl)  /  b : column 개수 (12까지)

    - breakpoint와 칸의 개수 없이 col만 사용하면 요소들을 등분

    - ```html
      <div class="item col-4 col-sm-3 col-md-6">숫자는 컬럼 개수를 의미</div>
      ```

      → 해당 요소는 viewport가 576px보다 작을 때는 4칸, 576px보다 클 때는 3칸, 768px 보다 클 때는 6칸을 차지하도록 한다.



- offset
  - Grid system 상에서 왼쪽에 빈칸을 두고 싶을 때 사용
  - 사용예시 : offset(-breakpoint)-숫자(빈칸의 개수)
  - 오른쪽 빈칸을 원할 경우 12개보다 숫자를 낮추면 됨.





## 기타 CSS 요소

### Favicon(favorite icon)

- 사이트를 대표하는 아이콘으로 브라우저 주소창, 탭, 북마크 바 등에 표시됨
- 사용자가 웹 사이트를 쉽게 시각적으로 식별하는데 사용되며, 일반적으로 브랜드 로고와 동일한 것으로 사용
- 사용예시

```html
<link rel="apple-touch-icon" sizes="180*180" href="/apple-touch-icon,png">
<link rel="icon" type="image/png" sizes="32*32" href="/favicon-32x32.png">

#link 태그이기 때문에 <head> 안에 작성해야함
```

- favicon 생성기를 통해 favicon을 쉽게 생성 (https://favicon.io)
  - 생성된 이미지를 프로젝트 폴더 내에 images 폴더를 하나 만들고, link 태그 코드를 복사하여 사용하면 됨.



### Icon

- 일반적인 웹 사이트에서 활용되는 아이콘은 이미지가 아닌 i 태그로 구성되어 있음
- Icon 제공 사이트
  - Font Awesome
    - https://cdnjs.com/libraries/font-awesome 에서 cdn을 복사하여 사용
    - 이후 font awesome 사이트에서 icon을 고른 후 코드 복사 후 사용
    - 이미지가 아닌 아이콘을 쓸 경우, style을 활용하여 색변경도 가능하고 사이즈 조정도 쉬움(`font_size:` or `fa-사이즈` 활용)



### Font

- 개발자 pc에 있는 font를 사용할 경우 해당 font를 갖고 있지 않은 PC에서는 해당 글꼴이 보이지 않음.

- Font 제공 사이트

  - Google Font

    - 원하는 font를 모두 담은 후 CDN 코드 복사 및 추가

    - 이후 해당 글꼴 관련 코드를 style 지정에 사용

      

      
