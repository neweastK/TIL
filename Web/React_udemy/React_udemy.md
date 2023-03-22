# React

## Section 1. Getting Started

### 리액트란?

- 모바일 앱은 상당히 괜찮은 사용자 경험을 제공

  - 화면 전환이 매우 부드럽고 빠르기 때문
  - 전통적으로 웹사이트들은 그러지 않았음
    - 요청을 보내면 서버는 새로운 html 페이지를 브라우저로 보내줌
    - 새로운 html 페이지가 로딩될 때까지 기다려야했음
  - Javascript는 새로운 html 페이지를 불러오지 않고도 사용자에게 다른 것을 보여줄 수 있음
    - 리액트는 javascript의 라이브러리로, 클라이언트 사이드의 라이브러리
    - 다양한 기능과 도구를 활용해 복잡한 사용자 인터페이스를 쉽게 만들 수 있게 해줌
    - 고수준 구문을 통해 선언형 방식, 선언형 컴포넌트 중심의 방식으로 코드 작성 (JS는 명령)
    - 즉, SPA는 첫번째 요청 후에 더 이상 새로운 페이지를 받지 않고, JS를통해 화면에 표시되는 내용을 제어하는 것

- 리액트는 컴포넌트 기반의 프론트엔드 프레임워크

  - 컴포넌트에 집중하기에 내장 기능이 다양하지는 않음
  - 때문에, 다양한 서드 파티 라이브러리가 필요

  



## Section 2. JavaScript Refresher

#### let vs const

- 변수를 생성하는 방법
- let은 값을 수정할 수 있는 변수를 선언할 때
- const는 한번 지정하면 절대 변하지 않는 값인 상수를 선언할 때
  - const 변수에 값을 할당한 후, 재할당 할 경우 오류 발생



#### 화살표 함수

- `const arrowFunction = () => {}`
  - 받는 인자가 1개라면 `()`도 생략 가능
  - 받는 인자가 없거나 2개 이상이면 `()` 필요
  - `{}` 안에 코드가 return문 하나라면, return과 `{}` 생략 가능
- function 키워드 생략
- thils 문제 해결



#### Exports & Imports

- JS는 다른 JS 파일의 기능이나 데이터에 액세스하기 위해 export 와 import 사용
- export
  - `export default 변수`
    - import 할 때, 따로 변수를 지정해주지 않아도 기본적으로 지정한 변수를 넘겨받음
    - 파일 하나는 오직 하나의 default 를 갖ㄹ 수 있음
  - `export const 변수` (naemd export)
    - import 할 때, 해당 변수를 지정해줘야만 해당 변수를 받을 수 있음
- import
  - `import {변수명} from 원본파일`
    - named export 방식으로 export한 변수를 받을 때 사용
    - 정확한 변수명을 지정해줘야함
    - `{변수명 as 변경할이름}` 으로 원하는 이름으로 할당받을 수 있음
  - `import * as 변수명 from 원본파일`
    - 하나의 파일에서 여러개의 데이터를 export 할 때, 한번에 받는 방법
    - 객체처럼 `변수명.원본변수` 와 같은 식으로 접근
  - `import 지정이름 from 원본파일`
    - 원본파일에서 defaut export한 값을 지정이름으로 할당



#### class

- 클래스는 객체를 생성하기 위한 청사진 

- class 키워드로 생성

- Property와 Method를 가질 수 있음

  - Property는 클래스 내부의 변수
  - Method는 클래스 내부의 함수

- constructor는 클래스 내부에서 선언되며, 클래스의 객체를 생성할 때마다 실행될 함수

  - 주로 내부에서 Property를 선언함

- 클래스는 다른 클래스를 상속 받을 수 있음

  - extends 키워드 사용
  - extends 키워드를 사용하여 클래스를 생성하고, 해당 클래스의 생성자 함수를 선언할 때 반드시 super 메서드가 들어가야함
    - `super()`는 상위 클래스의 생성자함수를 실행하는 역할
    - 즉, 서브클래스의 생성자함수를 실행할 때, 상위 클래스의 생성자함수도 같이 실행시켜서 상속 받은 것들을 사용할 수 있도록 하는 것
    - 서브클래스에서 슈퍼 클래스의 property를 오버라이딩 할 수 있음

