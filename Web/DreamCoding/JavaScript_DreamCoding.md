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

  

## 6강 _ Class vs Object

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

  

## 7강 _ Object

> - JS 데이터 타입 중 하나
> - 기능적으로 연관된 데이터의 모음
> - 거의 모든 오브젝트는 Object 클래스의 인스턴스
> - Object는 키와 값의 집합체
>   - Object는 키로 접근해서 값을 얻어온다



#### Object를 만드는 법

- Object Literal Syntax
  - `const obj1 = {}`
- Object Constructor Syntax
  - `const obj2 = new Object()`
- 처음 생성한 이후에도 새로운 키와 값을 추가하거나 기존 값을 삭제 할 수 있음
  - 새로운값 추가 : `obj.키이름 = 값` or `obj['키이름'] = 값`
  - 기존값 삭제 : `delete obj.삭제할키이름`



#### Computed properties

- 키에 접근하는 방법
  - `obj.키이름`
    - 어떤 키를 받을지 명확하게 아는 경우
  - `obj['키이름']`
    - 반드시 키 이름은 문자 타입으로
    - 코딩 시점에 정확하게 어떤 키가 필요한지 모를 때 사용 (사용자에게 입력을 받는다거나 할 때)



#### Property value shorthand

- 객체 내의 key와 value의 이름이 같다면 둘 중 하나만 작성해도 됨

  - 예시

    ```js
    function makePerson(name,age) {
        return {
    	    name,
        	age
        }
    }
    ```

    - `{ name: name, age:age }` 처럼 작성할 필요가 없다는 것



#### 연산자

##### in

- `key in object` : 해당 키가 객체 안에 있는지 true/false 반환 (key는 문자열로 작성)

##### for in

- 객체를 순회하면서 객체의 키값을 반환
- 배열에 사용할 경우 인덱스 반환

##### for of

- 배열을 순회하면서 각 값을 반환
- 객체에서 사용할 경우 오류남



#### 복사

- 기존에 있던 obj1을 obj2라는 새로운 변수에 할당하게되면 얕은 복사가 됨
  - obj1에서 값을 바꾸면 obj2도 값이 바뀌고, obj2에서 값을 바꾸면 obj1에서도 값이 바뀜
- 깊은 복사
  - Object 클래스의 assign 메서드 사용
    - `Object.assign(target, source)`
    - 복사하고자 하는 source를 복사하려는 target 
    - 여러개의 source를 매개변수로 설정할 수 있음
    - 따라서, target에는 빈 객체를 넣고 복사하고 싶은 객체를 source에 넣으면 됨
    - source가 여러개이면서 key값이 겹치는 경우가 있다면 가장 뒤에있는 값으로 덮어 씌워짐



## 8,9강 _ Array

#### 선언

1. `new Array()`
2. `[]`



#### 접근

- `배열[index]`
  - 생각해보니 객체의 value에 접근할 때는 `객체[key]`로 접근
  - 배열도 위와 마찬가지, 배열에서의 key값은 인덱스이기 때문



#### 순회

- `for (let i = 0; i<array.length; i++) {}`
- `for ( a of array) {}`
- `forEach (callback(value, index, array){})`



#### 삽입, 삭제

- `Array.push()` : item을 뒤에 삽입
- `Array.pop()` : item을 뒤에서 추출
- `Array.unshift()`: item을 앞에 삽입
- `Array.shift()`: item을 앞에서 추출
- **pop,push보다 shift,unshift가 훨씬 느림!!**
  - 특히, 배열이 길면 길수록 성능은 더 안좋아짐
- `Array.splice(start,count)`: 배열의 start 인덱스부터 count만큼 삭제
  - 만약, count를 지정하지 않으면 array[start:] 삭제
  - count 인자 뒤에는 해당 값을 지우고 삽입할 값들 입력
    - ex. `arrays.splice(1,1,"hi","hello")`
    - 배열의 1번 인덱스 값을 지우고 "hi", "hello" 문자열 삽입
- `Array.concat(newArray)` : 기존에 있던 배열에 새로운 배열을 이어붙임



#### 검색

