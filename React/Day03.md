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