- 클래스 인스턴스는 new 키워드로 생성

- 예시

  ```js
  class Human {
    constructor () {
      this.gender = "Male"
    }
  
    printGender () {
      console.log(this.gender)
    }
  }
  
  
  class Person extends Human {
    constructor() {
      super()
      this.name = "KIM";
    }
    
    printMyName () {
        console.log(this.name);
    }
  }
  const person = new Person();
  person.printMyName(); // "KIM"
  person.printGender(); // "Male"
  ```

- but, 최신 자바스크립트에서는 Property를 생성자 함수와 this 없이 선언할 수 있음

- 또한, 메서드도 화살표 함수로 선언할 수 있음

  - 예시

    ```js
    class Human {
    	gender = "Male"
    
    	printGender = () => {
            console.log(this.gender)
        }
    }
    
    
    class Person extends Human {
        name = "KIM";
        
        printMyName = () => {
          console.log(this.name);
      }
    }
    
    const person = new Person();
    person.printMyName(); // "KIM"
    person.printGender(); // "Male"
    ```



#### Spread & Rest Operators

- 둘 다, `...`으로 사용

- spread

  - 배열의 원소나 객체의 프로퍼티를 나눌 때 사용

  - 예시

    ```js
    const newArray = [...oldArray,1,2]
    const newObject = {
        ...oldObject,
        newProp:3
    }
    ```

    - 이후 스프레드로 나눈 객체나 배열의 값이 변경되어도 새로 할당된 변수에는 적용 안됨

      ```js
      let oldObject = { name: 1, kim:2}
      const newObject = {...oldObject, dong:3}
      console.log(newObject) // { name: 1, kim: 2, dong: 3 }
      oldObject.shin = 3
      console.log(oldObject) // { name: 1, kim: 2, shin: 3 }
      console.log(newObject) // { name: 1, kim: 2, dong: 3 }
      ```

- rest

  - 함수의 인수목록들을 배열로 합칠 때 사용
  - `function function1 (...args) {}`
    - 원하는 개수만큼 인자를 받고, 하나의 배열로 묶음 (args = [ 인자1, 인자2, 인자3 ...])
    - 함수 내에서 배열 메서드를 통해서 다양하게 활용 가능



#### Destructuring(구조 분해 할당)

- 배열이나 객체에서 특정 원소나 속성을 추출하는 방법

- 배열의 경우 `[변수명]`, 객체의 경우 `{변수명}`으로 사용

- 예시

  ```js
  const numbers = [1,2,3];
  [num1, num2] = numbers;
  console.log(num1,num2) // 1,2
  
  [num1, ,num3] = numbers;
  console.log(num1,num3) // 1,3
  
  const person = { name:'Max', age:25 }
  const {name} = person
  console.log(name) //'Max'
  ```

  

#### 데이터 타입

- 원시형 데이터
  - number, string, boolean 등
  - 재할당하거나 변수를 다른 변수에 저장할 때마다 **값을 복사**
    - 즉, 원래 값이 변경되도 따라 변경되지 않음
- 참조형 데이터
  - 객체, 배열
  - 특정 객체가 할당된 변수를 다른 변수에 재할당하면 얕은 복사가 이뤄짐
    - 즉, 원래 객체를 수정하면, 두 변수 모두 변경된다는 것
  - 깊은 복사를 위해서는 spread 연산자 사용
    - ex) `const secondObject = { ...firstObject }`
    - 위처럼 할 경우 firstObject를 아무리 수정해도 secondObject에는 영향을 주지 않음



## Section3. React Basics & Working With Components

**★React is a JavaScript library for building user interfaces★**

**→ 리액트는 사용자 인터페이스를 구축하는 자바스크립트 라이브러리이다!**

**→ 리액트는 컴포넌트에 관한 모든 것. 각각의 컴포넌트를 구축하고 최종 UI에서 어떻게 구성될 것인지 명령**

- 컴포넌트 사용은 재사용성과 코드 분리 장점을 갖고 있음
  - 재사용성은 반복을 줄여줌
  - 코드 분리는 코드를 작은 단위로 관리할 수 있게 해줌



#### 컴포넌트는 어떻게 만들어지는가?

