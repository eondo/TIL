# Namespace

---

현재에 있는 views함수를 가져오겠다 → 명시적 경로 from . import views

### Namespace의 필요성

- 문제점
1. articles app index 페이지에 작성한 두번째 앱 index로 이동하는 하이퍼 링크를 클릭 시 현재 페이지로 다시 이동 → 즉, 두번째 App의 index.로 가는 하이퍼링크를 클릭했는데 이동하지 못 함
    1. 원인 **: URL namespace**  
    
    → URL tag가 다음과 같이 되어있는데, 이때 articles의 urls.py에도 name=’index’가 있고, pages에도 있어서 문제 발생
    

```
<a href="{% url 'index' %}">
```

- 해결방안 : 각 앱들의 urls에 app_name을 정의하고 URL tag를 다음과 같이 작성

```
<a href="{% url 'app_name:index' %}">
```

1. 이제 pages index 요청은 잘 가는데 응답하는 페이지가 원하는대로 되지 않음 → 즉, pages app의 index url로 직접 들어가서 이동해도 해당 페이지가 안 뜨고 articles app의 index 페이지가 출력됨
    1. 원인 **:** **Template namespace**
    
    → django 입장에서 articles/templates/ ~ 와 pages/templates/ ~ 에서 ~부터 보기 때문에 index.html으로 이름이 같은 경우 앱의 등록 순서에 따라 인식한다.
    
    → firstpjt > settings.py에 INSTALLED_APPS의 등록 순서에 한정되어 영원히 articles의 index.html만 볼 수 없게 된다.
    
- 해결방안 : ‘articles/templates/’라는 기본 경로는 바꿀 수 없기 때문에 index 앞에 하나의 물리적인 폴더 생성

### URL Namespace

✅ 디렉토리 생성을 통해 물리적인 이름공간 구분

→ *app_name/templates/app_name*

✅ 템플릿 경로 변경

- 문제 상황 : 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음
    
    → articles앱의 urls.py와 pages앱의 urls.py에 있는 index/의 주소는 다르지만 주소 대신 이용하는 이름이 겹치는 현상 
    
    → name=’index’ 대신 app의 이름을 넣음
    
- 해결 : 각 App의 urls.py에 urlpatterns = [] 상단에 app_name = ‘articles’와 같이 URL namespace를 설정 후 템플릿 경로 변경 → {% url ‘article:index’ %} 으로 접근

### Template Namespace

- 문제 상황 : Django가 생각하는 template에 관한 경로가 2가지
    - articles/templates/ ~
    - pages/templates/ ~
    
    이후에 다르지만 동일한 이름을 가진 index.html을 구분할 수 없어, 겹치는 경우 렌더링할 때 앱의 등록 순서로 선택된다.
    
- 해결 : 같은 이름을 가진 index.html 앞에 물리적인 이름 공간(폴더 : 이름은 해당 앱과 동일한 이름으로 앱의 templates 아래에 articles 폴더 넣음) 생성하기
    
    → 앞으로 template 가져올 때, index.html이 아니라 pages/index.html, articles/index.html의 주소의 경로를 가져와야 한다. → views함수의 render 함수 쪽을 바꾼 주소로 변경해야 함
    

# Model

---

### Database

**기본 구조**

- 스키마
    - 뼈대
    - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
- 테이블(Table)
    - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
    1. 필드
        - 속성, 컬럼
    2. 레코드
        - 튜플, 행
        - 테이블의 데이터는 레코드에 저장됨
        

**Database**

- PK(Primary Key)
    - 기본 키
    - 각 레코드의 고유한 값 (식별자로 사용)
    - 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
    - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용됨
- 쿼리
    - 데이터를 조회하기 위한 명령어
    - 주로 테이블형 자료구조에서 조건에 맞는 데이터를 추출하거나 조정하는데 쓰임

## Model

- overview
    
    crud(pjt)의 models.py에서 class 작성 → 설계도 작성 (**makemigrations**) → 테이블 이 설계도 대로 만들어! (**migrate**)
    
- Model을 통해 간접적으로 DB에 접근, 관리

### Model 작성하기

### Model 이해하기