- `Array.indexOf(item)` : item의 가장 앞의 인덱스 번호를 반환 (없으면 -1 반환)
- `Array.lastIndexOf(item)` : item의 가장 뒤의 인덱스 번호 반환 (없으면 -1 반환)
- `Array.includes(item)` : 배열에 item이 있는지 없는지를 true/false로 반환



#### 메서드

##### join(`구분자`)

- 구분자를 생략하면 기본적으로 `,`로 구분된 문자열 반환
- 원본 배열 변화 없음



##### split(`구분자[,사이즈]`)

- 구분자를 생략하면 문자열 전체가 배열 하나의 원소가 되어버림
  - `['a,b,c,d']` 처럼 되어버림
  - 즉, 길이 1의 배열이 반환되는 것
- 사이즈는 return 받을 리스트의 사이즈 설정 가능



##### reverse()

- 배열을 역순으로 정렬
- 원본 배열도 순서가 변경됨
- 변수에 할당하면 해당 변수에도 정렬된 배열이 들어감
- 즉, 원본 배열 자체의 순서를 변경하면서, 변경된 배열을 반환도 함



##### sort(callback(previousValue,currentValue) { return previousValue-currentValue})

- 콜백함수의 return 값이 음수라면 첫번째 값이 다음 값보다 작다고 판단하고 정렬
- 오름차순 정렬할 때 
  - `array.sort((a,b) => a-b)`
- 내림차순 정렬할 때
  - `array.sort((a,b) => b-a)`









##### splice(start,end) & slice(start,end)

- splice는 원본 배열 자체를 변경하고, 삭제한 요소들을 return
- slice는 start인덱스부터 end인덱스까지의 배열을 반환함
  - 단, end는 포함하지 않음
  - 배열 자체를 수정하지 않음



##### find(`callback(value, idx, obj)`{return boolean})

- find 메서드를 호출한 배열의 각 요소를 순차적으로 호출
- find의 콜백함수는 boolean을 리턴해야함
- 만약, true값이 return 되면 find 메서드는 즉시 종료
  - 그러면서 true일 때의 원소를 반환
- 즉, true 값을 반환하는 첫번째 원소만 반환



##### filter(callback(value, idx, obj){return boolean})

- 콜백 함수가 true 값을 반환하는 원소들만 모아서 새로운 배열 반환



##### map(callback(value,idx,obj){ })

- 콜백함수가 반환한 값들로 이루어진 배열 반환
- 즉, 원본 배열의 요소들에 동일한 작업을 진행하고 싶을 때 사용할 수 있음



##### some(callback(value,index,obj){ return boolean })

- 배열의 원소 중 콜백함수의 반환값이 true인 원소가 하나라도 있다면 true 반환
- 하나도 없다면 some 메서드는 false 반환



##### every(callback(value,index,obj){return boolean})

- 배열의 모든 원소에 대해 콜백함수의 반환값이 true라면 true 반환
- 단 하나라도 false인 원소가 있다면 false 반환



##### reduce(callback(previousValue, currentValue, currentIndex), initialValue)

- 콜백함수에서 return 되는 값은 계속해서 누적되어감
- previousValue는 이전 단계에서 return된 값
  - 즉, 지금까지 누적된 값을 의미
- initialValue는 기본값 (시작값)





## 10강 _ JSON

#### HTTP

- Hyper Text Transfer Protocol
- 서버와 클라이언트가 어떻게 hypertext를 주고 받을지 정해놓은 규약
- hypertext는 웹사이트에서 전반적으로 이용되고 있는 문서,파일,이미지와 같은 모든 리소스들을 포함



#### AJAX

- Asynchronous JavaScript And XML
- HTTP를 이용하여 서버에게 데이터를 요청하여 받아올 수 있는 방법 중 하나
- 웹페이지에서 동적으로 서버에게 데이터를 주고 받을 수 있는 기술
- XML : HTML과 같은 마크업 언어 중 하나로 태그를 이용하여 데이터를 표현함
- 예시
  - XHR Object
    - XML Http Request
    - 브라우저 API에서 제공하는 Object 중 하나
    - 간단하게 서버에게 데이터를 요청하고 받아올 수 있음
    - but, XML은 불필요한 태그가 너무 많아 파일 사이즈가 커지고, 가독성이 좋지 않아 최근에는 많이 사용하지 않음
  - fetch() API



