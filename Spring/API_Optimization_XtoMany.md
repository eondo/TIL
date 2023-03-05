# 컬렉션 조회 최적화

- DB 입장에서 일대다 조회를 하면 데이터가 조인하면 조회되는 데이터가 많아진다. 즉, 최적화하기가 어려워진다. EX. Order 기준으로 OrderItem과 Item이 필요할 때. 주문한 내역과 주문한 item의 이름까지 뽑아오는 법을 예제로 알아보자.

- proxy 강제 초기화하기 되면 데이터가 있을 때 데이터를 뿌리게 된다.
- orderItems도 item도 DTO로 바꿔줘야 함

### 엔티티를 DTO로 변환하여 노출

```java
@GetMapping("/api/v2/orders")
public List<OrderDto> ordersV2() {
  List<Order> orders = orderRepository.findAllByString(new OrderSearch());
  List<OrderDto> result = orders.stream()
    .map(o -> new OrderDto(o))
    .collect(Collectors.toList());
  return result;
}

@Getter // 이게 없으면 no property 에러
static class OrderDto {
  // 생성자가 있어야 함
  private Long orderId;
  private String name;
  private LocalDateTime orderDate;
  private OrderStatus orderStatus;
  private Address address;
  // 추가된 것
  private List<OrderItem> orderItems;

  public OrderDto(Order order) {
    orderId = o.getId();
    name = oreder.getMember().getName();
    orderDate = order.getOrderDate();
    orderStauts = order.getStatus();
    address = order.getDelivery().getAddress();
    orderItems = order.getOrderItems();
  }

}
```

- 위의 문제 -> orderItems가 null로 나옴. -> 얘는 엔티티이기 때문!

```java
ordder.getOrderItems().stream().forEach(o => o.getItem().getName()) // 이거로 proxy 초기화하고 돌리면 해결
```

- 현재 문제) DTO 안에 엔티티가 있으면 안 됨. WHY? 엔티티가 외부에 노출되기 때문에. 단순히 DTO 안에 감싸는 것뿐만 아니라 엔티티에 대한 의존을 완전히 끊어야 함. 즉, Order뿐만 아니라 OrderItem 조차도 다 DTO로 변환해야 함.
- OrderItemDto 클래스 추가

```java
static class OrderDto {
  ...
  public OrderDto(Order order) {
    ...
    orderItems = order.getOrderItems.stream()
      .map(orderItem -> new OrderItemDto(orderItem))
      .collect(orderItem -> new OrerItemDto())
  }
}
@Getter
static class OrderItemDto {

  // orderItem에서 노출하고 싶은 것 작성
  private String itemName; //상품명
  private int orderPrice; //주문 가격
  private int count; //주문 수량

  public OrderItemDto(OrderItem orderItem) {
    itemName = orderItem.getItem().getName();
    orderPrice = orderItem.getOrderPrice();
    count = orderItem.getCount();

  }
}
```

- 쿼리 너무 많이 날리는 문제 발생

### 컬렉션으로 페치 조인 최적화

- OrderRepository에 `findAllWithItem()` 작성

```java
public List<Order> findAllwithItem() {
  return em.createQuery(
      "select distinct o from Order o" +
      " join fetch o.member m" +
      " join fetch o.delivery d" +
      " join fetch o.orderItems oi" +
      " join fetch oi.item i", Order.class)
    .getResultList();
}
```

- apiController파트
  - 문제 : orderId에 따른 orderitem 개수만큼 다 join되어서 늘어남! order가 orderItem 수만큼 곱하기 증가! -> `distinct` 사용 -> db 쿼리의 결과를 뽑을 때에는 효과가 없으나 JPA에서 자체적으로 제공하는 order가 같은 id 값이면 중복 제거해준다!

```java
@GetMapping("/api/v2/orders")
public List<OrderDto> ordersV2() {
  List<Order> orders = orderRepository.findAllWithItem();
  List<OrderDto> result = orders.stream()
    .map(o -> new OrderDto(o))
    .collect(Collectors.toList());
  return result;
}

@Getter // 이게 없으면 no property 에러
static class OrderDto {
  // 생성자가 있어야 함
  private Long orderId;
  private String name;
  private LocalDateTime orderDate;
  private OrderStatus orderStatus;
  private Address address;
  // 추가된 것
  private List<OrderItem> orderItems;

  public OrderDto(Order order) {
    orderId = o.getId();
    name = oreder.getMember().getName();
    orderDate = order.getOrderDate();
    orderStauts = order.getStatus();
    address = order.getDelivery().getAddress();
    orderItems = order.getOrderItems();
  }

}
```

- 페치 조인으로 SQL이 1번만 실행됨!
- 단점 : 페이징 쿼리가 불가능하다!, 컬렉션 페치 조인은 1번만 가능하다!
  - 페치 조언을 썼지만 메모리에서 페이징 처리를 해버려서 경고가 발생 -> 쿼리 많이 들어오면 out of memory 발생 가능

#### 📌 페이징과 한계 돌파

- 페이징 + 컬렉션 엔티티를 함께 조회하기 위한 방법을 알아보자.

