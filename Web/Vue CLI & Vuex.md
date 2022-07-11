# Vue Advanced

[toc]

## Vue CLI

### SFC(Single File Component)

- Vue의 컴포넌트 기반 개발의 핵심 특징 
- 하나의 컴포넌트는 `.vue` 확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물
- 화면의 특정 영역에 대한 **HTML, CSS, JavaScript 코드를 하나의 파일(.vue)에서 관리**
- 즉, `.vue` 확장자를 가진 싱글 파일 컴포넌트를 통해 개발하는 방식
- `.vue` 확장자를 가진 하나의 파일은 하나의 vue instance와 동일
  - `new Vue()` 로 생성했던 instance와 같다는 의미
  - 원래는 하나의 파일에서, `new Vue()`를 여러번 사용함



#### Component

- 기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화 하는데 도움을 줌

- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미

- 즉, 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라, 재사용성의 측면에서도 매우 강력한 기능을 제공

- 쉽게 말해, **한 페이지를 여러개의 부품(=component)으로 만드는 것**

  - 지금까지는 한 페이지는 하나의 html 파일로만 구성했었음
  - 즉, 한 화면을 여러개의 컴포넌트로 구성하는 것
    - 하나의 컴포넌트는 하나의 .vue 파일로 형성
  - 처음 개발을 준비하는 단계에서 시간 소요가 증가하지만 이후 변수 관리가 용이하며 기능별로 유지&보수 비용이 감소함

- 하나의 컴포넌트는 여러 개의 하위 컴포넌트를 가질 수 있음

  - 상하관계가 있다는 뜻

- Vue는 컴포넌트 기반의 개발 환경을 제공

- Vue 컴포넌트는 `const app = new Vue({...})`의 app을 의미하며 이는 Vue 인스턴스

  - 단, 컴포넌트 기반의 개발이 반드시 파일 단위로 구분되어야 하는 것은 아님
    - 즉, 언제나 컴포넌트 기반의 개발은 여러개의 파일로 나눠서 개발하는 것이다 는 틀린말
  - 즉, 기준이 파일 단위가 아니라는 것. 하나의 html 파일 안에서도 여러 개의 컴포넌트를 만들어 개발 가능

- Vue 컴포넌트 구조

  ![Component Tree](../assets/web/vue_component_structure)

![image-20220511192726338](../assets/web/vue_component_structure(2))



### Vue CLI

- 공식문서

  - VUE CLI 란?

    vue-cli 는 기본 vue 개발 환경을 설정해주는 도구입니다. vue-cli 가 기본적인 프로젝트 세팅을 해주기 때문에 폴더 구조에 대한 고민, lint, build, 어떤 라이브러리로 구성을 해야되는지 webpack 설정은 어떻게 해야되는지에 대한 고민을 덜을 수 있습니다.

- Vue.js 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할을 하며 Vue 개발 생태계에서 표준 tool 기준을 목표로 함
- 확장 플러그인, GUI, Babel 등 다양한 tool 제공



### Node JS

- 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 **런타임 환경**
  - 브라우저 밖을 벗어날 수 없던 자바스크립트 언어의 태생적 한계를 해결
  - 즉, 물고기가 물 밖에서 살 수 있도록 물 밖의 환경을 물고기가 살 수 있는 환경으로 바꿔주는 것
- Chrome V8 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경을 제공
- 즉, **단순히 브라우저만 조작할 수 있던 자바스크립트를 SSR 아키텍처에서도 사용할 수 있도록 함**
- 예시
  - 이전에는 `console.log()` 를 브라우저에서만 실행시킬 수 있었으나, node js 설치 이후에는 PC에서도 실행이 가능해짐




#### NPM (Node Package Manage)

- 자바스크립트 언어를 위한 패키지 관리자

  - Python에서의 pip와 같은 역할
  - pip와 마찬가지로 다양한 의존성 패키지를 관리

- **Node.js의 기본 패키지 관리자**로 Node.js 설치시 함께 설치됨

- Vue 시작하기

  - 설치 및 버전 확인

    ```bash
    $ npm install -g @vue/cli
    $ vue --version
    ```

    - `-g` : 특정 프로젝트에 귀속되지 않고 PC 전체에 설치하도록 설정하는 명령어
    - npm의 경우 python과 다르게 자동으로 프로젝트별 가상환경 생성 

  - 프로젝트 생성

    ```bash
    $ vue create my-first-app
    ```

    - 환경에 따라 npm 레지스트리 변경 여부를 물어볼 수 있음 (Yes 입력)

  - Vue 버전 선택 

    ```bash
    ? Please pick a preset: (Use arrow keys)
    > Default ([Vue 3] babel, eslint)
      Default ([Vue 2] babel, eslint)
      Manually select features
    ```

    - 생태계 구축과 같은 이유로 아직까지는 Vue2 사용 권장

  - 프로젝트 생성 성공 후 이동

    ```bash
    $ cd my-frist-app
    ```

  - 서버 실행

    ```bash
    $ npm run serve
    ```

    - 프로젝트 메인 페이지 확인 가능

  - 기본 뼈대 작성

    - html에서의 `!+tab` 과 같은 역할을 하는 `vue+tab` 
    - vetur를 설치했기 때문에 가능

    

- npm은 pip와 다르게 자동으로 프로젝트의 별도 폴더 내부에 설치함

  - Python은 venv를 설치하고, source로 활성화 한 후에 설치해야했음

  - but, Vue CLI는 알아서 되고, 글로벌 환경에 설치하고 싶으면 `-g` 를 사용해야함
    - 단, 공식문서에서 `-g`를 쓰라고 한 경우를 제외하고는 쓰지 말 것





### Vue 프로젝트 구조

> vue cli를 통해 생성된 구조이며 Babel과 Webpack에 대한 초기 설정이 자동으로 되어있음



#### Babel

> "JavaScript compiler"
>
> 자바스크립트의 ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해주는 도구

- 과거 자바스크립트의 파편화와 표준화의 영향으로 코드의 스펙트럼이 매우 다양
  - 이로 인해, **최신 문법을 사용해도 이전 브라우저 혹은 환경에서 동작하지 않는 상황이 발생**
