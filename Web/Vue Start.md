# Vue

[toc]

## Vue.js

- 사용자 인터페이스를 만들기 위한 진보적인 **자바스크립트 프레임워크**
- 현대적인 tool과 다양한 라이브러리를 통해 SPA를 완벽하게 지원
- 구글의 Angular 개발자 출신인 Evan You에 의해 발표 (2014)
- **html과 css로도 가능한 Front-End를 더 효과적으로 그리고 높은 품질로 개발하기 위한 프레임워크**



### SPA 

> Single Page Application (단일 페이지 애플리케이션)

- 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 애플리케이션
- 단일 페이지로 구성되며 서버로부터 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM을 구성
  - 처음 페이지를 받은 이후부터는 서버로부터 새로운 전체 페이지를 불러오는 것이 아닌, **현재 페이지 중 필요한 부분만 동적으로 다시 작성**함
- 연속되는 페이지 간의 사용자 경험(UX)을 향상 (분절 현상의 감소)
- 동작 원리의 일부가 CSR(Client Side Rendering)의 구조를 따름
- 즉, vue로 제작하게 된다면 단 한장의 html로 모든 애플리케이션을 구성할 수 있음
  - 하나의 HTML과 많은 JS를 전달하여 앱을 구성한다고 생각하면 됨
- 과거 웹 사이트들은 요청에 따라 매번 새로운 페이지를 응답하는 방식인 MPA
  - but, 스마트폰이 등장하면서 모바일 최적화의 필요성이 대두됐으며, 모바일 네이티브 앱과 같은 형태의 웹 페이지가 필요해짐
  - 이러한 문제를 해결하기 위해 Vue.js와 같은 프론트엔드 프레임워크 등장
  - 한 개의 웹 페이지에서 여러 동작이 이루어지며 모바일 앱과 비슷한 형태의 사용자 경험을 제공



### CSR과 SSR

#### CSR(Client Side Rendering)

- 서버에서 화면을 구성하는 SSR 방식과 달리 **클라이언트(=브라우저)에서 화면을 구성**
- 최초 요청시 HTML, CSS, JS 등 데이터를 제외한 각종 리소스를 응답받고 이후 클라이언트에서는 필요한 데이터만 요청해 JS로 DOM을 렌더링하는 방식
- 즉, 처음에는 뼈대만 받고 브라우저에서 동적으로 DOM을 그리며 SPA가 사용하는 렌더링 방식

- 장점 
  1. 서버와 클라이언트 간 트래픽 감소 (사용자가 오래 머무르는 경우)
     - 웹 애플리케이션에 필요한 모든 정적 리소스를 최초에 한 번 다운로드 후 이후에는 필요한 데이터만 갱신
  2. 사용자 경험(UX) 향상
     - 전체 페이지를 다시 렌더링하지 않고 변경되는 부분만을 갱신하기 때문
- 단점
  1. SSR에 비해 전체 페이지 최종 렌더링 시점이 느림
  2. SEO(검색 엔진 최적화)에 어려움이 있음 (최초 문서에 데이터 마크업이 없기 때문)
     - 검색 엔진의 스파이더 봇들은 검색할 때 마크업만 보기 때문에 마크업이 없는 CSR은 당연 불리함

<hr> ※ SEO(Search Engine Optimization)
- 웹 페이지 검색엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성해서 검색 결과의 상위에 노출될 수 있도록 하는 작업
- 인터넷 마케팅 방법 중 하나
- 구글의 등장 이후 검색엔진들이 컨텐츠의 신뢰도를 파악하는 기초 지표로 사용됨
  - 다른 웹 사이트에서 얼마나 인용되었나를 반영하며, 결국 그 횟수를 늘리는 방향으로 최적화

	<hr>

#### SSR(Server Side Rendering)

- 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식 (ex. django)
- JS 웹 프레임워크 이전에 사용되던 전통적인 렌더링 방식

- 서버가 HTML의 완성본을 사용자에게 전달
- 장점 
  1. 초기 구동 속도가 빠름. 따라서 클라이언트가 빠르게 컨텐츠를 볼 수 있음
  2. SEO(검색 엔진 최적화)에 적합
     - DOM에 이미 모든 데이터가 작성되어있기 때문
