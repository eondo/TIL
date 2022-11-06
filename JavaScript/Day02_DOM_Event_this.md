### Intro
- 브라우저에서의 JavaScript
  - 정적인 정보만 보여주던 웹 페이지 → 데이터가 주기적으로 갱신, 사용자와 상호 작용, 애니메이션 동작 O
  - html으로 응답할 땐 요청을 할 때마다 새롭게 응답했는데, DOM을 통해 화면상에서 실시간으로 바뀔 수 있음 

자바스크립트가 client side에서 자스가 추가적으로 사용할 수 있는 기능이 있고, 이것은 API를 통해 가능함.

- 대표적으로 제공되는 대표 API
- Browser APIs
  - 현재 컴퓨터 환경에 관한 데이터를 제공, 오디오 재생 등 여러가지 복잡한 일을 수행할 수 있게 함
  - JavaScript로 Brower API들을 사용 가능
  - 대표적인 종류 : DOM


### DOM
문서 객체 모델, 문서의 구조화된 표현을 제공, 프로그래밍 언어는 DOM 구조

- JS는 브라우저에서 DOM API라고 하는 것을 통해서 문서를 동적으로 수정하고, 사용자 인터페이스를 실시간으로 바뀌게 함

- DOM은 문서를 논리 트리로 표현
- DOM 메서드를 통해 문서의 구조, 스타일, 컨텐츠를 변경 가능
- 즉, 웹 페이지의 객체 지향 표현으로, JS와 같은 스크립트 언어를 이용해 DOM을 수정 가능

- DOM에 접근하기
  - DOM의 주요 객체(주요 상위 클래스)들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

- DOM의 주요 객체
  - window, document

### window object
DOM을 표현하는 창
- 가장 최상위 객체로서 생략 가능
- 각각의 탭을 각각의 window 객체로 나타냄, 즉 하나 탭의 전체 창을 의미함 → 기능이 있으면 그에 대한 메서드도 존재하는 것! ex. 새로운 탭 열기 → window.open()

우리는 브라우저 조작보다 문서 조작을 많이 할 것 → document

### document object
브라우저가 불러온 웹 페이지
- 페이지 컨텐츠의 진입점, 문서 전체를 접근하기 위한 객체 document

- title 탭에 접근 html 코드로 접근한 게 아니라 js로 객체로 접근해서 속성값을 바꿈 즉, 하나의 요소를 속성과 객체로 바라보겠다. 그래야 프로그래밍 언어를 사용할 수 있기 때문에.


## DOM 조작
Document가 제공하는 기능을 사용해 웹 페이지 문서 조작하기
1. 선택 → 2. 조작

### 선택 관련 메서드
1. document.`querySelector`(selector)
  - 제공한 선택자와 일치하는 element 한 개 선택
  - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환

2. document.`querySelectorAll`(selector)
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 매칭하는 하나 이상의 셀렉터를 포함하여 인자(문자열)로서 NodeList로 반환받음

- id를 통해서 h1 선택해보자 -> '#title'
- class를 통해서 p태그 선택해보자 '.text'
- 

단일 선택으로 클래스 선택하면 어떻게 될까?
ul-li 타고 가야 하는 경우는?
```js
    console.log(document.querySelector('#title'))
    console.log(document.querySelectorAll('.text'))

    console.log(document.querySelectorAll('body > ul > li'))
    // body > ul > li
    // body > ul > li:nth-child(1)
```
[참고] NodeList
- index로만 각 항목에 접근 가능
- 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
- querySelectorAll()으로 나오는 NodeList는 정적 콜렉션이므로 DOM의 변경사항을 실시간으로 반영 X → 순회 중이거나 list 길이값을 이미 사용하고 있는 중에 바뀌는 것은 오히려 역효과!


### 조작 관련 메서드(생성, 입력, 추가, 삭제)
- 생성
  - document.`createElement`(tagName)
  - 작성한 tagName의 HTML 요소를 생성하여 반환
- 입력 관련 메서드
  - 메서드로 분류됐지만 속성값임
  - Node.`innerText` : 만들어진 태그 안에 text 형태로 채워지는 내용
- 추가
  - Node.`appendChild()`
  - 문서에 실제로 최종적으로 올리려면 누군가의 태그의 자식으로 넣어야 하는데 이 중 어디에 배치할 것인가 → 하나하나가 DOM 구조, 트리 구조로 되어있어서 어떤 것의 하위로 넣어줘야 함
  - 한 Node(태그)를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 한 번에 하나의 Node만 추가 가능
  - 추가된 Node 객체를 반환
- 삭제
  - Node.`removeChild()`

