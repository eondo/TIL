# 사용자 인증 시스템

### INDEX
- The Django authentication system
- HTTP Cookies
- Authentication in Web Systems
- Authentication with User
- Limiting access to logged-in users
<br>
<br>

## The Django authentication system
인증 시스템 : 인증(Authentication)과 권한(Authorization) 부여를 함께 제공하는 기능
- 필수 구성은 settings.py에 이미 포함되어 있음 (settings.py의 INSTALLED_APPS에서 확인 가능)
- __Authentication(인증)__ → ❗ 여기에 집중
    - 신원 확인
    - 사용자가 자신이 누구인지 확인하는 것
  
- Authorization(권한, 허가)
    - 권한 부여
    - 인증된 사용자가 수행할 수 있는 작업을 결정
    - Django가 가지는 것 : admin / staff / 일반사용자

- 인증 관련된 앱 → __accounts__ : 회원, 인증, etc.
- 주의 사항 : 인증시스템에 관련된 앱의 이름은 __accounts__ 로 정의 - 추후에 추가 설정을 해야 할 경우를 방지

settings.py은 global_settings.py를 받아서 덮어씌운 것이기 때문에 AUTH_USER_MODEL이 보이지 않아도 이미 존재하는 것이다. 이 값을 프로젝트를 시작할 때 다른 유저 모델을 가리킬 수 있도록 바꿔야 한다. 즉, 만든 accounts 앱에 대체된 유저 모델로 설정값을 바꿔주고 시작해야 한다.
<br>
<br>

## Substituting a custom User model
Custom User Model로 대체하기

❓ 기본 User Model을 Custom User model로 대체하는 이유\
  → 작성하는 일부 프로젝트에서는 django에서 제공하는 built-in User model의 기본 인증 요구사항이 적절하지 않을 수 있고, 기존 User model 수정은 어려운 작업임

  → 커스텀한 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우, 나중에 맞춤 설정할 수 있기 때문 (주의 : User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함)

### Custom User model로 대체하는 방법 (*주의)
#### 1. AbstractUser를 상속받는 커스텀 User 클래스 작성
#### 2. auth.User였던 값을 우리가 만든 유저 클래스로 프로젝트의 기본 user 모델을 바꿈 
- 지금 우리의 기본 유저 모델은 이거야, 말해주는 작업
#### 3. admin.py에 커스텀 User 모델을 등록
- accounts의 admin.py에 추가적으로 import하고, 등록하는 작업

[참고] User 모델 상속 관계
class User의 기능은 부모인 class AbstractUser가 모두 가지고 있음.
[참고] "관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스" 
Abstract base classes(추상 기본 클래스)란? - 본래 클래스가 존재하면 테이블로 만들어질 수 있는데, Abstract bae classes는 데이터베이스 테이블을 만드는 데 사용되지 않고, 다른 클래스를 만들 때 핵심적인 기능들을 제공만 하기 위함.
[*주의] 프로젝트 중간에 AUTH_USER_MODEL 변경하기
- 변경사항이 과거에 만들어놨던 테이블 관계들이 자동으로 변경될 수 없기 때문에 직접 수정이 어렵기 때문에 중간 변경은 권장하지 않고 프로젝트 처음에 진행해야 함!

### 🧷 데이터베이스 초기화
(프로젝트 중간인 경우)
- 수업 진행을 위한 데이터베이스 초기화 후 마이그레이션
#### 1. migrations 파일 삭제
#### 2. db.sqlite3 삭제
#### 3. 새로 migration 진행
-> [accounts]
accounts에 새로 만들어진 설계도를 확인해보면, 필드가 굉장히 많고, 결국 이 필드들은 AbstractUser의 정보들인 것이다. 
-> 이제 auth_user가 아니라 accounts_user로 대체되어 있는 것을 database에도 확인할 수 있음.

### User 모델을 꼭 대체해야 하는 이유?
기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있다는 강점 존재!

### HTTP Cookies
로그인, 로그아웃을 이해하기 전에 학습해야 할 내용이다.

#### HTTP
- HTML 문서와 같은 리소스(데이터)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
- 클라이언트-서버 프로토콜이라고도 부름

