AJAX - 비동기적인 방식으로 js가 실행되는데 서버와 통신할 때 XML를 가지고 통신하는 법

- CSV, XML, JSON
- 무엇을 쓸지는 상황, 넘길 데이터에 따라 달라질 수 있으나 대부분 XML, JSON을 일반적으로 많이 쓰게 된다.


AJAX를 사용하는 법 -> 
1. XMLHttpRequest 내장 객체 사용
   1. 브라우저가 가지고 있는 내장 객체
   2. 상당히 복잡 (내부적인 처리까지 모듈화하기 위해 null값 체크 등 필요)
2. fetch() 브라우저 내장 함수
   1. 복잡한 게 간단하게 끝낼 수 있음
   2. js를 지배한 라이브러리인 jQuery가 가진 ajax 함수를 이용한다면 복잡한 것을 해결 -> 대략적인 jQuery 이해를 추천 (for 레거시 프로젝트)
3. jQuery
4. axios 라이브러리 : 외부 라이브러리!


## AJAX(Asynchronous Javascript and XML)
1.1 Ajax 소개
- 언어나 프레임워크 X, 구현하는 방식 O
- 웹에서 화면을 갱신하지 않고 특정 부분만 데이터를 서버로부터 가져와 처리하는 방법
- js의 XMLHttpRequest 객체로 데이터를 전달하고 비동기 방식으로 결과를 조회
- 동작 방식
  - data를 입력 후 event 발생
  - AJAX 적용했으므로 event 발생 시 서버에서 요청을 처리한 후 Text, XML, JSON 으로 응답
  - client(브라우저)는 이 응답 data를 이용하여 화면 전환 없이 현재 페이지에서 DOM을 통해 동적으로 화면을 구성
  - 즉 웹 화면 구성하는 방식이 SSR (X) -> CSR (O)
- 공부 순서 : callback -> Promise -> async/await + axios
- GET 방식, POST 방식
  - get은 URL에 변수(데이터)를 포함시켜 요청, 데이터를 Header에 포함하여 전송
  - post는 데이터를 Body에 포함시키며 변수를 노출하지 않고 요청

## XMLHttpRequest
- 정적 페이지 : html, css, javascript로만 만드는 페이지 -> 코딩하는 만큼만 보여줌
- 동적 페이지 (Dynamic Web Page): JSP, servlet 이용하면 내가 보내준 데이터에 따라 페이지를 바꿀 수 있음

1. New - Dynamic Web Project 생성
- 프로젝트를 java로 만들긴 하지만 내 컴퓨터에서 돌아가는 게 아니라, 서버에서 돌아가게 할 것
- Target Runtime : 이 프로젝트를 어떤 서버에서 실행할 것이냐?