- **원시 코드(최신 버전)를 목적 코드(구 버전)로 옮기는 번역기**가 등장하면서 개발자는 더 이상 내 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있게 됨



#### Webpack

> "static module bundler"
>
> 모듈 간의 의존성 문제를 해결하기 위한 도구

- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함

- 모듈

  - 모듈은 단지 파일 하나를 의미 (ex. js 파일 하나 === 모듈 하나)

  - 배경

    - 브라우저만 조작할 수 있었던 시기의 자바스크립트는 모듈 관련 문법 없이도 사용됨(ex. `<script src>`)
    - 하지만 js와 애플리케이션이 복잡해지고 커지자 전역 scope를 공유하는 형태의 기존 개발 방식의 한계점이 드러남
    - 그래서 라이브러리를 만들어 필요한 모듈을 언제든지 불러오거나 코드를 모듈 단위로 작성하는 등의 다양한 시도가 이루어짐
    - **모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기가 어려움**

  - 즉, Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장

    - **Js의 생태계는 의존성 문제가 매우 심각하기 때문**

    

- 번들

  - 모듈의 의존성 문제를 해결해주는 작업을 Bundling이라 함
    - 모듈끼리 매우 심각하게 엉켜있고 연결되어있는 것을 정리하는 것

  - 이러한 일을 해주는 도구는 Bundler 이고, Webpack은 다양한 Bundler 중 하나
  - 여러 모듈을 하나로 묶어주고 묶인 파일은 하나로 합쳐짐
  - **Bundling 된 결과물은 더 이상 순서에 영향을 받지 않고 동작하게 됨**
  - webpack 이외에도 snowpack, parcel, rollup.js 등의 다양한 모듈 번들로 존재
  - Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음




#### 프로젝트 디렉토리 구조

##### node_modules

- node.js 환경의 여러 의존성 모듈

- venv와 같은 역할

  - 따라서 git에 올리면 안됨
  - gitignore은 자동으로 만들어져있고 node_modules도 자동으로 등록되어있음


##### public/index.html

- Vue 앱의 뼈대가 되는 파일
- 실제 제공되는 단일 html 파일
  - 해당 부분에서 bootstrap CDN 삽입 등 django base.html의 일부 역할 수행 가능
- 아무리 많은 코드를 작성해도 사용자가 받는 html은 index.html 파일 하나



※ src 주소의 상징은 @


##### src/assets

- webpack에 의해 빌드 된 정적 파일

##### src/components

- 하위 컴포넌트들이 위치

##### src/App.vue

- 최상위 컴포넌트
- 캔버스 역할
- 최상위 컴포넌트는 따로 관리

##### src/main.js

- webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry  point
- 실제 단일 파일에서 DOM과 data를 연결했던 것과 동일한 작업이 이루어지는 곳
- Vue 전역에서 활용할 모듈을 등록할 수 있는 파일

##### babel.config.js

- babel 관련 설정이 작성된 파일

##### package.json

- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션이 포함
- python은 freeze로 requirements.txt 를 업데이트 시켜줬어야함
- but vue 프로젝트에서는 package.json이 자동으로 업데이트됨

##### package-lock.json

- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 팀원 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용할 패키지의 버전을 고정
- 개발 과정 간의 의존성 패키지 충돌 방지



#### 컴포넌트 구조

##### 템플릿(HTML)

- 최상단에 위치
- HTML의 body 부분
- 각 컴포넌트를 작성
- \<template> 태그로 둘러쌓여있는 부분



##### 스크립트(JavaScript)

- JavaScript가 작성되는 곳
- 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
- \<script> 태그로 둘러쌓여있는 부분



##### 스타일(CSS)

- CSS가 작성되며 컴포넌트의 스타일을 담당
- \<style> 태그로 둘러쌓여있는 부분



#### 컴포넌트 등록

- 부모 - 자식의 관계를 만드는 것

- 새로운 컴포넌트 생성 후 `vue`+`enter` 로 기본 뼈대 생성 가능(Vetur 확장 프로그램 때문)

- 불러오기(import) → 등록하기(register) → 보여주기(print)

  - 각 단계별로 이름을 다르게 지정해도 되지만 굳이 다르게 지정할 필요가 없으므로 주로 같은 이름을 지정
  - 등록은 components 에 내부에 등록
  - components에 등록할 때는 key : value 방식으로 등록
    - 단, key : value 에서 key 문자열과 value 값이 같으면 key 하나만 써줄 수 있음
    - 이 때문에 아래 예시에서 About만 작성해도 됨 
  - 최근 버전에서는 변수명을 두단어 이상으로 지정해야함 ex) TheAbout

- 컴포넌트 등록시 맞춰줘야하는 변수

  - import 변수명 => components의 value값
  - components의 key값 => html의 태그명
  - 만약 components의 key값과 value값이 같으면 한번만 써도 됨 (ex. { About : About } === { About } )

- chrome 확장자 프로그램을 활용하여 브라우저 내에서 컴포넌트 관계 확인 가능 (in 개발자 도구-Vue)

- 보여주기 단계에서는 두 가지 방법으로 진행 가능

  1. CamelCase ex) `<TheAbout />`
  2. kebab-case ex) `<the-about></the-about>`

- 예시

  ```vue
  <template>
  	<div>
          <img alt='Vue logo' src='./assets/logo.png'>
          <!-- 3. 보여주기(print) -->
          <!-- 아래 두 가지 방법으로 보여주기 가능 -->
          <!-- 케밥케이스 -->
          <the-about> ... </the-about>
          <!-- 카멜케이스 -->
          <TheAbout />
      </div>
  </template>
  
  <script>
  <!-- 1. 불러오기 (import)-->
  import About from './components/About.vue' //아래줄과 같은 의미
  import About from '@/components/About.vue' 
  //import는 as 와 같은 역할(단순한 변수명 할당 역할, 하지만 주로 vue파일 이름과 똑같이 지정함)
  
  export default {
      // name은 단지 컴포넌트의 이름을 뜻하며 빈 vue inspecter(개발자 도구의 extension)에서 확인할 때 태그가 변경됨
      name : 'App',
      components : {
          // 2. 등록하기(register)
          About
          // About:About
      }
  }
  </script>
  ```

  - 부모 - 자식 관계 형성 완료
  - 자식 컴포넌트는 여러번 불러올 수 있고 불러올 때마다 자식 컴포넌트에게 각기 다른 props를 전달할 수 있음

