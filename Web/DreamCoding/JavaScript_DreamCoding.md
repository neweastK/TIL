# JavaScript_DreamCoding

[toc]

## 1강

- 모든 사용자들이 최신 브라우저들을 사용하고 있지 않음
  - 개발할 때는 최신버전의 ECMAScript로 이용하고 배포할 때는 Javascript Transcompiler를 이용하여 좀 더 낮은 버전의 ECMAScript로 변환하여 코드를 생산
  - 위 역할을 수행하는 것이 Babel!
- SPA
  - 하나의 페이지 안에서 업데이트가 필요한 부분만 수정할 수 있도록 하는 것
  - SPA를 쉽게 만들기 위해 React,Vue 와 같은 프레임워크가 등장





## 2강 _ JS 파일 딩

- Web API
  - 브라우저가 제공하는, 브라우저가 이해할 수 있는 함수들
  - Javascript가 제공하는게 아님
- Javascript의 공식사이트는 developer.mozila.org를 이용할 것



#### HTML에서 Js 파일 포함하기

1. Head 태그 안에 script 포함

   1. HTML을 파싱하다가 script 태그를 만나면 잠시 정지

   2. 지정한 자바스크립트 파일을 다운 받고 실행시킴

   3. 다시 파싱 시작

      ![image-20230202030120852](asset/parsing)

   - 문제점
     - js 파일의 용량이 크다면 소요시간이 매우 길어짐

2. body 가장 아래 script 포함

   1. 전체 페이지가 준비된 다음에 js 파일 다운

   2. 사용자는 페이지를 먼저 확인할 수 있음

      ![image-20230202030441189](asset/body_script)

   3. 문제점

      - 사용자가 기본적인 HTML 컨텐츠를 빨리 볼 수 있지만, JS에 매우 의존적인 사이트라면 사용자가 정상적인 페이지를 볼 때까지 대기시간이 길어짐

3. Head 태그 + asyn

   1. `<script asyn src='main.js'></script>`처럼 head 태그 가장 아래 script 태그를 삽입

   2. 이때, asyn 을 사용하면 main.js 파일 다운로드를 비동기로 실행

   3. main.js를 다운 받으면서 HTML parsing 진행

   4. 만약, 다운로드가 완료되면 잠시 parsing을 멈추고 JS 파일 실행

   5. 그리고 다시 HTML parshing

      ![image-20230202030821476](asset/head_asyn)

   - 문제점
     - 다운로드 받는 시간을 절약할 수 있으나, JS 파일이 HTML parsing 이전에 실행되기 때문에 JS 파일에서 요구하는 HTML 내용이 아직 준비되지 않은 상태일 수 있음
     - 사용자가 페이지를 보는데 여전히 시간이 걸림

4. Head 태그 + defer

   1. main.js를 다운 받으면서 HTML parsing

   2. 만약, parsing이 끝나면, 그때 main.js 실행

   3. 가장 좋은 옵션

      ![image-20230202031123056](asset/head_defer)

   4. 특히, 여러개의 자바스크립트 파일을 사용할 시 더더욱 좋음2



#### Use Strict

- Javascript의 비상식적인 일들을 막아주는 역할
- `'use strict'` 를 가장 위에 작성해주면 예상치 못한 오류를 막을 수 있고, JS 엔진이 더 효율적으로 JS를 분석할 수 있음
  - 즉, 성능 향상까지 기대할 수 있다는 것





## 3강_변수와 데이터 타입

### 변수

- {} 안에서 특정 변수를 선언하면 블록 밖에서는 해당 변수는 참조할 수 없음
- {} 밖의 변수는 글로벌 변수라고 하며, 어디에서든 참조할 수 있음
  - 특정 블록 안에서도 참조 가능
  - 글로벌 변수는 어플리케이션 실행부터 끝날 때까지 메모리에 저장됨
    - **따라서, 최소한으로 사용하는 것이 좋음**
- var의 경우 호이스팅이 되기 때문에 지금은 사용하지 않는게 좋음
  - 게다가, 블록 스코프가 아니기 때문에 혼란스러워짐
    - 즉, 블록 안에서 var 변수를 선언해도, 블록 밖에서 해당 변수 참조 가능
- let vs const
  - const는 해당 변수를 선언하면 수정이 불가함 (Immutable)
    - 웬만하면, 할당 후 변경이 필요없는 값을 const로 선언 및 할당
  - let은 수정이 가능하므로, 수정이 필요한 값에 사용



#### 변수 타입

