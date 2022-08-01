#### Introduction

## HTML

웹 사이트 : 브라우저를 통해서 접속하는 웹 페이지(문서)들의 모음

- 글, 그림, 동영상 등 여러가지 정보를 담음
- 마우스로 클릭하면 다른 웹 페이지로 이동하는 ‘링크’들이 있어 이를 통해 웹 페이지를 연결한 것을 웹 사이트라고 함
- 구성 요소
    - HTML - 구조
    - CSS - 표현
    - Javascript - 동작
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우 존재(파편화) -> 해결책 : 웹표준
- MSword, 한컴 문서 (브라우저) -> 문서 (HTML)

### 웹 표준
- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)

### HTML이란?
Hyper Text란? 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

### Markup Language
태그(ex. <h1>) 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
ex. HTML, Markdown
즉, HTML는 웹페이지를 작성(구조화)하기 위한 언어
- HTML 스타일 가이드 : 마크업 스타일 가이드(2 space)

## HTML 기본 구조
- html : 문서의 최상위(root) 요소
- head : 문서 메타데이터(실제 데이터를 위한 데이터, 내용) 요소 (ex. 찍은 곳, 시간, 해상도)
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등 
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소 (ex. 사진)

### head 예시
- <title>
- <meta>
- <link>
- <script>
- <style>

- 예시) Open Graph Protocol : 메타 데이터를 표현하는 새로운 규약으로 HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
- ~놓침~

### 요소
태그 + 내용

#### 속성
- 태그의 부가적인 정보를 설정
- 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하여 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(Global)이 있음
  - HTML Global Attribute
    - data-* : 좋아요 기능

### 시맨틱 태그
HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것
웹 사이트 읽어주는 빅스비 인공지능들이 <header>을 파악해서 읽어주는 기술에 사용되기도 함
검색 엔진 최적화를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야 함

----
렌더링 : 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정
DOM 트리
: 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
- HTML 문서에 대한 모델을 구성
- HTML 문서 내의 각 요소에 접근/수정에 필용한 프로퍼티와 메서드를 제공

## HTML 문서 구조화
#### 태그들
- 텍스트 요소
- 그룹 컨텐츠

### form
<form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그 -> Django에서 깊게 배움
- ex. 로그인 창 같은 거 :  ID, PW가 서버에 전송이 되는데 이때 사용됨
- <form> 기본 속성
  - action : form 처리할 서버의 URL(데이터 보낼 곳)
  - method : form 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
  - enctype :
    - 텍스트 기본값
    - 파일 전송시
  - GET 방식 예시)

### input
다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
form 안에 input 태그를 넣어서 데이터를 입력 받는다
- 대표적인 속성
  - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
- input label 
  - input 태그에 대한 상세한 설명을 label 태그로 사용
  - <input>에 id 속성(태그의 스페셜한 별명)을, <label>에는 for 속성을 활용하여 상호 연관을 시킴
  - ex. 아이디(label, for) : ____ (아이디 넣는 칸, input)

#### input 유형 - 일반
- text : 일반 텍스트 입력
- password : 특수기호로 표현
- email : 이메일 형식이 아닌 경우 form 제출 불가
- number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
- file : accpet 속성을 활용하여 파일 타입 지정 가능
- checkbox

항목 중 선택
- label 태그와 함께 사용하여 선택 항목을 작성
- 동일 항목에 대하여는 name 지정, 선택된 항목에 대한 value 지정
  - checkbox
  - radio

기타
- color, date, hidden

<a 태그 안에 글자만이 아니라 이미지도 넣을 수 있음>

- 정리
- 태그가 있고 태그 + 속성을 만들어서 구조를 잡으면 되는구나
- iinput태그같은 경우 속성에 뭐뭐뭐가 있고, 이 속성은 태그마다 다르기때문에
- form이랑 input태그, input태그에 쌍으로 label태그


## CSS
계단식으로 퍼져나가는, 상속되는 개념처럼! 작성한 코드나 표현, 꾸미기가 퍼져나간다
스타일을 지정하기 위한 언어
HTML 태그(원하는 부분)를 선택하고, 스타일을 지정한다. 

