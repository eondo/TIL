static files 구성하기
- load tag : 특정 라이브러리, 패키지에 등록된 모든 템플릿 캐그와 필터를 로드
- static tag : `STATIC_ROOT`에 저장된 정적 파일에 연결

관련 Core Settings
#### STATIC_ROOT
1. collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
2. 장고가 local server에서는 정적 파일들의 위치를 알고 있지만 Cloud server에서는 모르기 때문에 배포 환경에서는 Django를 직접 실행하는 것이 아니라, 다른 서버에 의해 실행되기 때문에 내자되어 있는 정적 파일들을 인식하지 못함 -> STATIC ROOT를 통해 특정 경로에 꺼내주는 것!

#### STATICFILES_DIRS
app/static 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트

#### STATIC_URL
1. STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
2. 실제 파일ㄹ이나 디렉토리가 아니며, URL로만 존재
3. 개발 단계에서는 실제 정적 파일이 저장되어 있는 app/static/ 경로(기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색


### Staticfiles 사용하기
static file을 가져오는 2가지 방법
1. 기본 경로에 있는 static file 가져오기
2. 추가 경로에 있는 static file 가져오기


## Image 업로드하는 방법
Django의 ImageField를 사용해 사용자가 업로드한 정적 파일 처리하기

#### ImageField()
이미지 업로드에 사용하는 모델 필드
업로드 된 객체가 유효한 이미지인지 검사
- FileField()에 upload_to!

- 사용 단계
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. upload_to 속성을 정의하여 업로드된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정 (선택 사항) MEDIA_ROOT/이 이후의 이 부분! 관장

#### MEDIA_ROOT
- 사용자가 업로드한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
- 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않고 "파일 경로"를 저장함 -> 실제로 이미지를 어디에 모아둘 건지는 MEDIA_ROOT를 사용해야 함
- *주의) MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함

#### MEDIA_URL
- MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
- 업로드 된 파일의 주소를 만들어주는 역할

#### 개발 단계에서 사용자가 업로드한 미디어 파일 제공하기
업로드 된 파일의 URL == `settings.MEDIA_URL`
위 URL을 통해 참조하는 파일의 실제 위치 == `settings.MEDIA_ROOT`

### CREATE (미디어 파일을 저장하는 방법)
- blank=True : 빈 문자열을 허용하겠다. 즉, 이미지를 첨부하지 않아도 글을 작성하는데 문제 없도록 함 -> 유효성 검사에서 사용됨!
- null : True인 경우 Django는 빈 값을 DB에 NULL로 저장함 -> 유효성 검사 통과 여부에 영향을 끼치지 않음, DB-related
- 문자열 기반의 필드는 null 옵션 사용을 피해야 하고, 데이터 없음을 의미하려고 할 때, null이 아니라 빈 문자열을 사용하는 것이 규칙임

- 이미지 처리 도구를 위한 기반을 제공하는 Pillow 설치 후 makemigrations 진행

- 1. 폼에 input type file을 사용할 경우 -> form 태그 수정 `<form action="" method="POST" enctype="multipart/form-data">` -> 이를 통해 파일을 전송할 수 있음
- 2. 파일 및 이미지는 request의 POST 속성 값으로 넘어가지 않고 FILES 속성 값에 담겨 넘어감 -> `form = ArticleForm(request.POST, request.FILES) `

### READ (사용자에게 미디어 파일을 출력해주기)
### UPDATE

### 지금 이미지필드를 통해 업로드 되는 경로가 다 미디어 루트로 귀결되고 있는데, 그 이후 추가 경로를 작성할 수 있는데 UPLOAD_TO! 우리가 지정

### upload_to argument
사용자 지정 업로드 경로와 파일 이름 설정하기
1. 문자열 값이나 경로 지정 방법
2. 함수 호출 방법
- 1. instance : 폴더번호로 인스턴스에 pk값을 쓰는 것? save가 되기 전에 호출돼서 어려움. 대신 인스턴스가 가지는 다른 필드값을 경로 요소로 지정
```python
def articles_image_path(instance, filename):
    return f'images/{ instance.user.username}/{filename}'
...
image = models.ImageField(blank=True, upload_to=articles_image_path)
```

## 이미지 Resizing
방법은 많은데, 로컬에서 할 수 있는 방법 중 하나다. 실제 원본 이미지를 서버에 그대로 로드하는 것은 여러 이유로 부담이 큼. -> 업로드될 때 이미지 자체를 resizing하는 것을 사용해보자! `imagekit`