- 자바스크립트는 Dynamic typing 언어 
  - 변수를 선언할 때 어떤 타입인지 선언하지 않아도 되는 언어
  - 프로그램이 동작할 때 할당된 값에 따라서 타입이 변경될 수 있다는 것을 의미
  - 협업시 많은 충돌을 야기할 수 있음
    - 이에, 타입스크립트가 나오게 된 것
    - 자바스크립트 위에 타입이 얹어진 것



##### 원시타입

> - number, string, boolean, null, undefind, symbol

- number
  - 정수, 실수 상관없이 number로 타입 할당
  - Infinity, -Infinity, NaN 도 number 타입
    - NaN은 숫자가 아닌 값을 다른 숫자와 연산했을 때
    - Infinity는 양의 무한대로, 양수를 0으로 나누면 Infinity
    - -Infinity는 음의 무한대로, 음수를 0으로 나누면 -Infinity
  - -2^53 부터 2^53까지 표현 가능
    - cf) bigInt 타입은 위 범위 밖 숫자도 표현 가능. 숫자 마지막에 n 붙이면 bigInt형으로 변환
    - but, 흔하게 쓰여지지는 않음
- string
  - 모든 문자열의 타입
  - template literals
    - ` 으로 문자열 안에 변수 활용 가능
    - ` 과 ${} 이용
- boolean 
  - false : 0, null, nudefined, NaN, ""
  - true : false를 제외한 값들
- null vs undefined
  - null은 개발자가 의도를 갖고 지정
  - undefined은 변수에 어떠한 값도 없는 경우
- symbol
  - 고유한 식별자를 만들고 싶을 때 사용
  - symbol.description 으로 해당 값을 다시 변환시켜줘야함
    - 그냥 symbol을 사용하면 오류 발생



##### 객체타입

- first-class function이 지원되는 JS
  - 함수를 변수에 할당 가능하고, 다른 함수의 인자로도 전달이 가능하며, 다른 함수에서 return 할 수도 있다
- object를 const로 선언하면?
  - const는 변경 불가하기 때문에 해당 변수를 다른 객체에 할당할 수 없음
  - but, 객체의 내용을 변경하는 것은 가능
    - ex) const obj = { name: "kim", age=20 } 인 경우 obj = { name: "kim", age = 30}으로 변경 불가. but obj.age = 30 으로 변경 가능
    - const는 변수 포인터를 고정시키는 것이기 때문



##### immutable vs mutable

- immutable
  - 변경이 불가능한 데이터 타입
  - 원시타입, frozen objects

- mutable data
  - 변경이 가능한 데이터 타입
  - 모든 객체 타입, 배열
- 변경은 데이터 자체를 의미
  - 즉, 변수에 다른 값을 할당하는 것과는 다른 개념
  - 예를들어, string 타입의 데이터 "KIm"을 메모리에 저장했으면, 해당 값 자체를 "im"으로 변경할 수 없다는 것





## 4강_연산



#### 연산자 

##### String Concatenation ( + )

- 두 문자열을 하나의 문자열로 만들어줌
- 숫자를 나타내는 문자열과 number 타입 사이에 사용할 경우, 문자열로 인식
  - ex) '1' + 2 의 결과는 '12'
