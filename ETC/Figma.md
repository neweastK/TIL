# Figma 기초 강좌

## 1강

- File 생성

  - 좌측 메뉴바에서 `Team Project` 의 `+` 버튼 or `Drafts`의 `+` 버튼 으로 파일 생성 

  - File에는 두가지 타입 존재

    - Design File : UI/UX 디자인, 프로토타입핑, 디자인 시스템 연관

    - FigJam : UX 리서치, User Flow 제작, 아이디어 수집 등의 목적

- 파일의 위치를 변경하는 법
  - Figma 홈에서 파일을 좌측 메뉴바 중 원하는 위치로 Drag & Drop
- 파일 삭제 복구
  - 파일을 잘못 삭제한 경우 중앙 하단에 생성되는 `undo` 버튼 클릭시 복구
  -  `Undo`를 클릭하지 못한 경우 Drafts - Deleted - 우측클릭 - Restore 클릭
- UI Kit 활용
  - 컴포넌트 : 재사용이 가능한 UI 구성요소
  - Home - Explore Community - 원하는 ui kit 검색
  - 원하는 kit를 Duplicate 하여 개인 Drafts로 복제
  - 복제된 kit에서 `Layer` 옆에 `Assets` 활성화
  - 검색창에서 원하는 status 검색
  - 원하는 status 클릭시 캠퍼스 영역의 해당 status가 있는 컴포넌트 부분으로 Focus 됨
    - `Shift` +`2` 로 해당 영역으로 zoom in
  - 원하는 status가 있는 컴포넌트를 선택한 상태에서 Layer 패널을 보면 Layer명 앞에 4개의 마름모 기호가 표시되어 있음
    - 메인 컴포넌트라는 뜻
  - 해당 메인 컴포넌트의 하위 레이어에서 어떻게 variate 되어있는지 확인 가능
  - 컴포넌트를 감싸고 있는 가이드 Frame 전체를 복사하고 작성 중 파일로 이동하여 Page를 추가하고 해당 페이지에 붙여넣기
    - 외부이 컴포넌트를 복사하여 로컬 컴포넌트로 추가 가능
- 캔버스에서 객체 정렬
  - 화면의 전체 Frame 선택
  - Design 패널 - Align - Tidy up 옵션을 사용하여 Frame 간의 간격 일정하게 조율 가능
  - 마우스로 드래그하여 전체 간격을 일정하게 조정 가능
    - or 직접 숫자를 입력하여 Frame 간 간격 조절 가능
  - Frame 중앙에 있는 원형 Key를 마우스로 드래그하여 순서를 바꾸는 것도 가능
- 스크롤 기능
  - Frame의 사이즈가 목업 사이즈보다 길어야 함
  - 스크롤 시 고정이 되도록 하기 위해서는 특정 컴포넌트의 Design 패널에서 Fix position when scrolling 옵션 체크



## 2강

### [1. 피그마 스타일 정의 | 버튼 생성하기 Part1 ]

※ 컴포넌트 : 두 번 이상 재사용될 UI Asset



#### Create Style 기능 

- Button 생성 

  - Text 단축키 `T` - button 입력
  - 오른쪽 디자인 패널에서 원하는 텍스트 스타일 지정
    - Resize option의 Auto width : 텍스트 길이에 따라 가로 길이가 자동으로 조정됨
    - Type Details 에서 더 상세한 옵션 설정 가능 ex) 대문자 사용 방법 등
  - Drag & Drop으로 복사 이후 `ctrl`+`D` 입력시 같은 방향으로 객체가 자동으로 복사됨

- 스타일 저장

  - 디자인 패널 - Style - `+` 버튼(Create Style) - 스타일 이름 지정
    - 스타일 이름 지정시 `/` 로 구분하여 스타일을 Group화 가능 
    - `/` 앞이 그룹 뒤가 스타일 이름 ex) Button / Md : 버튼 그룹의 Md 스타일

- 스타일 편집

  - 스타일을 선택하고 오른쪽 Edit Style 버튼 클릭
  - 변경 시 같은 스타일로 연결된 모든 요소에 변경사항 자동 적용
  - `alt` + `좌우 드래그` 로 글자 size 조정 가능

- Figma Plugin

  - Figma Community - Styler 설치 (Plugin 이름임)

- 그룹 지정 및 동시에 이름 변경하기

  - 원하는 객체 모두 선택
  - Rename 단축키 `ctrl` + `R` 입력
  - `/`를 이용하여 그룹을 지정하고 `Current Name` 클릭
  - 그럼 지정한 그룹 안에 해당 객체의 이름들이 모두 한번에 저장됨

- 스타일로 지정하기

  - 위에서 생성한 그룹을 모두 선택 후 마우스 우클릭 - Plugins - Styler - Generate Styles를 클릭하여 Style 생성
  - 오른쪽 디자인 패널에서 텍스트 스타일 확인 가능
  - 텍스트 뿐만 아니라 컬러 스타일도 지정 가능

  



### [ 2. 피그마 오토 레이아웃 기능 | 버튼 생성하기 Part2 ]





### [ 작업시간을 줄여주는 Auto Layout 기능 | Figma 핵심 기능 Part1 ]

#### Auto Layout으로 버튼 만들기

1. Text만 입력(Button) 후 `Shift`+`A` 입력
   - `Shift`+`A` : Auto Layout 단축키
2. 왼쪽 Layers 에서 텍스트 바깥쪽으로 Frame이 생성됐음을 확인할 수 있음
   - 해당 프레임은 일반적인 프레임과 형태가 다름
   - `alt`+`마우스 Hover` 해당 객체의 여백 등 간격 정보 확인 가능
3. 텍스트를 수정할 때 혹은 여러개의 버튼을 만들 때 등 박스 길이,간격 등이 자동으로 조정되기 때문에 편리
4. 버튼끼리의 순서를 바꿀 때에도 디자인 패널에 상하 화살표 버튼으로 쉽게 이동 가능



### [ 효율적인 UI 디자인을 위한 컴포넌ㅌ 기능 | Figma 핵심 기능 Part2 ]

#### 컴포넌트

- 버튼, 카드, 다이얼로그처럼 반복적으로 사용될 UI 또는 패턴



#### 컴포넌트 만들기

- 컴포넌트로 만들 요소들을 선택 후 마우스 우클릭 - Create Component 클릭 == 마스터 컴포넌트 생성
- `Shift` + `alt` + `Drag` : 마스터 컴포넌트의 Instance 생성
  - 마스터와 instance는 앞에 아이콘으로 구분 가능
  - 마스터 컴포넌트를 수정하면 instance도 수정됨
- 여백을 조정할 때는 내부 요소의 크기를 조정함으로써 조정하는 것 같아 보임
  - Constraints에서 옵션을 가로는 Left & Right 로 설정 세로는 Center로 설정
  - 크기를 조정해도 가운데로 계속 정렬됨
  - 단 크기를 조정할 때 내부 요소의 크기도 같이 변경되는 것을 원할 경우 Constraints를 Scale로 변경해야함
- Instance를 선택한 후 중앙 상단에 마스터 컴포넌트 버튼을 누르면 해당 인스턴스는 새로운 마스터 컴포넌트가 됨

- 같은 그룹내의 마스터 컴포넌트들은 각각의 인스턴스에서 쉽게 스위칭이 가능함
