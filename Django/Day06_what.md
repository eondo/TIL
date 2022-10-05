# DB의 N : 1 관계
#### INDEX
- A many-to-one relationship
- N:1 (Article-Article)
- N:1 (Article-User)
- N:1 (Article-User)

__RDB의 특징__ : RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성 가짐, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계(테이블 간의 논리적인 연결)를 만드는 데 사용할 수 있음
- 주문 테이블에 + 고객 ID 컬럼(FK) → 고객 테이블(고객 id(PK))

#### RDB에서의 관계
1. 1:1
2. N:1 (다대일 관계) : 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
  - 주문(N) - 고객(1)

### Foriegn Key
외래 키 : 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행의 식별할 수 있는 키
- 참조하는 테이블에서 1개의 키에 해당하고, 참조되는 테이블의 기본키(PK)를 가리킴 (중복일 수 없음)

- 특징
  - 키를 사용하여 부모 테이블의 유일한 값을 참조 (by 참조 무결성 → 외래 키가 선언된 테이블의 외래 키 속성의 값은 그 테이블의 부모가 되는 테이블의 기본키 값으로 존재해야 함, 두 테이블 간의 일관성 유지 필요)
  - 외래키의 값은 일반적으로 부모 테이블의 PK 이용 (반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함)

## Comment(N)-Article(1) N:1 관계
Comment(N) - Article(1)
- 0개 이상의 댓글은 1개의 게시글에 작성될 수 있음

- Comment의 스키마
|id|
content
created_at
updated_at
Article의 id (FK)

- DB에서 테이블 작성할 때 필요했던 스키마 models.py 타입(모델 필드) / 제약조건(모델 필드에 적힌 옵션들(max_length 등))

## Django Relationshp Fields
Djagno Relationshp fields 종류
1. OneToOneField()
2. ForeignKey()
3. ManyToManyKey()

