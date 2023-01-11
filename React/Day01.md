# React의 기초

### Create React App
`npx create-react-app '앱 이름'` - node.js 환경에서 웹서버로 리액트 앱 만들기
- react앱이 실행되면 어떻게 화면을 구성할까?
  - src 디렉토리 밑 index.js가 실행되고
  - index.html 안의 id가 root인 div 아래로 App.js 안의 앱 함수가 리턴하는 값이 들어감

- node_modules 폴더
  - node.js의 패키지 중 하나로 외부 모듈을 저장하는 폴더
  - 리액트도 외부 모듈 중 하나
- public 폴더
  - 당장은 쓰지 않지만 모바일 환경에서 아이콘 적용, 옵션을 적용할 때 쓰이는 옵션과 아이콘
  - robots.txt - 구글이 수집하는데 검색 엔진에 띄워줄 때 이건 수집하고, 하지 말아라 경로를 기준으로 알려주는 것
- src 디렉토리
  - source의 약자로, 스타일 파일 존재
  - App.js
    - js와 html이 합쳐져 있는 느낌
    - 웹의 html의 요소를 만들기 위해 js와 html을 합쳐져 쓸 수 있는 문법을 JSX라고 함
    - 별도의 html 요소를 묶어서 모듈처럼 만들어서 다른 곳에서 쓸 수 있도록 하는 개념 -> 컴포넌트 방식
    - es 모듈 시스템 사용 -> export default App; -> import App from '파일 경로'

- index.js 파일에는 최상위 컴포넌트를 정의할 수 있다.

### JSX
1. self closing tag
- 닫힌 태그를 꼭 가져야 한다. 태그 클로징이 필요 없는 태그도 닫혀야 하므로 열자마자 닫히게 해준다. ex. `<image />`
2. 최상위 태그 규칙
- 가장 바깥의 최상위 태그는 반드시 하나로 존재해야 한다.
- 또는, react.fragment로 최상위 태그를 대체하여 최상위 태그로 두고 싶지 않은 것을 감싸기
  ```js
  import React from 'react';
  ...
  <React.Fragment>
  ```
3. CSS 적용을 위해서 `className='App'`
- css 파일 사용
- 객체로 style을 만들어서 inline 스타일로 적용

4. javascript의 값을 사용하는 법
- {숫자, 문자열, 식}
- 조건부 렌더링 가능
  - ```js
      const number = 5;
      ...
      {number}는 : {number % 2 == 0 ? "짝수" : "홀수"}
      ```

### State
계속해서 동적으로 변화하는 상태, 그 상태에 따라 다른 행동을 수행하게 한다.

### Props
화면에 구성할 property들을 props로 관리되며, 부모와 자식 간의 props 이동이 필요하다.

## 실습
### 배열 사용 - 데이터 수정
- 목표
  - 배열을 이용한 React리스트에 아이템을 동적으로 수정하기
  - 조건부 렌더링

- prop 보내기 코드 수정
  ```js
  const onRemove = (targetId) => (
    const newDiaryList = data.filter((it) => it.id != targetId);
    setData(newDiaryList);
  );

  return (
    <div className="App">
      <DiaryEditor onCreate={onCreate} />
      <DiaryList onRemove={onRemove} diaryList={data} />
    </div>
  );

- 수정하기 버튼 추가
- 삭제하기 버튼 수정
  - 수정 전
  ```js
  <button
    onClick={() => {
      if (window.confirm(`${id}번째 일기를 정말 삭제하시겠습니까?`)) {
        onRemove(id);
      }
    }}>
    삭제하기
  </button>
  ```
  - 수정 후
  ```js
  const handleRemove = () => {
    if (window.confirm(`${id}번째 일기를 정말 삭제하시겠습니까?`)) {
      onRemove(id);
    }
  }
  ...
  return (
    <button onClick={handleRemove}>삭제하기</button>
  )
  ```

- 수정
#### 본문 수정 폼을 state를 이용
1. `isEdit` state 선언
```js
import { useState } from "react";

