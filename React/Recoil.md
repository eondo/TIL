# Recoil
### Recoil이란?
> React를 위한 상태 관리(state management) 라이브러리
- props drilling과 같은 경우 global state 관리의 비효율을 state를 전역에서 다루기 위해 등장
- App 어딘가의 분리된 장소에 상태를 가진 recoil atom을 보관해두고 필요한 컴포넌트에서 직접 호출하는 방식
#### 설치
```
npm install recoil
```
### Recoil 사용하기
#### ▫ Usage
- App을 `RecoilRoot`로 감싼다.
- atom을 담을 파일을 생성한다.
  - key와 default로 atom을 저장한다.
  - atom이 필ㄹ요한 곳에서 값을 호출한다.
#### ▫ Set Atom Value
- `useSetRecoilState` : 호출한 atom의 default 값을 수정할 수 있음, 값의 수정만 필요할 때
- `useRecoilValue` : 값만 필요할 때
- `useRecoilState` : value와 변경 함수를 모두 사용 가능 (useState와 같이), 값과 값의 수정이 필요할 때

### Recoil 기초 실습
#### 🔹 RecoilRoot
- recoil 상태를 사용하는 컴포넌트는 부모 트리 어딘가에 나타나는 `RecoilRoot`가 필요하며 보통 루트 컴포넌트에 넣는다.
- `<CharacterCounter />`컴포넌트를 감싼다.
```js
import React from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

function App() {
  return (
    <RecoilRoot>
      <CharacterCounter />
    </RecoilRoot>
  );
}
```
#### 🔹 Atom
- Atom : 상태(state)의 일부를 나타냄
  - Atoms는 어떤 컴포넌트에서나 읽고 쓸 수 있다.
  - atom의 값을 읽는 컴포넌트들은 암묵적으로 atom을 구독한다.
  - atom에 어떤 변화가 있으면 그 atom을 구독하는 모든 컴포넌트들이 재렌더링된다.
- atom을 읽고 쓰기 위해 `useRecoilState()` 사용

```js
const textState = atom({
  key: 'textState', // 유니크한 ID
  default: '', // 디폴트, 초기값
});
```
```js
function CharacterCounter() {
  return (
    <div>
      <TextInput />
      <CharacterCount />
    </div>
  );
}

function TextInput() {
  const [text, setText] = useRecoilState(textState); // atom에 key로 적어둔 것, atom에 있는 textState를 text로서 사용함

  const onChange = (event) => {
    setText(event.target.value);
  };

  return (
    <div>
      <input type="text" value={text} onChange={onChange} />
      <br />
      Echo: {text}
    </div>
  );
}
```

#### 🔹 selector
- Selector : 파생된 상태(derived state)의 일부를 나타냄
  - 파생된 상태는 상태의 변화다.
  - 파생된 상태를 어떤 방법으로든 주어진 상태를 수정하는 순수 함수에 전달된 상태의 결과물로 생각할 수 있다.
```js
const charCountState = selector({
  key: 'charCountState', // 유니크한 ID
  get: ({get}) => {
    const text = get(textState);

    return text.length;
  },
});
```
- `useRecoilValue()` 훅을 사용하여 charCountState 값을 읽을 수 있음
```js
function CharacterCount() {
  const count = useRecoilValue(charCountState);

  return <>Character Count: {count}</>;
}
```

#### 결과
![image](https://user-images.githubusercontent.com/109258497/213928144-d8f7472f-9e08-4193-8176-bbce4cb7739c.png)

#### 🚫 궁금한 것
1. CharacterCount 함수 컴포넌트에서 이미 위에서 사용하는 중인 text를 그대로 쓰는 게 아니라, charCountState를 이용해서 한번 더 거쳐서 text의 length를 count에 담는 느낌인데 굳이 이러는 이유가 뭘까?
  - not yet 
2. selector의 역할이 정확히 어떤 것인가?
  - atom의 state를 가져다가 변형시켜서 return하고 싶을 때 사용할 수 있다.
  - 약간 Vue에서의 computed와 같은 느낌이라고 생각하면 될까?
