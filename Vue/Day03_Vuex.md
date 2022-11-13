## Vuex
Web Application의 상태 == 현재 App이 가지고 있는 Data로 표현

#### ◼ 상태 관리
- 여러 각각의 component가 같은 상태를 유지할 필요가 있음!
- 기존) props, emit으로 상태 관리를 해옴 → 같은 데이터를 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지하고 있음 → BUT 중첩이 깊어지면 데이터 전달 구조가 깊어짐
- 해결) `Centralized Store` 이용
- Centralized Store(중앙 저장소) : componenet는 중앙 저장소의 데이터를 사용하며 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경이 가능함!
  - 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영
  - 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 편리함

#### ◼ Vuex
중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 규칙을 설정, vue의 반응성을 효율적으로 사용하는 상태 관리 기능 제공
- Vue와 Vuex 인스턴스 비교
  - data → state
  - computed → getters : state에 있는 데이터를 기반으로 새롭게 저장된 값
  - methods → mutations, actions

#### ◼ Vuex의 핵심 컨셉 4가지
### 1. State
- 중앙에서 관리하는 모든 상태 정보
- `$store.state`로 state 데이터에 접근

### 2. Mutations
- 실제로 state를 변경하는 유일한 방법
- 데이터를 변경하는 메서드 모음집으로, Mutations에서 호출되는 핸들러 함수는 반드시 동기적이이야 함
  - if 비동기라면? state의 변화의 시기를 특정하기 어려울 수 있음
- 인자 : `state`, component 혹은 actions에서 `commit()` 메서드로 호출됨

### 3. Actions
- mutations과 비슷 + `비동기` 작업을 포함할 수 있음
- state를 직접 변경하지 않고, commit()메서드로 mutations를 호출해서 state를 변경함
- 인자 : context 객체, 이를 통해 모든 데이터에 접근 가능한 권한을 가짐
- component에서 `dispatch()` 메서드에 의해 호출됨

### 4. Getters
- state를 활용하여 계산된 값을 얻고자 할 때 사용
- 종속된 값이 변경된 경우에만 재계산
- getters에서 계산된 값은 state에 영향을 미치지 않음
- 인자: (`state`, `getter`)

#### 동작 cycle
상태가 component에 렌더링되고, component가 어떤 메서드를 호출 dispatch라면 그 액션이 호출되고, 최종적으로 state 변경하려면 액션 후에 muatation을 호출하여 최종적으로 state 변경하고 다시 렌더링... 반복
- 액션이 누구와 소통? Backend API, 외부 API... 이 코드들이 actions 안에 들어가서 쓰임
- 모든 데이터를 vuex에서 관리할 필요는 없다! 여전히 pass props, emit event 사용 가능, 적절하게 사용 필요
- 흐름 예시)
  - component에서 데이터 조작 시
    - `component -> (actions) -> mutations -> state`
    - 바로 mutations로 데이터 변경만 할 시 actions는 생략 가능
  - component가 중앙의 데이터 사용할 시
    - state -> (getters) -> component

## Vuex 실습
- actions에 원래대로면 axios 들어가고 여러가지 잡다한 코드 들어갈 것... actions가 하는 일. BUT 현재 실습처럼 actions가 별다른 일 없는 경우엔 actions 생략 가능함

#### ▪ state
1. store의 state에 message 데이터 정의
```js
state: {
    message: 'message in store',
  },
```
2. App.vue 컴포넌트에서 computed로 정의 후 해당 state 사용
```js
computed: {
  message() {
    return this.$store.state.message;
  },
```

#### ▪ actions
- `dispatch(A, B)`
- A : 호출하고자 하는 actions 함수, B : 넘겨주는 데이터(pay load)
- [참고] 액션은 다른 액션을 호출할 수도 있다!

1. actions에 함수 정의
```js
changeMessage(context, newMessage) {
  context.commit('CHANGE_MESSAGE', newMessage) // ('mutation 메서드 이름', 추가데이터)
```
2. 컴포넌트의 methods 객체를 통해 actions에 정의된 changeMessage 함수에 데이터 전달하기
- 함수 실행할 input 만들기
```html
<input type="text" @keyup.enter="changeMessage" v-model="inputData" />
```
- methods 안에 dispatch로 actions 호출
```js
methods: {
    changeMessage() {
      const newMessage = this.inputData; // 일단 저장하고
      this.$store.dispatch("changeMessage", newMessage); // ('액션 메서드 이름', 추가데이터)
      this.inputData = null
    },
```
3. store/index.js의 actions란에서 commit으로 mutations 호출
```js
actions: {
    changeMessage(context, newMessage) {
      context.commit('CHANGE_MESSAGE', newMessage) // ('mutation 메서드 이름', 추가데이터)
    }
```

#### ▪ mutations
1. mutations 함수 작성하기
- 첫 번째 인자 : state, 두 번째 인자 : payload
```js
mutations: {
    CHANGE_MESSAGE(state, newMessage) {
      state.message = newMessage
    }
```

#### ▪ getters


## Lifecyle Hooks
단계별로 초기화 단계 존재하는데, 이 중간마다 hook이 존재 → 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음

## 📌 Todo with Vuex
- 구현 기능
  - Todo CRUD
  - todo별 개수 반영 및 local storage 이용

### Intro
- 들어갈 component 만들고 상위-하위 연결 완료
- TodoListItem에서 props로 todo 객체 받아서 {{ todo.title }} 출력해서 READ 확인해보기