// 현재 수정 중인지 불린 값 isEdit
const [isEdit, setIsEdit] = useState(false)
```

2. `toggleIsEdit()` 함수 선언
- toggleIsEdit이 호출되면 원래의 isEdit 값을 반전시킨다.
```js
const toggleIsEdit = () => setIsEdit(!isEdit)
```
3. isEdit 값에 따른 버튼 반영
- 수정 폼의 데이터를 state로 핸들링할 수 있도록 state 만들기
```js
const [localContent, setLocalContent] = useState("");

...
// 
<div className="content">
  {isEdit ? (
    <>
      <textarea
        value={localContent}
        onChange={(e) => setLocalContent(e.target.value)}
      />
    </>
  ) : (
    <>{content}</>
  )}
</div>
```
4. 상태에 따라 다르게 보이는 수정 버튼 구현
- Vue.js에서 v-for를 사용한 것과 같이, {}안 삼항연산자 사용
```js
{isEdit ? (
  <>
    isEdit 참일 때 보일 버튼
  </>
) : (
  <>
    false일 때 보일 버튼
  </>
)}
```
5. 수정 시, 원본 콘텐츠가 있도록 하기
- 수정 폼을 관리할 state인 localContent의 기본값을 content로 함
```js
const [localContent, setLocalContent] = useState(content);
```
6. 수정 도중 취소 시, 도중에 수정하던 값을 초기화하기
- 초기화 함수 `handleQuitEdit()` 작성
```js
const handleQuitEdit = () => {
  setIsEdit(false); // 1. 수정 취소할 거니까 false로 바꿔준다
  setLocalContent(content); // 2.localContent의 값을 다시 content로 바꿔준다
}
```
6. 수정 완료 클릭 후, 수정본이 최종적으로 반영되게 하기
- '데이터는 위에서 아래로, 이벤트는 아래에서 위로'
- App 컴포넌트까지 전달하기 위해서, 데이터를 가지고 있는 App의 수정하는 기능의 함수를 만들어서 DiaryItem 컴포넌트까지 보내줘야 한다.
- 1. `onEdit()` 함수 작성
  - setData를 통해 어떤 값을 전달
  - onEdit은 특정 일기 데이터를 수정하는 함수니까 targetId를 갖는 일기를 수정하기 위하여 그 매개변수를 이용해 원본 데이터 배열 data에 map 내장함수 이용
  - 모든 요소를 순회하면서 새로운 배열을 만들어서 setData에 전달
  - 타겟 일기인 객체라면 객체의 content를 newContent로 바꾸고, 아니라면 it 그대로 유지
```js
// App.js

// 매개변수로 무엇을 어떻게 수정할지 받아와야 함
const onEdit = (targetId, newContent) => {
  setData(
    data.map((it) => it.id === targetId ? {...it, content:newContent} : it)
  )
}
```
- 2. DiaryItem에서 onEdit을 호출하니까 그 부모인 DiaryList에 onEdit 함수를 전달
  - App -> DiaryList -> DiaryItem 모두 화살표 함수의 input에 onEdit을 넣고, 자식 컴포넌트 태그에는 `onEdit={onEdit}`을 넣는다.
```js
<DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
```
- 3. 수정 완료 이벤트를 처리할 함수 `handleEdit()`
  - 컴포넌트는 위에서 내려온 것을 prop으로 받고, 해당 함수를 쓸 js 파일에서 onEdit을 호출하도록 `handleEdit()` 함수 작성
```js
// 1. 검사에 통과하지 않으면 줄 포커스 효과를 위해 레퍼런스 객체
const localContentInput = useRef();

// 2. 효과를 줄 위치에 localContentInput을 맵핑
<textarea
  ref={localContentInput}
/>

...

const handleEdit = () => {
  // 검사. 다섯 글자 이상이어야 함.
  if (localContent.length < 5) {
    localContentInput.current.focus();
    return;
  }

  if (window.confirm(`${id}번째 일기를 수정하시겠습니까?)) {
    onEdit(id, localContent)
    toggleIsEdit() // 수정 폼 닫기
  }
} ;
```