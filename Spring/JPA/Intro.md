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
  - 스프링 컨테이너가 JPA에 있는 영속성 컨텍스트라고 불리는 것인데, em를 가져다 줌 → 얘를 통해서 엔티티를 집어넣으면 JPA가 알아서 DB에 INSERT 쿼리를 날려서 저장(persist)하고, 해당 엔티티에 맞는 SELECT 쿼리를 날려서 DB에서 가져옴(find)

### Create Test

`Ctrl + Shift + T`

- Testing library : JUnit5 -> 2.2 이후부터는 이것으로 사용
- `@SpringBootTest` : 테스트도 스프링 빈을 주입 받아서 쓸 것이므로 스프링 컨테이너가 필요하기 때문에 사용

- JPA의 모든 데이터 변경은 트랜잭션 안에서 이뤄저야 하므로 `@Transactional`
  - JPA 특성 상 같은 트랜잭션 안에서의 영속성 컨텍스트의 동일성(같은 인스턴스임을)을 보장함 == 1차 캐시
- 트랜잭션 끝날 때 바로 rollback을 시켜서 DB에도 값이 없고 + JPA의 영속성 컨텍스트에도 플러시 안 함. 즉, DB에 아무 쿼리를 안 날림!
  - 콘솔에도 없어도 학습용으로 @Rollback(false) 처리 해주기 → 롤백 안 하고 커밋

#### 엔티티 설계 시 유의할 점

- 롬복
  - `@NoArgsConstructor AccessLevel.PROTECTED` : 기본 생성자 막고, JPA 스팩상 PROTECTED로 열어두기
  - `@ToString`의 of 안에는 연관관계 없는 필드만 작성
    - ex. 연관관계가 있는 Member <-> Team의 경우 서로가 연결되어 있어서 무한로딩 발생 가능성 O
- 연관관계 편의 메소드
  - `changeTeam()`으로 양방향 연관관계 한번에 처리

### 공통 JpaRepository 인터페이스

- 순수 JPA 기반 리포지토리
  - JPA를 통해 CRUD 작업을 리포지토리에다가 만듦
  - 엔티티 변경(update)의 경우, 변경 감지 이용
    - 트랜잭션 안에서 엔티티를 조회하고 데이터를 변경한다면 트랜잭션 종료 시점에 변경감지 기능이 작동되어 UPDATE SQL문을 실행함
    - 자바 컬렉션과 동일한 방식으로 업데이트

#### 공통 인터페이스

```java
public interface MemberRepository extends JpaRepository<Member, Long> {
} // <엔티티 타입, 식별자 타입>
```

- 스프링 데이터 JPA가 구현 클래스 대신 생성
- 구현체가 없는데 어떻게 동작할까?
  - proxy로 인해 스프링이 인터페이스를 injection해줌
- #### 주요 메서드
  - `save(S)` : 새로운 엔티티는 저장하고 이미 있는 엔티티는 병합한다.
  - `delete(T)` : 엔티티 하나를 삭제한다. 내부에서 EntityManager.remove() 호출
  - `findById(ID)` : 엔티티 하나를 조회한다. 내부에서 EntityManager.find() 호출
  - `getOne(ID)` : 엔티티를 프록시로 조회한다. 내부에서 EntityManager.getReference() 호출
  - `findAll(…)` : 모든 엔티티를 조회한다. 정렬(Sort) or 페이징(Pageable) 조건을 파라미터로 제공할 수 있다.

## 쿼리 메소드 기능

- 메소드 이름으로 쿼리 생성하는 방법
- NamedQuery
- @Query
- 파라미터 바인딩
- 반환 타입
- 페이징과 정렬
- 벌크성 수정 쿼리
- @EntityGraph

#### 쿼리 메소드 기능 3가지

1. 메소드 이름으로 쿼리 생성
2. 메소드 이름으로 JPA NamedQuery 호출
3. `@Query` 어노테이션을 사용해서 리파지토리 인터페이스에 쿼리 직접 정의

### 1️⃣ 메소드 이름으로 쿼리 생성

#### 필터 조건

- 스프링 데이터 JPA 공식 문서 참고: (https://docs.spring.io/spring-data/jpa/docs/current/
  reference/html/#jpa.query-methods.query-creation)

- 도메인에 특화된 조회 기능에 유용함
- 필드명과 인터페이스의 메서드 이름의 불일치 등 오류를 애플리케이션 로딩 시점에 미리 오류를 발견할 수 있음

### 2️⃣ JPA NamedQuery

- 실무에서 거의 쓸 일이 없음
- 쿼리에 이름을 부여하고 호출하는 기능
- Entity에 `@NamedQuery` 어노테이션 부착하고 name, query를 작성
- 작성한 NamedQuery를 불러오기 위한 편리한 방법 -> JpaRepository를 extends하는 MemberRepository에서 `@Query` 어노테이션을 붙여서도 사용 가능
  - ```java
      @Query(name = "Member.findByUsername")
    List<Member> findByUsername(@Param("username") String username);
    ```
- 장점
  - 애플리케이션 실행 시 문법적인 오류를 알려줌

### 3️⃣ `@Query`로 리파지토리에 쿼리 직접 정의

- 장점
  - 파라미터 길어지면 불편해지는 첫번째 방법에 비해 간결하게 이름을 지을 수 있음
  - 복잡한 쿼리를 직접 JPQL을 넣어서 해결 가능
  - property 오타를 애플리케이션 로딩 시점에 알려줘서 오류를 발생시킴
    - 정의한 쿼리로 일단 다 파싱을 해놓고 sql을 만들어놓아서 문법 오류 발견 가능
- 동적 쿼리는?
  - QueryDSL을 써야 함

### @Query로 값/DTO 조회하기

#### DTO로 조회하기

- id, username, team 등의 여러 데이터를 한 번에 가지고 오고 싶을 때 사용

- 단건일 때 없으면 null, 리스트는 null이 아니라 empty인 리스트를 반환
- 데이터가 있을지 없을지 모를 땐 Optional<> 사용
