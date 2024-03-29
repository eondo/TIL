# 리액트에서 Hooks를 사용하는 이유
### Hook의 개념
1. 기존의 함수 컴포넌트에서 할 수 없었던 작업을 class 기반의 코드 없이도 상태값과 여러 React의 기능을 사용할 수 있도록 한다.
2. React state와 생명주기 기능(lifecycle features)을 연동하는 기능 등을 제공한다.

### useState
```js
const [value, setValue] = useState(0)
```
- useState 함수가 호출되면 [상태 값, 상태를 설정하는 함수] 배열을 반환한다.
- `setValue(새로운 값)`을 통해 전달받은 새로운 값으로 바뀌고 컴포넌트가 리렌더링 된다.
- 관리해야 할 상태 개수만큼 useState를 여러 번 사용한다.

### useEffect
- 리액트 컴포넌트가 렌더링될 때마다 특정 작업을 수행하도록 설정할 수 있다.
- `useEffect.md` 참고

#### 1. 마운트 될 때만 실행
#### 2. 특정 값이 업데이트될 때만 실행
#### 3. 언마운트되기 전, 업데이트 되기 직전에만 실행 (뒷정리)

### useReducer
#### 1. 컴포넌트 로직 작성하기
- useState보다 더 다양한 컴포넌트 상황에 따라 다양한 상태를 다른 값으로 업데이트할 때 사용하는 Hook
- 리덕스 학습 시 추가적으로 공부한다.
- 리듀서
  - 현재 상태, 업데이트를 위해 필요한 정보를 담은 액션 값을 전달받아 새로운 상태를 반환하는 함수
  - 새로운 상태를 만들 때 반드시 불변성을 지켜야 함
- 장점
  - 컴포넌트 업데이트 로직을 컴포넌트 바깥으로 빼낼 수 있다.
```js
import React, { useReducer } from 'react';

// 리듀서 함수
function reducer(state, action) {
  ...
}

// 함수형 컴포넌트 Counter
const Counter = () => {
  const [state, dispatch] = userReducer(reducer, { value: 0}); // useReducer(리듀서 함수, 해당 리듀서의 기본값)
  // state : 현재 가리키고 있는 상태, dispatch : 액션을 발생시키는 함수
  // dispatch(action)으로 리듀서 함수가 호출됨

  return (
    <div>
      ...
  )
}
```
#### 2. 인풋 상태 관리하기
- useReducer로 인풋 여러 개인 경우, useState를 여러 번 사용할 필요 없이, 기존 클래스형 컴포넌트의 setState 방식과 유사하게 처리할 수 있다.

### useMemo
- `Optimization_useMemo.md` 참고

### useCallback
```js
useCallback = ( e => {
  // 생성하고 싶은 함수
}, [바뀌었을 때 함수를 새로 생성시킬 배열])
```
- 만들어놨던 함수를 재사용하는 방향으로 렌더링 기능을 최적화할 때 사용한다. 
- 즉, 컴포넌트의 렌더링이 자주 발생하거나 렌더링해야 할 컴포넌트가 많을 때 사용할 수 있다.

#### 예제
- 두 번째 파라미터 '배열'이 [] 빈 배열일 경우
  - 컴포넌트가 렌더링될 때 만들었던 함수를 계속해서 재사용한다.
- [함수 내부에서 의존해야 하는 기존 상태값(여러 개 가능)]인 경우
  - 기존의 값을 조회해서 생성하고 싶은 함수에 들어갈 함수 결과를 구해야 할 때는 꼭 해당 상태값을 넣어야 한다.

### useRef
- 함수형 컴포넌트에서 ref를 쉽게 사용할 수 있도록 한다.
- useRef를 통해 만든 객체 안의 current 값이 실제 엘리먼트를 가리킨다.
- 사용 목적
  - 리액트에서 DOM을 직접 선택해야 할 때
    - 특정 엘리먼트 크기, 스크롤바 위치 조회 또는 설정, 포커스 설정 등의 상황 모두 가능
- 예제
```js
const nameInput = useRef(); // 1. Ref 객체 만들기
// 2. 선택하고 싶은 DOM에 ref값으로 설정
// .3. .current값이 사용자가 원하는 DOM을 가리킴
```