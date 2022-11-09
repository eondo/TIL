# Vue Router

### INDEX
1. UX & UI
- 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계
- Prototyping Tool : Figma
2. Vue Router
3. Navigation Guard
4. Articles app with Vue

## 🤍 Vue Router
#### ◼ Routing이란?
- 네트워크에서 다음 경로를 선택하는 프로세스
  - ex. 유저가 방문한 URL에 대해서 적절한 결과를 응답하는 것
- SSR에서의 Routing
  - 서버가 모든 라우팅을 통제 (Django로 보낸 요청의 응답 HTML은 완성본인 상태로 render, redirect 방식을 사용)
- SPA/CSR에서의 Routing
  - 서버는 하나의 HTML만을 제공, 이후 모든 동작은 하나의 HTML 문서 위에서 JavaScript 코드를 활용 → 추가적인 데이터 필요할 시, axios 등 AJAX 요청 도구 이용
  - 하나의 URL로 해결) 새로고침 시 처음 페이지로, 브라우저의 뒤로가기 기능 X... etc. 문제 발생 → ✔ **Vue Router** 등장!

### ◻ Vue Router
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트에 컴포넌트를 라우터에 맵핑해서 여러 페이지를 보는 것처럼 제공
- 각각의 라우터에 URL 주소를 입력하여 사용하여 SPA를 MPA처럼 URL을 이동하면서 사용 가능
- 페이지는 하나, 단순히 보여지는 컴포넌트만 교체되는 것 (URL 교체)

#### ▪ History mode
- 브라우저의 History API를 활용하여 새로고침 없이 URL 이동 기록을 남길 수 있으므로 /를 이용한 URL 구조 사용 가능 

#### 🧷 `<router-link>`
- URL을 이동시키면서 그 변경된 URL에 등록된 컴포넌트와 맵핑됨
- a 태그와 달리 브라우저가 페이지를 다시 로드 하지 않도록 함
- `to`속성 : 목표 경로 지정

#### 🧷 `<router-view>`
- 라우터 링크를 클릭했을 때 routes에 매핑된 컴포넌트를 렌더링해서 보여질 화면
- 실제 컴포넌트가 DOM에 부착되어 보이는 자리
- 라우터의 변화에 따라 새로 컴포넌트가 렌더링하는 컴포넌트
- Django에서의 base.html 안의 block

#### 🧷 src/router/index.js
- 라우터에 관련된 정보 및 설정 작성
- routes == URL와 컴포넌트를 매핑 지정하는 곳
- 라우팅해주는 urls.py의 역할로, 주소 변경되면 해당 컴포넌트가 렌더링 됨! url을 맵핑하는 곳
- 보여지는 화면을 렌더링하는 담당 컴포넌트가 바뀐 것 → 이를 위해 라우터 링크에 하나씩 연결되어있어야 한다. 즉, 컴포넌트가 맵핑되어 있어야 한다.

#### 🧷 src/Views
- 컴포넌트를 넣을 수 있는 공간 2가지 - components와 views는 경로만 다르게 분리될 뿐
  - `views` : 라우터와 직접 매핑되는 컴포넌트들은 views에 작성! 구분을 위해 View로 끝나도록 작성
  - `components` : 라우터와 직접적으로 연결되지 않는 하위 컴포넌트들은 components에 작성!

### ◻ Vue Router 실습
◼ 주소를 이동하는 2가지 방법
- 선언적 방식
  - `<router-link :to="{ name: 'home' }">Home</router-link>`
  - 동적인 값 사용 → `v-bind`
- 프로그래밍 방식
  - Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근
  - 다른 URL로 이동) `this.$router.push`
    - history stack에 이동할 URL을 넣음, 기록이 남아 뒤로 가기 가능

#### ◼ Dynamic Route Matching
- URL을 일부분을 변수처럼 사용할 수 있도록 동적 인자 전달
  - `path: '/hello/:userName',`
- router 변수 중 `$route.params`로 변수에 접근, userName을 바꾸어줄 수 있음
- 프로그래밍 방식의 동적 변수 할당
  1. input 이용
  2. 실시간 양방향 바인딩 되는 데이터 필요
  3. 선언적(버튼)으로 여길 오지 않고, 프로그래밍적으로 네비게이션으로 push됨

#### ◼ routes에 component 등록하는 법
1) hello는 이동하지 않아도 로딩이 이미 완료되어 있음,
2) lazy-loading 방식
  - 들어갔을 때 로딩을 시작. 미리 로딩을 해놓지 않음.
  - 화살표 함수로, 나중에 실제로 동작할 때 로딩하겠다!

## 🤍 Naviation Guard
#### 네비게이션 가드란?
- Vue router를 통해 특정 URL에 접근할 때
- 1) 다른 url로 redirect
- 2) 해당 URL로의 접근을 막는 방법

#### 네비게이션 가드의 종류
- 전역 가드
- 라우터 가드
- 컴포넌트 가드

### 1. Global Before Guard
다른 url 주소로 이동할 때 항상 실행
- 설정) router/index.js에 `router.beforeEach()`
  - to : 이동할 URL 정보가 담긴 Route 객체
  - from : 현재 URL 정보가 담긴 Route 객체
  - next : 지정한 URL로 이동하기 위해 호출되는 함수로, 한 번만 호출되어야 함 (없으면 화면 전환되지 않고 대기 상태)
- 시점) URL이 변경되어 화면이 전환되기 전 호출됨

# 실습
views에 들어가는 애들은 라우트랑 맵핑되는 친구
- 만약 view가 여러개라면? 모두 추가? 

### 라우터 가드
전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
다른 경ㄹ에서 이 라우터로 들어올 때 실행됨
이미 로그인 되어있는 경우 HomeView로 이동

### 컴포넌트 가드
- 주소 변경을 감지하지 못함, 뒤에 변수값이 변했는데 url이 전환됐다고 감지하지 못 함 -> 이걸 가드를 통해 처리
- 변화하지 않은 이유 : 컴포넌트가 재사용되었기 때문


- 주소가 유효하지만 특정 리소스를 찾을 수 없는 경우
```
.catch((error) => {
  // this.message = `${this.$route.params.breed}은 없는 품종입니다.`;
  this.$router.push("/404");
```

# 2️⃣ CREATE
- 메서드의 인자로 받아올 수 있음
- 