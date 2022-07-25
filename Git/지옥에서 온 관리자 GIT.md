# GIT _ 지옥에서 온 관리자 GIT

[toc]

## 1강_GIT 배경지식

### GIT 

- UNIX = 대형 컴퓨터 운영체제
- LINUX = 리눅스 토발즈가 개인용 컴퓨터에 맞는 OS로 UNIX를 발전 시킨 것
- GNU(General Public License == 공개 소프트웨어 프로젝트)
  - 누구에게나 소프트웨어에 관한 모든 것을 공개하겠다
  - 단, 공개를 받았으면 **GPL 라이센스**를 따라야한다
- GPL 라이센스
  - GNU로 개발된 소프트웨어를 업그레이드 시켜서 새로운 소프트웨어를 만들었을 경우, 무조건 공개되어야한다(강제성)
  - LINUX의 철학
- LINUX에서 사용중이던 bitkeeper라는 이름의 분산 버전 관리 시스템 프로그램이 상용화되면서 유로로 바뀜
  - 이에 리눅스 토발즈가 Bitkeeper의 기술을 바탕으로 하며 부족한 점을 업그레이드 한 버전관리시스템 GIT을 만듦
  - GIT 역시도 GNU로서, GPL 라이센스를 따름



### Github

- GIT은 프로그램이고 Github는 개발자들의 코드가 저장되는 클라우드 저장소 == 개발자들의 놀이터

  

### 버전 관리 시스템

#### VCS

> 문서나 설계도, 소스 코드 등의 변경점(변경 이력)을 관리해주는 소프트웨어
>
> 수정할 때마다 전체를 변경하는 것이 아닌 변화 내용을 복사하고 기록하는 것

<img src="../assets/git/VCS.png" alt="img" style="zoom: 50%;" />

- 나중에 특정 시점의 버전을 다시 불러올 수 있음

- 부분 변경이기 때문에 시간과 용량 절약 가능
- but, 바이러스 걸리면 해결 불가(백업 필요)
- 협업이 불가함 
  - VCS는 로컬에서만 관리하기 때문
  - 로컬 버전관리의 경우 간단히 데이터베이스를 사용해서 파일의 변경 정보를 관리함



#### CVCS(중앙 집중형 버전 관리 시스템)

> 서버와 클라이언트를 분리하여 중앙의 서버에서 변경 이력을 관리하는 것

<img src="../assets/git/CVCS.png" alt="img" style="zoom:50%;" />

- 파일을 모두 중앙 집중 컴퓨터에서 관리

- 협업이 가능
  - but, 업로드 된 데이터로 덮어씌워질 가능성이 있어 백업이 필요
  
- 중앙 집중 컴퓨터에 문제가 생길 경우 모든 과정에 문제 발생

  - 서버의 정보가 날아갈 경우 모든 히스토리가 날아가게 됨

    == 클라이언트들은 히스토리를 갖고 있지 않다. 서버에만 히스토리가 저장되어있다

- ex) SVN



#### DVCS(분산 버전 관리 시스템)

> 분산식 버전 관리 시스템에서는 각 클라이언트들이 모두 서버의 백업본을 가진다.

<img src="../assets/git/DVCS.png" alt="img" style="zoom:50%;" />

- 로컬도, 서버도 모두 히스토리를 갖고 있음
  - 따라서, 서버에 문제가 생겨도 복원할 수 있음
- 단순히 파일의 마지막 스냅샷을 Checkout 하지 않고 저장소를 히스토리와 더불어 전부 복제
- ex) GIT



## 2강_GIT 실행 원리

- 로컬 폴더(A폴더)에서 Git 폴더로 쓰겠다고 선언 : git init
  - A 폴더는 작업 영역 (Working Directory가 됨)
  - 작업 영역 내에서는 변경을 감지함
- 일어난 변경을 기록할 것인지 안할 것인지 선택
  - 기록하게 되면 인덱스 영역에 기록 : git add
    - 변경이 감지된 내용만 기록
  - 인덱스 영역 : Tree 목차로 되어있음
    - Tree가 만들어지고 변경내용은 BLOB 객체로 기록됨
    - 쉽게 말하면 Tree는 폴더이고 BLOB 객체는 파일을 의미함