#### 요청과 응답
- 요청
  - 클라이언드(브라우저)에 의해 전송되는 메시지
- 응답
  - 서버에서 응답으로 전송되는 메시지

#### HTTP 특징
1) 비 연결 지향 : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
   -> 그렇다면 로그인한 페이지에서 벗어나면 로그인이 풀려야 하는데 그렇지 않음. 즉, 비 연결 지향임에도 불구하고 상태를 유지시켜주는 것이 Cookie!
2) 무상태 : 그렇기 때문에, 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음. 즉, 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

결론 : 서버와 클라이언트 간 지속적인 상태 유지를 위해 "쿠키"와 "세션"이 존재

#### 쿠키(Cookie)
HTTP 쿠키는 상태가 있는 세션을 만들도록 해 줌
쿠키 안에 상태를 유지시켜주는 역할의 쿠키를 세션(세션 쿠키)이라고 함
- 서버가 사용자의 웹 브라우저에 전송하여 설치되는 작은 기록 정보 파일
  - 브라우저는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  - 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 매번 저장된 쿠키를 함께 전송
  - ex. 쿠키 : '나 로그인된 사용자야!'라는 데이터가 담겨있기 때문에 로그인 상태가 유지됨
### 사용 목적
#### 1. 세션 관리 🔥 오늘의 핵심
- 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
  - 매 요청마다 내 장바구니에 이것들이 담겨져 있어! 데이터를 전송하기 때문에 장바구니는 페이지를 옮겨도 비워지지 않음
  - [개발자 도구] > [Network]탭의 [Cookies]탭에서 확인 가능
  - [Application] > Storage-[Cookies]에서 브라우저에 저장된 쿠키 삭제 가능
#### 2. 개인화
#### 3. 트래킹

### 세션
사이트와 특정 브라우저 사이의 상태를 유지시키는 것
클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키 안에 저장 -> 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
1. Session cookie
  현재 세션이 종료되면 삭제됨
  브라우저 종료와 함께 세션이 삭제됨
2. Persistent cookies
  지정된 날짜나 기간이 정해짐

### Django에서의 Session
Django는 database-backed sessions 저장 방식을 기본 값으로 사용하며 Django DB의 django_session 테이블에 저장함
첫번째 칸 KEY만 클라이언트에 브라우저에 주고, 실제 사용자에 대한 데이터는 2번째 컬럼은 서버에 들고 있겠다, 키만 다음 요청마다 보내면 됨. 중간에 확인하고 분석, 응답 등 session 메커니즘은 Django가 알아서 해줌

# Authentication in Web requests (요청에 대한 인증을 진행해보자)
🔥 Django가 제공하는 인증 관련 built-in forms 익히기
- 이전 학습에서 Form, ModelForm을 배우면서 직접 ArticleForm을 만들었지만 "인증"은 직접 form을 구현하기 어렵기 때문에 기본 built-in-forms를 제공함

# 📌 Login
그 상태를 유지시키기 위한 Session을 Create하는 과정
```
1. admin 계정을 하나 만듦
```
## AuthenticationForm
: 로그인을 위한 built-in-form
**login(request, user)**

