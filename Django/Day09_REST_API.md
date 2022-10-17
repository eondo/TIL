# REST API
#### HTTP 기본 개념 학습
HTTP Request Methods : 요청 시에 리소스(HTTP 요청의 대상)에 대한 행위를 정의
- 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음
1. GET
- 서버에 리소스의 표현을 요청
- GET을 사용하는 요청은 데이터만 검색해야 함
2. POST
- 데이터를 지정된 리소스에 제출
- 서버의 상태를 변경
3. PUT
- 요청한 주소의 리소스를 수정
4. DELETE
- 요청한 주소의 리소스를 삭제
→ 요청에 행동 응답에는 상태가 정의되어 있음

#### 웹에서 리소스를 식별하는 방법은?
#### URI
인터넷에서 하나의 리소스를 가리키는 문자열, 일반적인 URI는 웹주소 URL! + 특정 이름 공간에서 이름으로 리소스를 식별하는 URI는 URN!

#### URL
통합 자원 위치
#### URL 구조
- 스키마(or protocol)
- 권한 : 스키마 다음으로 문자 패턴 :// 으로 구분됨
  - 1. Domain Name : 요청 중인 웹 서버를 나타냄
  - 2. Port : 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문 → 생략 가능, 별도로 쓸 필요 X
- Path : 웹 서버의 리소스 경로, 실제 위치가 아닌 추상화된 형태의 구조를 표현
- 파라미터 : & 기호로 구분되는 key-value 쌍 목록
- 앵커 : 하나의 원하는 리소스에서 특정 위치를 가리킴
- 부분 식별자 '#' 이후 부분은 서버에 전송되지 않음 → 브라우저에게 해당 지점으로 이동할 수 있게 함

### REST API
### API(Application Programming Interface)
애플리케이션과 프로그래밍으로 소통하는 방법
- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)!
- __Web API__
  - 웹 서버 or 웹 브라우저를 위한 API
  - 여러 Open API를 활용 가능함
  - API가 응답하는 다양한 타입의 데이터 → HTML, XML, __JSON__ 등
### REST
Representational State Transfer : API 서버를 개발하기 위한 일종의 소프트웨어 설계 방법론 == 소프트웨어 아키텍쳐 디자인 제약 모음
- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술
- REST에서 자원을 정의하고 주소를 지정하는 방법
1. 자원의 식별 - URI
2. 자원의 행위 - HTTP 메서드
3. 자원의 표현
- 자원과 행위를 통해 궁극적으로 표현되는 결과물
- JSON으로 표현된 데이터를 제공

#### JSON이란?
- 자바스크립트의 표기법을 따른 단순 문자열
- 파이썬의 dict, 자바스크립트의 object처럼 C계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 key-value 형태의 구조를 가짐 → 어떤 언어, 환경으로 변환했을 때도 누구나 쓰기 쉬움! 기계가 파싱(해석&분석)하고 만들어내기 쉬움!

### Response JSON
- 장고의 역할이 바뀜
- 과거 - Django로 작성한 서버는 사용자에게 HTML로만 응답 → 현재 : JSON 데이터를 응답하는 서버로의 변환!
- JSON을 응답하는 Django 서버를 구성하는 법을 학습
- WHY❓ 하나의 페이지에서 출력되는 데이터 양이 굉장히 많기 때문에 서버가 페이지를 다 완성해서 보내주는 것은 비효율적이므로 JSON을 응답으로 이용함

- 응답의 방법
1. HTML 응답
2. *JsonResponse()*을 사용한 JSON 응답
3. Django Serializer를 사용한 JSON 응답
4. Django REST framework → 컬럼을 일일이 명시하지 않음

### Serialization
데이터 구조나 객체 상태를 나중에 쉽게(다양한 환경에서) 재구성할 수 있는 포맷으로 변환하는 과정
- Django의 `serailize()`는 퀴리셋, 모델 인스턴스와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 python 데이터 타입으로 만들어줌
- 즉, json으로 최종적으로 가야 하며 object 덩어리를 json으로 만들 수 없는데, 이때 이를 가능하게 하는 중간 과정이 `serialize()`

- __Django REST framework (DRF)__
  - Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리로 DRF의 serailizer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동함
  ```python
  return Response(serializer.data)
  #.data를 통해 json이 나옴
  ```

## 단일 모델 data의 Serialization
### ModelSerializer
`ModelSerializer 클래스`는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
1. Model 정보에 맞춰 자동으로 필드 생성
2. serializer에 대한 유효성 검사기를 자동으로 생성
3. .create() 및 .update()의 간단한 기본 구현이 포함됨
- many option : 단일 객체 인스턴스 대신 쿼리셋 or 객체 목록을 serialize하려면 many=True 처리