- 기록한 내용을 영구적으로 저장하기 위해서는 헤더 영역에 등록 : git commit
  - commit을 하지 않은 채로 다시 add 를 하게되면 변경된 내용으로 덮어 씌워져버림
  - commit을 하고 나서 다시 add를 하면 이전에 있던 버전(트리 구조)의 상위에 또 다른 트리 생성
    - 기존에 있던 변경 내용은 참조만 하여 기록해놓음 (python의 변수에 할당하는 것과 같음)
    - 변경 내용은 40자의 해쉬값으로 기록되고 해당 내용을 저장하는 것
    - 해당 해쉬값은 .git/objects/ad 에 기록되어있음
    - commit을 할 경우 .git/refs 에 기록이 남게됨
      - master 에는 Master 브랜치가 가르키고 있는 곳 즉 ,head가 가르키고 있는 해쉬값이 나옴
  - commit을 할 때마다 모든 것을 복사하는 것이 아니며, 이미 있는 내용들은 참조만 한다

그림 그려넣을 것



## 3강_GIT 기본기

- 소유자 정보 등록

  - 소유자의 정보를 알려주는 것 (초기에만 설정 필요)

    ```bash
    git config --global user.name "지정값"
    git config --global user.mail "지정값"
    ```

- 파일 등록

  - git init - git add - git commit



### git reset

> log를 복구할 때 (= 특정 지점으로 돌아가고 싶을 때) 사용하며 3가지 옵션이 존재

#### 옵션

##### soft

- 이전 로그로 돌아가되 이전 로그 이후, 헤더 영역에서 발생한 내용만 삭제

- commit 로그 변경시

##### mixed

- 이전 로그로 돌아가되 이전 로그 이후 인덱스 영역, 헤더 영역에서 발생한 내용들 모두 삭제

- 작업 영역의 내용 변경이 필요 할 때

##### hard

- 이전 로그로 완전히 돌아가는 것
- 이전 로그 이후의 작업 영역, 인덱스 영역, 헤더 영역 에 발생한 내용들 모두 삭제
- 이전 커밋으로 완전히 돌아가고 싶은 경우



#### 명령어

#### soft

```bash
git reset --soft 돌아가고싶은hash번호
```

- add까지는 되어있는 상태
- 따라서, commit만 하면 됨



#### mixed

```bash
git reset --mixed 돌아가고싶은hash번호
```

- add가 아직 안된 상태로 돌아감
- 파일 내용에 수정 작업이 가능
- 잘 사용하지는 않음
  - 차라리 파일을 변경하고 새로 commit하는게 더 낫기 때문



#### hard

```bash
git reset --hard 돌아가고싶은hash번호
```

- 작업 영역에 있는 파일까지 날아가버림
  - 즉, 로컬 폴더에 파일까지 사라진다

#### 

### git reflog

> 한 번이라도 커밋했던 모든 내용들이 담겨 있음

- 모든 커밋 내용들을 확인 할 수 있음
- 해당 명령어를 통해 확인한 후 hash 번호를 확보할 수 있음
- git reset으로 해당 커밋으로 되돌아가기 가능



### git amend

> 최종 커밋 로그를 변경하는 명령어

#### 명령어

```bash
git commit --amend -m "커밋메시지"
```

- log가 하나밖에 없을 때는 reset 명령어 사용불가(돌아갈 히스토리가 없기 때문)

  - 그 때도, amend 명령어 사용
  - `.git` 폴더를 삭제하고 다시 init 한 후 commit 하는 것과 같은 과정

  



## 4강_GIT Branch

- branch를 하나로 합치는 과정 : merge

  - main branch와 branch 의 형상이 같은 경우 : fast-foward merge

  - main branch와 branch 의 형상이 다른 경우 : 3-way merge

    이미지 넣기



#### branch pointer

- 첫 commit을 하면 main branch 가 생기는 것 같으나 사실은 main branch pointer가 가르키고 있는 것 뿐
- 새로운 branch를 만드는 것도 새로운 branch pointer가 생기는 것이며, 그 다음 작업들을 새로운 branch pointer 가 가르킴
  - main branch는 분기점을 계속 가르키고 있음