- 로그인도 사실 2가지 처리가 필요함 (페이지, 인증)
- 페이지는 GET, 인증은 POST로 new-create, edit-update 구조처럼 메서드로 분화해서 한 번에 처리할 수 있음
<과정>
  1. 로그인을 진행할 페이지를 보여줄 view 함수 필요하니까
  2. accounts앱의 url에서 path('login/', views.login, name='login'), 작성
  3. view에서 login 함수 작성
    - 로그인을 하기 위한 페이지가 리턴되는 것이 필요함(GET에 대한 처리) + 로그인을 실제 진행하기 위한 인증 과정이 필요(POST에 대한 처리) -> 메서드로 분화해서 한 번에 처리할 수 있음

  4. def login의 else:부분을 먼저 작성
    ```python
    else:# 로그인할 form 보여줌
          form = AuthenticationForm()
      # 이 form을 페이지에 렌더링해야 함
      context = {
          'form': form,
      }
      return render(request, 'accounts/login.html', context)
    ```
  5. templates/accounts에서 login.html을 작성
    ```html
    {% extends 'base.html' %}

    {% block content %}
      <h1>LOGIN</h1>
      <!--여기에 이제 Authentication form 써야 하니까-->
      <form action="{% url 'accounts:login' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
    {% endblock content %}
    ```
  6. [view]에서 login 함수의 실제 로그인을 시켜주는 파트 작성
  ```python
  from django.shortcuts import render, redirect
  from django.contrib.auth.forms import AuthenticationForm
  from django.contrib.auth import login as auth_login # 실제 세션 데이터를 만들어주는 함수 import

  # Create your views here.
  def login(request):
      if request.method == 'POST': # 사람을 실제 로그인을 시켜주는 파트
          form = AuthenticationForm(request, request.POST)
          # form = AuthenticationForm(request, data=request.POST)
          if form.is_valid():
              # 실제 로그인이 이뤄짐 (주의:save가 아님, 세션을 만듦)
              auth_login(request, form.get_user()) # 이 인증된 유저 정보를 어디서 들고올 것인가?
              return redirect('articles:index')

      else:# 로그인할 form 보여줌
          form = AuthenticationForm()
      # 이 form을 페이지에 렌더링해야 함
      context = {
          'form': form,
      }
      return render(request, 'accounts/login.html', context)
  ```

### 실습 중 설명
AuthenticationForm은 모델폼일 필요가 없음. DB에 username과 password를 저장하려는 게 아니라 인증 과정에서 쓰일 뿐이니까 모델폼이 아니라 폼으로 만들어짐

### def login 코드 외 설명 - get_user()
❓ auth_login(request, 유저정보) -> 이때 이 인증된 유저 정보를 어디서 들고올 것인가?
request.POST에 사용자 정보 들어있을 거니까 form이라는 인스턴스에 유저 정보가 들어있을 것이다.
```
form.get_user()

AuthenticationForm의 인스턴스 메서드로,
유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
```

입력된 데이터를 판단해서 현재 세션에 데이터를 입력하는 과정이 필요함 : 이 과정을 login이라고 함
- 첫 번째 인자 HttpRequest(요청 객체)와 두번째 인자 User 객체가 필요함
- django가 session_id가 있으면 로그인 됐음을 알 수 있음 -> Value가 key 실제 암호화된 데이터는 django가 들고 있기 때문에 django_session 열어보면 session_key와 브라우저의 value가 같음을 알 수 있음. -> 세션 잘 만들어지고 session_key 잘 발급 받은 거면 잘 로그인 됐다고 볼 수 있음

❓ 세션 데이터는 DB에 저장하는데, 그럼 모든 쿠키 데이터를 서버에 저장하면 안되나? 왜 어떤 건 브라우저에 저장하고, 어떤 건 서버에 해?
-> 과부화 방지를 위해 서버가 관리해야 하는 대상이 아니라면 브라우저가 저장하게 위탁하기 때문, 어떤 것을 서버에, 어떤 것을 브라우저에 관리할지 결정하는 것도 현업에 중요

- 템플릿에서 인증 관련 데이터를 출력하는 방법
### 현재 로그인 되어있는 유저 정보 출력하기
❓ 로그인하면 됐다고 인증에 관련한 데이터를 출력하는 방법 -> base.html에서 {{ user }} 사용
❓ 어떻게 base.html에 context를 받아오지 않고도 {{ user }}이 출력되는가?
-> 'django.contrib.auth.context_processors.auth'가 로드되고 있어서 모든 template에서 user 객체를 출력할 수 있음

#### context processors
- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
(*주의) 따라서, 실제로 context를 사용할 때 view에서 context로 key값이 'user'인 것을 넣으면 안 됨!

- 로그인 하지 않은 경우는 anonymous 유저로 출력됨
- django는 유저를 나타내는 2가지 클래스(User : 인증된 사용자, AnonymousUser : 인증되지 않은 유저)가 존재


