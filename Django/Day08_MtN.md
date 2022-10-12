# Many to Many Relationship

## Intro
1. 병원 시스템에서 핵심이 되는 모델? 의사와 환자
2. 둘의 관계를 어떻게 표현?
- 데이터 모델링 : 주어진 개념으로부터 논리적인 데이터 모델을 구성하는 작업
- 용어
  - target model : 관계 필드를 가지지 않은 모델
  - source model : 관계 필드를 가진 모델
  - ex. Comment-source 모델 → Article-target 모델
- 초기 모델의 문제
  - 동일한 환자인데도 다른 의사를 예약하기 위해 새로운 환자 객체를 생성해야 함
  - 외래 키 컬럼에 1, 2 형태로 참조하는 것은 불가능하다
- 해결
1. doctor, patient를 외래키로 가지는 예약 테이블을 따로 만들기
- 1번 의사가 오늘 본인에게 예약된 모든 환자를 조회하려면? `doctor1.reservation_set.all()`
  ```python
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

      def __str__(self):
          return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
  ```
2. `ManyToManyField()`을 통한 다대다 관계 테이블 만들기 : Doctor 또는 Patient 클래스에 해당 필드를 따로 만들어서 참조/역참조 방향만 고려해서 작성 → 중개 테이블을 자동으로 생성함
- 생성 `add()`
```
patient1.doctors.add(doctor1) : patient1이 예약할 의사 지정
doctor1.patient_set.add(patient2) : 역참조로(mtm필드가 Patient 클래스에 있기 때문) 관계가 맺어짐
```
- 삭제 `remove()` : 의사가 원하는 환자 예약을 취소할 수 있고, 환자도 원하는 의사 예약을 취소할 수 있음
```
doctor1.patient_set.remove(patient1)

patient2.doctors.remove(doctor1)
```
3. 중개 테이블에 추가 데이터가 있는 상황에서의 다대다 관계 연결
#### 'through' 인자
예약 생성할 때 reservation 중심으로 생성해야 했어서 불편했으나, through를 통해 reservation이 주체가 되지 않는 위와 같은 구조로 흐름을 유지할 수 있다.
- Rerservation 클래스 선언
```python
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```
- 쉘에서의 조작
```
patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
```

### SUMMARY
- M:N 관계로 맺어진 두 테이블에는 변화가 없다.
- Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관이 없고, 필드 작성 위치에 따라 참조와 역참조 방향을 주의하자.
- N:1은 완전한 종속의 관계였지만, M:N은 그렇지 않다.

### ManyToManyField(to, **options)
다대다 관계 설정 시 사용하는 모델 필드
- related manger
*add(), remove(), create(), clear(), set()* 등
- 인자
  - related_name
  - through
  - symmetrical : 재귀적(self)참조, ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용 → True면 데이터베이스에 1,2가 추가될 때 1, 2 / 2,1 두 줄이 함께 추가됨

- 메서드
  - add()
    - 지정된 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계라면 관계가 복제되지 않음
  - remove()
    - 관련 객체 집합에서 지정된 모델 대체를 제거

### 중개 테이블 필드 생성 규칙
1. 소스 및 대상 모델이 다른 경우
2. MtMField가 동일한 모델을 가리키는 경우

## Article과 User의 M:N 관계
### LIKE
- 역참조 매니저의 충돌 → M:N의 역참조를 바꿈
```
지금까지 쌓여있는 매니저

Article:User (N:1)
article.user
user.article_set

Article:User (M:N)
article.like_users
user.article_set => user.like_articles
```
1. 클래스에 like_users 추가
```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

2. likes 함수
좋아요 추가할지 취소할지 무슨 기준으로 if문을 작성할까? → 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
```python
if request.user in article.like_users.all():
```
- *exists()*
  - 쿼리셋에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환함, 큰 쿼리셋에 있는 특정 개체의 존재와 관련된 검색에 유용함
```python
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    # 좋아요 추가할지 취소할지 무슨 기준으로 if문을 작성할까?
    # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
    # article.like_users.filter(pk=request.user.pk)
    # if request.user in article.like_users.all():

    # 현재 게시글에 좋아요를 누른 유저 중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인
    if article.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소 (remove)
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가 (add)
        article.like_users.add(request.user)
    return redirect('articles:index')
