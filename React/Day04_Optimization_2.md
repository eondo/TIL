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
- 똑같은 props로 동일한 결과를 렌더링한다면 컴포넌트를 다시 계산하지 않고 강화된 컴포넌트를 반환한다.
- React.memo(리렌더링 하지 않았으면 하는 컴포넌트)
```js
const MyComponent = React.memo(function MyComponent(props) {
  // props를 사용하여 렌더링
})
```
#### 예제
- 기존 자식 컴포넌트 TextView
```js
const TextView = ({ text }) => {
  useEffect(() => {
    console.log(`Update : Text : ${text}`);
  });
  return <div>{text}</div>;
};
```

- 컴포넌트를 재사용하기 위해 React.memo로 감싸줌
  - prop인 text가 바뀌지 않는 이상 렌더링이 일어나지 않음
```js
const TextView = React.memo(({ text }) => {
  useEffect(() => {
    console.log(`Update : Text : ${text}`);
  });
  return <div>{text}</div>;
});
```

### React.memo의 prop이 객체 형태라면
같은 값으로 할당하여 실제 state의 값은 변화가 없음에도 리렌더링되는 경우가 발생
- 이유
  - js는 기본적으로 객체 비교할 때 얕은 비교를 진행한다.
  - 객체, 함수, 배열 등의 자료형 비교할 때 값에 의한 비교가 아니라 객체의 '주소'에 의한 비교를 하기 때문이다.

1. 객체를 prop으롤 받는 컴포넌트 CounterB 선언
```js
const CounterB = ({ obj }) => {
  useEffect(() => {
    console.log(`CountB Update - count : ${obj.count}`);
  });
  return <div>{obj.count}</div>;
};
```

2. `areEqual` 함수 정의
- 객체의 주소값이 아니라 값 자체를 비교하도록 하기 위해 따로 함수를 정의하여 사용한다.
```js
const areEqual = (prevProps, nextProps) => {
  if (prevProps.obj.count === nextProps.obj.count) {
    return true;
  }
  return false;
};
```

3. 정의한 `areEqual`을 비교 함수로 쓰기 위해 강화된 컴포넌트 `MemoizedCounterB`를 만듦
```js
const MemoizedCounterB = React.memo(CounterB, areEqual);

...

const OptimizeTest = () => {
  ...
  return (
    ...
    <MemoizedCounterB obj={obj} />
  )
}
```