# 📌 Logout
로그아웃은 Session을 Delete하는 과정(O) 유저 데이터를 삭제하는 것 (X)
서버와 브라우저 양쪽에서 모두 Session을 지워줌
- 로그아웃 함수를 지원해줌
**logout(request)**
- HttpRequest 객체를 인자로 받고 반환값이 없음
- 처리하는 일 2가지
  - 현재 요청에 대한 session data를 DB에서 삭제
  - 클라이언트의 쿠키에서도 sessionid를 삭제
    - __why?__ 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위해 2가지를 모두 진행

### logout 로직 작성
1. def logout 작성하고 
2. 로그아웃 버튼 만들려가자
3. 로그아웃 누르면 이제 username이 상단에 뜨던 게 anonymous user로 바뀜


# Authentication with User
본격적으로 user와 상호작용해보자 (아직 user model을 제대로 안 쓰고 있었음)
\
회원 가입, 탈퇴, 정보 수정, 비밀번호 변경 

# 📌회원 가입
User을 CREATE하는 것으로 UserCreationForm을 사용
- UserCreationForm
  - 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm (createsuperuser로 만들어진 회원이 아닌 일반 회원)
  - 가지는 필드 3가지
    - username (from the user model)
    - password1
    - password2

<과정>
1. url 작성
2. 회원가입도 사실 2개의 view함수가 필요함을 인지 (회원가입 페이지를 렌더링할 뷰함수 1개 + 그 페이지에서 입력한 걸 받아서 저장을 할 뷰함수 1개) -> create랑 똑같음! 
3. view에서 usercreationform 만듦
4. signup하기 편하게 가는 링크 위에 만들어주고
5. 이제 view함수에 pass해놨던 부분 채우러 간다
6. 다 하고 이제 signup하면 에러 발생
   -> __why?__ UserCreationForm은 ModelForm이라서 class meta로 어떤 model이 등록되어 있을 텐데 기본 유저로 만들어진 modelform이야. 프로젝트에서 사용할 기본 user를 대체를 했지만 내부 form들을 코드는 바꾸지 않았기 때문에... 우리가 쓰는 accounts.User가 될리가 없다. 그래서 usercreationform을 그대로 못 써!\
   -> __solution!__ 상속의 개념 이용. UserCreationForm 그대로 상속받아서 이름 바꾸고, class Meta의 model만 우리가 쓰는 유저로 덮어쓰자. 그리고 커스텀한 그걸로 form 만들 때 쓰는 클래스를 바꿔줌 걔로.
7. UserCreationForm 바꾸러 가자 forms.py 파일 생성할 때 get_user_model을 import해서 CustomUserCreationForm 클래스를 정의한다.
8. ...

# Custom user & Built-in auth forms
### 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms
1. UserCreationForm
2. UserChangeForm

- get_user_model()
  - 현재 프로젝트에서 활성화된 사용자 모델을 반환\
🚫 오류 발생
forms.py에서 runserver할 시에 
AttributeError: 'function' object has no attribute '_meta'
-> 해결 : get_user_model()에 괄호를 안 붙여줘서 ...

- 근데 admin 할 때처럼 email도 보이게 나오게 하고 싶은데? -> password1, password2는 저장을 위한 데이터가 아니라 인증 수단으로 쓰고 있는 중. user에 등록돼서 출력되는 건 username 밖에 없으니까 더 받고 싶은 필드를 재정의로 추가
- 그렇다면 user가 가지는 컬럼은 뭐가 있는지 확인하는 방법 : 유저 설계도의 필드 확인, db에서 확인, 공식문서에서 django user object 검색

❓ 회원가입하면 자동으로 로그인 상태로 만들어주고 싶다면?
-> sign up 뷰함수를 건드려야 함


# 📌회원 탈퇴
: DB에서 유저를 Delete하는 것

<로직 작성 과정>
1. path 작성
2. 유저데이터.delete() 해서 삭제하면 되는데 이때 유저데이터는 어딨을까? -> request -> 그래서 request.user까지 유저 객체
3. 삭제하려면 이제 삭제를 요청할 폼이 필요하겠지? > base.html에서 form에서 회원탈퇴 버튼 만듦
  [참고] 탈퇴하면서 세션 데이터는 남아있음! 이것까지 없애려면?
  로그아웃 시키고 탈퇴를 시키는 걸 view함수에 구현하기?
  ```python
  auth_logout(request.user)
  request.user.delete() # 근데 이러면 logout했으니까 request.user.delete할 때 request.user를 받아낼 수 없음
  ```