- CSS 구문
  ```
  h1(선택자, h1 태그를 의미) {color : blue; font-size: 15px;}
  ```
  선택자를 통해 스타일을 지정할 HTML 요소를 선택, 속성과 값을 ?

- 정의 방법
  - 인라인 - 해당 태그에 직접 style 속성을 활용
  - 내부참조
  - 외부참조 - 분리된 CSS파일, 가장 많이 쓰임
- 선택자의 우선순위가 존재 태그 고른 다음에 너 이 스타일 해!
- 인라인
  
### CSS Selectors
- 요소 선택자 : HTML 태그를 직접 선택 EX. 서울 사람
- 클래스 선택자 : .문자로  시작, 해당 클래스가 적용된 항목을 선택 EX. 서울 사람 중 김, 이, 박, 최, 씨
- 아이디 선택자 : #문자로 시작, EX. 최지웅 (점점 범위가 좁아짐)
클래스, 아이디, 태그로 스타일 지정?

- CSS 적용 우선순위
- 범위가 좁을수록 강하다!
'*' VS '태그' 라면 태그가 이김 (태그가 범위가 좁으니까)

- QUIZ
- 1 : 아무 것도 없으니까 P로 가서 yellow
- 2 : .class 로 가니까 blue
- 3 : blue green인데 : green
- 4 : green blue인데 왜 blue가 아니지? 적는 순서에서 밑에 있는 애가 이김, 파일 밑에 있는 애가 이김 -> green
- 5 : id red class blue에선 id가 이김 -> red
- 6 : h2에 !important -> darkviolet
- 7 : id red class blue style color : yellow로 인라인이 범위가 젤 좁음 -> yellow
- 8 : 인라인 있어도 important가 이김 -> darkviolet

#### CSS 상속
<div> 얘가 red면 
  ㄴ<p> 얘네들
  ㄴ<p> red를 상속받음
속성 중 상속되는 것 / 되지 않는 것
: Text 관련 요소 / 여백이나 레이아웃 관련된 것
```
<p>안녕하세요
  <span>테스트</span> SPAN은 P의 border는 상속받지 못함
  입니다
</p>
```

#### CSS 기본 스타일
- 크기 단위
- no class에도 상속돼서 들어갑니다?

#### 결합자 (Combinators)
자손(공백), 자식, (<<이 두개가 많이 쓰임) 일반 형제, 인접 형제
- 자손 결합자
  div 태그 안에 있는 모든 span 태그가 자손이 돼서 다 빨간 색이 됨
- 자식 결합자
  selectorA 바로 아래의 selectorB요소라 바로 아래 자식만 해당되니까 밑 span은 부모가 <p>라서 적용이 안됨
- 일반 형제
  p 뒤에 있는 span 태그를 의미. 같은 레벨
- 인접 형제
  바로 뒤에 있는 것만 해당

### CSS Box Model
css의 큰 원칙 중 하나 : CSS의 모든 것은 BOX다!
모든 요소는 네모(박스 모델)이고, 위에서부터 아래로 왼쪽에서 오른쪽으로 쌓임 (좌측 상단에 배치)

- Box Model 구성
  - Maring, Border, Content, Padding

- margin/padding : shorthand를 통해서 표현 가능 상하/좌우, 상/좌우/하, 상/우/하/좌

### CSS Display
display : block
  테트리스처럼 취급, 한 줄 다 차지하면서 쌓인다.
display : inline
  글자처럼 취급, 상하 여백은 line-height로 지정한다. 

text-align : 부모요소에다 해줘야 함?
none과 hidden의 차이 이해하기

### CSS Position
레이아웃을 다루는 것
- static
- relative
  - 기존 위치 대비 offset
- absolute
  - static이 아닌 친구를 찾는다. relative 못 만나면 브라우저 기준으로 포지션이 옮겨감, 공중에 떠서 위치 차지 X
- fixed
  - 화면 기준으로 옮김, 위치 차지 O