- 단점
  1. 모든 요청마다 새로운 페이지를 구성하여 전달
     - 반복되는 전체 새로고침으로 인해 사용자 경험이 떨어짐
     - 상대적으로 트래픽이 많아 서버의 부담이 클 수 있음



#### SSR vs CSR

- 두 방식의 차이는 최종 HTML 생성 주체가 누구인가에 따라 결정 (서버? 클라이언트?)
- 즉, **실제 브라우저에 그려질 HTML을 서버가 만들면 SSR, 클라이언트가 만들면 CSR이다**
-  SSR과 CSR을 단순 비교하여 '어떤 것이 좋은가'를 판단할 수 없음
- 따라서, 내 서비스 또는 프로젝트 구성에 맞는 방법을 적절하게 선택해야함



### MVVM Pattern

> 애플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴

- Vue의 디자인 패턴

#### Model

- Vue에서 Model은 JavaScript Object다
- Object === {key:value}. 즉, 객체로 이루어져있음을 의미
- Model은 Vue Instance 내부에서 **data**라는 이름으로 존재
- 이 data가 바뀌면 View(DOM)가 반응



#### View

- Vue에서 View는 DOM(HTML)이다
- Data의 변화에 따라서 바뀌는 대상



#### ViewModel

- Vue에서 ViewModel은 **모든 Vue Instance이다** 

- DOM과 Data의 중개자
  - 데이터만 변경되면 알아서 View가 변경되도록 만드는 역할
  - View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리
- ViewModel을 활용해 Data를 얼마만큼 잘 처리해서 보여줄 것인지(DOM)를 고민하는 것



####  vs Django

- DJango 
  - 데이터의 흐름대로 코드 작성
  - url → views → template
- Vue
  - Data가 변화하면 DOM이 변경
    - Data 로직 작성 (CDN 필요)
    - DOM 작성

- 결론적으로 vue는 Data만 지정 혹은 변경되면 나머지는 알아서 해결됨



### Syntax of Vue.js

#### Vue Instance

- html body 가장 아래쪽에 Vue.js CDN 삽입

  ```html
  <body>
      <script src = 'https://cdn.jsdelivr.net/npm/vue/dist/vue.js'></script>
  </body>
  ```

  

- 모든 Vue 앱은 Vue 함수로 새 인스턴스를 만드는 것부터 시작

- Vue 인스턴스를 생성할 때는 Options 객체를 전달해야함

- 인스턴스 내에서 여러 Options들을 사용하여 원하는 동작을 구현

- Vue Instance === Vue Component

- 예시

  ```javascript
  const app = new Vue({
  
  })
  ```



#### Options/DOM - 'el'

- Vue 인스턴스에 연결(=마운트)할 기존 DOM 요소 필요

- 'el' 옵션의 이름은 바꿀 수 없음 (무조건 'el'로 써야함)

- CSS 선택자 문자열 혹은 HTML Element로 작성

- new를 이용한 인스턴스 생성 때만 사용

- 예시

  ```javascript
  const app = new Vue({
  	el : '#app'
  })
  ```



#### Options/Data - 'data'

- Vue 인스턴스의 데이터 객체. Model과 같은 역할
- Vue 인스턴스의 상태 데이터를 정의하는 곳
- Vue template에서 interpolation을 통해 접근 가능
- v-bind, v-on 과 같은 directive에서도 사용 가능
- **Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능**

- 예시

  ```javascript
  const app = new Vue({
      el: '#app'
      data: {
    	  message: 'Hello',
  	}
  })
  ```

  

#### Options/Data - 'methods'

- Vue 인스턴스에 추가할 메서드
- Vue template에서 interpolation을 통해 접근 가능
- v-on과 같은 directive에서도 사용 가능
- Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능
- 주의
  - **화살표 함수를 메서드를 정의하는데 사용하면 안됨**
  - 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에, this 는 Vue 인스턴스를 가르키지 않음
    - 우리의 눈에는 특정 함수가 메서드 안에 있어서 this는 `methods`를 가르켜야할 것 같지만, 자동으로 vue가 해당 코드를 분해하기 때문에 실제로는 Vue 인스턴스를 가르키게됨

- 예시

  ```javascript
  const app = new Vue({
      el: '#app',
      data: {
          message: 'Hello',
      },
      methods: {
          greeting: function(){
              console.log('hello')
          }
      }
  })
  ```

  

#### this

- Vue 함수 객체 내에서 vue 인스턴스를 가리킴

