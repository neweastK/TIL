# UI/UX 특강

## UI/UX/DX 디자인 개론, 그래픽 디자인 프로세스 (2022.07.18)

### UI vs UX vs DX

[notion](https://euid.notion.site/euid/SSAFY-UI-UX-8df43425c3794e36bd227003d6c474f4)

#### UI (User Interface)

> 사용자 인터페이스 (User Interface)란 ''사용자가 화면을 통해 시스템을 작동할 수 있는 프로그램"을 말한다

- 웹 애플리케이션 UI, 데스크탑 애플리케이션 UI, 모바일 애플리케이션 UI 등

#### UX (User Experience)

> "사용자가 직접 참여함으로써 생기는 지식이나 기술의 축적"을 말한다.

- 사용자에게 어떤 편의성을 줄 수 있고, 어떤 다양한 경험을 줄 수 있는지 고민을 하며 개발을 한 적이 있는가?

##### UX VS UXD (사용자 경험 VS 사용자 경험 디자인)

- UX : 서비스를 사용하는 사용자의 관점, 생각, 느낌 등을 말함
- UXD : 지속적으로 사용자 경험을 연구해 가정을 검증하는 것을 중심으로 하는 디자인프로세스를 말합니다. 즉, UXD는 설계 프로세스입니다.



##### UI VS UXD

- UI : 사용자와의 상호작욕을 위한 버튼, 이미지, 제목, 표 들이 구성된 인터페이스(ㅍ로그램)
- UXD : 사용자가 이용하는 패턴 혹은 소비심리학 등을 연구하는 것. 즉 UXD의 결과물이 UI인 것



#### 사용자 경험 비교하기

- 좋은 사용자 인터페이셔(UI) 디자인은 사용자가 콘텐츠를 보기 전에 관심을 불러 일으켜야 합니다. 에를 들어 콘텐츠 카드는 이를 위한 완벽한 컴포넌트입니다. 하지만 많은 디자인 결과물은 효율적으로 디자인 되지 못한 모습을 보여줍니다. **너무 많은 정보는 사용자를 압도하고 피곤하게 만듭니다.**
- 콘텐츠 카드 디자인은 **선택에 불필요한 정보를 과감히 제거**해야 사용자 선택을 유도하기 용이합니다. **사용자 결정에 도움이 되는 꼭 필요한 정보만 표시**해야합니다.



#### delete vs remove

- 세트에서 데이터를 제거하는 경우 remove가 적절
- 데이터베이스에서 데이터를 삭제하는 경우 delete가 적절. 
- 즉, 복구가 안되는 경우 delete. 다시 추가가 가능한 경우 remove가 적절
- 이러한 사소한 내용들을 종종 검색해보며 어떤 내용이 더 맞을지 찾아보는 것도 추천



#### 보다 나은 사용자 경험 A11Y

- 사용자 접근을 고려할 때는사용성, 성능, 접근성을 항상 고려하며 개발을 해야함
- 대부분 접근성을 고려하지 못함. 접근성 역시도 사용자 경험 내에서 중요한 부분



#### DX (Designer or Developer Experience)

> "설계자(디자이너 또는 개발자)가 소프트웨어를 사용하는 경험"을 말한다.
>
> 소프트웨어를 경험하는 방식과 프로젝트 내에서 기술을 얼마나 쉽게 사용할 수 있는지에 관한 척도

- 막연하게 개발자의 수고만 요구할 수는 없음
- DX가 높아야 개발자 역시도 UX,UI에 대해 더 쉽게 생각하고 다양하게 생각함



### Graphic Design

#### 유용한 무료 IMAGE 사이트

- xframe.io
- freepik.com
- pexels.com

#### 그래픽을 내보내는 방법

##### Vector(SVG) vs Bitmap

- 로고나 아이콘, 텍스트 같이 단순한 이미지는 Vector가 훨씬 가볍고 빠름, but 사진과 같은 복잡한 이미지를 Vector로 내보낼 경우 매우 무거워짐



- UI 적인 측면에서는 (특히 로고나 버튼) Vector가 용이함
  - but, 구식 브라우저를 지원해야하는 특성상 Vector를 쓰기 어려워함
- 

### Interface Design (with Component)





## UI 디자인 프로세스 (컴포넌트 주도 설계, 아토믹 디자인) (2022.07.20)



## 디자인 토큰을 활용한 UI 디자인 프로세스 (2022.07.22)

> 피그마에서 사용한 토큰을 어떻게 개발자들이 사용할 수 있을까?



#### Figma Tokens Plugin

> 피그마에서 제공하는 navtive token으로는 할 수 없는 것들까지 가능하도록 해주는 매우 강력한 도구

##### 색 배합 만들기(토큰 만들기)

- 색 선택
- Talwind Color Generator 플러그인 선택
- Base Name 선택
- 해당 색을 기준으로 하는 색 조합 생성



##### 토큰 추출 _ 미쳤따리....

- Figma Tokens 열기
- global 선택 & Styles 누르고 import styles 선택
- 원하는 스타일 선택
- 토큰 선택
- 검색창 옆에 json화 시키는 버튼 있음
  - 그럼 모든 figma 토큰들이 json으로 변환됨
- 중간에 닫아버리면 데이터가 날라가므로 접기 버튼을 누를 것!
- create styles를 누르면 Figma Tokens에 저장이 되어있는 스타일들을 현재 작업창에 추가할 수 있음



##### Figma Token을 활용하여 간격을 토큰으로 관리하기

- snap pixel grid 사용
- Nudge amout 로 간격을 지정하면 shift를 누르고 방향키로 이동했을 때 지정한 간격만큼 이동함
- Figma Token 사용하기
  - base로 기준값을 만들어놓음 (ex. spacing.base = 4)
  - 각각 기준에 맞게 스타일 추가
    - spacing.md = {spacing.base} * 2
    - spacing.lg = {spacing.base} * 3
    - spacing.xl = {spacing.base} * 4
  - {} 안에는 기존에 만들어놓은 스타일 토큰을 가져올 수 있음
- 추가로! Theme를 만들어서 적용할 수도 있음



##### Figma Token으로 만든 코드를 JS에서 쓸 수 있도록 변환해야함

> 즉, 컴파일러가 필요함



##### 만약 Token을 수정해야한다면?

- Token을 수정하면 자동으로 json 코드도 수정되게 할 수 없을까?
- Figma Tokens - Settings - Token Storage 설정 (github or gitlab)
  - 수정사항 수정 후 push를 하면 알아서 push 되서 json파일도 수정됨



##### Token내 {}안에 있는 내용들은 figma 안에서만 사용 가능. json에서는?

- package.json의 scripts 에 각 테마별로 저장

- 패키지를 이용 (token-transformer)

- npm run theme:token 찾아보자....

  
