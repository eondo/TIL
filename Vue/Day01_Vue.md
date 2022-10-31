### Vue Intro
- Front-end 개발은? Vue.js라는 javascript로 쓰는 프레임워크 이용!
- FE의 개발의 결과물 : Web App(SPA)

#### Web App
웹 페이지가 디바이스에 설치된 App처럼 보이는 것
#### SPA(Single Page Application)
- 이전) 페이지 별 template 반환 -> SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 수정하여 대응하는 방식. 즉, 한 페이지로 모든 요청에 대응
- CSR (Client Side Rendering) 방식으로 요청 처리
- [참고] SSR의 단점 : 전달 받은 새 문서를 받을 때마다 새로고침 진행
#### CSR
- 이제, 화면을 만드는 주체가 서버 X 클라이언트 O
- 최초 한 장의 HTML을 서버로부터 받아오는데, 빈 HTML을 받는다. 그리는 것은 Client, 즉, javascript가 그린다.
- axios으로 추가 요청 보낸 것처럼, 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링

1. 필요한 페이지를 서버에 AJAX로 요청
2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
3. JSON 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링) - 렌더링이 브라우저에서 발생

#### CSR의 장점 및 단점
- 모든 요청에 대해서 새로운 페이지를 받아올 필요 X -> 트래픽 감소, 응답 속도 개선
- 필요한 부분만 고쳐나가므로 요청이 끊김없이 진행
- 첫 구동 시 필요한 데이터 많을수록 최초 작동 시작가지 오랜 시간이 소요
- 검색 엔진 최적화가 어려움

#### CSR vs SSR
- 타겟 서비스에 적합하 렌더링 방식을 적절하게 활용

#### 타 FE 프레임워크
- FE Framework == HTML + CSS + JS를 더 편한게 작업하기 위한 툴
- 생산성과 협업으 위해 Framework를 사용해서 개발

### Vue 어떻게 쓸 수 있는지?
HTML 내에서도 사용 가능 -> CDN 가져와야 함

- 연쇄적인 데이터 변경 필요한 경우 -> Vue) 데이터 하나로 관리하기 때문에 데이터 하나를 변수로 뿌려주기만 하면 됨. 컴포넌트 한꺼번에 다 바뀜. 데이터를 사용하고 있는 모든 DOM에서 리렌더링이 발생함.


## Vue
어떤 역할? 어떤 문법?
- MVVM Pattern
  - 1) Vue Model : event를 듣고, directives로 조작
    - View와 연결된 Action을 주고 받음 : DOM에서 발생한 액션을 주고받음
    - Model이 변경되면 뷰 모델도 변경되고 바인딩된 view도 변경
  - 2) DOM : View 우리 눈에 보이는 부분
  - 3) Plain JS Objects - 실제 데이터 = JSON!
  - 정리 : 독립성 증가, 적은 의존성, 그 사이에서 Vue Model이 중간에서 소통
