# React LifeCycle 제어 - useEffect

### React 컴포넌트의 Lifecycle
![image](https://user-images.githubusercontent.com/109258497/211903235-7f0c2f9e-d344-45d7-9248-b54ebd3a95e3.png)
- 탄생
  - 화면에 나타나는 것
  - EX. 초기화 작업
  - `Mount`
- 변화
  - 컴포넌트의 업데이트(리렌더)
  - EX. 예외 처리 작업
  - `Update`
- 죽음
  - 화면에서 사라짐
  - EX. 메모리 정리 작업
  - `UnMount`

#### Lifecycle마다 실행할 수 있는 메서드
- 클래스형 컴포넌트에서 사용 가능한 메서드
  - `ComponentDidMount`
  - `ComponentDidUpdate`
  - `ComponentWillUnmount`

#### React Hooks?
클래스형 컴포넌트가 근본적으로 가지고 있는 기능을 함수형 컴포넌트에서도 훅킹해서 쓸 수 있는 기능들
- `useState`, `useEffect`, `useRef`
- 클래스형은 같은 기능을 제작하는데 길어지는 코드 길이 문제, 중복 코드, 가독성 문제가 존재하므로 함수형 컴포넌트를 사용

### useEffect
- 사용법
  ```js
  import React, { useEffect } from "react";
  ```
  - 두 개의 파라미터를 전달 1) Callback 함수, 2) Dependency Array(의존성 배열)
  - 배열 내에 들어있는 값이 변화하면 콜백 함수가 수행된다.
  ```js
  useEffect(() => {
    // todo... 콜백 함수
  }, [])
  ```
#### 1️⃣ 컴포넌트 마운트
- 의존성 배열을 [] 빈 배열로 사용
  ```js
  useEffect(() => {
    console.log("Mount");
  }, []);
  ```
#### 2️⃣ 컴포넌트가 업데이트된 순간 작업하고 싶은 게 있다면?
- state 변경, 부모에서 받는 props 변화, 부모 리렌더링 상황
- useEffect()을 의존성 배열 없이 사용
  ```js
  useEffect(() => {
    console.log("Update");
  });
  ```
#### 3️⃣ 컴포넌트의 특정 파트의 변경 감지를 하고 싶다면
- useEffect()을 감지할 state를 의존성 배열로 넣어 사용
  ```js
  useEffect(() => {
    console.log(`count is update : ${count}`);
    
  }, [count]);
  ```
#### 4️⃣ 컴포넌트가 화면에서 사라지는 순간(언마운트)
- ON/OFF
  - 단락회로 평가를 이용하여 inVisible 변수가 false, true에 따라 unMountTest 자식이 화면에 렌더링 or not 할 수 있다.
  - `{inVisible && <UnmountTest/>}`
- 콜백함수가 함수 하나를 return하게 하면 Unmount 시점에 실행된다.
  ```js
  useEffect(() => {
    console.log("Mount");
    
    return () => {
      // Unmount 시점에 실행되게 함
      console.log("Unmount");
    };
  }, []);
  ```