- fast-foward merge : main branch pointer가 단순히 최종 new branch pointer가 있는 곳으로 이동
- 3-way merge : 실제로 가지(branch)가 생기게되며 main branch pointer가 최종 branch pointer가 있는 곳으로 이동하게 되면 main branch에서 만든 것들이 날아가게됨 



#### branch

##### 브랜치 생성

```bash
git branch 브랜치명
```

- 새로운 branch pointer가 생성됨
- 단순히, `git branch` 만 했을 경우 branch 목록 확인 가능
  - 별이 붙어있는 곳이 HEAD가 있는 곳



##### 브랜치 이동

```bash
git checkout 브랜치명
```

- 지정한 브랜치로 헤더가 이동

- 옵션 

  ```txt
  git checkout -b 브랜치명
  ```

  - 지정한 브랜치명을 갖는 브랜치를 생성 후 해당 브랜치로 이동
  - 즉, `git branch` + `git checkout` 인셈



#### merge

##### fast-foward merge

- master branch 로 헤더를 이동시킴

- 명령어 실행

  ```bash
  git merge master브랜치를이동시킬브랜치명
  ```

  - 실행 결과, master branch가 해당 브랜치로 이동함과 동시에 헤더는 master branch 를 가리킴
  - 즉, 본래는 master branch를 가리킬 때는 새로운 branch에서 볼 수 있는 것을 볼 수 없었는데 이제는 볼 수 있게됨.



##### 3-way merge

- master branch로 헤더를 이동시킴

- 바로 merge 명령어 실행

  ```bash
  git merge master브랜치와합칠브랜치명 
  ```

- log를 어떻게 남길지 물어보기 위해 vi 에디터 실행

- `:wq`로 저장 후 종료하기

- git log로 확인



##### merge conflict

- 충돌이 일어나면 해당 파일을 수정 후 다시 commit
- 해당 파일을 실행시키면 conflict 부분 확인 가능
- 수정 후에 다시 add - commit 하면 자동으로 merge 됨



## 5강_GIT Rebase

> 코드에 대한 로그를 깔끔하게 정리하는 것

### squash

- 찌그러트리다, 압축하다 라는 뜻으로 가장 첫번째 로그로 나머지 로그를 모으기 위한 작업

- 남길 로그를 pick, 합칠 로그를 squash 한다
  - 가장 위에 있는 로그를 남겨야함
  - 이전 로그와 이후 로그 사이에 붕 뜨면 안되기 때문에
- 1번 - 2번 - 3번 - 4번 - 5번 중 2,3,4를 하나로 합칠 경우
  - 2번을 pick, 3번,4번을 squash 해야함



### rebase

```bash
git rebase -i HEAD~개수
```

- HEAD를 기준으로 개수만큼 합칠 것이다
- 여러 작업을 위해 vi 에디터 실행
  - 각종 옵션 존재
    - `d` 해당 로그는 아예 지워버림
    - `r` 해당 로그를 수정함 (수정 페이지로 이동)
    - `pick` 합칠 때 남겨놓을 로그 (무조건 제일 과거 로그를 지정)
    - `s` 합칠 때 없앨 로그 (수정 페이지로 이동되며, 각 로그 이름을 삭제 및 수정하면 완료)





## 6강_Github

※ 클라우드 저장소 : 나의 컴퓨터가 아닌 다른 사람의 컴퓨터에 나의 저장소를 들고 있는 것 

- Github는 분산 버전 관리가 가능한 클라우드 저장소

- 해당 클라우드 저장소의 이름은 origin



#### github와 로컬 저장소의 연결

```bash
git remote add origin github저장소주소
```

- 연결여부 확인

  ```bash
  git remote -v
  ```

  또는

  ```bash
  git ls-remote
  ```

- 연결 취소(삭제)

  ```bash
  git remote rm origin
  ```

  

#### github 업로드 & 다운로드

- 업로드

  ```bash
  git push origin master
  ```

  - 파일 업로드와 병합을 한번에 시켜주는 명령어

- 다운로드

  ```bash
  git pull
  ```

  - 파일 다운로드 + 병합

- clone

  - `git init` + `git remote` + `git pull`

    ```bash
    git clone github저장소주소
    ```

    

#### github branch