- **data 객체나, method를 정의할 때는 화살표 함수를 사용하면 안됨**

  - this가 가리키는 대상이 달라지기 때문

- 예시

  ```vue
  <div id="app">
      <button @click='myFunc'>a</button>
  	<button @click='yourFunc'>b</button>
  </div>
  
  <script src='https:cdn.jsdelivr.net/npm/vue/dist/vue.js'></script>
  <script>
      const app = new Vue({
          el:'#app'
          data: {
         	 a: 1,
      	},
      	methods: {
           myFunc: function() {
          	console.log(this) //Vue instance
  	     },
           yourFunc: () => {
               console.log(this) //window
           }
  		}
         })
  </script>
  ```

  

### Template Syntax

- 렌더링 된 DOM을 기본 Vue 인스턴스의 데이터에 선언적으로 바인딩 할 수 있는 HTML 기반 템플릿 구문을 사용
- Interpolation 과 Direvtive가 있음



#### Interpolation(보간법)

> ※ 간단히 말하면 중괄호를 사용하여 데이터를 불러오는 것

1. Text
   - `<span>메시지: {{ msg }}</span>`
2. RawHTML
   - `<span v-html="rawHtml"></span>`
3. Attrributes
   - `<div v-bind: id="dynamicId"></div>`
4. JS 표현식
   - `{{ number +1 }}`
   - `{{ message.split('').reverse().join('') }}`



#### Direvtive(디렉티브)

- v-접두사가 있는 특수 속성
- vue한테 명령을 내리고 태그에서 다양한 일을 할 수 있게 해줌
- 속성값은 단일 JS 표현식이 됨 (v-for는 예외)
- 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 역할을 함

- 전달인자 (Argument)
  - `:`(콜론)을 통해 전달인자를 받을 수도 있다
    - 전달인자란 속성 의미 ex) v-on의 click, submit 등
- 수식어 (Modifiers)
  - `.`(점)으로 표시되는 특수 접미사
  - directive를 특별한 방법으로 바인딩 해야함을 나타냄



##### v-text

> 엘리먼트의 textContent를 업데이트

- 내부적으로 interpolation 문법이 v-text로 컴파일 됨

- 예시

  ```vue
  <body>
      <div id='app'>
          // 아래 두 코드의 결과값은 똑같음
          <p>{{ message }}</p>
          <p v-text='message'></p>
      </div>
  </body>
  
  <script src='https://cdn....'></script> //vue cdn 입력
  <script>
  	const app = new Vue({
          el: '#app',
          data: {
              message: 'Hello'
          }
      })
  </script>
  ```

  - 위 코드의 결과를 browser의 개발자도구 - elements 에서 확인해보면 코드 그대로가 아닌 p 태그 안에 'Hello' 가 들어가있음을 확인 가능
    - 브라우저가 script들을 조합으로 최종 html을 만들어냈다는 뜻 == CSR



##### v-html

> 엘리먼트의 innerHTML을 업데이트

- XSS 공격에 취약할 수 있음
- 따라서, 임의로 사용자로부터 입력 받은 내용은 v-html에 절대 사용 금지

- 예시

  ```vue
  <body>
      <div id='app'>
          // 아래 두 코드의 결과값은 똑같음 (== <strong>message</strong>)
          <p>{{ message }}</p>
          <p v-text='message'></p>
          <p v-html='message'></p> // v-html의 결과는 bold 처리가 된 message 문자열
      </div>
  </body>
  
  <script src='https://cdn....'></script> //vue cdn 입력
  <script>
  	const app = new Vue({
          el: '#app',
          data: {
              message: '<strong>Hello</strong>'
          }
      })
  </script>
  ```

  - javascript의 innerHtml과 같은 역할

    

##### v-show

- 조건부 렌더링 중 하나
- **요소는 항상 렌더링 되고 DOM에 남아있음**
- 단순히 엘리먼트에 display CSS 속성을 토글하는 것

- 예시

  ```vue
  <body>
      <div id='app'>
          <p v-show='isTrue'>True</p>
          <p v-show='isFalse'>false</p>
      </div>
  </body>
  
  <script src='https://cdn....'></script> //vue cdn 입력
  <script>
  	const app = new Vue({
          el: '#app',
          data: {
              isTrue: true,
              isFalse: false,
          }
      })
  </script>
  ```

  - `v-show=` **이후의 값이 true로 평가될 때 설정한 내부 문자열을 출력**함

  - **false일 경우 해당 코드가 문서에는 존재**하지만 display 속성을 hidden으로 설정하여 사용자의 눈에 보이지는 않음
  - **화면에서 보였다가 안보였다가를 자주 반복할 때 사용하기 좋음**

  

