### INDEX
1. Vue CLI
2. SFC
3. Pass Props & Emit Events

## Vue CLI
#### Node.js
- 브라우저 밖에서 구동할 수 없었던 자바스크립트를 런타임 환경인 Node.js로 인해 서버에서도 구동할 수 있게 됨
#### NPM
- 자바스크립트 패키지 관리자
- Node.js의 기본 패키지 관리자로서 Python의 pip 역할
- Node.js를 통해서 Vue의 프로젝트를 생성할 것! 브라우저 밖을 벗어나 서버 side에서 프로젝트를 진행해보자!

#### Vue CLI
- Vu 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할

#### 준비 과정
1. `npm install -g @vue/cli` : git bash에 설치
2. `vue create (vue-cli)` : 프로젝트 생성(위치 : vscode의 terminal)
3. Vue 2 선택
4. `cd vue-cli/` : 디렉토리 이동
5. `npm run serve` : 서버 구동

- git init이 되어있는 상태 → git으로 관리 중인 폴더 안에 생성했다면 .git을 삭제하고 push해야 함!

### Vue CLI 프로젝트 구조
#### 📁 node_modules
- Python에서의 가상 환경의 역할
- 모듈 간 서로에게 복잡한 의존성을 가짐
- __Babel__
  - 컴파일러 역할
  - 원시 코드(최신 버전)를 과거의 레거시로 작성된 목적 코드(구 버전)로 번역/변환을 함
- __Webpack__
  - "static module bundler" - 정적인 파일로 정리해주는 역할
  - 모듈 간의 의존성 문제를 해결하기 위한 도구
  - Module?
    - 애플리케이션 크기 증가 -> 파일 하나에 모든 기능 담기 어려워짐 -> 파일을 여러 개로 분리 -> 하나의 .js 파일 == 모듈
    - 기능 단위로 분리, 클래스 하나 or 특정한 목적을 가진 복수의 함수로 구성
    - Module의 의존성 문제 : 모듈 증가, 라이브러리 or 모듈 간의 의존성 깊어짐
  - Bundler?
    - 모듈 의존성 문제를 해결해주는 도구
    - 모듈들을 하나로 묶어주고 하나(or 여러개)의 파일로 만들어짐
#### package.json
- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션 포함
#### package-lock.json
- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 개발 과정 간의 의존성 패키지 충돌 방지
- python에서 requirements.txt의 역할

#### 📁 public/index.html
- 클라이언트가 그리는 페이지 하나
- `<div id="app"></div>` : vue와 연결된 부분 - 루트 컴포넌트라고 하는 뷰 파일 하나와 연결되어 여기에 출력됨

#### 📁 src
#### 🧷 assets
- 정적 파일을 저장하는 디렉토리
#### 🧷 components
#### 🧷 App.vue
- 최상위 컴포넌트를 가짐, index.html의 div의 위치에 App.vue가 렌더링 될 것
#### 🧷 main.js
- 웹팩이 프로젝트 빌드를 시작할 때 가장 먼저 사용하는 파일
- index와 App.vue를 연결시키는 작업이 이루어지는 곳

### SFC
### Component
UI를 독립적이고 재사용 가능한 조각들로 나눈 것으로 __기능별로 분화한 코드 조각__
- 보편적으로 중첩된 컴포넌트들의 tree로 구성
- App.vue를 루트(최상위) 컴포넌트로 하여 여기서 tree가 만들어지는 구조 → 유지보수, 재사용성, 확장 가능

- 그렇다면 Vue에서 말하는 componenet? 
  - 이름이 있는 재사용 가능한 Vue instance!
- 그렇다면 Vue instance란?
  - `new Vue()`로 만든 인스턴스 
  - 템플릿의 하나의 구역을 담당했으니 컴포넌트의 역할

#### SFC
하나의 .vue 파일이 하나의 인스턴스이고, 하나의 컴포넌트이다.
- Vue instance를 기능 단위로 작성하는 것이 핵심! → 컴포넌트 기반 개발의 핵심 방법
- HTML, CSS, JS를 .vue라는 확장자를 가진 파일 안에서 관리하며 개발 진행
- 해당 파일을 vue 인스턴스이자 vue 컴포넌트이며 기능 단위로 작성

### Vue Component 구조
#### 템플릿
#### 스크립트(JS)
- 자바스크립트 코드가 작성되는 곳
- 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
#### 스타일(CSS)

### Vue Component 실습
NOW, 어떻게 연결하고 사용하는지 배워보자!

#### 📍 유의사항
- 상위 컴포넌트가 script 태그 안 name으로 인식해서 가져감
- 하나의 컴포넌트에서 template은 html 영역라고만 선언하는 태그일 뿐이지 사실상 태그가 없는 것이기 때문에 렌더링되는 곳으로서 반드시 최상위 태그가 하나 있어야 함 (div 외의 태그 모두 가능)

#### 1️⃣ MyComponent.vue 생성
1. src/components/ 안에 생성
2. script에 이름 등록
3. template에 요소 추가

#### 2️⃣ Component 등록
1. 불러오기
```js
import MyComponent from './components/MyComponent.vue.'
import MyComponent from '@/components/MyComponent' // @ : src 의미 (절대 경로)
```
2. 등록하기
```js
export default {
  name: "App",
  components: {
    HelloWorld,
    // 2. 등록하기
    MyComponent,
  },
};
```
3. 보여주기
```html
<div id="app">
    <!-- 3. 보여주기 -->
    <MyComponent />
```
❗ 하위 컴포넌트의 - 또 하위 컴포너트를 만들 수 있고, 형태는 같은데 내용은 다른 재사용까지 가능하다.

