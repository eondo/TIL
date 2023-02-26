API 잘 설계하고 개발하는 것이 중요
단순히 SQL를 써서 API 끌어오는 것과 다르다. JPA를 쓴다면 Entity 개념이 있기 때문에 이 상태에서 API를 만드는 것은 다른 차원이다.
JPA 사용하면서 API를 만들 때 어떤 식으로 하는 것이 올바른 방향인지 배워야 한다.

- api 폴더를 따로 둠 -> 공통으로 예외처리 등을 할 때 패키티, 구성 단위로 공통처리하기 때문에, api와 화면은 다르기 때문에 따로 분리함
- @Controller + @ResponseBody -> @RestController
  - ResponseBody : 데이터 자체를 json, xml로 바로 보낼 때 주로 쓰는 annotation
