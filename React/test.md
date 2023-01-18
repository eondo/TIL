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
    - app.js는 기본적으로 app 컴포넌트를 내보내고 부가적으로 이를 내보내고 있다고 이해
- Context Provider를 통한 데이터 공급
```js
// 컴포넌트의 자식으로 컴포넌트를 전달. children props
// value라는 props로 받아서 이 값들을 자식 컴포넌트들에게 전달 가능
<MyContext.Provider value={전역으로 전달하고자 하는 값}>
  {이 Context안에 위치할 자식 컴포넌트들}
</MyContext.Provider>
```