- 컴포넌트는 HTML, CSS, JS 를 결합하여 생성
- 컴포넌트를 결합하면 사용자 UI 생
- 선언적 접근 방식 사용
  - JS 처럼 직접 DOM을 업데이트 하는 작업 X
  - 어떤 상태가 되어야하는지 목표 상태를 정의하는 것이 중요
    - 목표 상태는 html 형식으로 작성하고, 함수로 해당 html 코드를 반환한다



#### 리액트 프로젝트 만들기

##### react-create-app

- react-create-app 이란?

  - Webpack, Babel, 패키지 등 번거로운 react 초기 셋팅 작업을 미리하고 그 환경을 다시 패키징 한 것	
  - 메타에서 개발한 보일러 플레이트로 React 프로젝트 개발 초기 세팅에 필요한 여러가지 라이브러리나 패키지의 설치 및 설정 없이 간편하게 시작할 수 있도록 환경 제공
  - 축약하여 CRA라고 부름

- 반드시 node.js 설치 필요

- 사용법

  ```bash
  npx react-create-app 프로젝트명
  ```

- 참고

  - https://velog.io/@devsaza/cra
  - https://www.incodom.kr/ReactJS/Create-React-App

- 관련 명령어

  ```bash
  npm install
  ```

  - package.json에 있는 관련 라이브러리들을 모두 설치
  - node_modules에 설치된 요소들이 모두 포함되어있음

  ```bash
  npm start
  ```

  - 개발 서버 구동
  - 작성한 코드의 결과물을 미리볼 수 있음



#### 리액트 프로젝트 구성

#### src

- 컴포넌트별 파일을 따로 생성하고, 해당 파일들을 관리하기 위해 components 폴더 생성하여 관리

  - but, App.js 는 옮겨서는 안됨
  - 파일 생성시 파일명은 파스칼 케이스로 작성

  

###### index.js

- 페이지가 로드되면 가장 먼저 실행되는 파일
- npm start 프로세스는 브라우저에 코드를 전달하기 전에 코드 변환 작업을 거침
  - 예를들어, import 문은 일반적인 JS구문이 아님
    - cf) import로 파일을 가져올 때, js파일은 확장자를 입력하면 안됨
  - 즉, 브라우저에서 실행할 수 있는 코드로 변환한다는 것
- react-dom 서드 파티 라이브러리로부터 ReactDOM이라는 객체를 가져옴
  - react-dom은 디펜던시 중 하나이며 로컬에 다운로드 되어있음
  - ReactDOM의 createRoot 메서드를 통해 react를 통해 만든 사용자 인터페이스가 위치해야할 요소를 알려줌
    - index.html의 root 아이디를 가진 div태그를 가리키고 있음(`ReactDOM.createRoot(요소)`)
    - root 객체를 반환하며 이 객체는 render 메서드로 지정한 위치에 무엇이 렌더링되어야하는지 알려줌 (`root.render(주로 App.js)`)
- 렌더링은 루트 컴포넌트 한번만 실행



###### App.js

- root라는 id를 갖는 요소가 있는 곳에 렌더링되는 컴포넌트
- 최신 JS에서는 한 파일에 정의된 함수, 클래스, 객체를 다른 파일에서 사용하고자 하는 경우 export로 내보낼 수 있음
- 루트 컴포넌트로서 ReactDOM에 의해 html 페이지에 직접 렌더링 될 수 있는 유일한 컴포넌트임
  - 모든 컴포넌트들은 다른 컴포넌트 혹은 app.js에 중첩될 것






##### public

###### index.html

- SPA인 react 앱에서 유일하게 사용될 html 파일

- react가 관리하는 사용자 인터페이스 전반이 렌더링될 위치

- ```html
  <div id="root"></div>
  ```

  - 이곳에 react가 관리하는 사용자 인터페이스가 연결됨(by. createRoot)



#### JSX란?

- react 팀에서 개발한 syntax로 브라우저에서 실행하기 전 자바스크립트 형태의 코드로 변환됨
- JSX는 자바스크립트에 XML을 추가 확장한 문법
  - Javascript 코드 내부에 html 코드를 작성할 수 있도록 함
- 크롬에서 개발자도구로 변환된 코드 확인 가능
  - source 탭 - static/js 에서 확인할 수 있음
  - 전체 리액트 라이브러리 소스 코드와 우리가 작성한 코드가 변환된 것을 볼 수 있음



