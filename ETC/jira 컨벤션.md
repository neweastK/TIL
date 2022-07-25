# JIRA 컨벤션 및 사용법



### 공통

- 월요일 오전에 그 주에 필요한 모든 업무를 등록합니다.
  - Story, Task 단위의 양식은 당일 논의를 통해 지정해나갑니다.
- 또한, 매일 매일 본인의 업무를 체크하여 workflow를 잘 관리합니다.
  - 업무를 시작했을 경우 in_progress, 업무를 마쳤을 경우 Done으로 이동시킵니다.
- 개인별 주당 40시간의 업무를 등록해야합니다.

- 업무 담당자 확인은 아바타를 통해 확인합니다.

  | 담당자 | 아바타                                                       | 담당업무 |
  | ------ | ------------------------------------------------------------ | -------- |
  | 김선후 | <img src="https://jira.ssafy.com/secure/useravatar?avatarId=10503" alt="img" style="width:8%;" /> | BE       |
  | 정승우 | 이수랑 선점 탈유령하세요                                     | BE       |
  | 김호진 | <img src="https://jira.ssafy.com/secure/useravatar?avatarId=10349" alt="img" style="width:8%;" /> | FE       |
  | 이수랑 | <img src="https://jira.ssafy.com/secure/useravatar?avatarId=10341" alt="img" style="width:8%;" /> | FE       |
  | 김동신 | <img src="https://jira.ssafy.com/secure/useravatar?avatarId=10351" alt="Edit avatar" style="width:8%;" /> | FE       |

- Story Point는 반드시 4 이하로 작성합니다.

  - 4보다 초과될 경우 더 작은 Story 혹은 Task로 분류해야합니다.

    

### Epic 

> Epic은 여러 Sprint에 걸쳐서 끝날 수도 있습니다.
>
> 각종 Story, Task의 집합입니다.
>
> Backlog에서 라벨처럼 보여집니다.

- 분류
  - ~~`기획`, `FE`, `BE`, `문서` 중 택1~~
- 네이밍 컨벤션

  ```txt
  [기획] JIRA
  [디자인] 스토리보드 작성
  [기본기능] 로그인
  [기본기능] 회원가입
  [게임] 동상이몽
  ```

  



### Story

> 서비스 고객과 관련이 있는 기능
>
> 주로 구현, 개발과 관련된 과업을 의미합니다

- 가능한 Story를 상세하게 만들어야합니다.

- labels에 `BE`/`FE`/`공통` 을 작성해주면 추후에 업무가 많아져도 본인 파트의 업무들만 찾아보기 쉽습니다. 

- Description에 반드시 상세하게 업무 내용을 기술합니다.

  - 담당자가 아닌 제 3자가 봐도 업무를 이해할 수 있도록 하기 위함(누군가...또 떠날 수도 있으니....^^)

  - 예시 (단지, 예시일뿐입니다.)

    ```txt
    업무 상세 내용 :
    마감 기한 :
    주의사항 : (반드시 기억해야할 내용)
    ```

- 테스트 결과 sub_task에서 지정한 story point는 sprint에 반영이 되지 않습니다.

- 따라서, Story에서 Story Point를 정합니다.

  - 단, 4시간이 넘어가는 Story는 더 작은 Story로 나눠야합니다!

- sub_task는 상세 업무를 기록하는 용도로 사용합니다. 

  - Story를 위해 필요한 작업들을 작성하는 용도
  - 팀원과의 원활한 소통을 위해 Story Points가 없어도 상세 업무를 기록하는 연습을 합시다! 

- 네이밍 컨벤션

  - ```txt
    [BE/FE/공통] 업무 내용
    
    - 예시
    [BE] 회원가입 Form 작성
    [FE] SNS 계정 연동
    [FE] 랜덤 배정 기능 구현
    ```



### Task

> 개발과 관련 없는 과업을 의미합니다.
>
> 문서 작업, 기획, 보고 등

- Story와 동일하게 진행합니다.

  - Story Point도 작성합니다.

- 네이밍 컨벤션

  - ```txt
    [Topic] 업무 내용
    
    - 예시
    [공통] 기능정의서 작성
    [공통] Figma 색상 팔레트 
    [공통] ERD 작성
    ```





#### 참고 사이트

> [팀에 맞게 Jira로 스크럼 관리하기 - 규칙 정하기](https://velog.io/@jinuku/%ED%8C%80%EC%97%90-%EB%A7%9E%EA%B2%8C-Jira%EB%A1%9C-%EC%8A%A4%ED%81%AC%EB%9F%BC-%EA%B4%80%EB%A6%AC%ED%95%98%EA%B8%B0-%EA%B7%9C%EC%B9%99-%EC%A0%95%ED%95%98%EA%B8%B0)
>
> [Atlassian JIRA를 이용한 애자일 Scrum 프로젝트 관리](https://bcho.tistory.com/826)
