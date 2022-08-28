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
- 기본값은 content-box 
  - 컨텐트 크기만큼 width와 height 지정
- border-box
  - border까지 포함한 사이즈를 width와 height로 판단
  - 주로, `*` 를 사용해서, 모든 태그들이 border를 기준으로 사이즈를 지정할 수 있도록 설정함



### 마진겹침

- 인접한 태그와 중복되게 margin값을 준 경우, 둘 중 더 큰 값을 기준으로 margin이 적용됨
  - 둘 다 적용되지 않음 (예를 들어, 위에 있는 box는 margin-bottom이 100px이고 아래 box의 margin-top이 50px일 경우, 위 아래 box의 margin은 150px이 아닌 100px이 된다.)