🧷 Comment 모델 정의
- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 위치함
- 인스턴스 이름은 참조하는 클래스의 단수형으로 적는 것을 권장함 → __article_id__ 자동적으로 컬럼 이름으로 생성되기 때문
```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

#### *ForeignKey(to, on_delete, options)*
- Django 모델에서 관계형 DB에서 외래 키 속성을 담당
- 필수 위치 인자(2가지)
  - 참조하는 model class
  - on_delete 옵션

#### *on_delete*
- 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지를 정의
- 데이터 무결성을 위해서 중요한 설정
- 옵션 값
 - CASCADE : 부모 객체(참조 된 객체 Article)가 삭제 됐을 때, 이를 참조하는 객체도 삭제함
 - 외에도 PROJECT, SET_NULL, SET_DEFAULT...

__[참고]__ 데이터 무결성
- 데이터의 정확성이나 일관성을 유지하고 보증하는 것
- 데이터베이스나 RDBMS의 중요한 기능
- 무결성 제한의 유형
  - 개체 무결성
  - 참조 무결성
  - 범위 무결성

Comment 객체에 article_id가 NULL로 들어가는 것 해결하기
```
In [6]: comment.article = article
In [9]: comment = Comment(content='second comment', article=a 
```

## 관계 모델 참조
N(FK) ↔ 1 : 1쪽에서는 N을 참조할 수 있는 정보가 없음! 어떻게 해결? Related manager!

#### Related manager
- N:1, M:N 관계에서 사용 가능한 문맥
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 **역참조**할 때에 사용할 수 있는 manager 생성
- 역참조 : 외래키를 가지고 있지 않은 1이 나를 참조하는 테이블(나를 외래 키로 지정한 N)을 참조하는 것 (ex. Article이 Comment를 참조하는 것) → __comment_set__
  - Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저
  - *article.comment_set.method()*
  - 반대 참조 상황인(Comment → Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능
```python
In [14]: article.comment_set.all()
Out[14]: <QuerySet [<Comment: first comment>, <Comment: second comment>]>
```
- view함수, template에서 응용 가능
```python
In [15]: comments = article.comment_set.all()

In [16]: for comment in comments:
    ...:     print(comment.content)
    ...: 
first comment
second comment
```

### Comment 구현
#### ✅ Comment 생성
댓글 작성하려면 댓글 작성 Form이 있어야 하므로 Form에 CommentForm() 클래스 생성, views.detail에 CommentForm 입력창을 context로 넘김, detail.html에서 form 출력!

- 문제 : detail 페이지에 출력되는 CommentForm에서 Article로 직접 게시글 번호를 선택하는 창이 함께 출력됨 → Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요하기 때문
- 원하는 것 : 해당 게시글에 댓글을 작성하면 자연스럽게 그 게시글에 댓글이 작성되어야 함

__< 해결 >__
1. urls에 comment_create path 작성
2. views에 comment_create 함수 작성
3. detail의 {{ comment_form }}가 든 form 태그의 action을 'articles:comments_create'로 해줌

❗ 외래 키 필드는 사용자의 입력으로 받는 것이 아니라, view 함수 내에서 받아 별도로 처리되어 저장되어야 함! → forms.py에서 Meta 클래스에 exclude로 처리
❓ 그렇다면 출력에서 제외된 외래키 데이터는 어디서 받아와야 할까?
  - detail 페이지의 주소에 variable 원리를 생각하면 routing처럼 사용자는 내용을 쓰기만 하면 되고, 저장될 때 보이지 않는 view함수에서 이 게시글을 pk를 저장해서 같이 넘기면 됨!
```python
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```
🚫 발생하는 에러! article_id 외래키값이 NULL *(NOT NULL constraint failed: articles_comment.article_id)*
- article.pk는 넣은 적이 없으니까, 근데 이게 들어갈 틈이 없다!
- comment.article = article로 넣어주기 위해선 comment 인스턴스가 필요하다 
- 그리고 넣을 거면 is_valid 통과한 다음에 넣어야 함, 사용자 내용만 검증하면 됨 사용자가 입력한 게 아니라 pk로 받아오니까!
- save 메서드가 한 가지 타이밍을 줌
- 잠시 save 안 하고, 저장되기 전에 comment 인스턴스에 추가적으로 넣을 값, 커스텀할 게 있다면 그걸 위해 인스턴스는 리턴해줌
- commit=False → commit을 꺼두면 저장만 안 할 뿐, save 됐을 때 나올 결과물을 인스턴스로 리턴은 해줌

- SUMMARY
  - 외래키가 있는 상황에서의 view 함수 : 1. 사용자로부터 입력 받지 않고, url의 variable routing을 통해 조회해서 그 객체를 준비하고, 2. 타이밍을 만들기 위해 commit옵션은 오프하고 저장만 안 하고 리턴만 받고, 3. 받은 comment를 작성한다
  - c.f. CommentForm에서 제외된 'article'은 valid에서 취급하지 않음, 사용자의 요청을 검증하는 작업이기 때문에!

#### ✅ Comment 조회
1. Related manager 사용
특정 게시물의 detail 페이지에서 등록된 comments를 출력하기 위해 views 함수에서 context로 넘겨줘야 함 → 역참조! *comments = article.comment_set.all()* 사용
2. detail.html에 comments 출력
```python
@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

#### ✅ Comment 삭제
1. comments_delete 함수
```python
# views.py
# def comments_delete(request, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     article_pk = comment.article.pk
#     comment.delete()
#     return redirect('articles:detail', article_pk)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

```python
# detail.html
<h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      </li>
    {% endfor %}
  </ul>
```
#### Comment 추가 사항

## Article(N)-User(1) N:1 관계
0개 이상의 게시물 - 1개의 회원
### Referencing the User mdoel
Django에서 User 모델을 참조하는 방법
1. *settings.AUTH_USER_MODEL*
- 반환 값(문자열)을 모델 필드에서 유저 모델을 참조할 때 사용
2. *get_user_model()*
- 반환값(객체) : models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용

```python
from django.conf import settings

# Article 모델에 User 모델을 참조하는 외래 키 작성
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```
❓ why : 유저 객체를 만들기 전에, models.py가 먼저 실행되기 때문에 여기서 get_user_model()을 써버리면, 여기서 호출은 했는데 장고 프로젝트 안에서 유저가 생성되지 않는 문제 생성 순서 타이밍 문제 -> 임시로 문자열로 일단 대체해두고 로딩 끝나고 유저 객체 생성되고 나면 그때 다시 참조할 수 있도록 하기 위해서!\
so! models.py에서만 *setting.AUTH_USER_MODEL*을 씀!

#### CREATE
인증된 회원의 게시물 작성
- 외래 키 데이터 누락 → article.user = request.user 사용
```python
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```
#### DELETE
남의 글을 삭제하면 안 됨(이제 누가 어떤 글을 썼는지 정보가 들어있기 때문에) 현재 삭제 요청 사람과 게시글을 작성한 사람을 비교하여 일치한다면 삭제할 수 있도록 함
```python
if request.user == article.user:
    article.delete()
    return redirect('articles:index')
```

#### UPDATE
수정을 요청하는 사람과 작성한 사람을 비교하여 본인의 글만 수정할 수 있도록 해야 함
- 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼 출력하지 않도록 함 
  - articles/detail.html의 버튼 태그들 바깥에 위와 동일한 조건문 사용

#### READ
작성자도 함께 출력 가능함
```
<p><b>작성자 : {{ article.user }}</b></p>
```

## Comment(N)-User(1) N:1 관계
- Comment와 User간 모델 관계 설정
  - Comment에 'User의 id(FK)' 추가됨
  - 몇번 게시글에 달린 건지, 누가 쓴 건지 2가지의 정보가 2개의 FK로 들고있음

#### CREATE
1. forms에 exclude 추가, 2. 외래 키 데이터 누락을 해결하기 위해 views에서 save 전 request.user 지정해서 작성자 정보가 함께 저장되도록 함

#### READ
누가 댓글을 썼는지 작성자 출력 → {{ comment.user }} 이용

#### DELETE
이 댓글을 작성한 사람만 지울 수 있게 함

[참고] 인증된 사용자에 대한 접근 제한하기


### SUMMARY
- 다대일 관계
  - Foreign Key
  - Django Relationship fields
    - 외래키를 django에서는 어떤 field를 쓰느냐
  - Related manager : 역참조 시에 발생하는 매니저
- 다대일 모델 관계 설정
  - 1. Comment-Article
  - 2. Article-User
    - 유저모델 참조 : models.py에서는 유저 모델을 settings.AUTH_USER_MODEL를 쓰는 점 기억하기
  - 3. Comment-User

#### EXTRA [참고] 
import문에 대한 스타일 가이드