```python
# 게시물 리스트
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 특정 게시물
class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
```

### 📌RESTful API - Article
### GET-List
게시글 데이터 목록 조회하기
- DRF에서 `api_view` 데코레이터 필수
- DRF view 함수가 응답해야 하는 HTTP 메서드를 리스트 안에 작성

```python
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)

        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)    # S된 데이터, 이걸 ㅇㅇ개발자한테 주면 json을 dict으로 변경해서 사용한다.

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
### GET-Detail
단일 게시물 데이터 조회하기

### POST
게시글 데이터 생성하기
- 데이터 생성 성공 시 201 Created 상태 코드, 응답하고 실패했을 경우 400 Bad request 응답
- raise_exception 인자 : 유효성 검사 오류가 있으 경우 validationError 예외를 발생시킴
```python
elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
### DELETE
게시글 데이터 삭제하기

### PUT
게시글 데이터 수정하기
- 첫번째 인자가 수정 전 기존값 = 인스턴스, 뒤가 수정 후의 값 data=request.data
```python
elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

## N:1 관계 모델 data의 Serialization
### 📌RESTful API - Comment
### GET-List
댓글 데이터 목록 조회하기
- Serializer 작성
```python
# 댓글 (ArticleSerializer보다 위에 존재해야 함)
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
```

### GET-Detail
단일 댓글 데이터 조회하기
- comment_list는 **comment_pk**가 없으므로 같은 함수를 사용하기 부적합 → comment_pk를 인자로 받는 새로운 함수 `comment_detail` 선언

### POST
단일 댓글 데이터 생성하기
- 특정 게시물의 댓글이니까 게시물의 id를 인자로 가지는 새로운 함수 `comment_create` 선언
```python
@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, article_pk)

    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)    # commit=False 대신 바로 article 지정해서 데이터를 넘겨 저장

        return Response(serializer.data, status=status.HTTP_201_CREATED)
```
- 🚫 CommentSerializer에서 article field 데이터 또한 사용자로부터 입력 받도록 설정되어 있어서 에러 발생 → `read_only_fields`
- 읽기 전용 필드 설정 : 데이터를 전송하는 시점에 해당 필드를 데이터 유효성 검사에는 제외시키고, 조회 시에는 출력되도록 함
```python
read_only_fields = ('article',)
```

### DELETE & PUT
댓글 데이터 삭제 및 수정하기
```python
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

## N:1 역참조 데이터 조회
1. 특정 게시글에 작성된 댓글 목록 출력하기 → 기존 필드 override
2. 특정 게시글에 작성된 댓글의 개수 출력하기 → 새로운 필드 추가

### 1️⃣
1. `PrimaryKeyRelatedField()` → "comment_set"이라는 key로 json 파일에 추가되어 출력됨
```python
comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
```
- 기존필드 쓰기, 역참조하는 대상의 pk만 가져옴

2. __Nested relationships__
```python
comment_set = CommentSerializer(many=True, read_only=True)
```
- 이미 있는 `CommentSerializer` 클래스 쓰기 → 동작하는 필드 전체 출력하는 걸 동작하는 그대로 가져올 수 있음
- 상황에 맞게 serializer들을 추가적으로 만들어가는 것, json을 보내줄 구조를 어떻게 할 것이냐에 따라!

### 2️⃣
- how 게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력? → 기존에 존재하는 필드 X, 완전히 새로운 카운팅을 해야 함, 연산값을 필드로 만들어줘야 함
```python
comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
```
- `source`(필드를 채우는 데 사용할 속성 이름)에 ORM 명령어를 써줌 → ArticleSerilizer라서 article 생략 가능 -> ORM 연산하는 부분이 문자열로 들어감
- override되거나 추가되는 필드는 read_only_fields가 동작하지 않으므로 (물리적으로 테이블에 존재하는 필드만 가능) 인자값으로 넣음

### Django shorcuts functions
- 두 가지 shortcut
  - `get_object_or_404()`, `get_list_or_404()`

- `get_object_or_404()` : 해당 객체가 없을 때 기존 DoesNotExit 예외 대신 Http404를 raise 함
- `get_list_or_404()` : 모델 manager objects에서 *filter()*의 결과를 반환, 해당 객체 목록이 없을 때 Http404를 raise 함
- WHY❓
GET의 특징은 없을 때 예외 발생, 한 개 이상일 때도 예외 발생! 즉, 코드가 더 진전되지 않고 예외가 발생하여 return까지 안 가서 온전하게 끝까지 가지 못 해 Django가 500을 말해준다. 하지만 이는 없는 게시글을 조회했기 때문에 서버는 클라이언트에게 올바른 에러인 404를 전달해야 한다. 따라서, GET의 동작은 유지하면서 요청을 수행할 수 없을 때 404를 주게 한다.
