## 사용자의 요구에 따라서 원하는 책을 추천받을 수 있는 Book SNS
- PageRank 알고리즘을 이용한 사용자 개인별 피드 분석을 통한 책 추천
- 사용자의 요구사항에 맞는 사용자 맞춤형 책 추천 
- 사용자 피드 및 프로필 기능
- 피드 공유 및 댓글 기능 
- PageStorage 사용자들이 가장 많이 기록한 책 기반 베스트셀러 추천
- Spring Security를 이용한 세션 기반 로그인


## 프로젝트 사용 기술 스택
- 프레임워크 : Spring Boot, Django
- Spring Data JPA
- Spring Security
- 언어 : Java 17, Python
- API : ChatGPT, Naver Book
- DBMS : MySQL

## 아키텍처
![스크린샷 2024-07-18 오후 9 11 52](https://github.com/user-attachments/assets/8c31015e-2aa4-4a5b-b448-f203113c4b1f)
- Spring Server
    - 클라이언트와 요청과 응답을 직접적으로 주고받는 핵심 서버 
    - API를 통하여 클라이언트의 요청을 받고, MySQL 데이터베이스 서버를 통해 저장 및 조회를 진행한 후, 요청을 처리 
    - 응답은 Spring Server에서 Thymeleaf 템플릿 엔진을 사용하여 동적으로 HTML을 생성하여 클라이언트에게 반환한
    - Naver Book, GPT API 및 Django Server에 요청을 보내고 응답을 받는다.
- Django Server
    - Spring Server에서 사용자의 피드 작성 내용을 전송
    - 받은 피드 내용을 바탕으로 내용의 핵심 키워드를 PageRank 알고리즘을 통해 추출하여 Spring Server로 반환
## DB ERD
<img width="891" alt="스크린샷 2024-07-18 오후 8 37 04" src="https://github.com/user-attachments/assets/ff8b096d-e8d6-47a4-a285-31402508960a">

- 로그인과 회원의 경우, Spring Security를 사용하여 로그인을 할 때 필요한 로그인 정보를
회원정보에서 따로 분리하여 설계하는 것이 확장성과 보안성 측면에서 이점을 가지고 있다고
판단했기에 분리함
- 회원과 로그인은 1:1관계이며, 로그인은 회원에 종속되어 있기 때문에 회원PK를 로그인 테이블의 식별관계 PK로 설정함
- Spring JPA의 경우 복합키를 기본키로 설정하게
되면 구조적인 측면에서 유연하지 않고, 따로 함수들을 오버라이딩해서 설정해줘야 하는 복잡
함을 가지고 있기 때문에 히스토리태그 테이블의 기본키를 식별관계 복합키(히스토리PK, 태그PK)로 설정하지 않고 히스토리태그
PK로 따로 설정함
- 히스토리키워드, 회원선호장르의 경우도 위와 같은 이유로 PK를 따로 설정함
## Spring Server 구조
![스크린샷 2024-07-18 오후 9 13 50](https://github.com/user-attachments/assets/77b92b8e-cefe-4e00-bc0e-097db64a8fe5)

## 프로젝트 실행 사진
### 키워드 추출 기반 책 추천
![스크린샷 2024-07-18 오후 9 15 38](https://github.com/user-attachments/assets/0ab98be1-bfed-4bfe-a43e-c2d2e90cc174)

### 자연어 입력 기반 책 추천
![스크린샷 2024-07-18 오후 9 16 20](https://github.com/user-attachments/assets/f3faa904-e603-40e8-9074-ef550de559c2)

### 피드
![스크린샷 2024-07-18 오후 9 17 51](https://github.com/user-attachments/assets/943c957b-6499-427a-b74a-263a4440e5f7)

- 보라색은 PageRank 알고리즘을 이용하여 추출된 키워드
- 회색은 사용자가 직접 입력한 키워드 

### 상세 피드
![스크린샷 2024-07-18 오후 9 19 45](https://github.com/user-attachments/assets/ff4682a8-9b4f-454b-922a-0a68bdb45cd0) 
