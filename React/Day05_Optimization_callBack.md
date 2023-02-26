## 최적화3 - callBack
- 컴포넌트를 최적화하기 위하여 어떤 컴포넌트가 최적화의 대상인지 찾을 수 있어야 한다.
  - React developer tools를 통해 
- 컴포넌트는 언제 렌더링?
  - 본인이 가진 state에 변화, 부모 컴포넌트가 리렌더링, 자신이 받은 prop이 변경될 때 
  - 컴포넌트가 굉장히 많아지면 매 컴포넌트마다 콘솔과 useEffect를 사용하는 것은 비효율적이다. highlight render로 쉽게 확인 가능하다.

### DiaryEditor 최적화하기 실습
### useCallback
App 컴포넌트는 마운트되자마자 2번 렌더링된다. 그래서 DiaryEditor 컴포넌트가 전달받는 OnCreate 함수도 렌더링될때마다 계속 다시 생성됨
즉, onCreate를 재생성되지 않게 해야 함. 
주의 -> `useMemo()`는 사용하면 안 된다.
- why? useMemo()는 결론적으로 함수가 아니라 값을 반환하는 것이므로 지금 원하는 건 onCreate 함수를 원본 그대로 DiaryEditor에 보내주는 것. onCreate가 어떤 값을 반환해선 안 된다.
- > Hook의 `useCallback`
  - 기능 : *메모이제이션*된 콜백을 반환한다. 두번째 인자로 전달하는 의존성 배열이 변하지 않으면 콜백 함수를 계속 재사용할 수 있도록 한다.
- 문제 발생 : onCreate 한 번 실행했을 때, 기존에 있던 onCreate로 만들어진 데이터가 사라지는 현상 발생
  - why?
    - 두번째 인자로 아무것도 안 넣어줘서
    - onCreate 함수는 컴포넌트 마운트되는 시점에만 한 번만 생성돼서 그 당시 데이터 state값이 빈 배열이라서 onCreate가 가장 마지막에 생성됐을 때 데이터 state가 빈 배열이라서.
    - 함수는 컴포넌트가 재생성될 때 다시 생성되는 이유 -> 현재 state값을 참조할 수 있어야 하기 때문.
    - `setData([newItem, ...data]);`에서 data가 빈 배열이다!
  - 해결
    - 의존성 배열에 data 넣어준다.
  - 2차 문제 : 의존성 배열에 data가 들어감으로써 data가 변할 때마다 onCreate 함수가 다시 생성되는 것을 막을 수 없음
  - 함수형 업데이트

### 함수형 업데이트
setData 상태변화 함수에 값을 전달하는 것 대신 함수를 전달.
```js
setData([newItem, ...data])
// 수정 후 (파라미터인 data는 최선 데이터로 들어가있음)
setData((data)=>[newItem, ...data])
```
- 의존성 배열을 []으로 하여도 최신의 state를 인자를 통해 참고할 수 있게 된다.


## 최적화4
- 문제 1. 아이템 하나를 삭제하면 해당 아이템 외의 것들도 다 리렌더링되는 문제
1. 컴포넌트를 React.memo()로 묶음
2. `useEffect`를 활용해서 어떤 아이템이 리렌더링되고 있는지 확인
3. memo로 묶어도 최적화되지 않는 prop으로 받아온 함수들을 최적화 -> `useCallback`
 


   
