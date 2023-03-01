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
