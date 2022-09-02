### Index

1. Django Intro
2. Django 구조 이해하기
3. Django Quick start
4. Django Template
5. Sending and Retrieving form data
6. Django URLs

## Django

python으로 작성된 프레임 워크 - Flask, Django, Fast API

Django 공식문서가 되게 잘 되어 있음

웹 서비스는 클라이언트-서버 구조를 기반으로 동작

→ 클라이언트-서버 구조를 만드는 방법을 배우고자 Django는 서버를 구현하는 웹 프레임워크

웹 페이지

- 정적 페이지
    
    작성된 HTML 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습을 전달되는 페이지
    
    → 서버에 미리 저장된 HTML 파일 그대로 전달된 웹 페이지
    
- 동적 페이지
    
    사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
    
    사용자마다 보여지는 페이지가 다름 → 웹 페이지의 내용을  바꿔주는 주체 == 서버
    

# Django 구조 이해하기

## MTV Design Pattern

Model, Template, View

- MVC 디자인 패턴을 기반으로 조금 변형된 패턴 (Model - View - Controller) → 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
    - Model : 데이터와 관련된 로직을 관리
    - View : 레이아웃과 화면을 처리
    - Controller : 명령을 model과 view 부분으로 연결

1. 1️⃣ **Model**
    1. 데이터와 관련된 로직을 관리
    2. 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
2. 2️⃣ **Template**
    1. 레이아웃과 화면을 처리
    2. 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
3. 3️⃣ **View**
    1. Model & Template과 관련한 로직을 처리해서 응답을 반환
    2. 화면과 데이터를 연결하는 것이라 생각
    3. 클라이언트의 요청에 대해 처리를 분기하는 역할
    4. 동작 예시
        1. 데이터가 필요하다면 model에 접근해서 데이터를 가져옴
        2. 가져온 데이터를 template로 보내 화면을 구성
        3. 구성된 화면을 응답으로 만들어 클라이언트에게 반환

요청 보내면 url로 분기되고 view에서 요청에 맞는 화면 처리해서 그걸 사용자에게 응답…?

# Django Quick Start

가상환경 venv 사용

python 또는 Django가 폴더 or 프로젝트 별로 다른 모듈 등을 제어하기 위하여 global 공간이 아니라 별도의 공간이 필요할 때 가상환경 사용

### 1. 프로젝트 생성

1. 가상 환경 만들기
    
    $ python -m venv venv
    
2. 가상 환경 활성화
    
    $ source venv/Scripts/activate
    
3. 가상환경 비활성화
    
    $ deactivate
    
4. django 설치하기
    
    $ pip install django==3.2.13
    
5. 가상환경 패키지 목록 조회
    
    $ pip list
    
6. 패키지 목록 requirements.txt 생성
    
    $ pip freeze > requirements.txt 
    
    → (pip list로 조회했던 목록들이 저장됨) : 가상 환경 자체 폴더는 git에 올리지 않음. 너무 무겁기 때문. 따라서, 이를 ignore로 넣어주고 대신 requirements.txt를 git에 올려준다. 이는 가상 환경에 들어갈 패키지 목록들을 저장해두고 다른 local에서 쓸 때 설치해줄 수 있음
    
7. requirements.txt 목록 설치
    
    $ pip install -r requirements.txt 
    
    → 한번에 다 다운받기 위하여 해당 목록을 읽어오면서 다운
    
8. django 프로젝트 생성
    
    $ django-admin startproject firstpjt .
    
    → .을 붙이지 않으면 현재 폴더에서 생기는 것이 아니라, starproject라는 이름이 중첩돼서 생성됨
    