#### Data & Methods

> Vue cli에서 data와 methods 정의하는 방법

##### data

- 컴포넌트의 'data'는 반드시 함수로 작성해야함

  - 기본적으로 각 인스턴스는 모두 같은 data 객체를 공유하기 때문에(하나의 컴포넌트를 여러번 썼을 경우) 할당, 얕은 복사의 문제가 발생하지 않도록 아예 새로운 객체를 반환해버리는 함수를 사용해야함

  - 함수가 return 하는 값을 data로 사용 (return 값은 참조가 아닌 아예 새로운 값으로 반환됨)

  - return 값은 객체로 되어있으며 `변수 : value` 형식으로 작성
  - 여러 데이터를 쓰고 싶을 경우, `key : value` 형태를 여러개 작성하면 됨

  ```js
  data : function () {
      return {
          data1: '',
          data2: '',
      }
  }
  ```

  

##### methods

- 기존 작성 방법과 같음

  ```js
  methods : {
      functionName : function() {
          console.log()
      },
      function2Name : function() {
          console.log('2번째 methods')
      }
  }
  ```

  

### Props & Emit

> 여러 컴포넌트간의 의사소통 방법

- Vue app은 자연스럽게 중첩된 컴포넌트 트리로 구성
- 컴포넌트간 부모-자식 관계가 구성되며 이들 사이에 필연적으로 의사 소통이 필요
  - 부모는 자식에게 데이터를 전달(=Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 메시지로 알림(Emit Event)
  - 부모와 자식이 명확하게 정의된 인터페이스를 통해 격리된 상태를 유지할 수 있음



#### Props

- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성

- 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야함

- 즉, 데이터는 props 옵션을 사용하여 자식 컴포넌트로 전달됨

- 모든 컴포넌트 인스턴스에는 자체 격리된 범위가 있음

  - 즉, 자식 컴포넌트의 템플릿에서 상위 데이터를 직접 참조할 수 없음!

- 작성법(전송 = 데이터를 자식 컴포넌트에게 내리는 것)

  - 자식 컴포넌트 태그(보여주기로 작성한 template 부분)의 **속성으로** prop 데이터 선언
  - `prop이름 = 데이터값` 과 같이 선언
  - 예시

  ```vue
  <template>
  	<div id='app'>
          <img alt="Vue logo" src="./assets/logo.png">
          <!-- 자식 컴포넌트(=About.vue)에 보낼 prop 데이터 선언 -->
          <about my-message='this is prop data'></about>
      </div>
  </template>
  ```

- 수신할 데이터는 자식 컴포넌트의 props 옵션에서 설정

  - **prop데이터 이름과 해당 데이터의 타입을 key:value 형태로 props 객체에 삽입**
  - **Props의 이름은 선언할 때(=스크립트에서)는 camelCase로 HTML에서는 kebab-case로 작성한다.**
    - 즉, 데이터를 자식에게 줄 때는 kebab-case 자식이 데이터를 받을 때는 camel 케이스


  ```vue
  <!--About.vue(자식 컴포넌트)-->
  
  <template>
  	<div>
          <h1>About</h1>
          <h2>{{ myMessage }}</h2>
      </div>
  </template>
  
  <script>
  export default {
      name: 'About',
  	// 수신할 prop 데이터    
      props: {
          myMessage: String,
      }
  }
  </script>
  ```

   - 전달 받은 props 데이터는 바로 데이터처럼 사용할 수 있음
     - 부모의 데이터이지만 넘어왔기 때문에 자식 컴포넌트의 스코프 안에서 자유롭게 사용 가능한 데이터가 됨

  - 템플릿 안에는 반드시 하나의 Element만 있어야함(Vue CLI의 규칙)
    - 따라서, div로 감싸주고 나머지 태그를 div 안에 삽입하면 된다는 뜻



#### Dynamic Props 

- v-bind directive를 사용해 부모의 데이터의 props를 동적으로 바인딩

  - v-bind(`:`) 는 html 태그의 기본 속성을 vue와 연결시켜주는 역할을 하며 props는 속성을 통해 하위 컴포넌트에 데이터를 전달하기 때문에 하위 컴포넌트에 전달할 데이터를 vue와 묶어준다고 생각하면됨

- 부모에서 데이터가 업데이트 될 때마다 자식 데이터로도 전달됨

- 예시

  ```vue
  <!--APP.vue(부모 컴포넌트)-->
  
  <template>
  	<div id='app'>
          <img alt="Vue logo" src="./assets/logo.png">
          <about my-message='this is prop data'
                 :parent-data='parentData'
          >
      	</about>
      </div>
  </template>
  
  <script>
  import About from './components/About.vue'
      
  export default {
      name: 'App',
      components: {
          About
      }
      data: fuction() {
          return {
              parentData: 'This is parent Data by v-bind'
      }
    }
  }
  </script>
  ```

  ```vue
  <!--About.vue(자식 컴포넌트)-->
  
  <template>
  	<div>
          <h1>About</h1>
          <h2>{{ myMessage }}</h2>
          <h2>{{ parentData }}</h2>
      </div>
  </template>
  
  <script>
  export default {
      name: 'About',
  	// 수신할 prop 데이터    
      props: {
          myMessage: String,
          parentData: String,
      }
  }
  </script>
  ```

  

- 모든 props는 하위 속성과 상위 속성 사이의 **단방향 바인딩**을 형성함
  - 부모의 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 그렇지 않다는 뜻
    - 자식 요소가 의도치 않게 부모 요소의 상태를 변경하여 앱의 데이터 흐름을 이해하기 어렵게 만드는 일을 방지하기 위함
  - 부모 컴포넌트가 업데이트 될 때마다 자식 요소의 모든 prop들이 최신 값으로 업데이트됨



#### Emit Event

- "Listening to Child Components Events"
- 부모 컴포넌트에게 메시지를 전달하는 인스턴스 메서드

##### $emit(eventname)

- 현재 인스턴스에서 이벤트를 트리거

  - 자식 컴포넌트에서 부모 컴포넌트에게 지정한 이벤트를 발생시킴
  - 따라서, 부모 컴포넌트에서는 어떤 이벤트가 발생했을 때 특정 행동을 취하도록 코드를 구현해야함

- 추가 인자는 리스너의 콜백 함수로 전달

  - 즉, $emit에서 두번째 인자로 전달한 데이터(첫번째 인자는 이벤트명)는 부모 컴포넌트에서 이벤트가 발생했을 때 시행되는 함수의 인자로 전달됨
  - 인자 개수가 두개 이상인 경우 하나의 변수에 객체로 할당하여 해당 변수를 전달하는 방식으로 구현할 것을 권장

- 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 v-on을 사용하여 자식 컴포넌트가 보낸 이벤트를 청취 (v-on을 이용한 사용자 지정 이벤트)

- 예시

  ```vue
  <!--About.vue(자식 컴포넌트)-->
  
  <template>
  	<div>
          <h1>About</h1>
          <h2>{{ myMessage }}</h2>
          <h2>{{ parentData }}</h2>
          <!-- 트리거가 발동되는 곳 -->
          <input type='text'
                 @keyup.enter = 'childInputChange'
                 v-model='childInputData'
          >
      </div>
  </template>
  
  <script>
  export default {
      name: 'About',
      data: function(){
          return {
              childInputData: null,
          }
      }
      props: {
          myMessage: String,
          parentData: String,
      },
      // emit을 통해 부모 컴포넌트에 이벤트 이름과 인자 전달
      methods: {
          childInputChange: function(){
              this.$emit('child-input-change', this.childInputData)
          }
      }
      
  }
  </script>
  ```

  ```vue
  <!--APP.vue(부모 컴포넌트)-->
  
  <template>
  	<div id='app'>
          <img alt="Vue logo" src="./assets/logo.png">
          <about my-message='this is prop data'
                 :parent-data='parentData'
                 @child-input-change="parentGetChange"
          >
      </about>
      </div>
  </template>
  
  <script>
  import About from './components/About.vue'
      
  export default {
      name: 'App',
      components: {
          About
      },
      data: fuction() {
          return {
              parentData: 'This is parent Data by v-bind'
      	}
    	},
          // inputData는 자식 컴포넌트에서 인자로 전달한 데이터
      methods: {
          parentGetChange: function(inputData){
              console.log('About으로부터 ${inputData}를 받음!')
          }
      }
  }
  </script>
  ```

  - 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 v-on directive를 사용하여 자식 컴포넌트가 보낸 이벤트(child-input-change)를 청취



##### event 이름 컨벤션

- 컴포넌트 및 props와는 달리, 이벤트는 자동 대소문자 변환을 제공하지 않음
- HTML의 대소문자 구분을 위해 DOM 템플릿의 v-on 이벤트 리스너는 항상 자동으로 소문자 변환되기 때문에 v-on:myEvent 는 자동으로 v-on:myevent로 변환
  - 예를들어, `this.$emit('myEvent')` 로 부모 컴포넌트에 메시지를 보내고, 부모 컴포넌트에서 `@myEvent` 로 받으려고 해도 html은 자동으로 `@myevent`로 변환.
  - 따라서, `$emit` 이벤트 이름에는 항상 kebab-case를 사용할 것을 권장



### Vue Router

> Vue.js 공식 라우터
>
> SPA의 장점은 부드러운 사용자 경험이지만 단점은 URL이 없다는 것 → 이 단점을 해결하기 위해 Vue Router 사용

- 라우트(Route)에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할지 알려줌

  - 즉, 컴포넌트를 URL에 매핑시켜주는 것 (BUT, 그런 척일 뿐 실제 하이퍼링크처럼 작동하는 것은 아님)

- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공

- url과 화면이 변경되어도 실제 화면 전환(혹은 새로고침)이 일어난 것은 아님

- router

  - 위치에 대한 최적의 경로를 지정하며, 이 경로를 따라 데이터를 다음 장치로 전향시키는 장치

- 시작하기

  - 프로젝트 생성 및 이동(원래 프로젝트 생성하는 방법! _ 이미 배웠던 내용)

    ```bash
    $ vue create my-router-app
    $ cd my-router-app
    ```

  - Vue Router Plugin 설치 (Vue CLI 환경)

    ```bash
    $ vue add router
    ```

    - 위 코드 실행시 자동으로 코드 일부를 수정해줌
    - 기존 프로젝트를 진행하고 있던 도중에 추가하게 되면 App.vue를 덮어쓰기 때문에 프로젝트 내에서 다음 명령을 실행하기 전에 필요한 경우 파일을 백업해야함

  - commit 여부와 History mode 사용 여부에 모두 Yes 입력

  - 설치 이후 자동으로 변경되는 사항

    - App.vue 코드에 router-link, router-view 태그 생성
    - router/index.js 생성
    - views 디렉토리 생성



##### router/index.js

- 라우트에 관련된 정보 및 설정이 작성되는 곳
- 마치 django의 urlpatterns 와 같은 모습을 가진 객체 확인 가능
  - path - 주소 / name - 별칭 / component - 이동할 컴포넌트
  - name 을 활용하여 목표 경로를 지정할 수 있음
- 컴포넌트를 지정하기 위해서는 해당 컴포넌트를 import 해와야함




##### router-link

- 사용자 네비게이션을 가능하게 하는 컴포넌트

- a 태그인 것 처럼 생겼으나 router-view는 **컴포넌트**

- 목표 경로는 'to' 속성으로 지정됨

  - 예시

    ```vue
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
    ```

  - django에서와 마찬가지로 url name을 활용하여 주소 지정 가능

  - 단, 바인드 지정 필수 

    ex) `<router-link :to = "{ name: 'about' }"> About </router-link>`