- 백팁(`)을 이용하여 literals 사용 



##### Increment and decrement oprators (++ or --)

- 앞에 사용할 경우 연산 후 할당

- 뒤에 사용할 경우 할당 후 연산

- 예시

  ```js
  let counter = 2;
  
  // preincrement
  const preIncrement = ++counter; 
  // 위 코드는 아래 코드와 동일
  counter = counter + 1;
  preIncrement = counter;
  
  // postincrement
  const postIncrement = counter++;
  // 위 코드는 아래와 같음
  postIncrement = counter;
  counter = counter + 1;
  ```



##### Logical Operators

- `||` 

  - 단, 하나라도 true면 true 출력

  - 하나라도 true 값을 확인하면 연산을 멈춤

    ```js
    let value1 = true
    let value2 = false
    function check () {
        console.log("hey")
    }
    console.log(`${ value1 || value2 || check()}`)
    ```

    - value1이 이미 true이기 때문에, true 값 반환 후 종료
    - check 함수를 실행하지 않음

  - 그래서, 함수 혹은 표현식으로 작성된 비교적 무거운 코드를 뒤에 놓는 것이 좋음

- `&&`

  - 단, 하나라도 false면 false 출력

  - `||`와 마찬가지로 하나라도 false 값을 확인하면 연산을 멈춤

  - 간편하게 null 체크할 때 많이 쓰임

    ```js
    nullableObject && nullableObject.something // nullableObject 가 null이 아닐 때만 뒤 메서드 실행
    // 아래 코드와 같음
    if (nullableObject != null) {
        nullableObject.something()
    }
    ```

- `!`

  - true는 false, false는 true를 반환



##### Equality

- `==`

  - JS 자체적으로 타입을 변환 후에 값 비교

  - 같은 값이면 true 아니면 false 반환

  - 같지 않음을 물어볼 경우 `!=`

  - 예시

    ```js
    const kim1 = { name: 'kim'}
    const kim2 = { name: 'kim'}
    console.log(kim1==kim2) // false
    console.log(kim1.name==kim2.name) //true
    ```

    

- `===` 

  - 데이터의 타입까지 비교
  - 같은 값이면 true 아니면 false 반환
  - 같지 않음을 물어볼 경우 `!==`



#### 조건문

##### if

- `if(조건){} → else if(조건){} → else{}` 순으로 작성

##### Ternary Operator

- 조건 ? 값1 : 값2 
- 조건이 true면 값1 실행, 아니면 값2 실행

##### switch

- ```js 
  switch (값) {
      case 조건1:
          console.log("조건1")
          break
      case 조건2:
          console.log("조건2")
      case 조건3:
      case 조건4:
          console.log("조건3 or 조건4")
      default:
          console.log("아무 조건에도 안걸리면")
  }
  ```

  - break가 없으면 위 조건에 해당된다 하더라도 다음 조건도 검사함
    - 즉, break가 없으면 처음부터 끝까지 모든 조건을 확인하게됨 (설령 중간에 조건에 맞는 경우가 있어도)



#### 반복문

##### while

- `while (조건) {}`
- 조건이 true면 계속 반복



##### do while

- `do{} while () {}`
- 먼저 do 안의 명령문을 한번 실행하고 while으로 반복



##### for

- `for (시작값, 조건, 연산) {}`
- 조건이 참이면 계속 반복
- 반복할 때마다 할당한 연산작업 수행
  - 해당 연산작업은 시작값과 조건에 사용된 값을 반드시 변경시켜야함
  - 예를들어, 2씩 증가시켜주는 연산이라면, i+2 가 아닌 i+=2 로 해야, i에 적용됨
- 시작점을 for문 안에서 새로운 변수로 선언할 경우 let 잊지말것!





## 5강 _함수

- 하나의 함수는 한가지의 일만 하도록 만들어야함
- 함수의 이름은 동사 형태로 이름을 지정
  - doSomething : 함수 이름을 짓기 힘들다? 내가 너무 많은 기능을 넣고 있는지 확인해볼 것
- 함수는 JS에서 객체이기 때문에 변수에 할당도 가능 
  - 객체의 메서드도 사용 가능
- 파라미터에 객체를 전달하면, 객체의 reference를 전달
  - 함수 안에서 object의 값을 변경하면, 해당 object 자체의 값이 변경됨
- 함수 안에서 선언된 변수는 함수 안에서만 접근 가능
- return문을 작성하지 않으면 기본적으로 undefined를 반환
- early return, early exit
  - 블록 안에서 로직이 길어지는 것은 좋지 않음
  - 이에, 함수 내에서 조건으로 분기될 때, 조건이 맞지 않는 경우를 위에 작성하는 것을 의미
    - 조건이 맞지 않으면 return을 하므로 맨 위에서 바로 return 하도록 하는 것
    - 가독성이 좋아짐



##### Default Parameters

- 파라미터가 전달되지 않을 때를 대비해서 기본값을 지정해주는 것

  ```js
  function functionName (parameter1='기본값') {
      return 0
  }
  ```

  - `매개변수 = 기본값` 으로 지정



##### Rest Parameters

- `...매개변수` 로 사용

- 해당 매개변수를 배열로 묶어서 전달

  ```js
  function printAll (..args) {
      return args
  }
  console.log(printAll('drama','movie','song')) //['drama','movie','song']
  ```



##### 함수 선언식 vs 함수 표현식

- 특정 변수에 할당한다면 표현식, 아니라면 선언식
- 함수 선언식은 기명 함수만 가능
  - named function(기명 함수) : 이름이 있는 함수
  - anonymous function(익명 함수) : 이름이 없는 함수
- 함수 표현식은 기명 함수, 익명 함수 모두 사용 가능
- 중요 point!!
  - 함수 선언식은 호이스팅이 됨
  - 함수 표현식은 호이스팅 불가



#### Arrow Function (화살표 함수)

- 화살표 함수는 항상 익명 함수
- function 키워드, 블록, 매개변수 괄호 등을 조건에 맞으면 없이 사용 가능



#### IIFE

- 함수를 선엄함과 동시에 호출하는 문법

- 함수 전체를 괄호로 묶고 마지막에 한번더 괄호 세트를 넣어주면 선언과 동시에 호출

  ```js
  (function hello() {
      console.log("hello")
  })()
  ```

  

## 6강 _ Class & Object

- Class는 관련있는 속성(fields)과 행동(methods)가 종합적으로 묶여있는 것
  - method 없이 field로만 있는 경우도 있음 (데이터 클래스)
- Class는 청사진으로 불림
  - 데이터가 들어있지 않고, 템플릿만 정의해놓고, 한번만 선언
  - Class를 이용해서 실제 데이터를 넣어 만들면 Object
  - Class는 메모리에 올라가지 않고, Instance를 생성해야 메모리에 올라감
  - 즉, 데이터가 없는 틀은 Class, 데이터를 틀에 넣어 만들면 Object



#### Class 사용하기

- 선언

  ```js
  class Person {
      constructor(name, age) {
          this.name = name;
          this.age = age;
      }
      speak() {
          console.log(`${this.name}: hello!`);
      }
  }
  
  const me = new Person("Kim", 20)
  
  ```

  - constructor은 new 연산자로 새로운 instance를 생성할 때 자동으로 실행됨

- Getter & Setter

  - 사용자가 잘못된 값을 넣었을 때를 대비해 기본값을 설정해주는 것
  - get은 값을 반환하고, set은 값을 설정
    - 따라서, set에 기본값 설정

  ```js
  class User {
      constructor(name,age) {
          this.name = name;
          this.age = age;
      }
      
      get age() {
          return this._age;
      }
      set age() {
          this._age = value<0 ? 0 : value;
      }
  }
  ```

- Public & Private fields

  - constructor를 사용하지 않고, 그냥 변수를 설정하면 Public Field
  - `#`을 붙여서 변수를 설정하면 Private Field
    - 외부에서 해당 변수에 접근시 undefined 반환

- Static

  - 데이터에 상관없이 클래스가 갖고 있는 고유한 값 혹은 모든 인스턴스에서 동일하게 사용되는 값을 정의

  - Object에 상관없이 공통적으로 클래스에서 쓸 수 있는 데이터는 static으로 작성하는 것이 메모리 사용에 도움을 줌

  - static 값은 Object마다 할당되지 않고 Class에 갖고 있음

  - 즉, static으로 설정하면 호출 주체를 Class로 지정해야함

    ```js
    Class Article {
        static publisher = "Daeshin"
        constructor (articleNumber) {
            this.articleNumber = articleNumber
        }
        
        static printPublisher() {
            console.log(Article.publisher)
        }
    }
    
    const article1 = new Article(1)
    console.log(article1.publisher) //undefined
    console.log(Article.publisher) //"Daeshin"
    ```

- 상속 & 다양성

  - 특정 클래스의 모든 데이터 혹은 메서드를 상속 받아 재선언 없이 사용 가능

    ```js
    class Shape {
        constructor(width, height, color) {
            this.width = width;
            this.height = height;
            this.color = color;
        }
        
        draw() {
            console.log(`drawing ${this.color} color of`)
        }
        
        getArea() {
            return width * this.height;
        }
    }
    
    class Rectangle extends Shape {} //Rectangle 클래스는 Shape 클래스에 있는 모든 요소들을 사용 가능
    
    const rectangle = new Rectangle(20, 20, 'blue');
    rectangle.draw() //drawing blue color of
    ```

  - 특정 클래스 내에서 상속받은 메서드 수정이 필요하다면, 재정의를 통해 수정할 수 있음

    ```js
    class Triangle extends Shape {
        // 부모클래스의 draw 메서드를 수정
        draw() {
            super.draw();
            console.log("modify!!")
        }
        
        // 부모 클래스의 getArea를 덮어 씌우는 것
        getArea() {
            return {this.width*this.height)/2
        }
    }
    ```

    - `super.메서드()`는 부모 클래스의 메서드를 그대로 유지한채 내용을 추가할 수 있도록 함
    - super를 쓰지 않으면 overridng. 즉, 덮어씌워버림
    - 따라서, 부모 메서드의 기능도 유지한채 수정만 하고 싶다면 super 메서드 필요

- instanceOf

  - `인스턴스 instanceOf 클래스` : 입력한 객체가 클래스의 인스턴스인지 아닌지 true/false로 반환
  - `모든 인스턴스 instanceOf Object` or `모든 클래스 instanceOf Object`는 모두 true 값
    - 따라서, Object가 갖고 있는 메서드들을 모든 클래스와 인스턴스는 사용 가능
    - 재정의도 가능

  

​	

