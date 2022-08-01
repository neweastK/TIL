# JavaScript with NomadCoders

## Section 1

- Js 는 브라우저 내부에 이미 존재하고 있음

  - 브라우저만 있다면 어떠한 것들을 작성하거나 설치할 필요가 없음

- 브라우저는 HTML을 열고, HTML은 CSS와 JS를 가져옴

  - CSS파일이나 JS를 브라우저에서 열지 않음

  - HTML에서 CSS와 JS 가져오기

    - CSS : head 태그 맨 마지막 부분에 

      ```html
      <link rel='stylesheet' href='style.css'>
      ```

    - JS : body 태그 맨 마지막 부분에

      ```html
      <script src='app.js'></script>
      ```

      

- const vs let
  - const로 생성한 변수는 값을 업데이트 할 수 없음
  - let으로 생성한 변수는 값을 바꿀 수 있음
  - 과거에는 오직 var만 있음
    - var은 원한다면 어디서든 업데이트 가능
    - 너무 많은 웹사이트가 이전 버전의 JS를 사용하고 있기 때문에 JS는 업데이트가 불가함
    - 많은 웹사이트 모두가 수정할 수 없기 때문
  - 기본적으로는 const를 사용하되 변수를 추후에 업데이트 하고 싶은 경우에는 let을 쓸 것
  - 만약 const로 array나 object를 생성했을 때라면, array나 object 내의 무언가를 수정한다고 오류가 생기지는 않음.
    단, 객체 자체를 바꿀 경우 오류 발생 (예를 들어 객체를 String으로 바꾼다, 아예 다른 객체로 생성한다 등)



- null vs  undefined
  - null : 변수에 아무것도 없다 
    - false와 다름. false는 해당 변수에 false라는 값이 존재하는 것이고 null은 어떠한 값도 존재하지 않는 것
  - undefined : 변수는 존재하나 정의되지 않음
    - 컴퓨터 메모리 안에는 존재함. 즉, 공간은 있는데 값이 들어가지 않은 것
  - null은 자연적으로 생기는 것이 아니며, 우리가 변수 안에 어떤 것도 없다는 것을 확실히 하기 위해 사용하는 것.
    - 즉, 값이 주어졌는데 그 값이 '비어있음'인 것
  - undefined는 변수가 존재하지만 값이 주어지지 않은 것



- array에 데이터 추가하기 = push

- prompt(문자열)  = 창을 띄워서 인자에 넣은 문자열을 보여주고 사용자로부터 입력값을 받음

  - 입력값을 받을 때까지 다음 코드로 넘어가지 않고 대기함
  - 그래서 사용하지 않음(대신 CSS나 HTML로 직접 입력값을 받도록 함)
  - 받은 입력값을 반환

- typeof 변수 = 변수의 타입 반환

  - 괄호나, `=` 없이 한칸의 공백으로만 변수와 구분
  - typeof(변수) 로 사용할 수도 있음

- parseInt(문자열) 

  - string 객체를 number로 변환해줌
  - string 객체의 내용이 숫자가 아니면 NaN 반환

- isNan(인자) 

  - 반환값이 True면 인자로 들어간 값의 타입이 숫자가 아니라는 뜻

    False면 인자로 들어간 값의 타입이 숫자라는 뜻

- if

  ```js
  if (condition1) {
      /// condition1 === true 이면 실행될 코드
  } else if (condition2) {
      /// condition1 === false이고
      /// condition2 === true 일 때 실행될 코드
  } else {
      /// condition1,2 === false 이면 실행될 코드
  }
  ```

  - else가 없으면 condition이 거짓일 때 아무것도 실행하지 않음

  - condition은 boolean으로 표현 될 수 있어야함

  - 하나의 조건문에서 여러 조건 설정하기

    - AND

      ```js
      if (condition1 && condition2) {}
      ```

    - OR

      ```js
      if (condition1 || condition2) {}
      ```

      

## Section 2

- console에 document를 입력하면 내가 작성한 HTML 파일 (JS와 연결된)을 확인할 수 있음
- console.dir(document)   명령어로 HTML document object를 JS 관점에서 확인 가능
  - `console.dir`은 요소를 더 상세하게(요소의 내부를) 보여주는 역할 수행
- 이를 통해 JS에서 HTML document 객체로부터 각종 정보를 갖고 올 수 있고, 변경도 가능함
  - ex) document.title, document.body ...
  - console에서 변경할 경우 새로고침시 원래대로 돌아옴. 따라서, JS 파일에서 수정해줘야함



#### HTML 요소 가져와서 고치기

##### HTML을 JS에서 읽어오기

```javascript
document.getElementById(원하는 HTML 요소의 id값)
document.getElementsByClassName(원하는 HTML 요소의 클래스명)
document.querySelector(css 태그) /// element를 css 방법으로 호출할 수 있음 
document.querySelectorAll(css 태그) /// 조건에 부합하는 모든 element 호출
```

