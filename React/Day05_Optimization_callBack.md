## 최적화3 - callBack
- 컴포넌트를 최적화하기 위하여 어떤 컴포넌트가 최적화의 대상인지 찾을 수 있어야 한다.
  - React developer tools를 통해 
- 컴포넌트는 언제 렌더링?
  - 본인이 가진 state에 변화, 부모 컴포넌트가 리렌더링, 자신이 받은 prop이 변경될 때


  - 컴포넌트가 굉장히 많아지면 매 컴포넌트마다 콘솔과 useEffect를 사용하는 것은 비효율적이다. highlight render로 쉽게 확인 가능하다.

### DiaryEditor 최적화하기 실습
App 컴포넌트는 마운트되자마자 2번 렌더링된다. 그래서 DiaryEditor 컴포넌트가 전달받는 OnCreate 함수도 렌더링될때마다 계속 다시 생성됨