- HTML5 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 브라우저가 페이지를 다시 로드하지 않도록 함

- a 태그지만 우리가 알고 있는 GET 요청을 보내는 a 태그와는 조금 다르게, 기본 GET 요청을 보내는 이벤트를 제거한 형태로 구성됨



##### router-view

- 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
  - 쉽게 말해, 지정한 포털을 불러오고 위치시킬 포털이라고 생각하면 됨
- 실제 컴포넌트가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 해당 경로와 연결되어 있는 index.js에 정의한 컴포넌트가 위치함



#### History Mode

- HTML History API를 사용해서 router를 구현한 것
- 브라우저의 히스토리는 남기지만 실제 페이지는 이동하지 않는 기능을 지원
- 즉, 페이지를 다시 로드하지 않고 URL을 탐색할 수 있음
  - SPA의 단점 중 하나인 'URL이 변경되지 않는다'를 해결
- History API
  - DOM의 Window 객체는 history 객체를 통해 브라우저의 세션 기록에 접근할 수 있는 방법을 제공
  - history 객체는 사용자를 자신의 방문 기록 앞과 뒤로 보내거나, 기록의 특정 지점으로 이동하는 등 유용한 메서드와 속성을 가짐



#### Named Routes

- 이름을 가지는 라우트

- 명명된 경로로 이동하려면 객체를 vue-router 컴포넌트 요소의 prop에 전달

