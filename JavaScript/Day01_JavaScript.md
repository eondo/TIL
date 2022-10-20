# JavaScript
- HTML 문서의 콘텐츠의 동적으로 변경할 수 있는 언어 → 웹 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게 된 기반
- for me, 언어 배우면서 언어 + framework 배우기

## JavaScript 기본 문법
### 코드 작성법
- 코드 블럭
  - 중괄호 {}를 사용해 코드 블럭을 구분
- 주석
  - //, /* */
### 변수와 식별자
- 케이스
  - 카멜 케이스
    - 변수, 객체, 함수에 사용
    - cameCase
  - 파스칼 케이스
    - 클래스, 생성자에 사용
    - PascalCase
  - 대문자 스네이크 케이스
    - 상수에 사용
    - SNAKE_CASE
### 변수 선언 키워드
1. `let`
- 블록 스코프 지역 변수를 선언
2. `const`
- 읽기 전용 상수를 선언
3. `var`
- 변수를 선언

[참고] 변수가 만들어지는 과정 - 선언, 할당, 초기화
- 선언 : 변수를 생성하는 행위 or 시점
- 할당 : 선언된 변수에 값을 저장하는 행위 or 시점
- 초기화 : 선언된 변수에 처음으로 값을 저장하는 행위 or 시점
[참고] 블록 스코드
- python의 이름공간
- if, for 함수 등의 중괄호 {} 내부를 의미
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

#### let
재할당 가능, 재선언 불가능
```
let number = 10
number = 20 (O)
let number = 20 (X)
```
```js
let line = ''
for (let i = 1; i < 6; i++) {
  let line = '*'.repeat(i)
  console.log(line)
}
// 되는 이유 : {} 이게 하나의 스코프, 그래서 여기서 안에서는 계속 바꿔지는 재할당이 허용됨
console.log(line)

// 재할당은 앞에 변수 타입 없이 변수에 값을 지정해주는 것, 
// 재선언은 앞에 변수 타입 let, const 등이 붙어서 값 지정해주는 것,
// 따라서 위의 경우 for 위의 line과 for문 안의 line은 다른 것이라 다르게 출력됨
```

#### const
읽기 전용이기 때문에 재할당 불가능, 재선언 불가능
- 선언 시 반드시 초기값 설정, 이후 값 변경 불가능
- let과 동일하게 블록 스코프를 가짐
```
const number = 10
number = 10 (X)
const number = 20 (X)
```
- 기본적으로 `const` 사용을 권장
  - 재할당해야 하는 경우만 `let`

#### var
재할당 가능, 재선언 가능 → 호이스팅 됨, 함수 스코프를 가진다는 특성으로 const, ley을 사용하는 것을 권장

### 🧷데이터 타입
- 원시 타입 : Number, String, Boolean, undefined, null, Symbol
- 참조 타입 : Objects - Array, Function, ...etc.

#### Number
- 정수 or 실수형 숫자를 표현하는 자료형
- `Nan`
  - 숫자로서 읽을 수 없음, 결과가 허수인 수학 계산식, 피연산자가 NaN

#### String
작은 따옴표 or 큰 따옴표로 표현, 덧셈을 통해 문자열 붙일 수 있음
- Quote 사용 시 선언할 때 줄 바꿈이 안됨 → \n 사용
- **Template Literal** : 문자열 사이에 변수를 삽입 가능 (파이썬에서의 f-string, 백틱 사용)
  - ex. `나는 ${age}세 입니다.`

#### Empty Value
- null
  - 변수의 값이 없음을 의도적으로 표현할 때 사용
  - 값으로써 쓰고 싶을 때
- undefined
  - 값이 정의되어 있지 않음을 표현하는 값
  - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

#### Boolean
조건문 or 반복문에서 유용하게 사용 
- true, false → 자동형변환 규칙 O

### 🧷연산자
#### 할당 연산자
c += 1
#### 비교 연산자
#### ❗동등 연산자
비교할 대 암묵적인 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교, 특별한 경우 제외하고 사용 X → 일치 연산자 사용!
- 1 == '1', 1 == true
#### 일치 연산자
값, 타입이 모두 같은 경우 true를 반환
#### 논리 연산자
and - *&&*, or - *||*, not - *!*
#### 삼항 연산자
return이 있어서 따로 변수에 할당 가능
```
const result = Math.PI > 4 ? 'Yep' : 'Nope'
```

### 🧷조건문
- 조건문의 종류와 특징
#### `if`
조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단 → *if, else if, else*
#### `switch`
주로 특정 변수의 값에 따라 조건을 분ㄴ기할 때 활용, 표현식의 결과값을 이용한 조건문
- fall through 현상 막기 위해 break를 작성
- 조건문이 많은 경우 switch문을 통해 가독성 향상 가능하나 기본적으로는 if문으로 작성
```
const name = '내이름'

switch(name) {
  case '내이름': {
    ...
  }
}
```

