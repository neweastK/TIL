# Property

## font

#### font-size

- 단위
  - 사용자가 브라우저의 글꼴 크기를 변경했을 때, px는 변경이 되지 않고, rem은 변경됨
  - rem은 html 태그(==root HTML)의 font-size와 비례하는 단위

#### color

- 색상을 지정하는 속성

- 이름

  > font 뿐 아니라 배경, 테두리 등 다른 색상 표현시에도 아래와 같이 사용됨

  - color name : `red`, `blue` 등 색상의 이름을 직접 지정
    - [w3schools](https://www.w3schools.com/colors/colors_names.asp) 에서 컬러 확인 가능
  - hex : 16진수 방법으로 색상 표현
  - rgb : red, green, blue 세가지 색상으로 다양한 색상 표현 
    - rgba 로 투명도까지 지정 가능
    - `color:rgb(red,green,blue)` 와 같이 표현

#### text-align 

> 텍스트를 정렬하는 방법

- `text-align: right` : 오른쪽 정렬
- `text-align: center` : 가운데 정렬
- `text-align: left` : 왼쪽 정렬
- `text-align: justify` : 양쪽 정렬

#### font-family

> 글꼴을 지정하는 방법

- 글꼴 이름에 띄어쓰기가 있으면 반드시 큰따옴표로 묶어준다
- 쉼표로 구분하여 여러가지 글꼴을 넣어놓으면, 사용자 pc에 맨 앞 글꼴이 없을 경우 다음 글꼴을, 그 글꼴도 없을 경우 그 다음 글꼴을 보여준다.
- 따라서, 맨 마지막에는 가장 포괄적인 어느 pc에나 있을법한 폰트를 지정한다. (영어에 한정)
  - serif : 장식이 있는 폰트 
  - sans-serif : 장식이 없는 폰트
  - cursive : 흘림체
  - fantasy : 옛글씨체 (중세시대 필체)
  - monospace : 고정폭 서체 
    - 가변폭은 글자마다 폭이 다르게 지정되는 것, 고정폭은 모두 같은 폭을 갖게 되는 것

#### line-height

> 줄간격 설정

- 기본값은 1.2
  - 특정 단위를 사용하지 않으면 폰트 사이즈의 n배만큼 줄간격이 떨어진다

#### font

> 위 모든 properties 들을 한번에 지정 가능

- 순서

  - font-style, font-variant, font-weight, font-size/line-height, font-family|icon|...
  - 위 순서대로 지정해줘야함

- 예시

  ```css
  p {
      font: bold 5rem/2 arial, verdana 
  }
  ```



### web font

> 사용자에게 css에서 사용된 폰트가 없으면 해당 폰트를 브라우저가 다운 받아서 사용할 수 있도록 하는 것
>
> 한글 폰트의 경우 용량이 크다는 점이 문제가 됨

- google fonts 는 대표적인 web font 사이트
- 만약 (특히, 한글 글꼴) 원하는 글꼴이 google fonts에 없다면, web-font-generator 에서 원하는 글꼴 파일을 web-font 파일로 만들어 사용한다.
  - 만들어진 파일에서 preview.html 에서 보면 해당 web font 파일을 사용하는 방법을 알 수 있음
  - style 태그 아래 `@font-face` 로 사용할 web font 파일에 대한 내용들을 작성하고 html에서 사용



## inheritance

> 상속 : 부모의 속성을 자식 태그들이 물려 받는 것

- css에는 상속되는 속성과 상속되지 않는 속성이 구분되어 있음
  - 따라서, 각 속성별로 상속 가능 여부를 확인해봐야함
  - 상속되는 속성은 자식 태그에서 따로 지정하지 않아도 해당 속성이 저절로 적용됨



## Cascading

> 하나의 웹페이지에 웹 브라우저의 기본 디자인, 사용자가 원하는 디자인, 컨텐츠 생성자가 적용한 디자인 모두를 적용하기 위해서는 우선순위 필요
>
> 동일한 태그에 여러 스타일이 적용되었을 때 웹브라우저는 어떤 스타일을 우선적으로 적용할 것인가?

- 기본 규칙
  $$
  웹브라우저 < 사용자 < 저자
  $$

  - 동일한 태그에 속성을 지정했을 경우 저자가 지정한 속성이 우선적으로 적용됨
  - 사용자가 디자인을 적용하는 경우는 매우 적음

  

- 스타일 지정 방법 우선순위
  $$
  !important>인라인 > id > class|attribute|pseudo > 태그
  $$

  - 하나의 태그에 스타일이 중첩 적용 되어있을 때, 어떤 것을 우선적으로 적용할 것인가?

![img](https://stuffandnonsense.co.uk/archives/images/css-specificity-wars.png)



## Brackets

> html과 css를 훨씬 더 편리하게 사용할 수 있는 프로그램

- emmet extension을 설치하여 활용 가능

  - `html>body>ul>li` 와 같이 한줄로 코드 작성 가능

    - 결과물

      ```css
      <html>
      <body>
      	<ul>
      		<li></li>
      	</ul>
      </body>
      </html>
      ```

  - `li*3` 과 같이 한번에 여러 태그 생성 가능

    - 결과물

      ```css
      <li></li>
      <li></li>
      <li></li>
      ```

- emmet 공식문서 존재 [이동](docs.emmet.io)

  - emmet이라는 체계에 대한 설명 확인 가능
  - 여러 단축된 코드가 있어서 사용하기 용이함

- emmet에서는 저장된 포토샵 파일을 레이어 단위로 분리하여 해당 레이어에 대한 코드 힌트 제공



## display

### inline

- 자신과 자신을 둘러싸고 있는 태그들과 같은 줄에 위치하는 태그
- 해당 줄에서 **자신의 컨텐츠 사이즈만큼만 사용**

### block

- 자신 혼자서 줄 전체를 사용하는 태그
- 각 태그별로 기본이 inline인지 block인지 확인하며 사용할 것



## Box Model

- padding
  - 테두리와 컨텐츠 사이의 간격
- margin
  - 테두리와 다른 요소들 사이의 간격
- width
  - 박스 요소의 너비 지정
- height
  - 박스 요소의 높이 지정
  - but, 높이 지정시 컨텐츠가 over 되는 경우 발생
- inline 태그 안에서는 width와 height 값을 지정해도 무시됨



### box-sizing

- width와 height 는 content의 영역만을 의미한다. 따라서, border 값이나 다른 값에 의해 영향을 받게됨
- 이를 해결하고자, box-sizing 속성을 활용한다.
- content-box (기본값)
  - 컨텐트 크기만큼 width와 height 지정
- border-box
  - border까지 포함한 사이즈를 width와 height로 판단
  - 주로, `*` 를 사용해서, 모든 태그들이 border를 기준으로 사이즈를 지정할 수 있도록 설정함



### 마진겹침

- 인접한 태그와 중복되게 margin값을 준 경우, 둘 중 더 큰 값을 기준으로 margin이 적용됨
  - 둘 다 적용되지 않음 (예를 들어, 위에 있는 box는 margin-bottom이 100px이고 아래 box의 margin-top이 50px일 경우, 위 아래 box의 margin은 150px이 아닌 100px이 된다.)

- 부모 엘리먼트와 자식 엘리먼트 모두 margin 값이 있는 경우
  - 부모 태그가 시각적으로 아무 효과가 없는 투명한 상태가 되면 자식 태그와 부모 태그의 margin 값이 합쳐지는 결과를 낳는다
  - 합쳐진 경우, 둘 중 더 큰 값을 기준으로 자식 엘리먼트에 margin이 적용됨
- 어떤 태그의 시각적인 효과가 없다면, 그 태그의 margin 값은  margin-top 값과 margin-bottom 값 중 더 큰값을 margin 값으로 갖는다 
- [마진겹침 정리 잘되어있는 블로그](https://velog.io/@raram2/CSS-%EB%A7%88%EC%A7%84-%EC%83%81%EC%87%84Margin-collapsing-%EC%9B%90%EB%A6%AC-%EC%99%84%EB%B2%BD-%EC%9D%B4%ED%95%B4)



## Position

> 엘리먼트의 위치와 관련된 속성

### offset

- left : 왼쪽으로부터 지정한 값만큼 이동
- right : 오른쪽으로부터 지정한 값만큼 이동. left와 같이 쓰이면 left가 우선 적용됨
- top : 위쪽으로부터 지정한 값만큼 이동
- bottom : 아래쪽으로부터 지정한 값만큼 이동. top과 같이 쓰이면 top이 우선 적용됨

### position

##### static (기본값) 

- 지정한 offset 값들을 모두 무시하고 자신의 원래 위치에 정적으로 위치. 
- 즉, 위치와 관련된 속성을 지정하지 않은 상태

##### relative 

- 자기 자신의 static 위치를 기준으로 지정한 offset만큼 이동

##### absolute 

- 조상 요소 중 position 속성이 static이 아닌 요소가 나오면 해당 요소를 기준으로 위치 적용
  - 끝까지 없을 경우 root HTML을 기준으로 지정한 offset만큼 이동. 
- but, absolute 속성 부여 후 offset 관련 속성을 주지 않으면 부모 엘리먼트를 기준으로 위치
  - 왜냐햐면, position이 absolute일 경우 left,right등의 offset은 본인의 원래 위치를 기본값으로 가지기 때문
- absolute 속성 부여시, 부모와의 연결 관계는 끊김
  - 따라서, 상속 받던 모든 속성들도 끊기게 됨
    - 이에 크기는 자신의 컨텐츠만큼으로 수정됨
  - 부모 요소도 자식 요소를 없는 취급한다.

##### fixed

- 스크롤과는 무관하게 지정된 위치에 계속 고정시키는 것
- absolute와 마찬가지로 부모 요소와의 관계가 끊김
  - 따라서, 크기를 따로 지정하지 않을시 자신의 content만큼으로 지정됨
  - 부모 요소는 자식 요소의 크기를 포함하지 않는다 (관계가 끊겼기 때문)



## Flex

> 페이지의 layout을 위해 사용되는 속성
>
> flex를 통해 정렬하고자 하는 태그들은 container 태그를 부모로 가져야함

- container 태그에 부여되는 속성
  - display, flex-direction, flex-wrap, flex-flow, justify-content, align-items, align-content
- item 태그에 부여되야하는 속성
  - order, flex-grow, flex-shrink, flex-basis, flex, align-self
- container 태그나 item 태그는 클래스명이나 태그명이 따로 지정되어있지 않음

#### flex 사용하기

- container 태그 스타일에 `display:flex` 부여

##### container 태그에 사용되는 속성

- flex-direction

  - 정렬 되는 조건

  - row : 행의 방향으로 정렬 (기본값)
  - row-reverse : 행의 역방향으로 정렬, container 태그의 오른쪽부터 정렬되어 여백이 왼쪽에 생김
  - column : 열의 방향으로 정렬
  - column-reverse : 열의 역방향으로 정렬, container 태그의 아래쪽부터 정렬되어 여백이 위쪽에 생김
  - flex이 item들은 기본적으로 지정한 방향으로, 부모 요소 전체만큼의 크기를 차지함

- flex-wrap

  - 컨테이너의 크기보다 아이템들의 크기가 더 큰 경우 아이템 배치를 어떻게 할 것인지 결정
  - nowrap (기본값)
    - 아이템들에 줄바꿈 없이 배치
  - wrap
    - 아이템들에 줄바꿈 적용
  - wrap-reverse
    - 위-아래 순서가 아닌 아래-위 순서로 정렬

- align-items

  - 모든 item들이 자신의 content만큼의 크기를 갖게되고 flex-direction과 반대되는 축 방향의 정렬 방법 설정(stretch 제외)
  - flex-start : flex-direction이 row이면 위쪽, column이면 왼쪽에 정렬
  - flex-end : flex-direction이 row이면 아래쪽, column이면 오른쪽에 정렬
  - center : 정중앙에 정렬
  - baseline : 각 itme의 content들의 bottom line을 모두 동일하게 맞춤
  - stretch(기본값) : flex-direction이 row이면 item들의 높이가, column이면 item들의 너비가 container의 것과 같아짐 

- justify-content

  - flex-direction에서 지정한 축 방향의 정렬 방법 설정
  - flex-start, flex-end, space-between, center, space-around 설정 가능

- align-content

  - 같은 행의 item들을 하나의 그룹으로 지정하여 각 그룹간 정렬 방법을 지정하는 것
  - 즉, 아이템들이 두 줄일 때 의미가 있음
  - 아이템 그룹의 라인 자체를 정렬하는 것

  

##### item 태그에 부여되는 속성

- flex-basis
  - 아이템 태그에 부여되는 속성
  - 지정한 방향으로의 기본 크기 지정
    - 방향이 row이면 width를, column이면 height를 지정해준다
- flex-grow
  - 아이템 태그에 부여되는 속성
  - container 태그의 여백을 꽉 채우기 위해 사용
  - 기본값은 0으로, 여백을 채우지 않음
  - 1로 지정하면 모든 아이템들이 1/n만큼의 크기를 가짐
    - 2로 지정하면 2로 지정한 아이템은 1로 지정한 아이템의 2배 사이즈를 갖는다.
    - 단, 여백의 크기 안에서 서로서로 분배하는 것
- flex-shrink
  - 아이템 태그에 부여되는 속성
  - 기본적으로 basis값을 갖고 있어야함
  - 속성값에 0을 부여할 경우, 컨테이너의 크기 아무리 작아져도 아이템 태그는 사이즈가 작아지지 않도록 함
  - 속성값이 1 이상이면, 컨테이너의 크기가 아이템 태그보다 작아질 때, 사이즈가 지정한 속성값 비율만큼 같이 작아짐
    - 예를 들어, item1은 1, item2는 2 일 경우 item2는 2/3씩 줄어들지만, item1은 1/3씩만 줄어든다
  - 위 3가지 속성은 `flex : flex-grow flex-shrink flex-basis;` 와 같이 한번에 사용 가능 
- align-self
  - 특정 item 요소만 예외적으로 다르게 정렬하고 싶을 때 사용
  - auto, flex-start, flex-end, center, baseline, stretch 설정 가능
- order
  - 특정 item들의 순서를 바꾸고 싶을 때 사용
  - 기존 코드 작성한대로 0,1,2... 로 지정되어있음
  - 따라서, -1로 설정시 가장 앞으로 이동함

#### holy grail layout

>  다음과 같은 레이아웃을 의미
>
> ​	![img](https://s3-ap-northeast-2.amazonaws.com/opentutorials-user-file/module/2367/4744.png)

- Header, Section, Footer 세개를 하나의 container 태그 안에 형제 관계로 생성
  - flex-direction은 column
- section을 또 다른 하나의 container로 설정하고, 그 안에 nav,main,ad를 생성
  - flex-direction은 row
  - nav와 ad에 flex-basis 지정 (150px 정도) 후, flex-shrink에 0 지정
  - 그러면, 전체 사이즈와 별개로 nav와 ad는 고정값이 유지되고, main 영역이 사이즈가 변동됨



## Multi Column

> 엘리먼트를 지정한 개수만큼의 다단을 생성하는 것

- column-count
  - 분할할 다단 개수 지정
  - 하나의 문단이 담겨있는 태그에 해당 속성 적용
- column-width
  - 분할할 다단의 폭 지정
  - 각 다단이 지정한 너비가 되도록 자동으로 다단 분리
  - column-count와 함께 사용되면 지정한 column-count 이하의 개수, 지정한 column-width 이상의 너비를 유지하도록 자동으로 설정함
- column-gap
  - 다단 사이의 여백 지정
- column-rule
  - 다단 사이에 생성할 선 속성 지정
  - column-rule-style : 단선, 점선 등 설정
  - column-rule-width : 너비 설정
  - column-rule-color : 구분선 색상 설정
- column-span: all
  - 본 속성을 지정한 대상은 다단에 구애받지 않고 본래 자신의 위치와 크기를 갖게됨



## float

> 기본적으로 본문에 이미지를 삽입하기 위해 고안된 속성

- 사진을 두고 싶은 위치를 속성값으로 지정
  - ex) `img{ float : right; }`

- 특정 엘리먼트에 float를 지정하면 모든 하위 엘리먼트가 해당 엘리먼트를 피해감
  - but, 피해가지 않기를 원하는 엘리먼트에는 `{ clear : both; }` 적용
  - 만약, float가 right라면 clear도 right, float가 left라면 clear도 left로 지정하면 됨
  - 상관없이 모두 지우려면 both
- float 속성이 적용된 바로 하위 엘리먼트에 또 float를 부여하면 두번째 엘리먼트는 첫번째 엘리먼트 밑으로 가지 않는다.
  - 쉽게 비유하자면, 둘 다 자존심이 세져서 누군가의 밑으로 가지 않고 서로 동등한 위치에 있다는 뜻
  - 그리고 그 다음 태그들은 사이즈에 따라 아래로 가거나 옆에 있거나 한다.



## background

> 엘리먼트의 배경을 설정하는 속성

- background-color 
  - 배경색 설정하기
- background-image 
  - 이미지로 배경 채우기
  - `{ background-image : url('이미지 주소') }` 와 같이 사용 
  - 이미지와 컬러는 동시에 적용할 수 있음.
  - 단, 이미지가 너무 크면 배경 컬러가 가려짐
- background-repeat
  - 배경에 쓰인 이미지의 반복 여부를 결정
  - no-repeat : 반복 제거
  - repeat-x : x축만 반복
  - repeat-y : y축만 반복
  - repeat : 전체 반복 (기본값)
- background-attachment 
  - 스크롤했을 때 배경 이미지도 같이 스크롤되게 할 것인지의 여부 설정
  - scroll : 함께 스크롤
  - fixed : 배경 이미지는 고정
- background-size
  - 배경의 사이즈 조절
  - cover : 화면 전체를 이미지가 덮게 함 (이미지가 잘림)
  - contain : 화면에 모든 이미지가 들어가게 함 (여백이 생김)
- background-position
  - 배경이 반복되지 않을 때, 해당 배경 이미지의 위치 조정
  - `{ background-position : left/center/right top/center/bottom }` 로 사용
- background
  - 위 모든 속성을 축약하여 적용
  - ` { background : color image repeat attachment position }` 의 순서대로 지정



## filter

> 엘리먼트에 다양한 필터 기능 적용

- [필터 확인 사이트](https://developer.mozilla.org/ko/docs/Web/CSS/filter) or `CSS fliter playground` 검색

- 필터 기능은 아직 적용이 되지 않은 브라우저가 있을 수도 있어서 Vendor Prefix와 함께 사용 (현재는 되는 것으로 추정)

- Vendor Prefix

  - 주요 웹 브라우저 공급자가 새로운 실험적인 기능을 제공할 때 이전 버전의 웹 브라우저에 그 사실을 알려주기 위해 사용하는 접두사

  - 즉, 아직 CSS 권고안에 포함되지 못한 기능 혹은 CSS 권고안에는 포함되어 있지만, 아직 완벽하게 제정된 상태가 아닌 기능을 사용할 때 사용

  - 브라우저별 벤더 프리픽스

    | 브라우저          | 벤더 프리픽스 |
    | ----------------- | ------------- |
    | Internet Explorer | -ms-          |
    | Chrome, Safari    | -webkit-      |
    | Firefox           | -moz-         |
    | Opera             | -o-           |

- 사용 예시

  ```css
  img {
      -webkit-filter: grayscale(100%);
      -o-filter: grayscale(100%);
      filter: grayscale(100%);
  }
  p {
      -webkit-filter: blur(3px);
      -o-filter: blur(3px);
      filter: blur(3px);
  }
  ```



## blend

> 여러 속성을 혼합하여 사용하는 것

- background-blend-mode
  - background 효과들간의 속성 믹싱
  - 다양한 속성 보유
  - 직접 써보고 선택하는 것이 용이
  - 어떠한 속성을 부여했을 때, background-image와 background-color 가 서로 혼합됨
- mix-blend-mode
  - content와 background 사이의 속성 블렌딩
  - mix-blend-mode 속성이 적용된 엘리먼트와 그 엘리먼트의 배경으로 존재하는 다른 이미지들과 합성하는 것
  - 따라서, 해당 속성은 배경이 아닌 content에 이 속성을 부여해야함



## Transform

- transform은 여러개의 속성값을 할당시 하나의 transform 속성에 모두 넣어야함

  - 예시

    ```css
    h1 {
        transform: scaleX(0.5) scaleY(0.5)
    }
    ```

- transform 속성은 엘리먼트의 display가 block 혹은 inline-block 일 때만 적용됨 

- 어떤 속성값이 있는지는 codepen에서 확인 가능

  - translate, skew, scale, rotate 등이 있음
  - 각각의 속성에 따라 적용하는 단위가 다르기 때문에 어떤 속성에 어떤 단위를 사용해야하는지 공식문서 확인 필요 (turn, degree, angle 등이 있음)

- transform-origin

  - 어떤 위치를 기준으로 transform 속성을 적용시킬 것인가?
  - `transform-origin: x축 y축 z축` 과 같이 사용
    - 속성값은 %, left,top 등을 사용할 수 있음

- 참고 사이트

  - css shake
  - magic animations
  - transform css library 로 검색하면 다양하게 나옴



## Transition

> 전환되는 효과를 부드럽게 적용시켜주는 것
>
> 즉, 어떠한 변경 사항을 이어져서 표현되게 하는 것

- transition-property
  - 어떠한 속성에  장면전환 효과를 적용시킬 것인가?
  - transform 속성을 할 수도 있고, font-size를 더 작게 설정하여 글자가 작아지는 전환 효과를 내기위해 font-size 속성을 지정할 수도 있음
  - 복수의 속성을 지정하고 싶으면 띄어쓰기로 구분하여 여러개 적용
  - ex) `{ transition-property : transform font-size }` 또는 `{ transition-property : all }`
- transition-duration
  - 장면 전환을 얼마동안 일어나게 할 것인가?
  - ex) 1s, 0.5s 등
- transition
  - `{ transition: transition-property transition-duration }` 으로 압축하여 사용 가능
  - `{ transition: transition-property1 transition-duration1 transition-property2 transition-duration2 }` 와 같이 여러개에 적용 가능
- transition-delay
  - 어떠한 장면 전환 효과가 시작될 때 지정한 시간만큼 지연한 후에 장면 전환 효과가 적용되도록 하는 것
- transition-timing-function
  - 어떠한 장면 전환 효과의 속도가 균일하지 않게 하는 것
  - linear  : 속도가 균일하게 적용
  - ease (기본값): 천천히 시작했다가 천천히 끝남
  - [다른 속성값들 확인 가능 사이트](https://matthewlein.com/tools/ceaser)
    - 기본 css에서 제공하지 않는 속성값은 코드를 복사해와서 사용
    - cubic-bezier를 사용한 경우가 많음
    - 여기에 Vendor Prefix를 더해준 것