##### v-if, v-else-if, v-else

- 조건에 따라 요소를 렌더링

- directive의 표현식이 true일 때만 렌더링

- 엘리먼트 및 포함된 directive는 토글하는 동안 삭제되고 다시 작성됨

- 예시

  ```vue
  <body>
      <div id='app'>
          <p v-if='seen'>seen is True</p>
          <p v-else-if='myType === 'A''>A</p></p>
  	    <p v-else-if='myType === 'B''>B</p></p>
  	    <p v-else-if='myType === 'C''>C</p></p>
          <p v-else>Not A/B/C</p>
      </div>
  </body>
  
  <script src='https://cdn....'></script> //vue cdn 입력
  <script>
  	const app = new Vue({
          el: '#app',
          data: {
              seen: false,
              myType: 'A',
          }
      })
  </script>
  ```

  - 조건문을 판별한 값이 false일 경우 **아예 문서에 존재하지도 않음**(주석으로 표현됨)

    

###### v-show vs v-if

- v-show(Expensive initial load, cheap toggle)

  - CSS  display 속성을 hidden으로 만들어 토글

  - 실제로 렌더링은 되지만 눈에서 보이지 않는 것이기 때문에 딱 한번만 렌더링이 되는 경우라면 v-if에 비해 상대적으로 렌더링 비용이 높음

    - 즉 v-show 는 무조건 모든 요소를 문서에 올려놓음(설령 화면에 안보이더라도)

  - 하지만, 자주 변경되는 요소라면 한 번 렌더링 된 이후부터는 보여주는지에 대한 여부만 판단하면 되기 때문에 토글 비용이 적음

    - 즉, show는 화면에 자주 등장해야하는 요소들에 적용하면 좋음

    

- v-if(Cheap initial load, expensive toggle)

  - 전달인자가 false인 경우 렌더링 되지 않음
    - 즉, 조건에 참인 값만 문서에 올려놓음(나머지는 주석처리)
  - 화면에서 보이지 않을 뿐만 아니라 렌더링 자체가 되지 않기 때문에 렌더링 비용이 낮음
  - 하지만, 자주 변경되는 요소의 경우 다시 렌더링 해야하므로 비용이 증가할 수 있음
    - 즉, 변경되면 다시 해당 태그를 만들어서 html에 삽입해야하므로 비용이 크다는 것



##### v-for

> 원본 데이터를 기반으로 엘리먼트 또는 템플릿 블록을 여러번 렌더링

- `item in items` 구문 사용

- item 위치의 변수를 각 요소에서 사용할 수 있음

  - 요소 뿐 아니라 index를 같이 뽑고 싶은 경우
    - `(item,idx) in items` 구문 사용 
    - 반드시 index가 두번째 인자로 와야함

  - 객체의 경우 기본적으로 value를 반환하기 때문에 key를 뽑고 싶은 경우 위 idx와 같이 두번째 인자에 넣는다.
    - `(value, key) in items` 구문 사용

- v-for 사용시 반드시 key 속성을 각 요소에 작성

- v-if와 함께 사용하는 경우 v-for가 우선순위가 더 높음

  - 단, 가능하면 v-if와 v-for를 같이 사용하지 말 것

- 예시

  ```vue
  <div id="app">
      <h2>String</h2>
      <div v-for="char in myStr">
          {{ char }} // 'Hello World!'를 한글자씩 출력
      </div>
      <h2>Array</h2>
      <div v-for="fruit in fruits">
          {{ fruit }} // fruits 배열의 요소를 하나씩 출력
      </div>
      <div v-for="(fruit, idx) in fruits">
          {{ idx }} => {{ fruit }} // index는 두번째 인자에 넣어야함
      </div>
      <div v-for="todo in todos">
          <p>{{ todo.title }} => {{ todo.completed }}</p> // 객체 반환
      </div>
  
      <h2>Object</h2>
      <div v-for="value in myObj">
          {{ value }} // 객체를 반복시키면 기본적으로 value값 반환
      </div>
      <div v-for="(value, key) in myObj">
          {{ key }} => {{ value }} // key 값을 원할 때는 두번째 인자에 넣어줌
      </div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
      const app = new Vue({
          el: '#app',
          data: {
              myStr: 'Hello World!',
              fruits: ['apple', 'banana', 'coconut'],
              todos: [
                  { id: 1, title: 'todo1', completed: true },
                  { id: 2, title: 'todo2', completed: false },
                  { id: 3, title: 'todo3', completed: true },
              ],
              myObj: {
                  name: 'kim',
                  age: 100,
              }
          }
      }) 
  </script>
  ```

  