### 썸네일 만들기
1. 원본 이미지 저장 X
```python
image = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 80},
    )
```
2. 원본 이미지 저장 O
- 물리적인 컬럼은 아니다 -> image_thumbnail은 테이블에 저장되는 개념이 아니라 원본을 기준으로 출력이 될 때, 그때 썸네일을 생성
```python
    image = models.ImageField(blank=True)

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 80},

# detail.html
<img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
```

## QuerySet API Advanced
### CRUD

### Sorting data
#### values()
모델 인스턴스가 아닌 딕셔너리 요소들을 가진 쿼리셋 반환
필드 지정 시, 각 딕셔너리에는 지정한 필드에 대한 key과 value만을 출력
원하는 값을 보기 위해 많이 쓰이는 메서드

### Filtering data
#### filter()
- Field lookups
  - SQL에서 WHERE 절의 상세한 조건을 지정하는 방법
  - 필드명 뒤에 '__' 이후 작성
  - User.objects.filter(age__gte=30, balance__gt=500000) 
    ...: .values('first_name', 'age', 'balance')
- 어떤 게 포함되는 거 찾기 *contain*
  - User.objects.filter(first_name__contains='호').value 
    ...: s('first_name', 'last_name')
- 특정 단어로 시작, 끝나는 것 *startswith*, *endswith*
  - User.objects.filter(phone__startswith='011-').values 
    ...: ('first_name', 'phone')
- a 혹은 b? -> 포함 관계 사용 *in=[리스트]*
  - User.objects.filter(country__in=['강원도', '경기도'] 
    ...: ).values('first_name', 'country')

#### exclude()
- 주어진 매개변수와 일치하지 않는 경우

#### 'Q' object
기본적으로 filter()와 같은 메서드의 키워드 인자는 AND를 따름
더 복잡한 쿼리를 실행해야 하는 경우 -> Q 객체
- 두 가지 조건을 or로 해당하는 객체 출력 
  - `from django.db.models import Q` 후, 파이프라인 사용 가능
  - User.objects.filter(Q(age=30) | Q(last_name='김'))


### Aggregation data(Grouping)
#### aggregate()
- Aggregation 함수 : Avg, Count, Max, Min, Sum, ...etc.
```
In [33]: User.objects.filter(age__gte=30).aggregate(Avg('age' 
    ...: ))
Out[33]: {'age__avg': 36.2093023255814}
```
#### annotate()
쿼리의 각 항목에 대한 요약 값을 계산해서 만드는 것, 실제로 있지 않은 컬럼에 대하여 주석 달기
- 각 지역별로 몇 명씩 살고 있는지 조회하기
```
In [38]: User.objects.values('country').annotate(Count('count 
    ...: ry'))
Out[38]: <QuerySet [{'country': '강원도', 'country__count': 14}, {'country': '경기도', 'country__count': 9}, {'country': '경
상남도', 'country__count': 9}, {'country': '경상북도', 'country__count': 15}, {'country': '전라남도', 'country__count': 10}, {'country': '전라북도', 'country__count': 11}, {'country': ' 
제주특별자치도', 'country__count': 9}, {'country': '충청남도', 'country__count': 9}, {'country': '충청북도', 'country__count': 14}]>
```
- N : 1 모델 관계에도 사용 가능
```python
```

- Either Project 예시
```python
# models.py에

pick = models.BooleanField()

# forms.py에서
class CommentForm(forms.ModelForm):
    PICK_A = False
    PICK_B = True
    PICKS = [
      (PICK_A, '왼쪽'),
      (PICK_B, '오른쪽'),
    ]

    pick = forms.ChoiceField(choices=PICKS)
    # -> 댓글에서 선택할 수 있게 함

# views.py의 detail에서
from Django.models import Q, Count

def detail(request, question_pk):
    # 계산이 필요한 것 : 1) 왼쪽을 선택한 댓글의 개수, 2) 오른쪽 댓글의 개수
    count_a = Count('comment', filter=Q(comment__pick=False))
    count_b = Count('comment', filter=Q(comment__pick=True))
    total_count = Count('comment')

    # ❗ POINT
    question = Question.objects.annotate(
        count_a=count_a,
        count_b=count_b,
        total_count=total_count,
    ).get(pk=question_pk) 
    # 질문 하나를 가져오면서, 질문 하나에 딸린 댓글 왼쪽댓 카운트, 오른쪽댓 카운트를 한꺼번에 가져옴

    # question.count_a    # a를 선택한 댓글의 개수
    # question.count_b

    if question.total_count == 0:
      a_per = 0
      b_per = 0
    else:
      a_per = round(question.count_a / question.total_count * 100, 2)
      b_per = round(question.count_b / question.total_count * 100, 2)

    context = {
      'a_per': a_per,
      'b_per': b_per,
    }
```