#### JSON

- JavaScript Object Notation
- key와 value로 이루어진 데이터 포맷
- 데이터를 주고 받을 때 쓸 수 있는 가장 간단한 파일 포맷
- 텍스트 기반으로 매우 가볍고 가독성이 좋음
- 프로그래밍 언어나 플랫폼과 관계없이 사용할 수 있음
- serialize와 deserialize에 대해 공부해야함



##### serialize & deserialize

- `JSON.stringify(객체[,replacer])`

  - 데이터를 문자열로 변환

  - 객체 내 함수는 제외된 후 변환

  - replacer로 상세하게 조정 가능

    - 배열로 사용할 경우, 배열 내 원하는 프로퍼티를 지정하면 해당 프로퍼티의 값만 변환됨

      ```js
      const json = JSON.stringify(obj. ['name','size'])
      ```

    - 콜백함수는 key와 value를 매개변수로 받는 함수 선언

      - return값에서 3항 조건문으로 원하는 value로 수정 가능

        ```js
        const json = JSON.stringify(obj, (key,value) =>
                                    return key==='name' ? 'kim' : value
        ```

        

- `JSON.parse(문자열[,reviver])`

  - 문자열(json)을 객체로 변환

  - stringfy 과정에서 사라진 함수는 parse를 통해 객체로 되돌려도 다시 생기지 않음

  - 또한, stringfy 과정에서 Date 객체 같은 것들도 모두 string 형태로 변환됐었음

    - 따라서, parse를 통해 object로 가져온다해도, Date 객체로 살아나지 않고 string으로 되어있음

  - reviver로 상세하게 조정 가능

    - 콜백 함수에서 key와 value를 매개변수로 가짐

    - 삼항 조건문으로 여러 조건에 따라 받아오는 데이터의 타입을 바꿀 수 있음

      ```js
      const obj = JSON.parse(json, (key,value) => {
          return key==='birthDate' ? new Date(value) : value
      })
      // 키가 birthDate면 Date 객체로 받고, 아니면 그냥 문자열 그대로 받겠다는 뜻
      ```



##### 유용한 사이트

- JSON Diff
  - 두 JSON을 비교해서 다른 부분을 찾아줌
- JSON Beautifier
  - JSON의 포맷을 예쁘게 수정해줌
- JSON Parser
  - JSON이 object로 변환시켰을 때의 모습을 보여줌
- JSON Validator
  - JSON이 유효한 데이터인지 아닌지 오류를 찾아줌





## 11강,12강,13강 _ 비동기 프로그래밍

#### 동기(synchronous) vs 비동기(Asynchronous)

- 자바스크립트는 동기적 언어
  - 호이스팅 된 이후부터 코드가 작성한 순서대로 하나씩 수행된다는 것

- 비동기는 언제 코드가 실행될지 예측할 수 없는 것
  - 즉시 코드를 실행하지 않고 다음 코드로 넘어감
  - 정해진 시점에 코드가 실행됨
    - 즉, 정해진 순서대로 코드가 실행되지 않는다는 것을 의미
- 콜백함수라고 무조건 비동기인 것은 아님
  - 어떻게 함수를 구성하냐에 따라 동기,비동기로 나눠짐



#### 콜백지옥

- 콜백함수 내에서 다른 콜백함수를 호출하고 또 내부에서 다른 콜백함수를 부르면서 가독성이 매우 떨어지는 코드
  - 이해하기도 읽기도 어려움
  - 에러와 디버깅이 아주 어려워짐
- 콜백지옥 해결하기
  - Promise, Async & Await



#### Promise

> - JS에서 제공하는 비동기를 간편하고 깔끔하게 처리해주는 내장 Object
> - 정해진 기능을 수행하고 나서 정상적으로 기능이 수행됐다면 성공 메시지와 결과값 전달
>   - 기능이 수행되지 못했다면 에러 발생



##### 중요 포인트