- 브랜치를 만들어서 작업한 경우

  - github에도 브랜치를 만들어서 올려야함

    ```bash
    git push origin 브랜치명
    ```

  - 다운을 받을 때도 브랜치를 다운 받아야함 

    - 3가지 모두 같은 코드 (브랜치명은 topic으로 가정)

    ```bash
    git checkout -b topic
    # github에 있는 모든 브랜치를 다운 받는다
    git fetch origin
    # origin에 있는 topic 브랜치와 병합한다
    git merge origin/topic
    ```

    ```bash
    # 브랜치 생성
    git checkout -b topic
    # topic 브랜치 다운로드 및 병합
    git pull origin topic
    ```

    ```bash
    # 모든 브랜치 다운로드
    git fetch origin 
    # 브랜치 생성 및 병합
    git checkout -b topoic origin/topic
    ```

    - `git branch` 로 확인
    - 주로 마지막 방법을 사용하는데 그 이유는 pull의 경우 하나의 브랜치만 받을 수 있기 때문

  - 브랜치 병합

    - master로 이동한 후 merge 진행

      ```bash
      git merge --squash topic
      ```

      - commit 진행해주면 `rebase` 필요없이 지정한 메시지로 알아서 정리된 로그 기록



#### git remote branch

- fetch로 다운 받은 경우 (== 서버에는 branch가 있으나 로컬에는 branch가 없는 경우)

  - remote branch라는 곳에 모든 branch 다운

  - 로컬 저장소에 master branch 옮기기 위한 방법

    ```bash
    git branch master
    git checkout master
    git merge origin/master
    ```

    - 위 명령어는 `git clone` 명령어로 한번에 실행 가능
    - `git clone` 수행시 `git fetch origin` 의 역할도 수행함
    - `git clone`은 로컬 저장소에 모든 branch를 동기화 시키지 않음 (master or main만 동기화시킴)

  - 로컬 저장소에 다른 branch 를 다운 받는 방법

    ```bash
    git branch branch이름
    git checkout branch이름
    git merge origin/branch이름
    ```

    - 위 명령어를 한줄로 수행하는 법

    ```bash
    git checkout -b branch명 origin/branch명
    ```

  - 협업 중일때 누군가가 새로운 push를 하면 fetch로 remote branch를 업데이트해야함
    - 혹은, 해당 branch 로 이동한 후에 pull 받아도 됨



## 7강_협업 

### 1. 혼자 개발하기

> 시나리오 : 환경설정, 회원가입, 로그인, 글쓰기 기능 만들기
>
> branch명 : master(배포), dev(개발), topic
>
> 혼자 할 때는 굳이 필요없긴 함

1. 레포지토리 생성

   - github에서 repository를 만들 때, `add a README` 에 체크하면 아래의 작업이 진행됨

     ```bash
     git init
     touch README.md
     git add .
     git commit -m initial commit
     ```

     - 최종적으로 main 브랜치 생성

2. 레포지토리를 `clone` 받기

3. 필요한 브랜치 생성하기

   ```bash
   git checkout -b dev
   git checkout -b setting_topic # 환경설정 기능 구현
   ```

4. setting_topic에서 필요한 환경설정 기능 구현

   1. add - commit

5. dev 브랜치와 merge

   1. 그냥 merge 할 경우 fast-foward merge 진행 (dev 브랜치로 이동하고 해야함)

      - fast-foward merge는 merge log가 기록되지 않음
        - 즉, 로그에는 `1.환경설정 완료` 로만 로그가 남음
        - but, `1.환경설정 완료` `2. merge 완료` 처럼 두개의 로그를 남기고 싶음
      - 이를 해결하기 위한 옵션 설정

      ```bash
      git merge --no-ff setting_topic
      ```

      - 해당 코드 실행시, fast-foward merge임에도 merge 기록이 남음

6. 회원가입 기능 구현

   1. 브랜치 생성 및 이동

      ```bash
      git checkout -b join_topic
      ```

   2. 필요한 기능 구현 후 5번과 마찬가지로 dev와 merge

   3. merge log를 남기며 merge

7. 로그인 기능 구현

   1. 브랜치 생성 및 이동

      ```bash
      git checkout -b login_topic
      ```

   2. 필요한 기능 구현 후 dev와 merge (dev 브랜치로 이동 후 merge 해야함!!)

      ```bash
      git --no-ff login_topic
      ```