<br>
<br>

# 📌회원 정보 변경
사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
- UserChangeForm은 instance인자로 기존 user 데이터 정보를 받는 구조 동일함

<과정>
1. url 작성

- UserChangeForm 사용 시 문제점
문제 : 일반사용자한테 너무 많은 권한을 오픈함 기본적으로 UserChangeForm이 admin 페이지에서 쓰는 것이기 때문에! -> 서브 클래스 CustomUserChangeFormm에서 전에 회원가입할 때 email 컬럼 추가한 것처럼 반대로 여기는 출력될 것을 따로 선택해주기! 
-> *참고 : 비밀번호를 변경을 해주는 form은 따로 있음, 별도의 클래스가 있음
<br>
<br>

# 📌비밀번호 변경
PasswordChangenForm 사용

🚫user 인자를 필수적으로 넣어줘야 함 -> request.user

- 암호 변경 시 로그아웃이 됨 -> 즉, 세션에서 무언가 변화가 생겼다는 뜻
- 암호 변경 시 세션 무효화 방지하기
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하게 되지 않아 세션이
  - -> 해결 : update_session_auth_hash()
  - 새로운 password의 session data로 session을 업데이트함
  - 유저 정보 받아오는 인자는 어떻게 표현?
    - save 호출하고 return값으로 써도 되고, user = form.save() / user로 넣거나 그냥 인자 자리에 바로 form.user로 써도 됨
<br>
<br>

### 대주제 마지막! Limiting access to logged-in users
로그인된 사용자냐 아니냐에 따라 로직을 다듬는 과정
로그인 사용자에 대한 접근 제한하기 -> ex. 로그인 페이지, 회원가입 페이지 등
- 접근을 제한하는 2가지 방법
1. **is_authenticated** attribute
2. **login_required** decorator

#### is_authenticated
사용자가 인증되었는지 여부를 알 수 있음 -> 모든 User 인스턴스에 대해 항상 True, AnonymousUser에 대해서는 항상 False
- request.user에서 이 속성을 사용 __(request.user.is_authenticated)__
- 권한과는 관련이 없고, 로그인/비로그인 사용자인지만 확인하기 위한 속성

<과정>
1. base.html 수정
2. 근데 이건 출력만 안 보이게 해놓은 거고, 주소를 통한다면 갈 수 있음
```python
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
```
3. 비로그인 사용자는 create 못하게 하고 싶음
4. 로그인 된 사용자만 CUD를 할 수있도록 하기 -> articles의 view함수로 이동 -> decorator주기 -> create하려고 하면 login하라는 창으로 돌아감
   1. 이상한 점
      1. 우리 login 주소를 어떻게 알았을까? -> django도 모르는데 accounts/login/으로 기본 설정 주소로 이게 내부적으로 기본 설정 주소인데 우린 마친 accounts를 쓰고 있으니까 효율적
      2. next parameter 보통 검색할 때 출력되는데 뒤에 뭔가 붙어있음 -> 
      ?next=/articles/create/ : 직전에 요청했던 주소임! django는 로그인에 성공하면 여길 들어가겠다 싶어서 남겨준 것.
        근데 안 가줌 -> why? login.html에 보면 action주소에 보면 accounts:login으로 요청을 보내고, 여기엔 next는 없기 때문에...

- 정리하자면 "next" query string parameter
  - return redirect(request.GET.get('next) or 'articles:index')
  - login 템플릿에서 form action이 작성되어 있다면 동작하지 않음
<br>
<br>

### 두 데코레이터로 인해 발생하는 구조적 문제
1. 비로그인 상태롤 detail 페이지에서 
delete는 POST만 처리할 수 있는데 지금 next는 GET으로 보내고 있으니까 여기서 안 됨 -> 안에서 처리하도록 변경
즉, @login_required는 GET request method를 처리할 수 있는 view 함수에서만 사용해야 함
```python
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')
```