- querySelector는 만약 여러 요소가 같은 조건에 해당하면 조건에 해당하는 가장 첫번째 요소만 가져옴
  - 모든 요소를 갖고 싶다면 querySelectorAll 사용
- getElementsBy... 함수는 array에 조건에 부합하는 모든 요소를 담아서 반환
- getElement... 보다는 거의 대부분 querySelector 사용 (getElement... 의 모든 것들을 사용할 수 있기 때문)



##### ※ Point!

- document는 HTML이 app.js를 load 하고 있기 때문에 존재할 수 있음
- 그리고, 브라우저가 우리에게 document에 접근할 수 있게 해주는 것



- console.dir(object) 를 통해 element의 상세 내용을 확인해보고 어떤 것을 수정할지 선택
  - ex) element.style.color = ~~~ 를 통해서 해당 요소의 색을 지정할 수 있음



##### event 듣기

```js
element.addEventListener(event, function)
```

- element에 event가 발생하면 function을 실행시킨다는 것

- 함수 이름만 넘겨줌으로써 실행은 Js에게 맡기는 것
  - 내가 직접 실행시키면 안됨!
  
- event 검색하는 법
  
  1. mdn 페이지 활용
  
  - 찾고싶은 태그를 mdn에서 탐색
  - `태그-Web APIs`를 제목으로 하는 mdn 홈페이지로 이동 (JS 관점에서 설명한 태그)
  - HTML elements가 아닌 상위 Element 박스 클릭
  - 페이지에 해당 태그에서 사용할 수 있는 모든 event 확인 가능(사용할 때는 on을 제외하고 사용)
    - onclick은 click
    - onmouseleave는 mouseleave
  
  2. console.dir 활용
  
  - 선택된 태그를 console.dir로 출력할 경우 event 확인 가능
  - on이 붙은 모든 것들이 해당 태그에서 사용할 수 있는 event

- event 활용법은 기본적으로 2가지

  ```javascript
  title.addEventListener("click", function1)
  title.onclick = function1
  /// 위 두 코드는 완전히 동일한 작업 수행
  ```

  - addEventListener 는 나중에 removeEventListener로 삭제할 수 있다는 장점이 있음



##### window 활용하기

- window는 document와 같이 javascript에서 기본적으로 제공
  - wifi 연결 상태, 화면 사이즈 변경 등과 같은 다양한 이벤트 존재

  - window도 해당 이벤트를 활용할 수 있음
  
    ```js
    window.addEventListener('resize', funtion1)
    ```
  
  - 관련 이벤트는 mdn에서 탐색 가능
  
- document의 head, body, title 등과 같은 태그는 querySelector 없이 바로 접근 가능
  - document.body.style~~
  - document.title~~
  - but div, span 등과 같은 일반적인 태그는 반드시 querySelector 등을 통해 가져와야함



##### event와 css

> JavaScript에서 직접 style을 변경해주는 것은 그닥 바람직하지 않음
>
> → CSS를 통해서 style을 변경해주는 것이 가장 바람직함
> → style은 CSS로 animaition은 JS로 설정하자!

```html
<!-- index.html -->
<head>
    ...
    <link rel='stylesheet' href='style.css' />
</head>
```

- css 파일을 import 해오는 방법
- import 하면 css 파일에 있는 스타일들 지정 가능

1. css에 원하는 스타일 작성 (클래스 활용, 태그 활용 등등)

2. 만약 class를 활용하여 스타일을 작성했다면?

   - Ex

     ```css
     .active {
         color : tomato;
     }
     ```

3. javascript에서 원하는 행동 혹은 상황에 클래스를 추가

   ```javascript
   title.className = "active"
   ```

   - 이미 기존에 class가 있던 상태에서는 덮어쓰기가 되어버림
     - className이 아닌 classList를 활용 
   
     - 다양한 메서드 활용 가능
   
       ```javascript
       element.classList.contains(~~~)
       /// ~~~ 라는 클래스가 element(html태그)의 클래스리스트 안에 있는지 확인
       element.classList.remove(~~~)
       /// element(html태그)의 클래스리스트에서 ~~~라는 클래스 제거
       element.classList.add(~~~)
       /// element(html태그)의 클래스리스트에 ~~~라는 클래스 추가
       ```
   
     - toggle 메서드
   
       ```javascript
       element.classList.toggle('---')
       ```
   
       - 특정 element의 classList에 ---라는 클래스가 이미 있는지 확인하고 **있다면 제거해주고 없다면 추가해줌**
   
       ```js
       if (h1.classList.contains(someClass)){
           h1.classList.remove(someClass)
       } else {
           h1.classList.add(someClass)
       }
       
       // 위 코드와 아래 코드는 동일한 역할 수행
       h1.classList.toggle(someClass)
       ```
   
       