[실습] *02_create_append*
```
// 태그 생성
const h1Tag = document.createElement('h1')
<h1>​</h1>​
const h1Tag = document.createElement('hi')
undefined
ByteLengthQueuingStrategy
ƒ ByteLengthQueuingStrategy() { [native code] }
h1Tag
<hi>​</hi>​
h1Tag.innerText = 'DOM 조작`
VM401:1 Uncaught SyntaxError: Invalid or unexpected token
h1Tag.innerText = 'DOM 조작'
'DOM 조작'
h1Tag
<hi>​DOM 조작​</hi>​
divTag = document.querySelector('div')
<div>​</div>​
divTag.appendChild(h1Tag)
<hi>​DOM 조작​</hi>​
divTag.removeChild(h1Tag)
<hi>​DOM 조작​</hi>​
```

### 속성값 추가 및 삭제 가능
### 조작 관련 메서드(속성 조회 및 설정)
- Element.getAttribute(attributeName)
  - 해당 요소의 지정된 값(문자열)을 반환

- Element.setAttribute(name, value)
  - 지정된 요소의 값을 설정
  - name = 'value'
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 대로 새 속성이 추가됨

```html
const aTag = document.createElement('a')

// 속성 추가
aTag.setAttribute('href', 'https://google.com')
아직 여전히 출력되지 않음 태그가 바디에 추가된 것은 아니기 때문

// 속성 바꾸기 - 어떻게 클래스값에 접근하지?
h1Tag.classList
DOMTokenList ['red', value: 'red']

// 사용하는 메서드 toggle
h1Tag.classList.toggle('blue')

-> toggle이 기존 클래스가 존재하면 red를 지우고 온 게 아니라 blue가 추가된 것! css상에서는 마지막으로 선언된 게 적용되니까!
```

웹이 동작하는 과정은 무언가 발생해서 사건이 반드시 발생한다!

## Event
프로그래밍하고 있는 시스템에서 일어나는 사건 혹은 발생
각 이벤트에 대해 조작할 수 있도록 특정 시점을 시스템이 알려주는 것
- ex. 버튼 클릭 -> 클릭이라는 사건에 대한 결과를 받거나, 조작을 할 수 있음

### Event object
네트워크 활동이나 사용자와의 상호작용 같은 것을 알려주는 객체
1. DOM 요소는 Event를 받고 `수신`
2. 받은 event를 `처리`
   1. event 처리는 주로 `addEventListner()`라는 event 처리기를 다양한 html요소에 부착해서 처리함

#### Event handler
- 대상에 특정 event가 발생하면, 할 일을 등록하자
- EventTarget.addEventLitener(type, listener)

- eventtarget : event를 지원하는 모든 객체 element, document, window 등 다 가능?
- type : 반응할 event 유형을 나타내는 대소문자 구분 문자열
  - ex. *input, click, submit*
  - ?
  - 
- listner : 호출할 함수, 콜백 함수 들어감, event가 콜백함수의 인자로 들어감(이벤트 객체를 사용할 수 있도록),
```
<script>
    const btn = document.querySelector('#btn')
    let countNum = 0  // 초기값

    // 이벤트 핸들러 작성
    btn.addEventListener('click', function (event) {
      // console.log(event) // 이벤트 객체 : PointerEvent {isTrusted: true, pointerId: 1, width: 1, height: 1, pressure: 0, …}
      // 0을 바꿔야 하니까 0이 든 p 태그 선택
      const pTag = document.querySelector('#counter')

      countNum += 1

      pTag.innerText = countNum

    })
  </script>
```
- 입력하는대로 출력하기
```
<input type="text" id="text-input">
  <p></p>
  <script>
    // 1. input 태그에 이벤트 핸들러 부착하기 위해 input 선택
    const inputTag = document.querySelector('#text-input')

    // 2. 이벤트 핸들러 부착
    inputTag.addEventListener('input', function (event) {
      // console.log(event)
      // console.log(event.target.value)  // 어디서 입력한 값을 들고있을까?

      // 3. pTag 선택
      const pTag = document.querySelector('p')
      pTag.innerText = event.target.value

    })
  </script>
```

### Event 취소
event 동작이 불필요한 순간들이 있음
a 태그, form 태그의 기본 동작이 필요 없을 때가 있음 -> 다른 기능을 추가하고 싶을 때 기본 동작들을 막아주는 것
- `preventDefault()`
- ex. 복사 금지
```
<script>
    const h1Tag = document.querySelector('h1')
    h1Tag.addEventListener('copy', function (event) {
      event.preventDefault()
      alert('복사할 수 없습니다!')
    })
  </script>