1. ToOne 관계는 모두 페치 조인
2. 컬렉션은 지연 로딩으로 조회
3. 지연 로딩 성능 최적화를 위해 hibernate.default_batch_fetch_size, @BatchSize를 적용

- in 쿼리로 user 여러명 것을 한번에 다 가져옴, orderitem도 한 번에 가져옴
  - 1 + n + n -> 1 + 1 + 1로 만들어짐
- 페이징 한계 해결 전과의 차이점
  - 이전 버전) 쿼리는 한 번 나가지만 중복이 발생 일대다에서 다에 맞춰서 데이터가 전송이 되니까
  - 지금 버전) 데이터 전송량이 최적화됨. 중복 없으므로! like 정규화된 상태!
- 주의 : 사이징 변수를 조심히 적용하기
  - db에 따라 다르지만 주로 max는 1000개. 100~1000 권장.
  - 순간적으로 db에 부하가 안 가도록, db랑 어플리케이션이 끊어서 가지 않기 때문에. WAS랑 DB가 순간 부하를 견딜 수 있을 만큼으로!

### 컬렉션이 포함된 경우의 JPA에서 DTO 직접 조회

- 핵심 비즈니스를 위한 엔티티 찾을 때의 경우와 분리해서 화면에 fit한 쿼리를 이쪽으로 내보내서 -> 화면에 관련된 건 쿼리랑 밀접하므로! lifecycle이 다른 두 경우를 분리해서 사용
- 생성자에서 orderItems를 뺌 -> why? new 오퍼레이션에서 컬렉션을 바로 넣을 수 없기 때문. 일대다이기 때문에 한 줄로 플랫하기 못 넣기 때문.
  - 그래서, forEach로 루플 돌면서 `findOrderItems()` 함수를 따로 만들어서 orderItems를 위한 쿼리를 따로 짬. orderItems를 채워서 return
- N + 1 쿼리 문제 발생

#### 1️⃣ 컬렉션 조회 최적화

- 루프 안 돌도록 한다
- ToOne 관계 조회로 얻은 orderId로 ToMany 관계인 items를 in절로 한 번에 oi를 가져옴
- 최적화를 위해 orderItems를 Map을 사용해서 매칭 성능 개선
- 데이터 셀렉트 양은 줄어들었지만 직접 코드 작성해야 하는 번거로움 발생함

#### 2️⃣ 플랫 데이터 최적화

- 쿼리 1번으로 최적화해보자.

  1. OrderFlatDto 생성해서 row에 들어갈 값 정의

  - orderitem으로 들어가는 필드값도 다 넣어서 정의

  1. `findAllByDto_flat()` 정의해서 db에서 셀렉해오는 뭐리 작성

  - orderItems 기준으로 나오므로(중복) 페이징 불가능

- 쿼리 한 번으로 하면서 if 앞서 정의한 OrderQueryDto 타입으로 결과를 내고 싶다면?

  - QueryFlatDto가 결과로 나오는 함수를 한 번 거치고 그 결과를 받아서 stream으로 일일이 중복을 걸러내줘야 함 -> orderQueryDto, orderItemQueryDto 둘다 해준 다음에 map 함수로 최종적으로 OrderQueryDto로 반환
  - 묶어줄 때 `@EqualsAndHashCode(of = "orderId")`기준으로 묶어주도록 기준 정의해주기

- 장단점
  - 쿼리 1번
  - 애플리케이션에 전달하는 데이터에 중복 데이터가 추가됨
  - 애플리케이션에서 추가 작업이 큼

### Summary

2가지 경우가 존재한다. api를 뽑아낼 때 엔티티로 조회하냐, DTO로 조회하냐.

- 엔티티 조회
  - 그대로 조회해서 그대로 반환 X -> DTO로 변환해서 반환하기!
  - 이때 여러 테이블 조인해야 해서 성능이 안 나올 땐 페치 조인 이용!
  - 컬렉션의 경우 페이징이 안 되므로 ToOne은 페치 초인 + 컬렉션은 지연 로딩 유지하면서 hibernate에 batch 페치 사이즈 주기
- DTO 직접 조회
  - 1. 컬렉션의 경우, IN절 사용해서 메모리에서 미리 조회
  - 2. 애플리케이션에서 직접 분해/조립하여 원하는 모양으로 바꾸기

#### 결론

1. 엔티티 조회 방식으로 우선 시도 -> 해결이 안 되면 DTO 조회 방식

- WHY? 상황에 맞는 다양한 최적화 방법을 시도할 수 있음. DTO로 조회하면 많은 코드를 수정해야 할 수 있기 때문에.
- 캐시 등으로 다른 차원의 방식으로 최적화를 고민해봐야 할 수도 있음, 레디스...
  - 엔티티는 직접 캐싱 X, 캐시에 잘못 올라가면 영속성 컨텍스트에서 관리하고 있는데 캐시에 있으면 안 지워져서 꼬일 수 있으므로 DTO로 변환해서 DTO를 캐싱!
  - 레디스, 로컬 메모리 캐시 이용

2. 엔티티 조회는 JPA가 많은 부분을 최적화해줌, DTO 조회는 SQL을 직접 다루는 것과 유사함.
