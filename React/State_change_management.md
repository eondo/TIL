useState에서의 setData의 역할을 dispatch, reducer가 담당한다고 생각

1. dispatch 작성
```js
// 기존 일기 데이터 가져와서 등록할 때
setData(initData);

// useReducer를 사용한다면?
// 액션의 타입이 INIT이고, 액션이 필요한 데이터를 담아서 보낸다.
dispatch({type:"INIT", data:initData}) 
```

2. reducer 함수에서 해당 타입일 때의 동작 작성
```js
const reducer = (state, action) => {
  switch (action.type) {
    case "INIT": {
      return action.data;
    }
```
- useReducer를 사용할 때, 상태 변화를 발생시키는 함수를 dispatch로를 이용. dispatch는 함수형 업데이트 필요 없이, 호출하면 알아서 현재 state를 reducer 함수가 참조해서 자동으로 하기 때문에 useCallback과 배열을 신경쓰지 않아도 됨!

## Context
> 컴포넌트 트리에 전역적으로 데이터 공급하기
- 공급자 컴포넌트로 모든 자손 컴포넌트에게 직통으로 모든 데이터에 공급, 접근할 수 있다. -> props 드릴링 문제 해결

### Context API
- Context 생성
```js
const MyContext = React.createContext(defaultValue);
// 생성 후 export해야 다른 컴포넌트들이 Context에 접근할 수 있다.
```
  - export vs export default의 비교
    - app.js는 기본적으로 app 컴포넌트를 내보내고 부가적으로 DiaryStateContent를 내보내고 있다고 이해하자 -> ES 모듈 시스템 참고하여 더 공부 가능
#### DiaryStateContext의 공급 만들기
- Context Provider를 통한 데이터 공급
```js
// 컴포넌트의 자식으로 컴포넌트를 전달. children props
// value라는 props로 받아서 이 값들을 자식 컴포넌트들에게 전달 가능
<MyContext.Provider value={전역으로 전달하고자 하는 값}>
  {이 Context안에 위치할 자식 컴포넌트들}
</MyContext.Provider>
```

#### 자식 컴포넌트에서 공급받은 데이터 사용하기
- `useContext` : Context에서 값을 꺼내오는 Hook
- useContext 인자에 값을 꺼내고 싶은 Context 지정 
```js
import { DiaryStateContext } from "./App";


const DiaryList = ({ onEdit, onRemove }) => {

  const diaryList = useContext(DiaryStateContext)
  return (
    <div className="DiaryList">
      ...
  )
}
```

### 상태 변화 함수를 Context를 통해 전달하기
- DiaryStateContext가 내려주는 value props를 Provider 컴포넌트에 전달하는 value에 diaryList 데이터처럼 value에 단순히 다 담아서 전달하면 안 됨
- why? Proivder도 결국 컴포넌트이기 때문. 즉, prop이 바뀌면 재생성됨 -> 밑에 있는 컴포넌트도 강제로 재생성된다
- 따라서, 내려주는 value에 onCreate, onEdit, onRemove를 data랑 같이 내려주게되면 data state가 바뀔 때마다 리렌더링되어 최적화가 다 풀림
- 해결 : Context를 중첩으로 사용 (diarystate와 dispatch 함수를 따로) 이중으로 묶기

```js
// Context 생성
export const DiaryDispatchContext = React.createContext()
```
```js
// Provider를 배치
<DiaryDispatchContext.Provider>
</DiaryDispatchContext.Provider>
```
1. 전달한 dispatch 함수들을 하나로 묶기
- memoizedDispatches가 절대 재생성될 일 없도록 useMemo와 함께 빈 배열 이용
  - 그냥 `const dispathes = {onCreate, onRemove, onEdit}`으로 하면 App 컴포넌트가 재생성이 될 때 이 객체도 재생성될 수밖에 없으므로
```js
const memoizedDispatches = useMemo(() => {
  return {onCreate, onRemove, onEdit}
}, [])
```
2. memoizedDispatches를 Provider의 value로 전달
```js
<DiaryDispatchContext.Provider value={memoizedDispatches}>
</DiaryDispatchContext.Provider>
```