- 어떠한 모델이든 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
- 우리는 column과 datatype만을 지정해주고 있음
- 해당 클래스 Article에는 어떤 데이터 구조가 필요한지 정의하고(데이터 타입), 클래스 변수 title과 content는 DB 필드의 이름임
- 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구

### Django Model Field

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    # 필드 이름 = models.타입 -> 테이블 구축 전 DB의 스키마, 뼈대를 만드는 과정
    title = models.CharField(max_length=10)
    content = models.TextField()
```

- CharField(max_lenth=None, **options)
    
    : 길이의 제한이 있는 문자열을 넣을 때 사용
    
    - max_length
        - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용될 수 있음
- TextField(**options)
    
    : 글자의 수가 많을 때 사용
    

→ 완성한 데이터베이스 스키마 결과 (클래스로 스키마)

| Column | Data Type |
| --- | --- |
| title | VARCHAR(10) |
| content | TEXT |

## Migrations

---

- Django가 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영하는 방법
- Migrations 관련 주요 명령어
    1. makemigrations
    2. migrate

## makemigrations

: 모델의 변경사항에 대한 새로운 migration

`$ python manage.py makemigrations`

→ 이를 통해 ‘설계도’ 완성됨

## migrate

: makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정

`$ python manage.py migrate`

→ 모델의 변경사항과 데이터베이스를 동기화

(! 참고) : 우리가 등록한 App인 articles 말고도 Django 구동을 위해 기본적으로 내장된 App들의 설계도들도 내부적으로 존재하고 이것들과 같이 migrate됐기 때문에 출력 결과가 0001부터 000n까지 많이 나옴

### 추가 필드 정의

- 테이블이 만들어진 상태에서 추가로 필드를 정의하면 어떻게 될까?
- models.py에 변경사항이 생겼을 때 어떤 과정의 migration이 필요할까?
- 변경사항이 일어났을 때 → migration을 해야하는 시점!

models.py에 새로운 필드 추가 시, 그냥 makemigrations을 할 수 없음 → DB는 기본적으로 빈 값을 넣을 수 없으므로 단순히 필드를 옆에 붙인다고 생각하면 안됨 

→ 따라서 1) 기본값으로 일단 채워넣을 값을 입력한다, 2) 기본값을 넣은 코드로 수정하여 다시 makemigrations을 진행해야 한다.

### Model 변경사항 반영하기

```python
dependencies = [
        ('articles', '0001_initial'),
    ]

