## CSS Selectors

- cheet sheet 검색하여 활용 추천
- css는 같은 태그에 스타일이 두 개 이상 지정될 경우 뒤쪽에 있는 스타일이 지정됨

#### 각종 선택자 혼합하여 사용하기

- T라는 태그들 중 "active"라는 클래스를 가진 T 태그만 뽑고 싶다면?

  - `TagName.ClassName`처럼 사용 따라서, T.active라고 선택하면 됨

- 여러개의 선택자를 사용하고 싶다면, `,`로 여러 선택자를 사용할 수 있음

- 페이지 내의 모든 태그 선택하기 : `*`

- 형제 선택자 선택하기 (인접 태그 선택하기)

  - `Tag1 + Tag2` : 태그 1에 바로 인접해있는 태그2만 선택하기
  - `Tag1 ~ Tag2` : 태그 1에 인접되어 있는 모든 태그2 선택하기

- 그냥 띄어쓰기는 자손, `>` 는 자식

  - 자식은 바로 밑에 있는 태그들만 (위에 `+`와 비슷)
  - 자손은 자식의 자식, 자식의 자손까지도 영향력을 끼침
  - 인접 선택자는 태그 선택자 뿐만 아니라 id, 클래스 선택자 자식, 자손도 지정할 수 있다.

  

### pseudo class selector (가상 클래스 선택자)

#### active

- element가 클릭된 상태일 때의 스타일 지정

#### hover

- 마우스를 올려놓았을 때의 스타일 지정

#### visited 

- a 태그에서 방문한 경우의 스타일 지정
- 보안 문제로 일부 속성만 사용할 수 있음

#### link

- 방문하지 않은 a 태그의 스타일 지정

#### focus

- 해당 element에 focus 되어있을 때
  - ex) 여러 input 태그 중 입력하고 있는 input 태그
  - 혹은 tab 키를 눌렀을 때 선택되는 것을 focus 된 경우라고 함

#### first-child

- `Tag:firsth-child` 는 웹페이지에서 가장 첫번째로 등장하는 Tag
- `Parent Tag:first-child` 는 Parent 태그 밑에 있는 Tag 중에 첫번째로 등장하는 Tag

#### only-child

- 어떤 element 본인이 누군가의 **유일한** 자식일 경우, 해당 element를 선택
-  즉, 형제가 없는 자식 태그들을 의미

#### last-child

- 모든 마지막 자식 태그 선택
- `Tag:last-child`는 Tag들 중에 가장 마지막에 있는 태그만 선택
  - 만약, 해당 Tag가 마지막에 있는 경우가 없다면 선택 불가
- `ul li:last-child` 라고 한다면, ul 태그 아래에 li태그 중 위치가 맨마지막인 li태그만 선택

#### nth-child(N)

- `element:nth-child(N)` : element 태그들 중에서 N번째 자식으로 위치한 태그
- `div p:nth-child(2)` : div의 2번째 자식으로 위치하고 있는 모든 p태그
- 시작은 0이 아닌 1

#### nth-last-child(N)

- nth-child와 같지만 뒤에서부터 순서를 카운트한다
- 즉, 뒤에서 N번째에 위치한 자식 태그
- 시작은 0이 아닌 1

#### first-of-type

- 가장 처음으로 등장한 태그 선택
- `span:first-of-type` : span 태그 중가장 처음 등장한 span 태그 선택

#### nth-of-type(N)

- `div:nth-of-type(2)` : div 태그 중에서 두번째 div 태그 선택
- `div:nth-of-type(even)` : div 태그 중에서 짝수번째의 div 태그 선택
  - `nth-of-type(2n)` 과 같이 선택 가능
- `div:nth-of-type(odd)` : div 태그 중에서 홀수번째의 div 태그 선택
  - `nth-of-type(2n+1)` 과 같이 선택 가능
- 시작은 0이 아닌 1

#### only-of-type

- `element:only-of-type` : element의 형제 중 자기 자신과 같은 형제가 없는 element 선택
- 만약, 형제가 있다 하더라도 지정한 태그가 아니면 상관없음. 본인과 같은 태그가 형제로 존재하면 문제가되는 것

#### last-of-type

- `div:last-of-type` : div 태그 중에 가장 마지막 div 태그
- `p span:last-of-type` : p 태그 내에 존재하는 모든 마지막 span 태그

#### empty

- `div:empty` : div 태그 중 자식을 갖고 있지 않은 div 태그들

#### not(X)

- `:not(#fancy)` : id 값을 fancy로 갖지 않는 모든 태그
- `div:not(:first-child)` : 첫번째 자식이 아닌 모든 div 태그
- `:not(.big, .medium)` : big 클래스와 medium 태그가 아닌 모든 태그