8. 글쓰기 기능 구현

   - 위 모든 과정과 동일

9. main 브랜치로 돌아와서 merge & push

   ```bash
   git --no-ff dev
   ```

   - push 전에 tag를 달아줄 수도 있음

     ```bash
     git tag [태그명]
     ```

     - tag 확인

     ```bash
     git tag -n
     ```

   - tag까지 같이 올려주는 명령어

     ```bash 
     git push --tags origin main
     ```

   - dev도 push 해주는게 좋음



### 2. 소규모 프로젝트

> 학생일 경우 3~4명의 팀 프로젝트 운영시 효과적
>
> 시나리오 
>
> - 사용자 : Green(팀장), Meta(팀원)
> - 기능 : 환경설정, 회원가입, 로그인
> - 브랜치 : main(배포), dev(개발), 개별branch



1. 팀장이 개발환경 세팅

   1. repository 생성 

   2. 프로젝트 폴더 생성 & clone

   3. 필요한 설정 세팅

   4. add - commit

   5. dev 브랜치 생성

   6. 모든 브랜치 업로드

      ```bash
      git push --all
      # 원래는 각각의 브랜치를 다 push 해줘야함
      ```

   7. repository에 팀원 추가

      1. github settings에서 초대
      2. branch 보호 설정
         - settings-branches-add rule
         - require a pull request before merging 설정 : 승인을 해줘야만 push 가능
         - main, dev branch 보호 설정

2. 개발을 시작할 팀원

   1. 팀장이 업로드 해놓은 git을 clone
   2. clone 해도 branch들은 remote branch에 있지 팀원의 로컬에는 저장되어있지 않음
   3. 따라서, `checkout -b`명령어를 이용해서 생성 및 이동 필요
   4. `dev`에서 개발하는 것은 지양해야함 
      1. 자신의 개별 브랜치를 만들어서 해당 브랜치에서 개발 후 PR 요청
      2. 자신의 개별 브랜치에서는 `rebase`해도 되지만 공용에서는 지양할 것
      3. 따라서, 자신의 로컬에 새로운 브랜치를 만들고 해당 브랜치에서 개발하고, 로그를 정리한 후 push
   5. merge 요청하기
      1. github - pull reauests - new pull request
      2. where ← what 설정
      3. create pull request
      4. draft pull request : 중간보고 (아직 완료되지 않았으나 확인을 요청할 때)
         create pull request(3번이랑 다름) : 최종보고 (최종 확인 요청)

3. PR 받은 팀장

   - 3가지 옵션 중 하나 선택
     1. request changes : 거절
     2. approve : 승인
     3. comment : 멘트 
   - submit review 하면 팀원이 확인 가능
   - 승인되면 팀원, 팀장 둘 중 아무나 merge pull request 가능

4. 승인 받은 후의 팀원

   1. branch 삭제 

      ```bash
      git push --delete origin 브랜치명
      ```

      - 위 코드는 github에서 해당 브랜치가 삭제되는 것
      - 팀원의 로컬에는 남아있음 (혹시 모를 상황 대비)

   2. dev 브랜치 동기화

      ```bash
      git checkout dev
      git pull origin dev
      ```

5. git 과정을 문서화해놓는 것이 좋음

   ```txt
   1. 개별 브랜치(topic) 생성
   2. 해당 브랜치에서 개발 진행
   3. 로그 깔끔하게 rebase로 정리
   4. topic 브랜치 push
   5. dev 브랜치로 merge 요청
   6. 팀장 승인 대기
   7. merge 완료시 github에서 branch 삭제
   8. 최종적으로 본인 로컬에서 dev 브랜치 pull
   ```

    

##### 팀장이 거절하는 경우

- 다시 수정해서 올려야하는데 이때, commit을 달리 할 경우 push가 안됨

- github 의 log와 local의 log가 다르기 때문

  - 해결법

    1. 강제로 push

       ```bash
       git push -f origin login_topic
       ```

    2. 새로운 branch 생성 후 해당 branch 업로드

- rebase 는 반드시 자신의 브랜치에서만 진행해야함