### 🧷반복문
*while, for, for...in, for...of*
#### while
#### for
초기문은 처음 한 번만 동작, 조건문 보고 증감문 동작을 반복
```
for ([초기문]; [조건문]; [증감문]) {
  // 작업
}
```
#### for...in
객체 전용! 객체 속성을 순회할 때 사용
- 객체 : key-value 형태로 되어있는 것 (파이썬의 딕셔너리), 여기서 객체의 속성 값에 접근하는 것이 for...in
- 인덱스 순으로 순회한다는 보장이 없으므로 배열에는 사용 X
#### for...of
객체를 제외한 나머지, iterable를 순회할 때 사용
- 반복 가능한 객체(iterable) : Array, Set, String 등
- *for in* vs *for of*
  - *for in*은 속성 이름을 통해 반복
  - *for of*는 속성 값을 통해 반복 

[참고] 반복 시 해당 변수를 새로 정의하여 사용하므로 const (재할당 불가능)를 사용할 수 있는데, 일반적인 for문에서는 최초 정의한 i를 재할당하면서 사용하기 때문에 const를 사용하면 x

## 함수
함수를 정의하는 방법 : 함수 선언식, 함수 표현식
### 함수의 정의
- 함수 선언식
- 함수 표현식
#### 매개변수와 인자의 개수 불일치 허용
#### Spread syntax(...)
전개구문
- 배열이나 문자열과 같이 반복 가능한 객체를 요소, 인자로 확장할 수 있음
1. 배열과의 사용
2. 함수와의 사용 : 정해지지 않은 수의 매개변수를 '배열'로 받을 수 있음

#### 선언식과 표현식
- 공통점
  - 데이터 타입, 함수 구성 요소(이름, 매개변수, 바디)
- 차이점
  - 선언식) 익명 함수 불가능, 호이스팅 있음
  - 표현식) 익명 함수 가능, 호이스팅 없음

### Arrow Function 화살표 함수
함수를 비교적 간결하게 정의할 수 있는 문법, fuction 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위함
- 익명 함수, 표현식에서만 사용 가능
1. function 키워드 생ㅇ략 가능
2. 함수 매개변수가 하나뿐 → () 생략 가능 (BUT 권장 X)
3. 함수 내용 한줄 → {}, return 생략 가능 (예외 : object를 리턴하는 경우, return을 명시적으로 적어줌)
```js
const greeting = function (name) {
  return `Hi ${name}`
}

// 1단계. function 없앰
const greeting = (name) => {
  return `Hi ${name}`
}
// 2단계. 인자의 소괄호 없앰 - 권장 X
const greeting = name => {
  return `Hi ${name}`
}
// 3단계. 중괄호, return 없앰
const greeting = name => `Hi ${name}`
```

#### 즉시 실행 함수
선언과 동시에 실행되는 함수, 함수의 선언 끝에 '()' 추가해서 실행
- 선언과 동시에 실행되어 같은 함수를 다시 호출 불가능 (일회성!)
- 중간에 코드에 끼인 경우 사용, 초기화 부분에 많이 사용, 익명함수로 사용하는 것이 일반적
```js
function (num) {return num **}
// 밑으로 변환(화살표 함수)
(num) => num ** 3

// 즉시 실행
((num) => num ** 3)(2)
```

## Array와 Object
JavaScript의 데이터 타입 중 참조 타입에 해당하는 타입 Array, Object으로 객체(속성들의 모음)이다.
  
### 배열(Array)
- 키와 속성들을 담고 있는 참조 타입의 '객체'
- 순서를 보장하는 특징
- []로 생성, 배열의 길이는 array.length로 접근

### 배열 메서드 기초
- reverse
- push & pop
- unshift & shift
- includes
- indexOf
- join

### 배열 메서드 심화
- Array Helper Methods 
  - 구조 : ex. numbers 배열의 요소가 하나마다 반복될 때마다 콜백 함수의 인자로 들어감! (number)로! 그래서 return된 결과가 2가 되는 거고...
  - 배열을 순회하며 각각에 뭘 해줄 것인가? 어떤 기준을 적용시킬 것인가? 이에 대한 로직을 작성해야 함 그 로직이 다른 함수 `callback` 함수에 들어있음
  - 메서드 호출 시 인자로 callback 함수를 받는 것이 특징
  - `callback 함수` : 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

#### forEach
array.forEach(callback(element[, index[,array]]))
```js
// 1.
const colors = ['red', 'blue', 'green']

const printClr = function (color) {
  console.log(color)
}

colors.forEach(printClr)
// red
// blue
// green

// 2. colors를 순회하자! forEach에 인자로 통째로
// colors 요소를 반복하면서 각각의 요소에 안에 함수를 적용시킴
colors.forEach(function (color) {
  console.log(color)
})


// 3. 실제로는 어떻게 쓰냐면, 화살표 함수로 바꾸기!
colors.forEach((color) => {
  console.log(color)
})
```