![1_1](https://user-images.githubusercontent.com/109258497/198967796-7dda3a63-6ff5-44eb-a58c-65a94b795751.png)

Vue : view model. () 괄호 안에 객체를 넣어서 하나씩 뷰를 사용하기 위한 속성값을 작성함.
2. 뷰 인스턴스 == 1개의 객체
   1. 많은 속성, 메서드를 기능들을 사용 가능
   2. new 연산자 이용 -> 매번 작성할 필요 없이, 똑같은 구조의 객체를 찍어낼 수 있음 생성자 함수
  ```
  function Member(name, age, sId) {
  this.name = name
  this.age = age
  this.sId = sId
  }

  const member3 = new Member('isaac', 21, 2022654321)
  ```
#### el (element)
- View 인스턴스와
- 생성자 함수의 첫번째 인자
- 그 영역만 뷰가 관할
- 뷰 모델로 인해서 모델과 뷰과 마운트 됨
#### data
- 데이터 객체는 반드시 기본 객체 {}(Object)여야 함, 들어가는 값은 어떤 타입이든 가능
- 정의된 속성은 interpolation {{ }}dmf xhdgo view에 렌더링 가능함
- 추가된 객체의 각 값들은 this.message 형태로 접근 가능

#### methods
메서드의 함수는 화살표 함수 x, 여기서 this는? 이 메서드를 호출하는 객체. 즉, new Vue({})
- 정해진 값에 접근할 때, console.log(this.$data.message)로 접근해야 하긴 하지만, 빼고도 데이터에 접근할 수 있음 -> $ : 다른 메서드나 변수값이랑 이름이 구분되기 위해 내부적으로 설정한 값. 기본적으로 쓰고 있는 속성값이구나! 이해하면 됨 -> 생략 가능
```js
// 2. el 
    const app = new Vue({
      el: '#app', // 뷰 모델과 위에 있을 DOM을 연결해주는 옵션
      // 3. data
      data: {
        message: 'Hello, Vue!'
      },

      // 4. methods
      methods: {
        print: function () {
          console.log(this.message)
        },

// Hello, Vue! 출력
```
- method를 호출하여 data 변경 가능
접근할 수있기 때문에 변경도 가능
객체 내 bye method 정의 -> message값을 바꿈
```js
bye: function () {
          this.message = 'Bye, Vue!'
        },
```
#### 주의
- 메서드를 정의할 때, 화살표 함수 사용 불가능 -> this가 윈도우를 가리키기 때문.
- 이 안의 콜백 함수에서는 화살표 함수 사용 가능하지만, 처음 메서드를 선언할 때에는 화살표 함수 만들 때 this가 바로 결정됨. 즉, 이 객체의 상위 스코프를 가리키게 됨(윈도우)
- this로 Vue의 data를 변경할 수 없음

## Vue의 문법 기초
### 1. Template Syntax
3가지 방법으로 출력 가능
1. 렌더링 된 DOM
2. HTML 기반 template syntax
3. 선언적으로 바인딩
```html
    <p>메시지: {{ msg }}</p>
    <p>HTML 메시지 : {{ rawHTML }}</p>
    <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
    <p>{{ msg.split('').reverse().join('') }}</p>
```

### Directives
- v-접두사가 있는 특수 속성에는 값을 할당할 수 있음
- 즉, 단순한 문자열이 아니라 js의 표현식이 들어갈 수 있음
- directive 역할 : 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
- `:`을 통해 전달인자를 받을 수 있음
- `.`으로 표시되는 특수 접미사-directive를 특별한 방법을 바인딩
```html
<p v-text="message"></p> // p 태그 비어있지만 directive로 변수값 출력
```
#### v-html
- raw HTML을 실제로 HTML로 표현할 수 있음
- 사용자가 입력하거나 제공하는 컨텐츠에서는 절대 사용 금지
- XSS 공격 참고

#### v-show, v-if
1. v-show
- element를 보여줄지 말지를 결정
- dispaly의 속성을 기본속성과 none으로 토글, 요소 자체는 존재는 하고 렌더링은 되어 있는데 보이냐 마냐의 차이이다.
2. v-if
- isActive 값이 변경될 때 반응
- 차이 : 값이 false인 경우 DOM에서 사라짐
- v-if v-else-if v-else 형태로 사용

3. v-show vs v-if
- v-show
  - 초기 로딩이 비싸지만, 토글은 cheap 이미 렌더링된 것을 css에서 속성만 바꿔준 것이니까
- v-if
  - 토글은 expensive. 왜? 애초에 태그 자체를 완전히 삭제했다가 다시 새로 만들고를 반복하는 것이니까. 
  - 토글이 많으면 show가 더 적합할 것.
  - 대부분 v-if 사용 (? else-if else문 사용하려면 필요하기 때문)

#### v-for
- 형식 : for .. in ..
- 반복한 데이터 타입에 모두 사용 가능
- 특수 속성 key
  - v-for 사용 시 반드시 key 속성을 각 요소에 작성
  - 결국 iterable이 반복을 도는데 반복이 되는 주체의 요소들을 확실하게 할 수 있는 식별값이 필요함. 여러개의 v-for가 있을 텐데 순회를 할 때 각각의 요소의 식별자를 부여하기 위함. 반복의 불변을 유지하게 하기 위함. 보장.
  - 다른 v-for의 key가 중복 X -> 경고 vue.js:5106 [Vue warn]: Duplicate keys detected: '0'. This may cause an update error.
  - 각 요소가 고유한 값을 가지고 있다면 생략 가능


#### v-on
- 이벤트 리스터의 역할을 함
- `:`를 통해 전달받은 인자를 확인, 전달된 인자에 따라 특별한 modifiers(수식어)가 있을 수 있음
- 값으로 JS 표현식 작성
- 표현식이 JS라서 메서드도 사용 가능하고, 인자값도 넣을 수 있음
```
<button @click="checkActive(isActive)">check isActive</button>
```
- 약어 : `@`


#### v-bind
HTML 기본 속성에 Vue data를 연결
이 속성값(href)을 url이라는 변수로 넣겠다!
- 이걸 응용해서 스타일 조정할 수 있음
```html
<p v-bind:class="redTextClass">빨간 글씨</p>
    <p v-bind:class="{ 'red-text': true }">빨간 글씨</p>
    <p v-bind:class="[redTextClass, borderBlack]">빨간 글씨, 검은 테두리</p> // 한꺼번에 적용 - 배열 이용
```
- 앞에 :key도 이것을 사용한 것
-> html의 속성값에 js의 표현식을 넣기 위한 것 v-bind
- 약어 : `:`

#### v-model
데이터랑 양방향 모델링, 바인딩
```html
  <div id="app">
    <h2>1. Input -> Data</h2>
    <h3>{{ myMessage }}</h3>
    <input @input="onInputChange" type="text">
    <hr>

    <h2>2. Input <-> Data</h2>
    <h3>{{ myMessage2 }}</h3>
    <input v-model="myMessage2" type="text">
    <hr>
  </div>
```

### Vue Advanced
#### ❗ computed 속성
- vue 인스턴스가 가진 옵션 중 하나
- 미리 계산한 값을 사용 / 메서드 : 그때그때 사용할 때마다 재호출
- 처음 한 번 실행되면 200이 저장되어 있고, 변화가 없다면 그 값을 그대로 씀 -> 호출을 아낌
- 종속된 대상의 변화가 있을 때! (ex.number1, number2) computed가 재계산됨
- method는 소괄호, computed는 함수가 아니라 계산된 '값'이므로 괄호가 없음
- computed도 처음에 계산될 땐 한 번은 호출은 되어서 함수 형태로 쓰지만, 사용할 때에는 값이므로

#### watch
- 특정 데이터의 변화를 감지하는 기능
1. watch 객체를 정의
2. 감시할 대상 data 지정
3. data가 변할 시 실행할 함수를 정의

```
name: {
          handler: 'nameChange'
        },
```
- handler 키 값 필요 : nameChange 함수 실행
- 배열, 객체를 감시하려면 옵션 `deep: true`가 필요 -> true, false 바뀌는 것을 감시 가능

#### filters
텍스트 형식화를 적용할 수 있는 필터
nums인자가 | 앞의 배열이 인자로 들어가고, 그래서 결과를 홀수만 내는 필터 가능
- 필터 체이닝 가능 -> 필터를 한 번 더 거칠 수 있음