#####  v-bind

> HTML 요소의 속성에 Vue 상태 데이터를 값으로 할당

- 즉, html 요소의 기본 속성을 vue와 연동시켜주는 것
  - href,src,class 등의 속성을 `v-bind:href`,`v-bind:src` 등과 같이 써주면 vue에서 작성한 data 를 활용하여 html 요소의 속성을 지정할 수 있음

- **Object 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당**

  - `<div v-bind:class="{key:value}"></div>` : key에는 지정할 클래스, value는 t/f 값을 할당

- 약어 (Shorthand)

  - `:`(콜론)
  - `v-bind:href` == `:href`

- 예시

  ```vue
  <style>
      .active {
        color: red;
      }
  
      .my-background-color {
        background-color: yellow;
      }
    </style>
  </head>
  <body>
    <div id="app">
      <!-- 속성 바인딩 -->
      <img v-bind:src="imageSrc" alt="">
      <img :src="imageSrc" alt="">
      <hr>
  
      <!-- 클래스 바인딩 -->
      <div :class="{ active: isRed }">
        클래스 바인딩
      </div>
      <hr>
  
      <!-- 스타일 바인딩 -->
      <p :style='{ fontSize: fontSize + 'px' }'>
          this is paragraph
      </p>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          fontSize: 16,
          imageSrc: 'https://picsum.photos/200/300/',
          isRed: true,
        }
      })
    </script>
  </body>
  ```

  - 여러 속성을 bind 하게 될 경우 각 속성에 모두 bind를 걸어줘야함
    - `<img :src='srcMsg' :alt='altMsg'></div>` 와 같이 각 속성에 다 걸어줌
  - 하나의 속성에 여러 값을 주고 싶다면 배열을 활용
    - 만약 클래스를 두 개 이상 넣고 싶다면?
    - `<p :class='[class1, class2]'></p>` 와 같이 지정
  - 스타일을 지정할 때는 `{지정할 스타일 : 데이터값}` 으로 지정해줘야함.
    - 단, 지정할 스타일이 html에서는 `-` 를 활용하여 쓰였지만 (ex. font-size) js에서는 `-`를 쓰지 않기 때문에, `fontSize`와 같이 바꿔서 지정해줘야함.

###### v-for & v-bind:key

- v-for를 사용할 때 반드시 key값을 넣어줄 것을 권장
- key 값은 for문으로 도는 각 요소별로 겹치면 안됨. 따라서, 각기 다른 값들을 넣어줘야하는데 주로 해당 요소의 id 값이나 idx를 활용함
- 위를 구현하기 위해 사실상 무조건 bind를 사용해야함
  - `<div v-for="{fruit, idx} in fruits" :key="idx"></div>`



##### v-on

> element에 eventListener를 연결

- 이벤트 유형은 전달인자로 표시함
- 특정 이벤트가 발생했을 때, 주어진 코드가 실행됨
- 약어 (Shorthand)
  - @
  - `v-on:click` === `@click`

- 이벤트를 발생시킬 요소 속성에 `v-on:event` 삽입

- 실행시킬 함수는 vue instance의 methods에 모여있을 것

  - 해당 함수 이름을 `v-on:event='함수'` 의 형태로 삽입

- 기존 이벤트 실행을 막는 방법 (==preventDefault)

  - `v-on:event.prevent` 와 같이 `.prevent` 사용
  - `@:event.prevent="function"` : 특정 함수의 기본 기능을 막고 function을 실행시킨다
  - `keyup`과 같은 이벤트는 `.enter`,`.space`와 같이 속성을 지정해줄 수 있음

