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







