# JavaScript_DreamCoding

[toc]

## 1강

- 모든 사용자들이 최신 브라우저들을 사용하고 있지 않음
  - 개발할 때는 최신버전의 ECMAScript로 이용하고 배포할 때는 Javascript Transcompiler를 이용하여 좀 더 낮은 버전의 ECMAScript로 변환하여 코드를 생산
  - 위 역할을 수행하는 것이 Babel!
- SPA
  - 하나의 페이지 안에서 업데이트가 필요한 부분만 수정할 수 있도록 하는 것
  - SPA를 쉽게 만들기 위해 React,Vue 와 같은 프레임워크가 등장





## 2강

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