- 상태 : 프로세스가 기능을 수행중인지 완료되었는지를 나타냄
  - 기능이 수행중일 때는 pending 상태
  - 기능을 성공적으로 끝내면 fulfilled
  - 파일을 찾을 수 없거나 네트워크에 문제가 생기면 rejected
- producer / consumer
  - Producer : 원하는 기능을 수행해서 해당하는 데이터를 만들어냄
  - Consumer : 우리가 원하는 데이터를 소비
- Promise를 활용한 비동기 작업은 주로 무거운 일들을 수행
  - 네트워크에서 데이터를 받아오거나 파일에서 데이터를 읽어오는 경우
  - 즉, 시간이 조금 걸리는 일들은 비동기 처리하는것이 좋음



##### 사용법

- new 키워드로 Object 생성(Producer)

  - `new Promise(callback(resolve:기능을 정상적으로 수행했을 경우 호출할 함수,reject:기능을 수행하다가 오류가 발생했을 경우 호출할 함수))`
  - **Promise가 생성되는 순간 callback 함수는 자동으로 수행됨!!**

  ```js
  const promise = new Promise((resolve,reject)=>{
      // 2초 뒤에 실행하는 함수는 resolve에 kim을 넣어서 반환
      setTimeout(()=>{
          resolve('kim')
          reject(new Error('no network'))
      },2000)
  })
  ```

  - resolve는 정상적으로 수행됐을 경우 전달할 데이터를 매개변수로 가지며 호출 - promise 객체의 then이 수행됨
  - reject는 작업이 비정상적으로 종료됐을 때 호출되며, 주로 매개변수로 Error 객체를 받음 - promise 객체의 catch가 수행

- 만들어진 promise 사용하기

  - then, catch, finally 사용
  - then : 작업이 정상적으로 잘 수행된 경우
    - `promise.then(callback(value=resolve로부터 받은 데이터))`
  - catch : 에러가 발생했을 경우
    - `promise.catch(callback(error))`
  - finally : 성공,실패 상관없이 마지막에 무조건 호출됨
    - `promise.finally(callback())`

  ```js
  // setTimeout으로 resolve에 전달한 kim이 value에 담김
  promise
      .then(value=>{
      	console.log(value)
  	}) // then은 같은 promise 객체를 반환함. 따라서, catch를 바로 붙일 수 있음
  	.catch(error=>{
  	    console.log(error)
  	})
  ```

- 즉, promise 객체를 만들 때, 비동기적으로 수행하고 싶은 코드를 작성

  - 성공적으로 잘 됐다면 resolve 호출
    - then으로 성공한 값을 받아와 처리
  - 실패했다면 reject를 호출
    - catch로 실패한 에러를 받아와 처리

- Promise Chaning

  ```js
  const fetchNumber = new Promise((resolve,reject) => {
      setTimeout(() => resolve(1),1000)
  })
  
  fetchNumber
  .then(value => value*2)
  .then(value => value*3)
  .then(value=> {
      return new Promise((resolve, reject) => {
          setTimeout(() => resolve(num-1), 1000)
      })
  })
  .then(num => console.log(num))
  ```

  - then은 값을 전달 할 수도 있지만, promise 객체를 전달해도 됨

- Error Handling

  ```js
  const getHen = () => 
      new Promise((resolve,reject) => {
          setTimeout(() => resolve('🐓'), 1000)
      });
  const getEgg = hen =>
  	new Promise((resolve, reject) => {
          setTimeout(() => resolve(`${hen} =>🥚`),1000)
      })
  const cook = egg =>
  	new Promise((resolve, reject) => {
          setTimeout(() => resolve(`${egg} =>🍳`),1000)
      })
  
  getHen()
  .then(hen => getEgg(hen))  // ==.then(getEgg)
  .then(egg => cook(egg))  // ==.then(cook)
  .then(meal => console.log(meal)) // ==.then(console.log)
  // 결과값
  // 🐓=> 🥚 =>🍳
  ```

  - 만약, 오류가 생겼고, 이때 다른 자원으로 대체하고 싶다면?

  ```js
  const getHen = () => 
      new Promise((resolve,reject) => {
          setTimeout(() => resolve('🐓'), 1000)
      });
  const getEgg = hen =>
  	new Promise((resolve, reject) => {
          setTimeout(() => reject(new Error(`error! ${hen} =>🥚`),1000)
      })
  const cook = egg =>
  	new Promise((resolve, reject) => {
          setTimeout(() => resolve(`${egg} =>🍳`),1000)
      })
  
  getHen()
  .then(hen => getEgg(hen))  // ==.then(getEgg)
  .catch(error => return '🥖')
  .then(egg => cook(egg))  // ==.then(cook)
  .then(meal => console.log(meal)) // ==.then(console.log)
  // 결과값
  // 🥖=>🍳
  // catch를 중간이 아닌 맨뒤에 놓으면 (.catch(console.log(err)))
  /// 결과값은 에러 메시지가 나옴
  ```

  - 즉, 어떠한 에러를 처리하거나 대체하고 싶다면 해당 promise 뒤에 바로 catch를 사용해야함