#### 컴포넌트 작성하기

- 리액트의 컴포넌트는 **자바스크립트 함수**이다!

  - html 코드를 나타내는 JSX 코드를 반환하는 함수

- 다른 파일에서 사용할 수 있도록 export로 내보내야함

  - `export default 함수명or클래스명`
    - 기본적으로 지정한 함수 혹은 클래스를  내보낸다는 것
    - import 할 때, 따로 지정하지 않는 이상 default로 지정된 함수를 가져옴

- 다른 컴포넌트에서 import 로 컴포넌트를 가져와서 html 태그에 삽입

  - 이때, 사용자 지정 컴포넌트의 이름은 **반드시 대문자로 시작해야함**
  - JSX가 코드를 변환할 때, 사용자 지정 컴포넌트인지 아닌지를 대소문자로 구분하기 때문

  ```react
  import 컴포넌트명 from './컴포넌트경로' //js 파일은 확장자 빼야함!
  
  function 컴포넌트명() { // 관습적으로 컴포넌트명으로 함수명 작성
      return (
      	<div>
          	<h2>Let's get started!</h2>
              {/*이곳에 가져온 컴포넌트가 들어가게 됨. 시작글자는 대문자여야함!*/} 
              <컴포넌트명></컴포넌트명>
              {/*컴포넌트 사이에 다른 내용이 없으면 아래처럼 사용가능*/}
              <컴포넌트명 />
  
          </div>
      )
  }
  ```

- 정리

  1. Html 코드를 반환하는 함수를 생성해서 export
     1.  이때, 루트 태그는 하나만 존재할 수 있다
     2. 즉, 여러 html 코드를 작성할 경우 하나의 div 태그나 기타 다른 태그로 묶여있어야한다는 것
  2. 컴포넌트를 사용하고 싶은 파일에서 import
  3. import 후 원하는 위치에 html 태그처럼 삽입
     1. 이때, 이름은 반드시 대문자로 시작해야함



##### 만약, JSX를 사용하지 않는다면? (변환 중간과정)

```react
{/* JSX 사용 */}
import Expenses from './Expenses'

function Example() {
    return (
    	<div>
        	<h2>Let's get started!</h2>
            <Expenses items={expenses}/>
        </div>
    )
}
```

```react
{/* React 라이브러리 사용 */}
import React from 'react'
import Expenses from './Expenses'

functioin Example() {
    return React.createElement(
    	'div',{},
        React.createElement('h2', {}, "Let's get started!"),
        React.createElement(Expenses, {items: expenses})
    )
}
```

- React.createElement 매개변수 : 생성할 요소(html태그나 사용자 지정 컴포넌트), 속성, 태그 사이에 들어갈 컨텐츠
  - 이 과정을 거치기 때문에, JSX 코드를 리턴할 때, 하나의 루트 태그만 있어야했던 것
  - 안 그러면 변환 작업에서 React.createElement를 여러개 생성해야하는데 그럴 수 없음

- 과거에는 React 라이브러리를 반드시 import 해야했음. but, 이제는 그러지 않아도 됨



#### CSS 적용하기

- 보통은 특정한 컴포넌트의 CSS를 위해 `컴포넌트.css` 파일을 하나 생성
  - css 파일 작성
- 해당하는 컴포넌트 파일에 css를 적용할 수 있도록 import
  - 단지, import만 하면 됨
  - `import './컴포넌트명.css'`
- JSX 안에서 클래스를 지정할 때는 className으로 지정해야함
  - why?) 
    -  JSX로 작성되는 코드는 html처럼 생겼지만 html이 아닌 JS
    - JS에는 class 가 이미 예약어로 존재, 따라서 다른 클래스 지정 단어가 필요했던 것



#### 동적 데이터 작업하기

- 함수 내부에 필요한 상수 혹은 변수를 설정할 수 있음
  - 일반 자바스크립트 그대로 작성하면 됨
  - return 위에 작성
  - but, 만약 다른 컴포넌트의 데이터를 원한다면, props를 사용해야함
- JSX에 해당 변수 혹은 상수를 넣기 위해서 중괄호 사용
  - `{}` 안에서는 자바스크립트 언어를 작성할 수 있음
  - 변수나 상수를 넣을 수도 있고, 어떤 JS 코드든 가능
    - 단, 문자열로 출력될 수 있는 것만 가능
    - 그래서 date 객체는 그대로 출력이 안됨