9. django 서버 실행
    
    $ python [manage.py](http://manage.py/) runserver
    

firstpjt 안에 articles(영화 정보, 영화 댓글, 리뷰 etc을 띄워주는 어플리케이션) + 또 다른 어플리케이션이 구성되어 있음

### 2. Django Application 생성

서버를 실행하고 (venv)를 띄우기 위하여 Ctrl + C

프로젝트 전체의 관리자 manage.py

1. django 애플리케이션 생성 (영어로 복수형으로 하는 게 관례)
    
    $ python [manage.py](http://manage.py/) startapp articles
    
2. INSTALLED_APPS에 앱을 등록
    
    [firstpjt] > [settings.py](http://settings.py) > INSTALLED_APPS 리스트 안에 만든 앱을 상단에 첫 번째로 기재
    
    - 주의사항 : 반드시 앱을 생성 후 해당 위치에 등록
    

### 3. 간단한 클라이언트-서버 동작 구축하기

[urls.py]

path에 있는 거 하나하나가 메뉴라고 생각! 메뉴를 하나 등록하는 과정이라고 이해

admin/이 붙어서 이 요청이 들어감. url patterns 리스트에 추가!

```python
path('index/', views.index), # index/로 요청을 하면 articles에 있는 views에 있는 index라는 함수를 실행
```

articles의 view.py에서 views를 가져옴

articles의 views를 가지고 오기 위하여 urls 상단에 import 시켜줌

```python
from articles import views
```

1. urls.py에 path 등록
    
    index함수 실행해달라고 하면 index 함수 실행되고 return하는 것은 [articles] > 의 index라는 template 파일에다가 render하겠습니다!
    
2. views.py에 함수 생성
3. template 생성
    
    내가 해당 html을 넣고자 하는 app안에 template를 생성하고 거기에 html들을 저장
    
    template 폴더 안에 index.html(사용자에게 응답) 생성하면 자동으로 Django html 언어로 인식함
    

**프로젝트 구조**

- __init__.py
- [asgi.py](http://asgi.py) : 추후 배포할 때 사용됨, 수많은 요청을 한꺼번에 처리하는 비동기 처리 관련
- [settings.py](http://settings.py) : 프로젝트 설정
- [urls.py](http://urls.py) : url로 들어오면 적절하게 꾸며줌
- [wsgi.py](http://wsgi.py) : 추후 배포시에 사용하며 어플리케이션이 웹서버와 소통하는 것을 도움
- [manage.py](http://manage.py) : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
    - python [manage.py](http://manage.py) …
    

**Django Application**

구조

- [models.py](http://models.py) : MTV 패턴의 M에 해당됨 (ex. 영화 정보 데이터들이 명시되어 있음)
- [views.py](http://views.py) : V에 해당

# Django Template

**What?**

데이터 표현을 제어하는 도구이자 표현에 관련된 로직

Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입

### DTL (Django Template Language)

- DTL Syntax
    1. Variable : render()의 세 번째 인자로 들어감
    
    ```
    <h1>Hi! I'm {{ name }}.</h1>
    ```
    
    1. Filters : 변수에 어떠한 추가적인 수정을 할 때 사용
    
    ```
    <p>제 이름의 길이는 {{ name|length }} 글자 입니다.</p>
    ```
    
    1. Tags :  반복, 조건 등 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
    
    ```
    {% for food in foods %}
      {% if food|length > 6 %}
        <p>{{ food }}</p>
      {% endif %}
    {% endfor %}
    ```
    
    c.f. 더 많은 Tags - Django Template Tag documentation ([https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-tag-reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-tag-reference)) 
    
    1. Comments : 주석 넣고 싶을 때 사용
    
    ```html
    {# <p>이것은 주석입니다.</p> #}
    
    {% comment %} ## Ctrl + /
    <p>이것은 여러줄 주석입니다1.</p>
    <p>이것은 여러줄 주석입니다2.</p> 
    {% endcomment %}
    ```
    

[urls] → [views] → [해당 html]

request, 어디로 보낼 건데?, 뭘 보낼 거야?(데이터 ex. 딕셔너리 타입 등)

서버에서 주는 대로 페이지에 보이는 값이 동적으로 조작할 수 있구나

```
{% for food in foods %}
  <p>{{ food }}</p>
{% endfor %}
```

로직이 views.py에서 만든 다음에 보내줄래, 아님 raw 데이터를 template에서 손 볼래? 고민하게 됨

디자인 패턴에서는 약속으로 정해놓은 게 MTV 각각의 역할이 있기 때문에, 역할이 구분되어 있어서 더 효율적 웬만하면 views에서 데이터 처리를 모두 해서 만들어주고 넘겨주는 게 좋다!

- Django의 설계철학 : 모든 로직은 views.py에서 손 보고, 그 결과를 template에 넘겨주자
- View와 Django가 서로 소통 가능하다

### 템플릿 상속 (Template Inheritance)

base.html을 상속 받아서 block 안에는 유동적으로 내용을 갈아끼울 수 있도록 함

- extends, block 개념 등장!
- 아래의 코드는 base.html을 상속받을 html 파일의 상단에 위치

```html
{% extends 'base.html' %} !-- 가장 상단에 두어야 함 --!
```

```html
{% block content %}
  <h1>nice to meet you!</h1>
{% endblock content %}
```

→ base.html에 block content를 넣어둠, 상속받은 페이지에는 위와 같이 block안에 어떤 요소를 넣을지 선언

→ base.html을 만들고 상속을 받아서 이용하면 홈페이지의 메뉴바와 같이 어떤 페이지를 들어가도 똑같은 형식, 공통적인 부분이고 바뀌지 않는 부분을 수정하고 싶을 때 모든 페이지를 할 필요 없이, 하나에만 수정해서 유지보수가 용이하다. → 코드의 재사용성

< 추가 템플릿 경로 추가하기 >

만약 articles가 다수일 때도 base.html을 상속 받아 쓰려면?

- Django의 템플릿은 app/templates를 기본적으로 어떤 앱이 있으면 template 내부에 있겠구나 인식하는데, 어플리케이션의 templates 말고도 내가 만든 templates도 여기에 html 파일이 있다고 인식해달라고 해준 것

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
```

- 이 코드가 쓰인 파일(settings.py)의 절대 경로를 의미

```
BASE_DIR = Path(__file__).resolve().parent.parent
```

# Form data

client → server로 요청을 보낼 때, url로 보낼 수 있지만, 데이터를 담아서 그걸 요청을 보낼 경우가 있음 (ex. 로그인시 아이디, 비밀번호 담아서 요청!)

그 데이터를 어디에 담느냐? Form!

Form의 2가지 요소

- action : 어디에 요청할지, 전송할지 입력! URL
- method : 어떻게 전송할지 입력!
    
    c.f. HTTP Method -  GET / POST 2가지 방식
    
    : 클라이언트 - 서버 간의 주고 받는 메세지의 규약과 같은 것이 프로토콜이 있는데 이것에 따라 이때 뭘 요청을 할 것인가에 대한 것 → HTTP 메서드 존재! ex. GET(조회), POST(생성), PUT(변경), DELETE(삭제)
    

### GET

데이터는 URL에 포함되어 보내짐

사용자가 서버에 데이터를 넘기는 방법 중 하나

- GET 메서드 사용 시

?message = ‘안녕하세요’ → key = value

< 실습 >

```html
<!-- throw.html --!>

{% extends 'base.html' %}

{% block content %}
  <h1>Throw</h1>
  <form action="/catch/" method="GET">
    <label for="message">던져</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
{% endblock content %}
```

```html
<!-- catch.html --!>

{% extends 'base.html' %}

{% block content %}
  <h1>Catch</h1>
  <h2>여기서 데이터를 받았습니다!</h2>
  <a href="/throw/">다시 던지러 가자.</a>
{% endblock content %}
```

![0830_!.PNG](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/308cb318-eea1-40b1-9589-ae2696a1d3f1/0830_!.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/49c7b57d-31be-460e-b081-a45baf90f551/Untitled.png)

현재 throw 페이지는 정적 페이지! → 동적으로 만들어주려면?

```python
print(request.GET) ## Dictionary 통해 가져옴
print(request.GET.get('message')) ## hello --> 이걸 context 변수에 넣어서 동적으로 만들자
```

```python
def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    context = {
        'message': request.GET.get('message')
    }
    return render(request, 'catch.html', context)
```

```python
# views.py

def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    department = request.GET.get('department')
    name = request.GET.get('name')

    if department == '대전 2반':
        if name == '김도언':
            message = '교육생이시군요!'
        else:
            message = '교수님이시군요!'
    else:
        message = '다른 반이시군요!'
    
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)
```

→ request 객체를 통해 어떻게 form 데이터를 가져올 수 있는가를 배움!

Views.py에 로직이 쓰임

# Django URLs

웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함

/ 잘 쓰자!

# Variable Routing

URL의 일부를 변수로 쓸 수 있도록 하여, 매번 URL의 주소와 그 urls, views, 변수명.html 을 매번 생성할 필요 없이 type을 지정하고 변수명을 넣어 URL 일부를 매번 바꿔가면서 동적으로 줄 수 있다.

```python
# urls.py
path('show/<str:name>/', views.show) # <type:변수명>

# views.py
def show(request, name):
    context = {
        'name': name
    }
    return render(request, 'show.html', context)

# show.html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ name }}</h1>
{% endblock content %}
```

# App URL mapping

앱이 많아졌을 때 앱 하위의 urls들이 존재하는데 이때 url들을 분화할 수 있다!

- project의 urls는 articles/ pages/로 해주고 각자 a와 p의 urls에서 index/ greeting/ … 등을 만들어준다
- 

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('articles.urls')),
    # path('index/', views.index),
    # path('greeting/', views.greeting),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('show/<str:name>/', views.show)
]
```

# Naming URL patterns

url에 네임을 지정해서 매번 url 개수마다 html 파일들에 하나씩 다 수정해줄 필요 X