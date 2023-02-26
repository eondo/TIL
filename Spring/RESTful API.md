API 잘 설계하고 개발하는 것이 중요
단순히 SQL를 써서 API 끌어오는 것과 다르다. JPA를 쓴다면 Entity 개념이 있기 때문에 이 상태에서 API를 만드는 것은 다른 차원이다.
JPA 사용하면서 API를 만들 때 어떤 식으로 하는 것이 올바른 방향인지 배워야 한다.

- api 폴더를 따로 둠 -> 공통으로 예외처리 등을 할 때 패키티, 구성 단위로 공통처리하기 때문에, api와 화면은 다르기 때문에 따로 분리함
- @Controller + @ResponseBody -> @RestController
  - ResponseBody : 데이터 자체를 json, xml로 바로 보낼 때 주로 쓰는 annotation

### 회원 등록

- @PostMapping
- @RequestBody : JSON으로 온 Body를 Member에 그대로 맵핑해서 넣어줌
- memberService.join(member) : join하면 id값 반환해준 것을 받음

```java
@RestController
@RequiredArgsConstructor
public class MemberApiController {

  private final MemberService memberService;

  public CreateMemberResponse saveMemberV1(@RequestBody @Valid Member member) {
    Long id = memberService.join(member);
    return new CreateMemberResponse(id);
  }
}
```

- NULL값을 허용하지 않는 등의 제약이 있을 때, Control 단에서 validation 넣어놨으므로 Member 엔터티에서 @NotEmpty 어노테이션
  - @Valid -> javax.validation.constraints
- 같은 이름의 member를 post했을 때 이미 존재하는 회원입니다.로 에러 발생
- 화면에서 들어오는 validation을 presentation 계층에 대한 검증 로직이 엔티티에 다 들어가있는 문제(CreateMemberRequest라는 클래스를 따로 안 만들어도 됨)
  - 어떤 api마다 NotEmpty가 필요한 경우 필요하지 않은 경우 다름
  - name을 username으로 바꿈으로 인해서 Entity가 바뀌었을 때 api의 스펙이 바뀌는 점 -> api 스펙을 위한 별도의 DTO를 만들어서 파라미터로 받아야 함
  - 엔티티를 외부에서 JSON 오는 것을 바인딩 받아서 쓰면 안 됨 === 엔티티를 파라미터로 받지 마라

```java

```

#### DTO

- 중간에 엔티티와 파라미터를 컨트롤해서 맵핑해주는 장치
- 기존 문제 : 파라미터로 어디까지 들어와도 바인딩돼서 들어가서 API 문서 없이 엔티티만 보고 어떤 값이 들어올지 알 수 없음
- DTO를 보면? 어떤 값을 받게 되어있는지 정의되어있음, API마다 다른 validation에 대응 가능

### 회원 수정

- 수정할 때 가급적이면 변경 감지 사용

1. PutMapping 작성

```java
@PutMapping("/api/v2/members/{id}")
public UpdateMemberResponse updateMemberV2(
  @PathVariable("id") Long id,
  @RequestBody @Valid UpdateMemberRequest request) {

    memberService.update(id, request.getName());
}

@Data
@AllArgsConstructor
static class UpdateMemberResponse {
  private Long id;
  private String name;
}
```

2. service/MemberService.java에 update 함수 작성

- ```java
    @Transactional
    public void update(Long id, String name) {
      Member member = memberRepository.findOne(id); // MemberRespository에서 찾아옴
      member.setName(name)
    }
    // Transaction 시작이 되고 JPA가 영속성 콘텍스트에서 id, DB에서 끌고 올 거고, 영속 상태의 member를 name을 바꿔줘서 얘가 종료되면 Spring AOP가 동작하면서 @Transactional 어노테이션에 의해서 AOP가 끝날 때 영속성 컨텍스트 풀러시하고 DB에는 트랜잭션 커밋
  ```

3. 필요한 데이터 Response 객체 만들기

```java
Member findMember = memberService.findOne(id);
return new UpdateMemberResponse(findMember.getId(), findMember.getName());
```

- 커맨드와 쿼리 분리
  - update 함수에서 바로 Member를 넘기지 않고 update가 끝나면 `Member findMember = memberService.findOne(id);`를 이용하여 업데이트하면서 쿼리해버리는 상황 방지 -> id 정도만 반환하여 찾기
  - 유지보수에 효율적

### 회원 조회

- API 스펙이랑 화면에 위한 기능이 엔티티에 들어와버려서 엔티티로 의존관계가 들어와야 하는데 그 반대가 된 경우이므로 양방향 의존관계가 걸림으로써 애플리케이션 수정이 어려움
- 엔티티 변경해서 API 자체가 변경되는 엔티티 직접 반환 방법은 지양
