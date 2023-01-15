## 최적화2 - 컴포넌트 재사용

부모 컴포넌트 렌더링될 때 prop 중 특정 자식이 받은 prop은 업데이트 될 필요가 없는데도 부모 컴포넌트가 렌더링됨으로써 불필요한 연산이 다시 일어나는 상황이 있다.
-> 해결 : 업데이트 조건을 본인이 받은 prop이 변경될 때만 렌더링되도록 한다.
- 함수형 컴포넌트에 업데이트 조건을 걸자! -> `React.memo`

공식 문서 참고하기 https://ko.reactjs.org/docs/getting-started.html
[API 참고서]
- 고차 컴포넌트
  - 컴포넌트 로직을 재사용하기 위한 React의 고급 기술. 컴포넌트를 가져와 새 컴포넌트를 반환하는 함수.

### React.memo
- 매개변수로 컴포넌트를 전달
- 똑같은 props로 동일한 결과를 렌더링한다면 컴포넌트를 다시 계산하지 않음
- React.memo(리렌더링 하지 않았으면 하는 컴포넌트)
```js
const MyComponent = React.memo(function MyComponent(props) {
  // props를 사용하여 렌더링
})
```