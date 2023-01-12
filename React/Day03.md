### React Developer tools
- [>> 에서 Components 탭]
  - 계층 구조를 해석해서 보여줌
  - 어떤 state, Ref, Effect를 가지고 있는지
  - props들, 함수
  - 리스트로 렌더링한 key값까지
- [View settings]
  - 컴포넌트 렌더링 될 때마다 highlight 기능

## 최적화1 - 연산 결과 재사용 useMemo
리액트 어플리케이션 성능 최적화를 목적으로 한다.

### Memoization
이미 계산 한 연산 결과를 기억해두었다가 동일한 계산을 시키면, 다시 연산하지 않고 기억해두었던 데이터를 반환 시키게 하는 방법

### React 실습에 Memoization 적용하기
- emotion마다 개수를 분석하는 함수 `getDiaryAnalysis()`
1. 개수 세기) data 배열의 `filter()` 함수 사용
```js
const getDiaryAnaylsis = () => {
  // it) 배열의 각 요소
  const goodCount = data.filter((it) => it.emotion >= 3).length;
  
  // 위 함수로 구한 값들을 객체 형태로 return
  return {goodCount, badCount, goodRatio}
}
```
2. App 컴포넌트 return하기 전 호출
```js
// 위에 함수 호출 결과값 객체로 반환하니까 여기서도 객체로 비구조적 할당
const { goodCount, badCount, goodRatio } = getDiaryAnalysis;
```
3. DiaryList, DiaryEditor 사이에 렌더링
```html
<div>기분 좋은 일기 개수 : {goodCount}</div>
```

- 짚고 넘어갈 것
  - 함수형 컴포넌트를 만들었다고 해서 js의 함수가 아닌 건 아니다. App 컴포넌트가 리턴하는 jsx 문법의 html DOM 요소들은 화면에 반영이 될 뿐, js의 함수가 호출되고 반환하는 것은 같다.
  - 즉, 리렌더링 -> App 함수가 한 번 더 실행된다.

#### ❓ Memoization을 활용하는 현재 문제 상황
- 리렌더링될 때, 존재하는 특정 함수가 이미 계산된 값을 그대로 쓰면 됨에도 불구하고 함수가 호출이 되어 필요 없는 연산을 반복한다.
  - ex. 일기 컨텐츠를 수정할 때, 감정 점수는 수정할 수 없어 getDiaryAnaylsis 함수 실행 결과가 같을 텐데 컨텐츠 수정으로 인한 리렌더링으로 함수가 또 호출되고 있는 상황

#### 4. `useMemo()` 함수 사용
- 기존 getDiaryAnalysis 함수를 useMemo안에 넣어 콜백 함수 꼴로 만듦
  - [data.length]를 콜백 함수 뒤에다 추가하여 값이 변화할 때마다 콜백함수가 다시 실행되어 getAnalysis가 아무리 호출하여도 data의 길이가 변하지 않는 이상, 연산을 하지 않고 똑같은 return을 반환한다.
- TypeError: getDA is not a function 에러
  - 값을 리턴받으므로 값으로 사용
```js
const getDiaryAnalysis = useMemo(() => {
    if (data.length === 0) {
      return { goodcount: 0, badCount: 0, goodRatio: 0 };
    }
    console.log("일기 분석 시작");

    const goodCount = data.filter((it) => it.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100.0;
    return { goodCount, badCount, goodRatio };
  }, [data.length]);

// 리턴 값을 함수 호출이 아니라 변수로 받으므로 다음과 같이 변경
const { goodCount, badCount, goodRatio } = getDiaryAnalysis;
```
