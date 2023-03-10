# JPA

동적 쿼리랑 페이징할 때에만 Querydsl 쓰고 나머지는 쿼리문으로 그냥 작성!
스프링 스케줄러로 마감 기한 감지!

#### 이외의 궁금증

- entity랑 Repository는 일대일로 생기는 건가?
- Repository에 interface에 아무것도 정의되지 않은 거랑 뭐가 있는 거랑 무슨 차이지?
- enum의 역할, 언제 쓰이는지

#### OAuthController

- StringBuffer()가 무엇인가?
- 토큰 발급, 재발급, 로그인, 로그아웃이 GetMapping?

### 0306 QnA

1. SignupRequestDto만 RequestDto가 있는 이유?

- 필요없기 때문.
  무조건 response request 가 짝지어져서 있는 게 아니고 필요에 따라서 없애기도 함
  dto가 그런 용도니까.
  필요 여부의 판단 기준은 어떤 느낌인지?
  request가 필요로 하는 걸 요청하는 건데, 저때는 소셜로그인이라서 프론트쪽에서 받아서 소셜로그인쪽으로 보내버리니까 그냥 우리는 파싱해서 토큰 엑세스 값만 받아오면 되니까.
  네이버 단에서 한 번 처리되고 오니까 백단에서는 가지고 있을 필요가 없다.

- MemberEntity랑 MemberInfoEntity가 따로 있는 이유?
  - 기능을 기준으로 약간 나눈 것?
    필드가 너무 많아서 다 불러오져니까 너무 낭비다. 방법이 차이!
    provider가 뭔지 다시... 소셜로그인하면 카카오, 구글, 등등 여러 플랫폼에서 진행할 수 있으니까 그것의 구분을 위해서 -> status와 비슷하게 이해하면 좋긴 한데 다른 개념

MemberProfileEntity에 updateMemberProfile 함수는 Service에 들어가도 되는지?
질문 : 사실상 service단에서 하는 PutMapping이랑 동작이 비슷해보이는데 왜 굳이 여기에 위치하나요?
service단에서도 작성될 수 있긴 한데 MemberService에 함수가 정말 많아서 다 넣기에 서비스단이 복잡해짐.
바로 수정하는 거니까 엔티티단에서 처리해도 됨
그럼 서비스단 함수랑 엔티티단에서 적는 함수랑 뭐가 처리되는 과정이 다른가? ex) validation하는 거에서 보면! 프론트에서 받은 code, state를 가지고 파싱하는데 이건 다른 데서 많이 쓰인다? 근데 이건 너무 기니까 위에서 사용될 때 그대로 쓰면 너무 기니까 이런 과정은 메서드로 묶어놓고 (서비스단에서 쓰는 메서들들은) -> 코드 간결화
service단에서도 메서드화해서 하는 게 남들이 보기에도 좋음
set 없이 udpate하게 할 수 없음 엔티티에 일단 접근해야 하는데 private으로 다 막아놨으니까...
서비스 단에서 하면 set함수를 써야 함! 하지만 여기 프로젝트에서는 set이 아무데도 없음!
AwsS3Service?
AWS에 EC2, RDS, S3 등 이런 서비스들이 있는데, S3를 썼었는데 Controller 없어도 service는 만듦.
ex. 사진 업로드할 때 memberservice에 넣어도 되지만 복잡성 줄이기 위해 따로 service파일을 만듦
왜 controller 없냐? 회원가입 요청 한 번 보내는데 controller 또 있으면 이중으로 보내는데... 사진 업로드를 controller를 따로 빼기 위해 dto를 따로 만든다는 게... 트랜잭션 보낼 때?
s3 서비스가 member에 있어도 되는데, 그냥 분리한 것.
bucket이 큰 폴더 개념 정의해둔 토대로 implementation에 의존성 넣어놓고 받았으니까 받은 걸 활용할 수 있으니까