- 바인드가 있어야만 작동함

- 예시

  ```javascript
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import HomeView from '../views/HomeView.vue'
  import AboutView from '../views/AboutView.vue'
  
  Vue.use(VueRouter)
  
  const routes = [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
  ]
  ```

  ```vue
  <template>
    <div id="app">
      <nav>
        <router-link :to="{ name: 'home' }">Home</router-link> |
        <router-link :to="{ name: 'about' }">About</router-link>
      </nav>
      <router-view/>
    </div>
  </template>
  ```



#### 프로그래밍 방식 네비게이션

> 쉽게 말해, django에서의 redirect를 가능케 하는 것

- router-link 를 사용하여 선언적 탐색을 위한 a 태그를 만드는 것 외에도, router의 인스턴스 메서드를 사용하여 프로그래밍 방식으로 같은 작업을 수행할 수 있음

- 선언적 방식 : `<router-link to="이동할곳">`

- 프로그래밍 방식 : `$router.push(이동할 곳)`

- Vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근할 수 있음

- 따라서, 다른 URL로 이동하려면 `this.$router.push` 를 호출할 수 있음

  - 이 메서드는 새로운 항목을 히스토리 스택에 넣기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 누르면 이전 URL로 이동하게 됨

- `<router-link>`를 클릭할 때 내부적으로 호출되는 메서드이므로 `<router-link : to=''...">`를 클릭하면, `router.push(...)`를 호출하는 것과 같음

- 예시

  ```javascript
  // literal string path
  router.push('home') -> url을 변경하는 역할 수행
  
  // object
  router.push({ path: 'home'})
  
  // named route
  router.push({ name:'user', params: { userId: '123' } })
  
  // with query, resulting in /register?plan=private
  router.push({ path: 'register', query: { plan: 'private'} })
  ```

  ```vue
  <!-- About에서 Home으로 이동하는 로직 -->
  <template>
    <div class="about">
      <h1>This is an about page</h1>
      <button @click="moveToHome">To Home</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutView',
    methods: {
      moveToHome() {
        this.$router.push({ name: 'home' })
        //this.$router.push('/')  
      }
    }
  }
  </script>
  ```



#### Dynamic Route Matching

- 동적 인자 전달

- 주어진 패턴을 가진 라우트를 동일한 컴포넌트에 매핑해야하는 경우

- 예를 들어 모든 User에 대해 동일한 레이아웃을 가지지만, 다른 User ID로 렌더링 되어야하는 User 컴포넌트가 있다면?

  - django에서는 `<int:pk>` 처럼 사용했던 것을 router에서는 콜론 사용

  ```javascript
  const routes = [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
      // 동적인자는 :(콜론)으로 시작
    {
      path: '/user/:userId/:username/:major',
      name: 'profile',
      component: UserProfile
    }
  ]
  ```

  - 동적 인자는 컴포넌트에서 `this.$route.params` 로 사용 가능
    - data에 넣어서 주로 사용
    - `user : this.$route.params` 로 지정시 user에는 동적인자가 담긴 객체 전달
  - 동적인자 route push 법
    - `router.push({ name:'user', params: { userId: '123', username: 'kim', major: 'CS' } })`



#### vue router의 폴더 구조

- 기본적으로 작성된 구조에서 components 폴더와 views 폴더 내부에 각기 다른 컴포넌트가 존재하게 됨. 주로 아래와 같이 활용
  - App.vue : 최상위 컴포넌트
  - views/ : **router(index.js)에 매핑되는 컴포넌트를 모아두는 디렉토리**
  - components/ : **router에 매핑된 컴포넌트 내부에 작성하는 컴포넌트를 모아두는 디렉토리**



#### why vue router?

- SPA 등장 이전
  - 서버가 모든 라우팅을 통제
  - 요청 경로에 맞는 HTML 제공
- SPA 등장 이후
  - 서버는 index.html 하나만 제공
  - 이후 모든 처리는 HTML 위에서 JS 코드를 활용해 진행
  - 즉, 요청에 대한 처리를 더 이상 서버가 할 필요가 없어짐
- 라우팅 처리 차이
  - SSR 
    - routing에 대한 결정권을 서버가 가짐
  - CSR
    - 클라이언트는 더 이상 서버로 요청을 보내지 않고 응답받은 HTML 문서 안에서 주소가 변경되면 특정 주소에 맞는 컴포넌트를 렌더링
    - 라우팅에 대한 결정권을 클라이언트가 가짐
- 결국 Vue Router는 라우팅의 결정권을 가진 Vue.js에서 라우팅을 편리하게 할 수 있는 Tool을 제공해주는 라이브러리 