- 실행할 함수의 인자는 기본적으로 event가 들어감. 다만, 새로운 인자를 넣어주면 event 대신 해당 인자가 들어감

  ```vue
  <div id='app'>
      <input type='text' @keyup.enter='log'> #이벤트를 출력함
      <input type='text' @keyup.enter='log('asdf')'> # event 자리에 'asdf'가 들어가버려서 asdf를 출력함
  </div>
  <script>
      const app = new Vue({
          el:'#app',
  		methods: {
              alterHello: function(){
                  alert('hello')
              },
              log : function(event){
                  console.log(event)
              }        	
      }
      })
  </script>
  ```

  

##### v-model

> HTML form(input) 요소의 값과 data를 양방향 바인딩

- 즉, input으로 예를 들었을 때, input의 값이 data에도 적용이 되고, data의 값도 input에 적용이 되도록 하는 것

- 수식어
  - .lazy
    - input 대신 change 이벤트 이후에 동기화
  - . number
    - 문자열을 숫자로 변경
  - .trim
    - 입력에 대한 trim을 진행

- 예시

  ```vue
  <body>
      <div id="app">
          <h2>1. Input -> Data(단방향)</h2>
          <h3>{{ message }}</h3>
          <input @input='onInputChange' type='text'>
          <hr>
          
          <h2>2. Input <-> Data </h2>
          <h3>{{ myMessage2 }}</h3>
          <input v-model='myMessage2' type='text'>
          <hr>
             
          <h2>3. Checkbox </h2>
          <input type='checkbox' id='checkbox' v-model='checked'>
          <label for='checkbox'>{{ checked }}</label>    
      </div>
      
  	<script src = 'vue.cdn'></script>
      <script>
          const app = new Vue({
              el: '#app',
              data: {
                  myMessage:'',
                  myMessage2:'',
                  checked: true,
              },
              methods: {
                  onInputChange: function(event){
                      this.myMessage = event.target.value
                  },
              }
          })
          </script>
  </body>
  ```



##### computed

> 데이터를 기반으로 하는 계산된 속성

- 함수의 형태로 정의하지만 함수가 아닌 **함수의 반환 값**이 바인딩 됨
- 종속된 데이터에 따라 저장(캐싱)됨
- 종속된 데이터가 변경될 때만 함수를 실행
- 즉, 어떤 데이터에도 의존하지 않는 computed 속성의 경우 절대로 업데이트되지 않음
- 반드시 반환 값이 있어야함

- vs Methods

  - 기존에 갖고 있던 데이터의 모습을 바꿔서 쓰고 싶을 때 computed 사용
  - method는 실행되는 함수라면 computed는 함수가 실행된 값
  - computed는 종속된 대상이 변경되지 않는 한 computed에 작성된 함수를 여러번 호출해도 계산을 다시 하지 않고 계산되어 있던 결과를 반환
  - 이에 비해 methods를 호출하면 렌더링을 다시 할 때마다 항상 함수를 실행
  - 따라서, 결과값을 반환하고 싶은 경우 method는 함수를 실행시켜서 return값을 얻을 수 있어야함 (ex.`{{ method() }}`). but, computed는 이미 값이기 때문에 바로 출력 (ex. `{{ computed }}`) 
  - 주로 method는 데이터를 바꿀 때, computed는 데이터를 통한 값을 얻을 때 위주로 사용

- computed와 관련된 데이터가 변할 때만 작동함(== computed 속성은 종속 대상을 따라 캐싱된다.)

  - 즉, 종속 대상이 변하지 않는 한 계산되어 있던 결과를 계속 갖고 있음
  - method는 연관 없는 데이터가 변할 때도 매번 렌더링 할 때마다 작동함

- 예시

  ```vue
  <body>
      <div id='app'>
          <p>{{ num }}</p>
          <p>{{ doubleNum }}</p>        
      </div>
      <script src='cdn.vue'></script>
      <script>
          const app = new Vue({
              el:'#app',
              data: {
                  num:2,
              },
             	computed: {
                  doubleNum: function() {
                      return this.num*2
                  }
              }
          })
      </script>
  </body>
  ```

  

##### watch

> 특정 값이 변동하면 다른 작업을 한다

- 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야할 때 주로 사용

- 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수를 실행하는 방식

- 소프트웨어 공학에서 이야기하는 명령형 프로그래밍 방식

- 즉, 특정 대상이 변경되었을 때 콜백 함수를 실행시키기 위한 트리거

