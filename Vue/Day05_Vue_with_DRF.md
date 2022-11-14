### Intro
DRF API Service를 통해 정보만 제공

- 요청에 문제는 없으므로 DRF는 응답은 해서 게시글 목록 응답을 주고 있음

### CORS
#### 배경
브라우저가 요청을 보내고, 서버의 응답이 브라우저에 도착했으나 브라우저가 막은 것
- WHY? 보안상의 이유로 브라우저는 동일 출처 정책(SOP)에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한함
- #### SOP
  - 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임 (기본적인 네트워크 상의 소통의 개념)
- #### Origin(출처)
  - 동일한 출처란? Protocol/Host/Port 세 영역이 일치하는 경우
#### 정의
교차 출처 리소스 공유
- 추가 HTTP Header를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제 → 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 **서버**에서 지정 및 처리
- 서버 → 브라우저 : 다른 출처지만 접근해도 된다는 사실 알림

- `CORS_ALLOWED_ORIGINS` : Sequences[str]
- CORS_ALLOW_ALL_ORIGINS : Headers에 *를 승인하는 응답

### Vue with DRF
### Article 조회
### 생성
```
createArticle() {
  const title = this.title;
  const content = this.content;

  if (!title) {
    alert("제목을 입력해주세요");
    return;
  } else if (!content) {
    alert("내용을 입력해주세요");
    return;
  }

  axios({
    method: "post",
    url: `${API_URL}/api/v1/articles/`,
    data: {
      title: title,
      content: content,
    },
  })
    .then((res) => {
      // console.log(res);
      this.$router.push({ name: "ArticleView" });
```
### DRF 인증 시스템
#### TokenAuthentication
- 회원가입 x, 이미 인증되어 있는 상대에 대해서 하는작업만있고, 회원가입은 Token 생성되므로 별도로 추가해야 할 것이 있다!

인증된 사용자에게 모든 뷰 함수 처리를 허용하겠다.
인증된 경우만 되도록 인증이 필요한 경우는 데코레이터로 따로 뺌
```
@permission_classes([IsAuthenticated]) // 토큰이 없으면 아래 못 함
```
뷰에서) 토큰 받아서 저장해두고 인증이 필요한 axios 요청에 토큰 값 만들어서 붙여줘야 한다!

## DRF Auth with Vue
DRF 설치/세팅, POSTMAN으로 이를 테스트함, 이제 POSTMAN을 Vue로 바꿔서 진행해보자.
### SignUp Request
- 회원가입 후 Token을 store에서 관리할 수 있도록 actions를 활용

### Login Request

### IsAuthenticated in Vue
- 회원가입, 로그인 요청에 대한 처리 후, 로그인 여부를 확인할 수 있는 수단이 없음
- state
- 토큰값 있냐없냐로만 연산되면 되기 때문에 getters에 작성
- 게시글 조회할 때 인증 회원인지 확인하고 싶을 때,

###
로그인까지 해도, 게시글 달라고 할 때, Token 필요
django에서는 로그인한 것으로 인식 x, 발급받은 token을 요청과 함께 보내지 않았기 때문
```
headers: {
          Authorization: `Token ${context.state.token}`
        }
```

### 게시글 작성시 유저 정보 함께

### DRF API로 만들기
