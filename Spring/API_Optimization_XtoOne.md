- 컬렉션 조회 최적화
  - 테이블 관점에서 조인을 했는데 일대다 조인이 되면 데이터가 엄청나게 증가 -> 컬렉션 조회 최적화 필요
- 페이징과 한계 돌파
  - 페이징 쿼리를 작성해서 날리면 페이징 쿼리라는 것은 일이랑 다가 있으면 조인을 하면 제대로 페이징하기 어려움 (데이터가 증가되어버리니까)
- OSIV와 성능 최적화
  - 사용하면 지연 로딩이 편하게 됨, lazing loading exception이 일어나는 것을 방지함.
  - 어느 상황에 켜야 하는지에 대한 학습

### 질문

- private final EntityManager em; 에서 final
- public class InitDb 안에 static class InitService가 들어가있는데 클래스 안에 클래스 선언
- save()랑 persist()랑 다른 점은?
  - persist()는 리턴값이 없는 insert
  - merge()는 리턴값이 없는 update
  - save()는 리턴값이 있는 insert, update

### 내용

initDb
@Component -> spring이 컴포넌트 스캔 대상이 됨
@Transactional
@RequiredArgsConstructor

### 엔티티를 DTO로 변환

- List로 내보내면 안 되고, Result로 한 번 감싸야 함
- ## API 스펙을 명확하게 규정해야 함
- DTO가 엔티티를 파라미터로 받는 건 가능

```java
@GetMapping("/api/v2/simple-orders")
public List<SimpleOrderDto> ordersV2() {
  List<Order> orders = orderRepository.findAllByString(new OrderSearch());
  List<SimpleOrderDto> result = orders.stream()
          .map(o -> new SimpleOrderDto(o)) // 오더 리스트 map으로 A를 B로 바꾸는 작업
          .collect(Collectors.toList()); // 생성된 Dto를 쭉 리스트로 받음
  return result;
}

@Data
static class SimpleOrderDto { // 이건
  private Long orderId;
  private String name;
  private LocalDateTime orderDate;
  private OrderStatus orderStatus;
  private Address address;

  public SimpleOrderDto(Order order) { // 생성자에서 바로 완성시키게 해놓음
    orderId = order.getId(); // o로 들어오는 정보에 대해서 id 가져와서 넣어주기
    name = order.getMember().getName();
    orderDate = order.getOrderDate();
    orderStatus = order.getStatus();
    address = order.getDelivery().getAddress();
  }
}
```

- `collect()`
- collect 메소드는 Stream 인터페이스의 최종 연산으로 스트림의 요소들을 수집하여 반환
- 매개변수로 컬렉터 필요
- `Collectors.toList()` -> 스트림을 컬렉션이나 배열로 반환하는 방법으로 `toList()`, `toMap()`, `toCollections(람다식)`이 있다.
- 컬렉션 객체 설정
  - list나 배열을 객체로 집어 넣어야 할 때, 컬렉션 객체를 의존성 주입하면 된다. 이를 위한 컬렉션 매핑 및 관련 엘리먼트가 지원된다.
- address의 경우, value object
  - 엔티티가 아니고 value object라서 address라는 타입을 정했다고 생각
  - 값 타입 관련 내용
- 지연 로딩으로 인한 데이터베이스 쿼리가 너무 많이 호출되는 문제
  - order, member, delivery 테이블 세 개 다 건드려야 하는 상황
  - order.getMember().getName() 부분에서 **LAZY 초기화**가 발생
    - LAZY 초기화란? 영속성 컨텍스트가 멤버 ID를 가지고 영속성 컨텍스트에서 찾아보는데 없으면 DB 쿼리를 날림. 그래서 데이터를 끌고 옴.
- DB 쿼리 조회 메커니즘
  - 제일 먼저 ORDER 조회, MEMBER 조회, D조회... 쿼리 총 3번 나가는데 ORDER, MEMBER, D조회하면 끝나야 할 것 같음. MEMBER, D에도 ID값 하나만 넘긴다. 첫번째 주문서는 쿼리 3번으로 완성. 두번째 주문서는 또 M, D를 또 가져온다. -> JPA의 LAZY 로딩 메커니즘 이해하기
  - ORDER 조회 -> 이때 SQL 1Q번 -> 결과 주문(ROW)수가 2개
  - 루프가 돌 때, ORDER 개수만큼 루프를 도니까 엄청나게 많은 쿼리를 날리게 됨 -> N + 1의 문제 (현재의 경우 1 + N + N번)

### 페치 조인 최적화

쿼리가 많이 날려지는 성능 문제가 발생하는 상황에서의 성능 최적화 방법

- 한 번 쿼리로 order, member, delivery를 한 번에 조인해서 select절에 다 넣고 한 번에 데리고 오는 것
  - member, delivery에 걸려있는 LAZY를 무시하고 진짜 객체 값을 채워서 가져온다. -> 페치 조인
  - fetch == SQL X, JPA에만 있는 문법
  - 성능 최적화를 위해 실무에서 자주 사용하므로 페치 조인을 완전히 이해하는 것이 중요

```java
public List<Order> findAllWithMemberDelivery() {
  return em.createQuery(
    // JPA 짜기
    "select o from Order o" +
    "join fetch o.member m" + // order 가져올 때, member까지 객체 그래프를 쿼리 한 번에 가져오겠다!
    "join fetch o.delivery d", Order.class // 타입을 Order.class
  ).getResultList();
}
```

### JPA에서 DTO로 바로 조회

- 이전에는 엔티티로 조회해서 중간에 엔티티를 DTO로 변환하는 방식이 아니라 JPA에서 바로 DTO로 꺼내오는 방식으로 진행하면 조금 더 성능 최적화가 가능하다.

1. ordersV4 작성

```java
@GetMapping("/api/v4/simple-orders") {
  return orderRepository.findOrderDtos();
}
```

2. DTO 바로 조회를 위해 DTO 클래스 만들기

- 컨트롤러에 dto가 있는데 repository쪽에 해야 하는데, 의존관계가 r에서 c를 보는 이상한 사태가 발생할 수 있기 때문에 repository 패키지에 따로 클래스 작성
- orderRepository에 controller가 import가 생기면 안됨

```java
// repository/OrderSimpleQueryDto
@Data
public class OrderSimpleQueryDto {
  private Long orderId;
  private String name;
  private LocalDateTime orderDate;
  private OrderStatus orderStatus;
  private Address address;

  public OrderSimpleQueryDto(Order order) {
    orderId = order.getId();
    name = order.getMember().getName();
    orderDate = order.getOrderDate();
    orderStatus = order.getStatus();
    address = order.getDelivery().getAddress();
  }

}
```

3. OrderRepository에 `findOrderDtos()` 작성

```java
public List<SimpleOrderQueryDto> findOrderDtos() {

}
```

- select는 줄어들지만 재사용성이 떨어짐. sql 짜듯이 로직이 재활용이 불가능. DTO로 조회해서 엔티티가 아니어서 변경할 수가 없음. 코드 상 조금 더 길어진다는 단점이 있음.
- new 명령어로 JPQL의 결과를 DTO로 즉시 변환
- API 스펙에 맞춰서 Repository(엔티티의 객체그래프를 조회할 때 사용되는 개념)에 들어가버리는 느낌이라 API 스펙이 바뀜에따라 유동적으로 대처 불가능
- 해결 : 하위에 새로운 성능 최적화된 쿼리용을 따로 만들어둠
  - R는 순수한 엔티티를 조회할 때 사용
  - QueryRepository를 따로 파서 복잡한 조인 쿼리를 가지고 DTO를 뽑아내야 할 때 사용
-