#### map
배열의 각 요소에 대해 콜백 함수를 한 번씩 실행하면서 콜백 함수의 반환값을 요소로 하는 새로운 배열을 반환한다. forEach의 기본적인 동작 + 반환!
- 기존 배열을 다른 형태로 바꿀 때 유용함
```js
const numbers = [1, 2, 3, 4, 5]

const doubleEle = function (number) {
  return number * 2
}

const newArry = numbers.map(doubleEle)

// 2.
const newArry = numbers.map(function (number) {
  return number * 2
})

// 3.
const newArry = numbers.map((number) => {
  return number * 2
})

// 4.
const newArry = numbers.map((number) => number * 2)

console.log(newArry)
// [ 2, 4, 6, 8, 10 ]
```

#### filter
map + 특정 조건의 true인 것만 걸러서 새로운 배열을 반환함
- 객체
```js
const fruitFilter = function (product) {
  return product.type == 'fruit'
}

const newArry = products.filter(fruitFilter)

// 2.
const newArry = products.filter(function (product) {
  return product.type == 'fruit'
})
```

#### reduce
인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과 값을 반환한다.
- reduce 메서드의 주요 매개 변수
  - acc
    - 이전 callback 함수의 반환 값이 누적되는 변수
  - initialValue(초기값)
    - acc의 초기값
```js
const numbers = [90, 80, 70, 100]

// 총합
const sumNum = numbers.reduce((result, number) => {
  return result + number
}, 0)
// result + number의 리턴값이 다음 callback 함수의 result인자로 들어감
// 첫번째 인자가 callback 함수, 두번째 인자 initialvalue로써 0
console.log(sumNum)

// 평균
const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length
```

#### find
콜백 함수의 반환값이 참이면, 조건을 만족하는 첫번째 요소를 반환한다.
- 찾는 값이 배열에 없으면 undefined 반환
```js
const avenger = avengers.find((avenger) => {
  return avenger.name == 'Tony Stark'
})

console.log(avenger)
// { 'name': 'Tony Stark', 'age': 42 }
```

#### some
배열 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환한다.
#### every
모든 요소가 주어진 판별 함수를 통과하면 참을 반환한다.
- 빈 배열은 항상 true 반환
```js
// some
const arr = [1, 2, 3, 4, 5]

const result = arr.some(function (elem) {
  return elem % 2 == 0
})

const result = arr.some((elem) => {
  return elem % 2 == 0
})

const result = arr.some((elem) => elem % 2 == 0)

// every
const result = arr.every((elem) => elem % 2 == 0)
```

#### 배열 순회 비교
for loop, for...of, forEach
- for...of : 인덱스 없이 배열의 요소에 바로 접근 가능 + break, continue 사용 가능
- forEach : break, continue 사용 불가능

## 객체 (Object)
❓ 객체 → 속성의 집합이며, {} 내부에 key-value의 쌍으로 표현됨
- key : 문자열 타입만 가능
- value : 모든 타입(함수 포함) 가능
- 객체 값에 대한 접근 : 점(.) 또는 대괄호([])로 가능
  - key 이름에 띄어쓰기 같은 구분자 있을 시 대괄호 접근만 가능

### 객체 관련 문법
#### 1. 속성명 축약
객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 축약 가능
#### 2. 메서드명 축약
메서드 선언 시 function 키워드 생략 가능
#### 3. 계산된 속성
객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능
```js
const myObj = {
  [key]: value,
}

console.log(myObj) // { country: ['한국', '미국', '일본', '중국'] }
console.log(myObj.country) // ['한국' ,'미국', ...]
```
#### 4. 구조 분해 할당
배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
- 변수에 중괄호 씌워서 .으로 접근하는 게 사라져서 오른쪽 객체를 왼쪽으로 할당할 때 분해해서 원하는 name만 찾아서 넣을 수 있다.
- 한번에 변수 여러 개를 할당할 때 편함
#### 5. Spread syntax(...)
객체 내부에서 객체 전개가 가능하다.
- 얕은 복사에 활용 가능

### JSON 변환
Object와 유사한 구조를 가지고 있지만, Object는 그 자체로 타입이고, JSON은 형식이 있는 '문자열' → 즉, 변환 과정이 필요하므로 js에서는 JSON을 Object로 바꿔야 함 (파이썬에서는 dict으로 바꿨었음)
- ❗ 결국 Django가 만든 json을 vue.js가 받아서 파싱해서 데이터 조작, 뿌리는 과정에 쓰임
```js
const jsonData = {
  coffee: 'Americano',
  iceCream: 'Mint Choco',
}

// 1. Object -> json 변환
const objToJson = JSON.stringify(jsonData)

console.log(objToJson) // {"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof objToJson) // string

// 2. json -> Object 변환
const jsonToObj = JSON.parse(objToJson) // API랑 소통할 때 사용해야 하는 코드, JS에서 쓰려면 Object로 바꿔야 함

console.log(jsonToObj) // { coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof jsonToObj) // object
console.log(jsonToObj.coffee) // 이제, 이런 방식으로 접근 가능
```