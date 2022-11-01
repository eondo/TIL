최소지연시간을 의미!
- 병렬성 vs 동시성
multi-thread /혼자 하지만 빨라서 동시에 처리하는 것처럼 보이는 것 → JavaScript는 single-thread로 동시성을 만족하면서 동작한다.

### JavaScript의 비동기 처리
JavaScript는 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 처리가 가능해짐

- 그럼 비동기 처리가 가능하긴 한데, 비동기로 보낸 작업 수행들의 순서를 정할 수 없음, 비동기 처리간의 선후 관계를 보장할 수 없음. 시간을 보장할 수 없음

- 실행된 순간 
1. call stack에 '전역'이 들어감 -> 2.foo() 호출되는 순간 'foo()' 쌓임 -> 3. call stack에 console.log() 쌓임 -> 출력되면 console.log()가 pop -> 5. foo()도 pop됨 -> 6. bar() 쌓임 -> 7. console.log() -> console.log()가 pop -> bar()도 pop -> 더 뭐 없으니까 '전역' pop
- 쌓이는 블럭 == 실행 컨텍스트

- setTimeout()가 실행된 순간, 괄호 안의 콜백 함수가 Web API에 들어감. 그리고 더이상 setTimeout()은 자바스크립트의 일이 아니라서 그 다음 line의 console.log()가 스택에 쌓임. 타이머 2초를 기다리지 않음. 

#### 브라우저 환경이 제공하는 것
chrome이 제공하는 요청은 두 가지. GET 방식, 그리고 form을 통한 것. 그럼 js에서는?

#### 비동기의 단점
get()함수가 같은 레벨이 있으면
Web API가 수행되는 동안 실행 컨텍스트도 실행돼서 응답이 오기 전에 실행 컨텍스트가 끝나버리기 때문에 어떤 응답을 받고 그것을 출력하려고 하면 undefined가 뜸.
즉, 비동기는 순서가 보장되지 않아서 순차적으로 원하는 기능의 순서가 제대로 이뤄지지 않을 수 있다. -> 순서 보장을 위해 콜백 함수 자체 안에다가 depth 하나 뒤로 respone받는다. -> 콜백 지옥

## Axios
Javascript의 HTTP 웹 통신을 위한 라이브러리
- 비동기 통신 기능을 제공
- 구조
```
axios.get('요청할 URL')
  .then(앞의 요청 성공하면 수행할 콜백함수)
  .catch(실패하면)
```
- 고양이
axios로 get방식으로 url 요청을 보냅니다. 저 url로. 그 응답이 성공하면 .then의 첫번째 콜백 함수의 인자로 들어옴. 응답 객체가. 그리고 걔를 출력 시도하는 것.
배열의 첫번째 인자로 들어가야 -> 객체가 나옴.
그 객체 데이터에서 url은 최종적으로 response.data[0].url로 접근 가능!
```js
axios.get(catImageSearchURL)
        .then((response) => {
          // console.log(response)
          imgElem = document.createElement('img')
          imgElem.setAttribute('src', response.data[0].url)
          document.body.appendChild(imgElem)
        })
        .catch((error) => { 
          console.log('실패했다옹')
        })
        console.log('야옹야옹')
```
여러번 처리를 했을 때, 먼저 로딩된 이미지부터 처리되어 온다.

- ❗ vue.js에서 결국 프엔이 json 데이터를 받으려면 django로 요청을 보낼 것이고, 그 요청을 axios를 통해서 보낸다! 즉, Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음.

## Callback & Promise
- 비동기 처리의 단점 : 코드 순서대로 callstack -> webAPI로 넘어가는 순서가 아니라 taskQueue로 들어온 순서가 우리가 응답을 받는 순서다!
- 즉, Web API로 들어오는 순서 X 작업이 완료되는 순서 O
- 실행 결과를 예상하면서 코드를 작성할 수 없다는 단점 -> 해결 : 콜백 함수 사용!

### 콜백 함수 : 비동기 작업을 순차적으로 실행할 수 있도록 함
콜백 함수 : 다른 함수의 인자로 전달되는 함수
- 비동기 콜백 : 시간이 걸리는 비동기 작업이 완료된 후, 실행할 작업을 명시하는데 사용
- EX. 이벤트 클릭 시 시점에 발생, 이 url로 요청이 들어오면! 콜백을 실행할 조건이 붙음
- 특정한 조건 혹은 행동에 의해 호출 -> 비동기 처리를 순차적으로 동작할 수 있게 함
- 문제 : 비동기적 처리가 하나가 아니라 연쇄적으로 쌓여있는 코드가 발생하면? → 콜백 지옥
- 콜백 지옥 : 연쇄적으로 발생하는 비동기 작업을 처리하다보니까 깊어짐

-> 해결 : 프로미스

- 보기엔 동긴데 왜 비동기라는 거? axios가 여러개 있으면 동시다발적으로 요청을 보낸다. axios 내부는 동기가 맞고, 강아지 고양이 사진 가져오는 이게 비동기라는 것. axios를 발동하는 건 동기 맞음! 

### 프로미스(Promise)
Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- 앞의 작업이 끝나면 실행 시켜줄게 -> 비동기의 순서를 보장!
- 비동기 작업의 완료 or 실패를 나타내는 객체
  - ex. Axios 라이브러리 : axios.get(CatImageSerachUrl).then(...) - 여기서 axios.get(...)이 promise 객체이다.

#### then & catch
#### then(callback)
- 요청한 작업이 성공하면 callback 실행
- callback은 이전 작업의 성공 결과(객체)를 인자로 전달 받음
#### catch(callback)
- then()이 하나라도 실패하면 callback 실행
- callback은 이전 작업의 실패 객체를 인자로 전달 받음 (왜 실패했는지에 대한 정보)

axios로 처리한 비동기 로직이 항상 promise 객체를 반환하기 때문에 계속 chaining할 수 있음 -> 즉, then을 계속 이어 나가면서 작성할 수 있음
-> 깊어지지 않고, 아래로 내려가고 순서를 보장함. 따라서, 2번 then은 1번 then이 성공해야 실행됨.
- catch를 마지막에만이 아니라, 중간중간에 섞어서 쓸 수도 있음 일반적으로는 마지막
- then chaining할 때 앞 then에서 return 중요!

#### Promise가 보장하는 것 (vs 비동기 콜백)

- 위의 get 경우, get 함수 함수 안에 인자로 넣어야 해서 관리하기 어려움 -> axios 객체를 호출해서 그 안에 넣어줄 것을 넣어서 추가데이터를 작성하기 편안하게 함
```js
axios({
  method: 'post', // 주의 : 객체 들어가는 이름은 정해져있음 (공식문서의 요청 형태 : config 참고)
  url: catImageSearchURL, // 우리 django의 서버 url이 될 것
  data : {
    title: '제목',
    content: '내용'
  }
}) // 이거의 결과가 promise 객체
  .then()
  .then()
  .catch()
```
요청을 보낼 땐, 응답 결과가 json으로 오는 거지, 쓸 때는 json으로 쓰지 않음. 이게 결국 drf에서 저번에 postman으로 요청을 보냈다면 이제 axios로 코드화해서 서버에 요청을 보내는 것.