# 1번 설계도에서 추가된 거니까 기존에 의존한다는 의미로 
# 해당 dependencies라는 새로운 것이 생기고, 그 안에 0001_initial이 존재함
```

- 최신 설계도만 두지 않고 0001, …, 0005로 쌓아나가는 이유
    
    → 그 순간의 변경사항을 기록하여 위험을 대비할 수 있기 때문
    

**추가 필드 예시**

DateTimeField()

선택 인자

1. auto_now_add
    - 최초 생성 일자
    - 데이터가 실제로 만들어질 때 현재 날짜와 시간으로 자동으로 초기화 되도록 함
2. auto_now
    - 최종 수정 일자
    - 데이터가 수정될 때마다 현재 날짜와 시간으로 자동으로 갱신 되도록  함

### **migration 3단계**

1. models.py에서 변경사항이 발생하면
2. migration 생성
3. DB 반영(모델과 DB의 동기화)

설계도는 python으로 적었는데 DB는 SQL만 이해하는데? → 중간에 번역해주는 친구가 있다! → ORM (객체로 무언가를 연결하겠다)

# ORM

---

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 SQL을 사용하지 않고 데이터베이스 조작 가능!
- DB를 객체로 조작하기 위해 ORM을 사용

**Model 정리**

API, ORM이 사용하는 메서드들의 이름

**사전준비**

1. $ pip install ipython django-extensions로 설치
2. 외부 라이브러리를 등록 

```
INSTALLED_APPS = [
    'articles',
    'django_extensions',
```

**[참고] Shell**

사용자 ↔ 셸 ↔ 운영체제의 소통을 도움

끝낼 땐 exit() 사용

**Django Shell 실행**

- ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용
- Django 환경 안에서 실제 Shell 테스트를 해보고 싶을 때 사용 실제 Model 데이터베이스에 반영도 됨

```python
$ python manage.py shell_plus

# Shell Plus Model Imports
from articles.models import Article # 우리가 만든 것도 자동으로 import됨
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User  
from django.contrib.contenttypes.models import ContentType      
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery
```

**ORM 동작 예시**

전체 데이터를 조회 : In [1]: Article.objects.all() → Out[1]: <QuerySet []> (현재는 빈 리스트)

## QuerySet API

### Database API 구문

- 형식 : **Article.objects.all() → 여기서 조회, 수정, 삭제 등 Queryset API**

→ objects가 API를 들고 있고, 얘가 데이터에 대한 조작, 명령을 이 메서드로 정의함

→ 현재, 레코드가 아예 없음 (빈 값 ≠ 레코드가 없는 것)

- objects manager
    
    DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager
    
- Query
    - 데이터베이스에 특정한 데이터를 보여 달라는 요청
    - 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료형태로 변환하여 우리에게 전달
- QuerySet 자료 형태란?
    - 데이터베이스에서 전달 받은 객체 목록(데이터 모음)
        
        → 순회가 가능한 데이터(iterable)로서 1개 이상의 데이터를 불러와 사용 가능
        
        → 리스트처럼 필터 걸기, 정렬 등 수행할 수 있음
        
    - 단일한 객체을 반환할 때에는 QuerySet이 아니라 모델의 인스턴스로 반환됨

### QuerySet API 익히기

**CRUD :** 생성 / 조회 / 수정 / 삭제

1️⃣ **CREATE**

1. article = Article()
2. article.title
3. article.save() → 이를 실행해야 DB로 감! DB에 최종적으로 반영되게 하고, id가 부여됨
    - 데이터 생성 시 save를 호출하기 전에는 객체의 id 값은 None
    - id 값은 Django가 아니라 데이터베이스에서 계산되기 때문
    - 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 save 호출해야 테이블에 레코드 생성됨

2️⃣ **READ**

QuerySet API method를 사용해 데이터를 다양하게 조회하기 가능, 조회를 얼마나 잘하느냐가 어려움

- 생길 수 있는 경우 2
1. 데이터 목록을 받느냐 return new querysets
2. 데이터 하나만 받느냐 do not return querysets

- get()
    
    : 단일 데이터 조회
    
    - 찾을 수 없으면 에러, 둘 이상의 객체를 찾아도 에러 → 고유성을 보장하는 조회에서 사용해야 함. 즉, 유니크한 값(pk) 조회에만 사용해야 함
- all()
- filter()
    
    무조건 새로운 QuerySet으로 반환! 0개여도, 1개여도
    
    - 왜 pk에 쓰지 않음?
        
        1) QuerySet으로 주니까 한 겹을 더 벗겨내야 하는 번거로움 존재 
        
        2) 해당 pk가 없는 경우 예외를 발생시켜 줘야 하는데, 없어도 빈 값을 주기 때문에 pk 타입을 이용할 때에는 적합하지 않음
        
- Field lookups
    
    조회할 때 조건을 붙여서 조회하고 싶을 때 사용 (ex. contain)
    
    ```python
    In [24]: Article.objects.filter(content__contains='ja')
    Out[24]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
    ```
    

3️⃣ **UPDATE**

- Update 과정
    1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
    2. article 인스턴스 객체의 인스턴스 변수 변경
    3. article.save() → 해야 DB에 반영됨
    

4️⃣ **DELETE**

```python
In [33]: article.delete()
Out[33]: (1, {'articles.Article': 1})
```

**[참고] ‘__str__()’ : 매직 메서드**

models.py에서 def __str__(self): 선언

```python
In [1]: Article.objects.all()
Out[1]: <QuerySet [<Article: second>, <Article: third>]>
```

- [models.py](http://models.py) 변경했으니까 migrations 해야 되는가? NO
- WHY? def str이 객체 인스턴스가 출려될 때 형식만 바꾼 것이지, DB에 전혀 영향을 주지 않기 때문에 makemigrations해도 No changes라고 뜨기 때문.