#### 스타일 가이드
- 싱글 파일 컴포넌트 이름 규칙 지정
  - `MyComponent` 형식
  - 베이스 컴포넌트 이름엔 `Base` 붙이기
  - `The` - 오직 싱글로만 존재할 경우 붙이기
  - 강한 연관성을 가진 컴포넌트 이름 - 하위 컴포넌트로 들어가는 파일의 이름은 상위의 것을 받아서 사용
  - ...

## 데이터 교환
❓ 이렇게 작성한 컴포넌트 구조에서, 데이터가 어떻게 교환될까?

- 프로젝트 있는 위치에서 `npm install`만 하면 clone 가능

## Pass Props & Emit Events
- 한 페이지 내에서 같은 데이터를 공유해야 함
- BUT 페이지들은 component로 구분이 되어있음
- 즉, 상위에서 정의된 data를 하위에서 사용하려면 어떻게 보낼 수 있을까?
- 또 다시 선언하는 것은 하나의 component에서 data가 변경된 것을 반영할 수 없으므로 공유해야 함
❓ 완전히 동일한 data를 서로 다른 독립적인 component에서 보여주려면? → 컴포넌트의 부모-자식 관계만 데이터를 주고받게 하자!

- 부모 -> 자식
  - pass `props`의 방식 - 데이터
- 자식 -> 부모
  - `emit` event의 방식 - 이벤트

### 📌 Pass Props
#### 정적인 props
- 요소의 속성을 사용하여 데이터 전달 : `prop-data-name="value"` kebab-case : html에서의 속성값은 대소문자를 구분할 수 없어서. 보내는 쪽 html(케밥) - 받아서 선언하는 곳 javascript(카멜)
  - 예시) msg-title → msgTile로 받아야 함
```html
<MyComponentItem static-props="MyComponent에서 보낸 데이터" />
```
- Prop 명시
  - 하위 컴포넌트는 자신에게 부여된 msg property를 템플릿에서 {{ msg }} 형태로 사용
```
props: {
    staticProps: String, // 변수명: 타입
  }
```

#### Dynamic props
- 변수를 props로 전달할 수 있음
- 단순 문자열이 아니라 javascript 표현식으로! → `v-bind` 디렉티브로 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 반영됨
- data는 함수의 return 객체여야 함 → vue-cli에서는 이름 공간 스코프 문제 때문!

- 컴포넌트의 data → return으로 감싸줘야 다른 컴포넌트와 공유하지 않도록 됨

#### props 데이터는 단방향 데이터 흐름!
- 모든 props는 부모 - 자식으로 아래로 단방향 바인딩을 형성
- 부모 업데이트 -> 자식 업데이트, 반대는 불가능
- 이유
  - 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 어려워지는 것을 방지

### 📌 Emit Event
- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 간접적으로 이벤트를 발생시킴
- 이벤트를 발생시키는 것이란?
  - > 데이터를 이벤트 리스너의 콜백함수의 인자로 담아서 위로 전달
  - > 상위 컴포넌트는 계속 듣고 있다가 해당 이벤트를 통해 데이터를 받음

#### `emit` 메서드
- 부모에게 소리칠 메서드를 호출
- $emit('event-name') 형식으로 부모에게 even-name이라는 이벤트가 발생했다는 것을 알려서 
- 실습

#### 과정
1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수 호출
2. ?
3. ?
```html
<button @click="childToParent">클릭!</button>

methods: {
    childToParent: function () {
      this.$emit("child-to-parent", "나는 자식이 보낸 데이터다.");
    }, // emit(단순 이름, 데이터)

<MyComponentItem
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent" // 발생했는지 듣고 있는 이벤트 = 실행할 메서드

methods: {
    parentGetEvent: function (childData) {
      console.log("자식 컴포넌트에서 발생한 emit 이벤트를 들었다!");
      console.log(childData);
    },
  }, // function의 인자로 밑에서 받은 데이터 사용 가능. 즉, 전달한 데이터는 부모 컴의 핸들러 함수의 인자로 사용 가능
```
- 여러 데이터를 보내는 방법은?
  - 리스트 활용... etc.
- IF 더 위에까지 보내고 싶다면?
  - 한 단계 상위 컴포넌트에서 자식처럼 그대로 또 끌어올려야 한다.

### emit with data 흐름 정리
1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수 호출
2. 호출된 함수에서 emit을 통해 부모 컴포넌트에 이벤트를 발생
3. 부모 컴포넌트는 자식 컴포넌트의 이벤트를 청취하여 연결된 핸들러 함수 호출, 함수의 인자로 전달된 데이터가 포함되어 있음
4. 호출된 함수에서 console.log(`~child data~`) 실행

### emit with dynamic data
- 양방향 바인딩
- 채워진 값을 바로 emit의 두번째 인자로 쏴줌
- 부모) 그 emit 이벤트를 들으면 실행할 핸들러 함수 연결
- 받은 데이터는 인자로 받아서 사용

#### case
> HTML 요소에서 사용 - kebab
> JS에서 사용 - camel
- props
  - 상위 -> 하위 : HTML 요소로 내림 - kebab
  - 하위에서 받을 때 : JS에서 받음 - camel
- emit
  - emit 이벤트 발생, HTML 요소가 이벤트를 청취 - kebab
  - 메서드, 변수명 등은 JS에서 사용 - camel