# :memo: JavaScript 알고리즘 관련 기록

[toc]



#### 입력값 받기

https://yoon-dumbo.tistory.com/entry/NODEJS-%EA%B8%B0%EB%B0%98%EC%9C%BC%EB%A1%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%92%80%EB%95%8C-%EC%9E%85%EB%A0%A5%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95



#### vs 파이썬

- `문자열 * 횟수` 는 파이썬만 가능

- JS는 `string.repeat(횟수)`로 반복

- 예시('abc' 세번 반복)

  - python

    ```python
    res = 'abc'*3  
    print(res) #'abcabcabc'
    ```

  - JavaScript

    ```js
    res = 'abc'.repeat(3)
    console.log(res) //'abcabcabc'
    ```

- `문자열+문자열`은 파이썬과 똑같이 작동

- 파이썬의 경우 `list(문자열)`로 각 문자를 원소로 하는 배열을 반환할 수 있지만, JS의 경우 `Array(문자열)`로 하면 문자열 전체를 원소로 하는 길이 1의 배열 반환

- replace

  - 파이썬은 따로 count를 지정하지 않는 이상 모든 글자를 지정한 글자로 바꿈
  - but, js는 가장 첫번째 글자만 지정한 글자로 바꿈
    - 모든 이전 사항을 변경하고 싶다면 replaceAll 메서드 사용

- 소수점 (파이썬은 import math 필요)
  - 올림
    - Math.ceil()
    - 파이썬 : math.ceil()
  - 내림
    - Math.floor()
    - 파이썬: math.floor는 내림
    - 파이썬에는 math.trunc() 메서드가 있음(무조건 버림. 걍 없애버리는 것)
  - 반올림
    - Math.round()
    - 파이썬 round()

- 아스키코드 변환
  - 아스키 → 문자열
    - 파이썬 : `chr()`
    - JS : `String.fromCharCode()`
  - 문자열 → 아스키
    - 파이썬 : `ord()`
    - JS : `String.charCodeAt()`
      - cf) charAt(index)는 index에 해당하는 문자열 반환
  
- Spread Operator는 iterable 객체에 다 가능하다!! 문자열도 된다고! [...문자열]