```

## User와 User의 M:N 관계
### Profile
- path 작성 시 주의
<str:username>앞에 'profile/'을 제외하면 어떤 문제가 발생? 매칭을 찾을 때 위에서부터 찾는데 username이 문자열이라서 모든 문자열 url이 다 profile url로 가서 밑에 위치한 login, logout, ... 모두가 profile로 가버린다. → profile과 섞어 씀

#### view의 profile 함수
```python
def profile(request, username):    # username : 내가 확인할 프로필의 주인공
    User = get_user_model()        # 유저 모델은 직접 참조하지 않음
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

#### profile 템플릿
- username의 모든 댓글, 게시글, 좋아요한 게시글을 출력 → `{% for article in person.like_articles.all %}`
- index에서 다른 사용자 프로필에 접근하기 위하여 user.username(X), article.user.username(O)
  ```python
  <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
  ```

### Follow
#### 1. 모델 관계 설정
- user와 user 사이의 관계이므로 `'self'`를 인자로, symmetrical은 False
- 관계 이름은 followings, followers가 사용하기 용이함
```python
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, 
    related_name='followers')
```

#### 2. url 및 follow 함수
- user_pk는 follow하고자 하는 상대방의 pk값
```python
path('<int:user_pk>/follow/', views.follow, name='follow'),
.
.
.
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()

        # me = request.user로도 사용 가능
        you = User.objects.get(pk=user_pk)   # person은 상대방
        
        if request.user != you:
            # 내가(request.user) 그 사람의 팔로워 목록에 있다면
            # if you.followers.filter(pk=request.user.pk).exists():
            if request.user in you.followers.all():
                # 언팔로우
                you.followers.remove(request.user)
            else:
                # 팔로우
                you.followers.add(request.user)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```
ex. 해시태그 : MtMField! (해시태그 - 게시글)

아까 exists 관련해서 첨언하자면, Django의 쿼리셋은 lazy loading(지연 평가)를 기본적으로 따르는데요. 여기서 평가란 실제로 DB에 쿼리를 날리는 것을 말합니다.즉 Django는 ORM 명령을 실행했다고 해서 바로 쿼리를 날리지 않고 마지막 필요한 순간에 날리게 됩니다.

​if queryset 으로 T/F 판단을 할 때는 평가가 이루어져 DB에 쿼리를 날리게 됩니다.하지만 if queryset.exists() 로 T/F 판단을 할 때는 평가가 이루어지지 않고 쿼리셋이 존재하는지만 검사합니다.그래서 불필요하게 쿼리를 발생시키지 않고 T/F만 빠르게 검사할 수 있으므로 exists()가 웬만하면 더 빠릅니다.

​참고) https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.exists

### Extra
### Fixtures
프로젝트를 시작할 때, 모델에 초기 데이터를 제공하는 방법
- 프로젝트 협업 시 프로젝트의 앱을 처음 설정할 때 동일하게 준비된 데이터로 데이터베이스를 미리 채우는 것을 가능하게 함 → fixtures로 data와 구조를 공유!

- fixtures 생성 및 로드
생성(추출) : dumpdata
로드(불러오기) : loaddata
```
# 앞에서 나온 결과물을 json 파일을 만듦
$ python manage.py dumpdata [app_name[.ModelName]] > {filename}.json

# json 파일들을 불러옴
$ python manage.py loaddata articles.json comments.json users.json
```

### Improve Query
1. annotate
- `articles = Article.objects.annotate(Count('comment')).order_by('-pk')`
- 
2. select_related
- 1:1 또는 N:1 참조 관계에서 사용
- Article이 User를 참조해서 모든 Article을 출력하는 페이지의 경우
  - `articles = Article.objects.order_by('-pk')` → `articles = Article.objects.select_related('user').order_by('-pk')`로 수정
  - 게시물 가져오면서 참조하는 user의 유저아이디까지 한 번에 다 들고옴
  - 
3. prefetch
- `articles = Article.objects.prefetch_related('comment_set').order_by('-pk')`
- 게시글 가져오면서 댓글들을 한번에 가져오면서, 댓글의 유저까지 다같이 가져옴
```python
articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')
```
```
SELECT ••• FROM "articles_comment" INNER JOIN "accounts_user" ON ("articles_comment"."user_id" = "accounts_user"."id") WHERE "articles_comment"."article_id" IN ('10', '9', '8', '7', '6', '5', '4', '3', '2', '1') -> INNER JOIN과 IN을 통하여 구현됨
```