```
### 종합 실습
- 실습 : 로또 번호
```html
<h1>로또 추천 번호</h1>
  <button id="lotto-btn">행운 번호 받기</button>
  <div id="result"></div>

  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    const btn = document.querySelector('#lotto-btn')
    btn.addEventListener('click', function (event) {

      // 공이 들어갈 컨테이너 (태그) 생성
      const ballContainer = document.createElement('div')
      ballContainer.classList.add('ball-container')

      // 공 만들기 전에 랜덤한 숫자 6개 만들기
      const numbers = _.sampleSize(_.range(1, 46), 6)
      // console.log(numbers)

      // 공 만들기
      numbers.forEach((number) => {
        const ball = document.createElement('div')
        ball.innerText = number
        ball.classList.add('ball') // 얜 왜 점이 없지?
        // css 넣기
        ball.style.backgroundColor = 'crimson'
        ballContainer.appendChild(ball)
      })
      // 최종적으로 공 컨테이너를 결과 영역의 자식으로 넣기
      const resultDiv = document.querySelector('#result')
      resultDiv.appendChild(ballContainer)
    })
  </script>
```

### 종합실습 2

## this
어떠한 object를 가리키는 키워드(python에서의 self로, 자기자신을 가리킴)
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
- 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작 
- 해당 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐
- 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 **함수가 어떻게 호출되었는지**에 따라 동적으로 결정됨

1. 함수 문맥에서의 this
   1. 단순 호출
   2. Method(객체의 메서드로서)
   3. Nested

#### 전역 문맥에서의 this
브라우저 전역 객체인 window를 가리킴

### 함수 문맥에서의 this
함수 내부에서 this의 값은

#### 1. 단순 호출
전역 객체를 가리킴

#### 2. Method
객체가 있으면 객체의 메서드가 있는데, 이 메서드가 같은 곳에 있는 객체 데이터인 1에 접근할 수 있음. 왜냐면 this가 본인이 들어가있는 객체를 가리키기 때문. 이 this는 전역이 아니라 해당 객체가 바인딩 됨. -> 장점 : 객체에 있는 데이터들을 이 메서드가 사용할 수 있음. 'this가 누구를 가리키냐?'

#### 3. Nested
함수 안에 함수, (콜백 안에)
- 함수의 this는 호출방식에 의해 결정되는데, 이 콜백 함수는 메서드로서 호출됐어? 함수 호출로서 호출됐나요? 후자! 스스로 함수가 호출함. -> 단순 호출은 전역 객체를 가리키므로 window가 됨. this가 미리 정해져있지 않음.
- 메서드로 호출됐다? 메서드로 호출된 객체를 가리킴
- 스스로 호출? 전역 가리킴
- 문제 : 하지만 myObj를 가리키게 만들어야 함! -> 해결 : 화살표 함수
- 화살표 함수에서 this는 자신을 감싼 정적 범위를 가리킴, 호출의 위치와 상관 없이 자동으로 한 단계 상위의 스코프(바로 myObj 안)의 문맥을 바인딩
- 결론 : 함수 내의 함수 상황은 '화살표 함수' 사용

- 주의 사항: eventListener 쓸 때, 화살표 함수 안 썼는데? 여기서 콜백 함수는 그럼 어떻게 되는 것? 이건 한 단계 위가 전역이라 window 가리킴 -> fucntion으로 쓰면 버튼을 가리킴, this.xx로 버튼 조작 가능

this가 호출되는 순간에 결정되는 것(런타임)에 대한
- 장점 : 함수(메서드)를 하나만 만들어서 여러 객체에서 재사용할 수 있다.
- 단점 : 이런 유연함이 실수로 이어질 수 있음

#### SUMMARY
객체의 형태는 key:value로, 
전역 객체에서의 this → window 자기자신
- ❓ 함수 안에서의 this의 인식
```
const func = function () {
  console.log(this)
}

const obj = {
  method: func,
}

❗ func()
-> 함수로서 호출할 때니까 window를 가리킴
❗ obj.method() : func이 발동되는 것은 똑같으나 obj의 객체에 종속된 메서드 != 함수
-> 메서드로서 호출 : 자기자신 객체 obj를 가리킴 (. 앞에 있는 객체)
```
3. bind를 통한 명시
```
inner함수.bind(this) -> 이 this를 함수 안의 this로 명시
```
4. 화살표 함수 -> 상위의 this 가리킴
- 호출이 아닌, 선언 기준으로 상위 스코프를 고려함

5. 콜백 함수에서의 this는 각각 다름
- 콜백 함수 : 제어권을 넘길 때 쓰는 함수
- 일반적으로 콜백 함수도 함수 호출이므로 this → 전역 객체
  - 콜백 함수를 제어하는 함수에서 this를 명시적으로 지정 가능한 경우도 존재
- addEventListener에서의 this → 이벤트가 발생하는 element를 가리킴