## Vuex

### Vuex(중앙 상태 관리)

- Statement management pattern + Library for vue.js
  - 상태 관리 패턴 + 라이브러리
- 상태(state)를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리
  - 상태가 예측 가능한 방식으로만 변경될 수 있도록 보장하는 규칙 설정
  - 애플리케이션의 모든 컴포넌트에 대한 중앙 집중식 저장소 역할
    - 즉, 중앙에서 모든 상태 정보를 관리하는 것
  - state는 곧 data이며 해당 애플리케이션의 핵심이 되는 요소이다.
- Vue의 공식 devtools와 통합되어 기타 고급 기능을 제공



#### 상태 관리 패턴

- 컴포넌트의 공유된 상태를 추출하고 이를 전역에서 관리하도록 함
- 컴포넌트는 커다란 view가 되며 모든 컴포넌트는 트리에 상관없이 상태에 엑세스 하거나 동작을 트리거 할 수 있음
- 상태 관리 및 특정 규칙 적용과 관련된 개념을 정의하고 분리함으로써 코드의 구조와 유지 관리 기능 향상



#### why Vuex?

- 기존에 각 컴포넌트는 독립적으로 데이터를 관리
- 기존의 부모 컴포넌트 - 자식 컴포넌트 간의 데이터 흐름은 단방향 흐름으로 부모 → 자식 간의 전달만 가능 (반대의 경우에는 이벤트를 트리거)
- 장점 : 데이터의 흐름을 직관적으로 파악 가능
- 단점 : 컴포넌트 중첩이 깊어지는 경우 동위 관계의 컴포넌트로의 데이터 전달이 불편해짐
  - 즉, 데이터를 부모로 전달하고 그 부모로 전달하고 다시 해당 부모의 다른 자식으로 전달하는 등 매우 복잡한 과정을 거쳐야함
  - 부모 자식 간의 컴포넌트 관계가 단순하거나 depth가 깊지 않은 경우에는 문제가 없음
    - 몇 단계만 거치면 데이터를 쉽게 이동 시킬 수 있으며 훨씬 직관적으로 데이터 흐름을 파악할 수 있음
  - 규모가 커질 경우 상태를 공유하는 컴포넌트의 상태 동기화 관리가 어려움
    - A 컴포넌트의 상태를 공유하는 다른 컴포넌트에 pass props & emit event 를 통해 동기화해야함



##### but, Vuex Management Pattern is...

- 중앙 저장소(store)에 state를 모아놓고 한번에 관리
  - 규모가 큰 프로젝트에서 매우 효율적
- 각 컴포넌트에서는 중앙 집중 저장소의 state만 신경쓰면 됨
  - 동일한 state를 공유하는 다른 컴포넌트들도 동기화 됨
- 상태를 올바르게 관리하는 저장소의 필요성을 느끼게됨
  - 상태를 한 곳에 모두 모아 놓고 관리하자
  - 상태의 변화는 모든 컴포넌트에서 공유한다
  - 상태의 변화는 오로지 Vuex가 관리하여 해당 상태를 공유하고 있는 모든 컴포넌트는 변화에 '반응'
    - A 컴포넌트와 같은 상태를 공유하는 다른 컴포넌트는 신경 쓰지 않고, 오로지 상태의 변화를 Vuex에 알림



### Vuex Core Concepts

![vuex](../assets/web/vuex.png)

#### State

>  중앙에서 관리하는 모든 상태 정보(data)
>
>  Mutate → State → Render

- Vuex는 single state tree를 사용
- 즉, 이 **단일 객체**는 모든 애플리케이션 상태를 포함하는 '원본소스(single source of truth)'의 역할을 함
- 이는 각 애플리케이션마다 하나의 저장소만 갖게 된다는 것을 의미

- 여러 컴포넌트 내부에 있는 특정 state, 즉 데이터를 중앙에서 관리하게 됨
  - 이전의 방식은 state를 찾기 위해 각 컴포넌트를 직접 확인했어야했음
  - Vuex를 활용하는 방식은 Vuex Store 에서 각 컴포넌트에서 사용하는 state를 한 눈에 파악 가능
- State가 변화하면(by Mutations) 해당 state를 공유하는 여러 컴포넌트의 DOM은 자동으로 렌더링
- 각 컴포넌트는 Vuex Store에서 state 정보를 가져와 사용



#### Mutations

> state를 변경하는 유일한 방법
>
> commit → Mutations → Mutate

- mutation의 handler(핸들러 함수)는 반드시 동기적이어야 함
  - 비동기적 로직은 state가 변화하는 시점이 의도한 것과 달라질 수 있으며, 콜백이 실제로 호출 될 시기를 알 수 있는 방법이 없기 때문
- state를 조작할 함수 등록
  - 함수명은 All Capital로 지정
  - `state.데이터이름.조작메서드()`

- mutations에 등록되는 함수는 **첫번째 인자로 항상 state를 받음**
- 직접 호출되는 것이 아닌 Actions에서 commit() 메서드에 의해 호출됨
- Actions에서 호출되어 state를 변경하는 과정이 Mutate



#### Actions

> state 변경 외의 모든 동작을 수행
>
> Dispatch → Actions → Commit

- Mutations와 유사하지만 다음과 같은 차이점 존재
  - state를 변경하는 대신 mutations를 commit() 메서드로 호출해서 실행
    - `context.commit('Mutation')`
  - mutations와 달리 비동기 작업이 포함될 수 있음
- context 객체를 인자로 받음
  - context 객체를 통해 store/index.js 파일내에 있는 모든 요소의 속성에 접근하거나 메서드 호출이 가능 (state, getters 등등)
    - state를 변경 할 수는 있으나 절대 직접 변경하지 않음
- 컴포넌트에서 dispatch() 메서드에 의해 호출
  - `this.$store.dispatch(호출할Action,)`

- Actions를 통해 state를 조작할 수 있으나 state는 오로지 Mutations를 통해서만 조작해야함
  - 명확한 역할 분담을 통해 서비스 규모가 커져도 state를 올바르게 관리하기 위함



