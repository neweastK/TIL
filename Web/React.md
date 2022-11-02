# React

## Initial Setting

1. `npx` 사용을 위한 nodeJs 설치
2. `npx create-react-app`으로 리액트 프로젝트 생성
3. `npm start` 로 해당 프로젝트 실행
4. `npm run build`는 빌드를 수행함
   - 빌드란 배포판을 만드는 과정
   - `npx serve -s build` 로 배포판 실행
   - `-s` 옵션은 사용자가 어떤 경로로 들어오든 index.html 파일을 서비스함
   - `build` 폴더를 지정했기 때문에, 폴더 내에 있는 index.html 파일을 서비스함



## 디렉토리 구조

#### src

- index.js: 여러가지 전역 설정이 들어감
- App.js: 실제 UI를 작성하는 곳
- App.css: App.js 의 CSS를 작성하는 곳

#### public

- index.html: Id가 Root인 태그가 존재하는 곳, 최상위 html 

  

## 사용자 정의 태그 만들기

- 함수를 정의함으로써 사용자 정의 태그를 만들 수 있음

- 사용자 정의 태그를 만들 때는 반드시 첫자를 대문자로 지정

- 그리고 return값으로 원하는 태그들을 설정

- 단, 하나의 태그로 감싸져있어야함(Vue2.0이랑 비슷한듯)  => `<> </> ` 으로 감싸도 됨 == <React.Fragment></React.Fragment>

- 예시

  ```react
  function App() {
      return {
          <div>
              <header>
              	<h1><a href='/'>WEB</a></h1>
              </header>
          	<nav>
                  <ol>
                      <li><a href="/read/1"></a></li>
                      <li><a href="/read/2"></a></li>                   
                  </ol>
              </nav>
              <article>
                  <h2>Welcome</h2>
                  Hello,WEB
              </article>
          </div>
      }
  }
  ```

  - 위 코드를 사용자 정의 태그로 아래처럼 바꿀 수 있음

  ```react
  function Header() {
      return 
          <header>
              <h1><a href='/'>WEB</a></h1>
          </header>
  }
  function Nav() {
      return 
          <nav>
              <ol>
                  <li><a href="/read/1"></a></li>
                  <li><a href="/read/2"></a></li>
              </ol>
          </nav>
  }
  function Article() {
      return 
          <article>
              <h2>Welcome</h2>
              Hello,WEB
          </article>
  }
  
  function App() {
      return {
          <div>
              // 위에서 정의한 태그
              <Header></Header>
          	<Nav></Nav>
              <Article></Article>
          </div>
      }
  }
  ```

  - 이 사용자 정의 태그가 바로 **컴포넌트**



## prop

- 함수로 정의한 컴포넌트에 파라미터로 props 설정

- 컴포넌트가 사용된 태그 내부에서 key,value를 설정

  ```react
  function Header(props){
      ...
  }
  <Header title = "REACT"></Header>
  ```

- 컴포넌트 정의 부분에서 props를 활용하여 컴포넌트 별 다른 속성값을 부여할 수 있음

  ```react
  function Header(props){
      return
          <header>
              <h1><a href='/'>{props.title}</a></h1>
          </header>
  }
  <Header title = "REACT"></Header>
  ```

- 만약, props에 문자열이 아닌 변수를 보내고 싶다면?

  - 중괄호 이용해서 value 전달

- 사용자 태그를 정의할 때, 태그들을 동적으로 활용할 수 있음

  - 예시

    ```react
    function Nav(props){
        const lis = []
        for (let i=0; i<props.topics.length; i++){
            let t = props.topics[i];
            lis.push(<li key={t.id}><a href={"/read/"+t.id}></a>{t.title}</li>)
        }
    }
    ```

    - for 문을 사용할 때, 반복되는 태그에는 고유한 값이 key값으로 주어져야함
    
    

## event

- 태그 내에서 태그 정의 부분으로 함수를 보낼 수도 있음

- 해당 함수는 event와 함께 사용 가능

- 이벤트의 경우 onClick과 같은 속성을 넣어주고, 그 안에 함수를 넣어줌으로써 실행

- 함수는 eventTarget을 첫 인자로 받음

- 예시

  ```react
  function Header(props){
      return <header>
          <h1><a href="/" onClick={
                      function(event){
                          event.preventDefault();
                          props.onChangeMode();
                      }}>{props.title}</a></h1>
      </header>
  }
  
  function App() {
      return {
          <div>
          	<Header title="WEB" onChangeMode={
                      function(){
                          alert('Header')
                      }}>
              </Header>
          </div>
      }
  }
  ```




## State

> prop과 마찬가지로 input에 따라 return값이 달라짐
>
> but, props는 컴포넌트를 사용하는 사람을 위한 장치이지만, state는 컴포넌트를 만드는 사람을 위한 장치

#### 사용법

1. import

   ```react
   import {useState} from 'react'
   ```

2. 일반 변수에 state 적용

   ```react
   // 원래 값
   const mode = 'WELCOME'
   // state 적용
   const _mode = useState('WELCOME')
   ```

3. _mode 는 즉, useState는 첫번째로 상태의 값을 갖고, 두번째는 그 상태의 값을 변경할 때 사용하는 함수를 갖는 객체임

   - 즉, _mode[0] 으로 상태의 값을 읽을 수 있음

   - _mode[1] 으로 _mode의 상태값을 바꿀 수 있음

   - 예시

     ```react
     // useState의 인자는 state의 초기값 설정
     // 아무런 값도 넣지 않으려면 null 사용
     const _mode = useState('WELCOME')
     
     // state의 값은 0번째 인덱스 값으로 읽음
     const mode = _mode[0]
     
     // state 값의 변경은 1번째 인덱스로 변경
     // _mode[1] 은 함수
     const setMode = _mode[1]
     
     // 위 세줄을 아래 한줄로 표현
     const [mode, setMode] = useState('WELCOME');
     // mode의 값을 welcome으로 바꾸겠다!
     setMode('WELCOME')
     ```

   - setMode 함수를 호출시 해당 함수가 있는 컴포넌트가 재실행됨

   - cf) 특정 숫자를 태그의 속성으로 넘기면 문자로 변경됨 주의

4. state에서 setState를 사용할 때 value의 타입에 따라 방법이 달라짐

   - 원시객체인 경우(string,number,boolean)

     - `setState('원하는 값')`

   - 범객체인 경우(object, array) 복제한 후에 복제값에 수정하고, 수정된 복제값을 set함수에 넣어줌

     ```react
     // 객체이면
     const newValue = {...value}
     // 배열이면
     const newValue = [...value]
     // 원하는 수정 작업 진행
     newValue.push("추가")
     setValue(newValue)
     ```

      

