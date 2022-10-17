## REST API
사전 : HTTP 기본 개념 학습
HTTP Request Methods : 요청 시에 리소스(HTTP 요청의 대상)에 대한 행위를 정의
- 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의
- GET, POST, PUT, DELETE
#### GET
- 서버에 리소스의 표현을 요청
- GET을 사용하는 요청은 데이터만 검색해야 함
#### POST
- 데이터를 지정된 리소스에 제출
- 서버의 상태를 변경
#### PUT
- 요청한 주소의 리소스를 수정
#### DELETE
- 요청한 주소의 리소스를 삭제

요청에 행동 응답에는 상태가 정의되어 있음

### 리소르를 웹에서 어떻게 식별하는가?
각 리소스는 식별을 위해 URI가 필요함
#### URI
인터넷에서 하나의 리소스를 가리키는 문자열, 일반적인 URI는 웹주소 URL! + 특정 이름 공간에서 이름으로 리소스를 식별하는 URI는 URN!

#### URL
통합 자원 위치
#### URL 구조
- 스키마(or protocol)
- 권한 : 스키마 다음으로 문자 패턴 :// 으로 구분됨
  - 1. Domain Name : 요청 중인 웹 서버를 나타냄
  - 2. Port : 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문 -> 생략 가능, 별도로 쓸 필요 X
- Path : 웹 서버의 리소스 경로, 실제 위치가 아닌 추상화된 형태의 구조를 표현
- 파라미터 : & 기호로 구분되는 key-value 쌍 목록
- 앵커 : 하나의 원하는 리소스에서 특정 위치를 가리킴
- 부분 식별자 '#' 이후 부분은 서버에 전송되지 않음 -> 브라우저에게 해당 지점으로 이동할 수 있게 함

## REST API
### API(Application Programming Interface)
애플리케이션과 프로그래밍으로 소통하는 방법
API를 제공하는 애플리케이션과 다른 SW 및 HW 등의 것들 사이의 간단한 계약(인터페이스)!
### Web API
웹 서버 or 웹 브라우저를 위한 API
- API가 응답하는 다양한 타입의 데이터 -> HTML, XML, __JSON__ 등
### REST
Representational State Transfer - API 서버를 개발하기 위한 일종의 소프트웨어 설계 방법론 == 소프트웨어 아키텍쳐 디자인 제약 모음
- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

- REST에서 자원을 정의하고 주소를 지정하는 방법
1. 자원의 식별
URI
2. 자원의 행위
HTTP 메서드
3. 자원의 표현
- 자원과 행위를 통해 궁극적으로 표현되는 결과물
- JSON으로 표현된 데이터를 제공

#### JSON
- 자바스크립트의 표기법을 따른 단순 문자열
- 파이썬의 dict, 자바스크립트의 object처럼 C계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 key-value 형태의 구조를 가짐 → 어떤 언어, 환경으로 변환했을 때도 누구나 쓰기 쉬움! 기계가 파싱(해석&분석)하고 만들어내기 쉬움!

### Response JSON
- 장고의 역할이 바뀐다! JSON 형태로의 서버 응답 등
- 서버가 응답하는 것 : 이때까지 HTML로 넘기던 걸 JSON 데이터를 응답하는 서버로의 변환!
- JSON을 응답하는 Django 서버를 구성하는 법을 학습
- WHY? 하나의 페이지에서 출력되는 데이터양이 굉장히 많기 때문에 서버가 페이지를 다 완성해서 보내주는 것은 비효율적

- 응답의 방법
1. HTML 응답
2. JsonResponse()
3. ? -> 컬럼을 일일이 명시하지 않음

### Serialization
데이터 구조나 객체 상태를 나중에 (다양한 환경에서) 재구성할 수 있는 포맷으로 변환하는 과정
- Django의 `serailize()`는 퀴리셋, 모델 인스턴스와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 python 데이터 타입으로 만들어줌
- json으로 최종적으로 가야 하는데 object 덩어리를 json으로 만들 수 없는데, 이때 이를 가능하게 하는 중간 과정이 serialize()!

4. ❗ Django REST framework (DRF)
- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리로 DRF의 serailizer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동함
```python
return Response(serializer.data)
#.data로 json이 나옴
```

## Django REST framwork - Single Model
### ModelSerializer
ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
1. Model 정보에 맞춰

- many option : 단일 객체 인스턴스 대신 쿼리셋 or 객체 목록을 serialize하려면 many=True 처리

### GET
1. 목록
2. 단일
### POST
```python
elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
### DELETE
### PUT
첫번째 인자가 인스턴스, 뒤가 data=request.data

## Nl1 관계
`read_only_fields`
- 데이터 유효성 검사에는 제외시키고, 조회 시에는 출력되도록

## N:1 역참조 데이터 조회
1. 특정 게시글에 작성된 댓글 목록 출력하기 → 기존 필드 override
2. 특정 게시글에 작성된 댓글의 개수 출력하기 → 새로운 필드 추가

- 관련 함수같은 거 쓰기, 역참조하는 대상의 pk만 가져옴
- 이미 있던 commentserial 클래스 쓰기 -> 동작하는 필드 전체 출력하는 걸 동작하는 그대로 가져올 수 있음
- 상황에 맞게 serializer들을 추가적으로 만들어가는 것, 어떻게 json을 보내줄 구조를 어떻게 할 것이냐에 따라

[2번]
- how?: 게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력하기 -> 기존에 존재하는 필드 x 완전히 새로운 카운팅을 해야 함, 연산값을 필드로 만들어줘야 함
- source(필드를 채우는 데 사용할 속성 이름)에다가 ORM 명령어를 써줌 -> ARTICLESERIZLIER라서 article 생략 가능 -> orm 연산하는 부분이 문자열로 들어감
- override되거나 추가되는 필드는 read_only_fields가 동작하지 않으므로 (물리적으로 테이블에 존재하는 필드만 가능) 인자값으로 넣음


### Django shorcuts functions
GET의 특징은 없을 때 예외 발생, 한 개 이상일 때도 예외 발생! 즉, 코드가 더 진전되지 않고 예외가 발생하고 return까지 안 가서 온전하게 끝까지 가지 못 해 Django가 500을 말해줌. 하지만 이는 없는 게시글을 조회했기 때문에 서버는 404를 줘야 함. GET의 동작은 유지하면서 없을 때 404를 주게 해야 함.
`get_object_or_404()`, `list_or_404()`