#### Getters

> state를 변경하지 않고 활용하여 계산 수행 (computed 속성과 유사)

- computed를 사용하는 것처럼 getters는 저장소의 상태(state)를 기준으로 계산
  - 따라서, 첫번째 인자는 무조건 state
- computed 속성과 마찬가지로 getters의 결과는 state 종속성에 따라 캐시되고, 종속성이 변경된 경우에만 다시 재계산 됨
- getters 자체가 state를 변경하지는 않음
  - state를 특정한 조건에 따라 구분(계산)만 함
  - 즉, 계산된 값만 가져옴
- 컴포넌트에서 Getters의 값을 사용할 때는 computed에 매핑시켜서 사용
  - data에 하면 안됨
    - state는 오로지 mutations를 통해서만 변경이 되어야함.
    - but, data에 넣는 순간 data를 통해서도 변경이 되기 때문에 매우 위험
    - component의 data는 변할 수 있음 (오히려 변하는게 핵심)
    - but, state는 변해서는 안됨. data에서 받아온 후, data의 값이 바뀌면 결국 state가 바뀌는 것
  - 따라서, state,getters는 모두 computed로 받아와야함






### Set project & Components

##### project 시작 과정 (with Vuex)

1. vue 프로젝트 생성

   ```bash
   $vue create project_name
   ```

   - 생성 후 해당 프로젝트로 직접 이동해줘야함

   

2. Vuex 설지

   ※ vuex나 vue-router는 vue에 포함되어있는 app이 아니라서 따로 설치해줘야함

   ```bash
   $ vue add vuex
   ```

   - commit 여부 물을 경우 yes 클릭
   - 설치시 , store 디렉토리와 해당 디렉토리 내에 index.js 설치됨
   - index.js에서 Vuex Core Concepts(state,getters 등등) 작성
   - script는 거의 state에서 데이터를 받아오기만 하는 역할로 축소

   

3. 컴포넌트 구조 설계

   - vuex를 사용한다고 해서 부모 자식 관계가 사라지는 것은 아님!
   - props emit과 같이 부모 자식 관계 설정 필요
   - 다른 컴포넌트 import 시 주소를 입력할 때 `@` 사용 가능 
     - @는 프로젝트 폴더 내에 src 디렉토리를 의미



4. state 작성 (= 모델링)

   - store/index.js 에서 진행

   - state와 레코드 모두 객체로 작성 

   - 예시

     ```javascript
     // store/index.js
     export default new Vuex.Store({
         state : {
             테이블1: [
                 {레코드1},
                 {레코드2}.
                 {컬럼1: value1, 컬럼2: value2...}
             ],
         	테이블2: [
         		{레코드2-1},
                 {레코드2-2},
         	]
         }
     })
     ```

     - vuex를 사용한다고 해서 Vuex Store에 모든 데이터를 넣어야하는 것은 아님



- 중앙 저장소에서 데이터 가져오기

  - `$store`로 중앙저장소에 접근 가능 ex)`$store.state.데이터`

  - computed로 맵핑 가능

    - 예시

      ```vue
      <template>
      	<div>
              <todo-list-item v-for='todo in todos' ...
                              :todo='todo'> 
                  			<--! 자식 컴포넌트에 todo 전송 -->
                  
          	</todo-list-item>
          </div>
      
      </template>
      <script>
          ...
          computed: {
              todos() {
                  return this.$store.states.todos (todos는 데이터테이블 이름)
              }
          }
          ...
      </script>
      ```

  - v-for를 사용하는 등의 여러 상황에서 중앙데이터가 아닌 props 로 데이터를 내려보내는 경우도 많음

    - 즉, 모든 경우에 중앙 저장소에서 데이터를 받아오는 것은 아님

- actions 인자 단축하기

  ```js
  actions: {
      createTodo({commit}){
          ...
      }
  }
  ```

  ```vue
  actions: {
  	createTodo(context){
  		...
  	}
  }
  ```

  - 위 두 코드는 완전히 같은 코드

    ```js
    const commit = context.commit // 이 코드는
    const { commit } = context // 이 코드와 같음
    ```

    - 따라서, actions의 함수는 context로 인자를 받아야하는데 해당 인자는 { commit }으로 대체 가능 
    - mutations 함수를 호출할 때 `context.commit`이 아닌 `commit` 으로만 사용 가능해짐



### Component Binding Helper

> JS Array Helper Method를 통해 배열 조작을 편하게 하는 것과 유사
>
> - 논리적인 코드 자체가 변하는 것이 아니라 '쉽게' 사용할 수 있도록 되어 있음에 초점



- 원래는 저장소의 state를 바꾸기 위한 과정은 매우 복잡함
  1. 컴포넌트에서 methods에 dispatch와 불러올 actions 등록
  2. store에서 actions에 불러올 mutations 등록
  3. mutations에서 state를 수정할 내용 등록
- 이를 조금이라도 간단하게 줄이기 위한 방법이 binding helper
  - 컴포넌트에서 바로 actions 등록없이 호출



````js
import vuex from 'vuex'
import vuex.mapActions from 'vuex' === import { mapActions } from 'vuex'
````

#### mapState

- **computed와 Store의 state를 매핑**
- Vuex Store의 하위 구조를 반환하여 component 옵션을 생성
- 매핑된 computed 이름이 state 이름과 같을 때 문자열 배열을 전달 할 수 있음

```vue
<script>
expoprt default {
    computed:{
        todos : function(){
            return this.$store.state.todos // 함수명과 불러오는 데이터 이름이 같음
        }
    }
}
</script>
```

- binding helper 사용시

```vue
<script>
import { mapState } from 'vuex'
expoprt default {
    computed:{
        mapState(['todos',])
        }
    }
}
</script>
```

- 다른 computed 요소를 추가할 수 있도록 객체 전개 연산자(Object Spread Operator)로 객체 복사

```vue
<script>
import { mapState } from 'vuex'
expoprt default {
    computed:{
        ...mapState(['todos',])
        }
    }
}
</script>
```



#### mapGetters