- 함수의 첫번째 인자는 변경된 값, 두번째 인자는 변경되기 전의 값이 할당됨

- 예시

  ```vue
  <body>
      <div id='app'>
          <p>{{ num }}</p>
          <button v-on:click="num+=1">add 1</button>
      </div>
      
      <script src='cdn.vue'></script>
      <script>
          const app = new Vue({
              el:'#app',
              data: {
                  num:2,
              },
             	watch: {
                  num: function() { //num을 감시하고 있다는 뜻
                      console.log('${this.num}이 변경되었습니다.')
                  }
              }
          })
      </script>
  </body>
  ```

  

- vs Computed

  | computed                                                     | watch                                                        |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | ~과 관련된 데이터가 변경될 때 ~을 수정해라                   | ~이 변경된다면 지정한 함수를 즉시 실행해라                   |
  | 특정 데이터를 직접적으로 사용/가공하여 다른 값으로 만들 때 사용 | 특정 데이터의 변화 상황에 맞춰 다른 data등이 바뀌어야할 때 사용 |
  | 속성값에 계산해야하는 목표 데이터를 정의                     | 속성값에 감시할 데이터를 정의                                |
  | 선언형 프로그래밍 방식                                       | 명령형 프로그래밍 방식                                       |

  

##### filters

> 텍스트 형식화를 적용할 수 있는 필터

- 즉, text의 re-formatting을 위해 존재

- interpolation 혹은 v-bind를 이용할 때 사용 가능
- filter는 자바스크립트 표현식 마지막에 `|`(파이프)와 함께 추가 되어야 함
- 이어서 사용 가능 == chaining 가능

- `{{ 요소 | 필터1 | 필터2 }}` 는 요소를 인자로하여 필터1과 2를 수행한 결과값을 return 한다

- 예시

  ```vue
  <body>
      <div id='app'>
          <p>{{ numbers | getOddNums | getUnderTenNums }}</p>
      </div>
      <script src='vue.cdn'></script>
      <script>
      	const app = new Vue({
              el: '#app',
              data: {
                  numbers: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
              },
              filters: {
                  getOddNums: function (nums) {
                      const oddNums = nums.filter(function (num) {
                          return num%2
                      })
                      return oddNums
                  },
                  getUnderTenNums(array) {
                      return array.filter(num => num<10)
                  }
  			}
      </script>
  </body>
  ```

  

### Lifecycle Hooks

- 각 Vue 인스턴스는 생성 될 때 일련의 초기화 단계를 거침
  - 예를 들어 데이터 관찰 설정이 필요한 경우, 인스턴스를 DOM에 마운트 하는 경우, 데이터가 변경되어 DOM을 업데이트하는 경우 등
  
- 그 과정에서 사용자 정의 로직을 실행할 수 있는 LifeCycle Hooks도 호출됨

- 즉, 원하는 특정 순간에 로직을 실행시킬 수 있도록 지정 가능
  - created : 인스턴스가 생성된 순간
    - 외부 API에서 초기 데이터를 받아올 때 주로 사용
  - mounted : 생성된 인스턴스를 화면에 부착(viewmodel과 view가 붙는 순간 = template과 연결될 때)
  - update : 데이터가 변할 때 순간순간 반응하는 것
  
- 주된 목적은 자동화

- 함수를 작성할 때는 this 필요!

- 기타 LifeCycle Hooks
  - beforeCreate, created, beforeMount, mounted, beforeUpdate, updated, destroyed

  <img src="../assets/web/lifecycle" alt="img" style="zoom:50%; border:solid gray 5px;" />
  
  출처 : vuejs.org
  
  
  
- 예시

  ```vue
  <body>
      <div id='app'>
          <img v-if="imgSrc" :src="imgSrc" alt='sample img'        
      </div>
         
   	<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    	<script>
          const API_URL = 'https://dog.ceo/api/breeds/image/random'
          const app = new Vue({
            el: '#app',
            data: {
              imgSrc: '',
            },
            methods: {
              getImg: function () {
                axios.get(API_URL)
                  .then(response => {
                    this.imgSrc = response.data.message
                  })
              }
            },
         	// vue instance가 생성된 순간에 실행시킬 로직   
            created: function () {
                this.getImg()
            }
          })
        </script>
  </body>
  ```

  