#### async & await

- promise도 chaining 되다 보면 코드가 복잡해짐
  - 이를 보완하기 위한 syntactic sugar

- promise를 사용하는게 옳을 때도 있고, async&await을 쓰는게 더 맞는 경우도 있음

  - 때에 따라 다르게 사용할 수 있어야함

- 예시

  ```js
  function fetchUser() {
      // 10초 걸리는 네트워크 작업이라 가정
      return 'kim'
  }
  
  const user = fetchUser();
  // 10초 후에 'kim'을 출력
  console.log(user)
  
  // ------ promise 로 비동기 처리 -----
  fuction fetchUserPromise() {
      return new Promise((resolve,reject) => {
          // 이 안에서 비동기로 처리할 작업 정의
          resolve('kim')
      })
  }
  
  const user1 = fetchUserPromise();
  user1.then(console.log)
  
  // ----- async -----
  async function fetchUserAsync() {
      return 'kim'
  }
  const user2 = fetchUserAsync();
  user2.then(console.log)
  
  
  // ----- await -----
  // async가 붙은 함수 안에서만 사용 가능
  function delay(ms) {
      return new Promise(resolve => setTimeout(resolve, ms))
  }
  
  async function getApple() {
      // delay 함수가 완료될 때까지 기다림
      await delay(3000);
      // async에서는 return 되는 값이 promise에서의 then의 인자
      return 'apple'
  }
  
  async function getBanana() {
      await delay(3000);
      return 'banana'
  }
  
  // getBanana를 promise로 만들면?
  function getBananaPromise() {
      return delay(3000)
      .then(()=>'banana')
  }
  
  // 좀 더 복잡한 함수 비교
  // promise
  function pickFruits() {
      return getApple().then(apple => {
          return getBanana().then(banana => `${apple} + ${banana}`);
      })
  }
  pickFruits().then(console.log) // 6초 뒤에 'apple+banana' 출력
  
  // async & await
  async function pickFruitsAsync() {
      const apple = await getApple()
      const banana = await getBanana()
      return `${apple} + ${banana}`;
  }
  pickFruitsAsync().then(console.log)
  ```
  
- async에서 오류 처리는 어떻게?

  - promise 는 reject를 이용했음

  - async에서는 try catch 를 이용하면 됨

    ```js
    async function pickFruits() {
        try {
            const apple = await getApple()
        }
        catch(err) {
            console.log(err)
        }
    }
    ```

- 두가지 비동기 함수가 서로에게 영향을 미치지 않을 때 동시 처리하기

  - Promise의 API (all) 사용

    ```js
    async function pickAllFruits() {
        // 인자로 넣은 배열에 속한 함수들이 모두 완료되면
        return Promise.all([getApple(), getBanana()]);
        // 반환값이 모두 담긴 배열 반환
        .then(fruits => fruits.join(' + '))
    }
    pickAllFruits().then(console.log)
    ```

  - Promise의 API(race)

    ```js
    function pickOnlyOne() {
        // 배열 안에 있는 함수 중 먼저 반환된 것만 반환
        return Promise.race([getAplle(), getBanana()]);
    }
    pickOnlyOne().then(console.log)
    ```

  



