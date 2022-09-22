# Media Query

> 미디어의 상태에 따라 다른 디자인을 적용시키는 것
>
> 반응형 디자인의 핵심

### 사용법

```css
<style>
    @media (width:500px) {
        body{
            background-color: red;
        }
    }
</style>
```

- 화면의 크기가 500px이 되었을 때 body 태그에 해당 스타일을 적용시키겠다

```css
<style>
    @media (max-width:500px) {
        body{
            background-color: red;
        }
    }
</style>
```

- 화면의 크기가 500px 이하일 때 body 태그에 해당 스타일을 적용

```css
<style>
    @media (min-width:500px) {
        body{
            background-color: red;
        }
    }
</style>
```

- 화면의 크기가 500px 이상일 때 body 태그에 해당 스타일 적용

- 만약, 범위를 지정하여 사용하고 싶다면, 스타일 지정하는 순서에 매우 신경써야함

  - 예시

  ```css
  <style>
  	/* 600px 이하일 때 */
      @media (max-width:600px) {
          body{
              background-color: blue;
          }
      }
  	/* 500px 이하일 때 */
      @media (max-width:500px) {
          body{
              background-color: green;
          }
      }
  	/* 600px 이상일 때 */
      @media (min-width:600px) {
          body{
              background-color: red;
          }
      }
  </style>
  ```

  - 500px 이하일 때와 600px 이하일 때 스타일이 겹침
    - but, 500px 이하가 나중에 작성되었기 때문에, 500px 이하에서는 초록색으로 500px~600px일 때는 파랑색으로 표시된다. 
  - 따라서, media query는 대부분 맨 아래에서 사용됨