### CREATE
- Todo가 새로 만들어지는 곳은 TodoForm
- 새로운 todo를 입력할 폼 input 태그 작성
    - 어떤 이벤트가 발생하면 어떤 함수를 실행시킬지 작성
    - 해당 텍스트를 콘솔에서 확인할 수 있고 주고 받을 수 있도록 v-model에 새로운 값이라는 변수 만들어서 작성
- 특정 이벤트로 인해 실행되는 함수를 methods 속성에 작성
    - store의 actions로 보내줄 것이기 때문에 `dispatch()` 사용
    - 이 `createTodo()` 함수는 여기서 만들어지는 이 것(`this`)을 상점(`$store`)으로 보낼 건데, 그 상점에서 `"createTodo"` 라는 코너로 가자. `this.newTodoInput` 을 들고.
    - input은 null로 초기화하기
- actions에 createTodo() 함수 받으면 뭘 해줘야 할지 작성
    - 단순히 받은 newTodoInput(문자열 타입)을 받아서 바로 commit으로 보내주면 문제 발생 ← why❓ TodoListItem에서는 List에서 Object 타입으로 props를 받는데, 현재는 지금 String 타입으로 받아서 mutations를 통해 문자열을 todos에 push해주고 있으니까!
    
    ```python
    [Vue warn]: Invalid prop: type check failed for prop "todo". Expected Object, got String with value "안녕".
    ```
    
    - actions에서는 실제로 todos에 저장될 형식을 맞춰주고 mutations로 보내줘야 함
    - createTodo() 코너로 오면 모든 정보를 담은 `context` 에다 newTodoInput을 넣어준다는 의미로 context를 첫번째 인자로 가져오고, 작업을 끝내면 newTodoInput을 담은 context를 통해 mutations로 `CREATE_TODO`  확정하러 가기 위해 `commit('CREATE_TODO', newTodo)` 호출
- mutations에서 마무리 작업
    - 현재 state의 todos 배열에 접근해서 받아온 인자로 받아온 newTodo를 push
    - 즉, 최종적으로 state를 변경함

### DELETE
- TodoListItem에서 todo마다 필요한 삭제 버튼 생성해서 deleteTodo 메서드가 실행되도록 함
- methods에 deleteTodo() 작성
    - dispatch로 actions로 보내줄 건데, 상점의 ‘deleteTodo’ 코너로, 현재 삭제할 todo인 `this.todo` 를 함께 보내줌
- actions와 mutations
    - actions에서 deleteTodo()로 올 때, context 봉투에 넘겨준 this.todo를 `todoItem` 으로 인자를 받고, 따로 더 데이터에 처리를 해줄 게 없으므로 바로 mutations로 commit을 통해 mutations의 DELETE_TODO 호출
    - mutations에서 state.todos에 접근해 특정 인덱스의 값을 `splice`

### UPDATE STATUS
- TodoListItem
    - 개별 todo를 클릭하면 해당 todo의 상태를 변경하겠다는 의미로 태그에 클릭 이벤트 추가 및 methods 작성 (actions 메서드 호출)
- actions와 mutations
    - actions에서는 단순히 UPDATE_TODO_STATUS 메서드 호출
    - mutations에서는 현재 state.todos 중 클릭한 todo의 isCompleted 값을 바꾼 것으로 새롭게 갈아끼워야 하므로 여기서 처리
    - map 함수를 이용하여 todo와 인자로 들어온 todoItem을 비교하여 같은 경우 해당 isCompleted 값을 반대로 바꿔주는 작업을 거친 후 반환되는 새로운 배열을 state.todos에 저장
- isCompleted가 새롭게 반영된 todos에 따라서 각 TodoListItem의 아이템들이 취소선이 토글되도록 <style>태그에 `.is_completed` 작성 후 <span> 태그에 vind로 묶어주기 → `:class="{ 'is-completed': todo.isCompleted }"`

### 상태별 todo 개수 계산
- App.vue의 computed와 Store의 getters 이용
- 미완료된 todo 개수
    - 전체 개수 - 완료된 개수
    - 즉, 이미 getters에 들어있는 변수를 활용해야 하므로, 두번째 인자로 getters를 받는 `unCompletedTodosCount(state, getters)` 형식으로 getters에 작성


### Local Storage
새로고침하면 사라지는 문제를 해결하려면 어딘가에 저장해야 한다. 현재는 브라우저 환경이고 백엔드도 없는데, 브라우저에 저장할 수 있을까
#### Window.localStorage
브라우저에서 제공하는 저장공간 중 하나로 데이터베이스를 내부적으로 가지고 있다!
- Local storgate에 todo 데이터를 저장하여 브라우저를 종료하고 다시 실행해도 데이터가 보존될 수 있도록 하기
- window가 local storage 속성값을 통해 .메서드() 이용
- 데이터가 문자열 형태로 저장됨
- 관련 메서드
  - `setItem(key, value)` : key, value 형태로 데이터 저장
  - `getItem(key)` : key에 해당하는 데이터 조회
  - localstorage에서 key를 가져오면 됨
- 사용
  - 데이터 → 문자열 형태로 변환 : `JSON.stringify(context.state.todos)`
  - 문자열 데이터 → object 타입으로 변환 : `JSON.parse(localStorageTodos)`
#### vuex-persistedstate
- Vuex state를 자동으롤 브라우저의 Local Storage에 저장해주는 라이브러리 중 하나
- 적용
  ```js
  import createPersistedState from 'vuex-persistedstate'
  ...
  plugins: [
    createPersistedState(),
  ]
  ```