- **Computed와 Getters를 매핑**
- getters를 객체 전개 연산자로 계산하여 추가
- 해당 컴포넌트 내에서 매핑하고자 하는 이름이 index.js에 정의해놓은 getters의 이름과 동일하면 배열의 형태로 해당 이름만 문자열로 추가

```vue
<script>
import { mapGetters } from 'vuex'
expoprt default {
    computed:{
        ...mapGetters([
        	'completedTodossCount',
        	'allTodosCount',
        ])
        }
    }
}
</script>
```



#### mapActions

- action을 전달하는 컴포넌트 method 옵션을 만든다

- actions를 객체 전개 연산자(Object Spread Operator)로 계산하여 추가

- 첫번째 인자로 action의 이름을 받음

  ```vue
  <script>
  import vuex from 'vuex'
  expoprt default {
      methods:{
          deleteTodo: vuex.mapActions(['deleteTodo','createTodo']).deleteTodo
      }
  }
  </script>
  ```

  - 만약 mapActions만 사용한다면?

  ```vue
  <script>
  import { mapActions } from 'vuex'
  expoprt default {
      methods:{
          deleteTodo: mapActions(['deleteTodo','createTodo']).deleteTodo
      }
  }
  </script>
  ```

  - binding helper가 반환하는 결과는?
    - 객체

  ```vue
  <script>
  // mapActions(['deleteTodo','createTodo']) === {deleteTodo:function(){}, createTodo:function(){}}
  // 따라서, methods를 아래와 같이 작성 가능 (결과값이 객체이기 때문에)    
  import { mapActions } from 'vuex'
  expoprt default {
      methods:{
          mapActions(['deleteTodo','createTodo'])
      }
  }
  </script>
  ```

  - 그렇다면 다른 methods를 추가하고 싶은 경우에는?
    - Object Spread Operator 사용

  ```vue
  <script>
  import { mapActions } from 'vuex'
  expoprt default {
      methods:{
          ...mapActions(['deleteTodo','createTodo']),
          mymethod () {
              // 함수 작성
          }
      }
  }
  </script>
  ```

  

#### 인자 전달

- binding helper를 사용할 경우 actions로 직접 전달해줫던 인자를 전달할 수 없게 됨

- 이를 해결하기 위해 이벤트 태그에서 함수 호출 방식을 변경해줘야함

  - 기존

  ```vue
  <template>
  	<button @click='호출할함수'>
      </button>
  </template>
  ```

  - 변경

  ```vue
  <template>
  	<button @click='호출할함수(전달할인자)'>
          <!-- 클릭했을 때 함수를 호출하는데 그 때 지정해놓은 인자를 같이 넘겨라! -->
      </button>
  </template>
  ```



### Scoped

> 해당 컴포넌트 내에서만 지정한 스타일을 적용시키고 싶을 때 사용

- Js는 single page spread이기 때문에 style을 모든 컴포넌트가 공유함.

- scoped를 지정함으로써 선택자에 해당하는 모든 요소가 아닌 해당 컴포넌트 내에 있는 요소에만 style이 적용되도록 함

  ```vue
  <style scoped>
      .is-completed {
          text-decoration: line-through;
      }
      span {
          cursor: pointer;
          #해당 요소에 마우스를 올렸을 때, 마우스 아이콘이 변경됨
      }
  </style>
  ```

  



### Browser Storage

> 데이터를 브라우저 데이터베이스에 저장시킬 때 사용

- 브라우저의 저장소
  - session storage : 탭이 켜져있는 동안 데이터 유지
  - local storage : 영구 저장, 데이터 삭제를 원할 경우 직접 delete 해야함



#### Local Storage

> ※ vue의 기능이 아닌 브라우저의 기능. 따라서, 다른 프레임워크에서도 사용할 수 있음

- 브라우저의 영역이기 때문에 직접 접근 및 조작 가능 

  - 데이터 저장

  ```js
  localStorage.setItem('저장할데이터이름',저장할데이터)
  ```

  - json(문자열)으로 데이터를 변경한 후에 저장해야함

  ```js
  JSON.stringify(데이터)
  ```

  - 저장된 데이터 불러오기

  ```js
  localStorage.getItem('데이터이름(Json)')
  ```

  - 불러온 데이터 파싱

  ```js
  JSON.parse(localStorage.getItem('데이터이름(Json)'))
  ```

  

- actions 에서는 내부적으로 활용하기 위한 함수도 작성할 수 있음

  - 다른 함수에서 context와 dispatch를 활용하여 해당 함수를 호출할 수 있음
  - 즉, 만든 함수가 반드시 컴포넌트에서 사용되어야만 하는 것은 아님
  - 데이터를 생성, 삭제, 수정 할 때마다 local storage에 저장된 값이 변경되므로, 각 함수 내부에 localStorage 관련 함수를 실행시켜야함. 

  

- Local Storage에 데이터가 저장이 되어 있어도, state에 비어있기 때문에 화면에 뜨지 않음

  - 따라서, mutations에서 localStorage에 저장되어 있는 데이터를 불러와서 조작해야함
  - 저장돼있는 JSON 데이터를 불러오고, 해당 데이터를 파싱하는 함수 생성
  - 페이지가 로드 될 때(created) 해당 함수를 불러오도록 코드 작성
    - 이 때, mapMutations 를 사용해서 컴포넌트에 불러올 수도 있음



#### Persistedstate 라이브러리 사용

##### vuex-persistedstate

> vuex state를 자동으로 브라우저의 LocalStorage에 저장해주는 라이브러리 중 하나

- 페이지가 새로고침 되어도 Vuex State를 유지시킴

- 설치

  ```bash
  $ npm i vuex-persistedstate
  ```

- impot(in index.js)

  ```js
  // store/index.js
  import createPersistedState from 'vuex-persistedstate'
  
  export default new Vuex.Store({
      plugins:[
          createPersistedState()
      ],
  })
  ```

  - 특별한 코드 작성 및 로직 구현 없이 위 코드만으로도 자동으로 LocalStorage에 저장되고, 이에 더해 state에까지 저장됨
