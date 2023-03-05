### DAO와 Repository의 차이점

- 공통점 : Data Access에 쓰인다.
- 차이점
  - DAO : Data Persistence의 추상화이며 데이터 저장소(DB 테이블) 중심이다.
  - Repository : 객체 Collection의 추상화이며, 객체 중심이다. (Domain 객체에 가까움)
    - DAO를 사용해 Repository를 구현할 수 있으며 그 반대는 불가능하다.
    - 객체 중심으로 데이터를 다루기 위해 하나 이상의 DAO를 사용할 수 있다.
    - 영구 저장소가 아니라 객체의 상태를 관리하는 저장소
