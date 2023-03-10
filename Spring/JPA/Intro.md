# 스프링 데이터 JPA

- 스프링 프레임워크와 JPA 기반 위에 JPA를 편리하게 사용하도록 도와주는 기술
- 리포지토리의 구현 클래스 없이 인터페이스만으로 개발 완료 가능
- 기본적인 CRUD 기능 제공 → 핵심 비즈니스 로직을 구현하는데 집중 가능

### 설정 파일 세팅

#### JPA 설정

- `ddl-auto: create`
  - 애플리케이션 로딩 시점에 테이블을 다 drop하고 다시 깨끗한 상태로 create
  - 마지막에 애플리케이션 내려가도 테이블을 남겨놔서 DB에 접근해서 결과를 확인할 수 있음
  - local 개발 환경(공부 시)에서만 사용하고 운영에서는 사용 X
- `properties - show-sql: true`
  - JPA가 실행하는 쿼리를 콘솔에 다 찍음 → 대신 로그 파일로 남기기 위해 `org.hibernate.SQL: debug`(옵션은 logger를 통해 hibernate 실행 SQL을 남김)

#### 레포지토리

- `@PersistenceContext`
  - 스프링 컨테이너가 JPA에 있는 영속성 컨텍스트라고 불리는 것인데, em를 가져다 줌 -> 얘를 통해서 엔티티를 집어넣으면 JPA가 알아서 DB에 INSERT 쿼리를 날려서 저장(persist)하고, 해당 엔티티에 맞는 SELECT 쿼리를 날려서 DB에서 가져옴(find)

### Create Test

`Ctrl + Shift + T`

- Testing library : JUnit5 -> 2.2 이후부터는 이것으로 사용
- `@SpringBootTest` : 테스트도 스프링 빈을 주입 받아서 쓸 것이므로 스프링 컨테이너가 필요하기 때문에 사용

- JPA의 모든 데이터 변경은 트랜잭션 안에서 이뤄저야 하므로 `@Transactional`
  - JPA 특성 상 같은 트랜잭션 안에서의 영속성 컨텍스트의 동일성(같은 인스턴스임을)을 보장함 == 1차 캐시
- 트랜잭션 끝날 때 바로 rollback을 시켜서 DB에도 값이 없고 + JPA의 영속성 컨텍스트에도 플러시 안 함. 즉, DB에 아무 쿼리를 안 날림!
  - 콘솔에도 없어도 학습용으로 @Rollback(false) 처리 해주기 -> 롤백 안 하고 커밋