#### Props 사용하기 (== 컴포넌트 재사용하기)

##### props

- 어떻게 다른 컴포넌트의 데이터를 사용할 것인가?

- 만약, 특정 컴포넌트 내에서 다른 데이터를 사용하고 싶다면 해당 데이터는 컴포넌트 바깥에서 선언되어야함

  - 바깥 컴포넌트에서 jsx 태그에 속성으로서 전달되기 때문

    ```react
    function App() {
        // 다른 컴포넌트에게 전달할 데이터
        const expense = [
            {
                id: "e1",
                title: "paper",
                amount: 123,
            },
            {
                id: "e2",
                title: "roll_paper",
                amount: 443,
            },
            {
                id: "e3",
                title: "plastic",
                amount: 1453,
            }
        ]
      return (
          // 특정 컴포넌트에 expense 데이터를 전달
          // 전달된 속성들은 전달된 컴포넌트의 매개변수로 받을 수 있음
          <div>
          	<특정컴포넌트 
                title={expense[0].title}
                amout={expense[0].amout}
                ></특정컴포넌트>
            <특정컴포넌트 
                title={expense[1].title}
                amout={expense[1].amout}
                ></특정컴포넌트>
            <특정컴포넌트 
                title="일반 문자열로도 전달이 가능하지"
                amout=14422
                ></특정컴포넌트>
          </div>
      )
        
    }
    ```

    ```react
    // 첫번째 매개변수로 전달받음
    // 이름은 임의로 지을 수 있지만 보통 props로 지음
    function 특정컴포넌트(props) {
        return (
            <div className="expenseItem">
                {/* expense의 title값이 올 것 */}
                <div>{props.title}</div> 
                <div>{props.amout}</div>
            </div>
        )
        
    }
    ```

- props 에는 지정한 모든 속성들이 하나의 객체로 합쳐진 상태로 존재
  - 따라서, `props.속성명` 으로 하위 컴포넌트에서 접근해야함

##### 동일한 컴포넌트를 여러 컴포넌트로 분리하기

- 컴포넌트가 점점 커질 때는 하나의 컴포넌트를 더 작은 컴포넌트 단위로 분리할 수 있음
- 컴포넌트를 작고 집중된 것으로 유지하는 것은 중요한 연습!



#### children props

- 사용자 정의 컴포넌트 태그 사이에 컨텐츠를 넣고 싶다면 children props 사용 필요

- 사용자 정의 컴포넌트 태그 사이의 내용들은 모두  `props.children`에 저장되어 있음

  - 따로 지정하지 않아도 자동으로 저장

- 컨텐츠를 포함하고 있는 컴포넌트 파일에서 래퍼 html 코드를 작성하고 해당 태그 사이에 `{props.children}` 이라고 넣어줘야함

- 사용자 정의 컴포넌트 태그에는 className 적용이 안됨

  - 따라서, className을 props로 받아서 해당 파일에서 직접 작성해야함

- 예시

  ```react
  {/* 메인 컴포넌트 */}
  import ExpenseDate from './ExpenseDate';
  import Card from './Card';
  
  function ExpenseItem(props) {
      return (
      <Card className='expense-item'> {/* 이 사용자 정의 컴포넌트로 아래 내용들을 감싸고 싶다면 Card 컴포넌트 파일에서 작업 필요 */}
              <ExpenseDate date={props.date} />
              <div className='expense-item'>
              	<h2>{props.title}</h2>
                  <div className='expense-item'>${props.amount}</div>
              </div>
      </Card>
      )
  }
  ```

  ```react
  {/* Card 컴포넌트 */}
  
  function Card(props) {
      {/* 사용자 정의 컴포넌트에 className은 적용되지 않음 */}
      {/* 따라서, 해당 컴포넌트 파일에서 아래처럼 직접 지정해주고, return값에 적용시켜야함 */}
      const classes = 'card '+ props.className
      
      return <div className={classes}>{props.children}</div> 
      {/* props.children에는 위 메인 컴포넌트에서 Card 컴포넌트에 감싸져있는 코드들이 있음 */}
  }
  
  export default Card
  ```

  
