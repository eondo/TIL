#### INDEX
- Django Form
- Django ModelForm
- Handling HTTP requests
- View decorators

## Django Form
지금까지 사용자로부터 데이터를 받아온 방식 : HTML의 form, input 태그

→ 현재 우리 Django 서버는 들어오는 요청을 모두 수용하고 있기 때문에 입력한 데이터가 우리가 원하는 데이터 형식이 맞는지에 대한 유효성 검증이 반드시 필요!

즉, 사용자가 보내는 데이터에 대한 유효성 검증을 용이하게 하는 도구가 Form

- Form에 대한 Django의 역할 : Form과 관련한 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공하는 프레임워크

#### Django가 처리하는 Form에 관련한 세 작업

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

→ 기존 input으로 받던 걸 Form으로 받는 작업 처리!

### Django Form Class

### 1. Form Class 선언
- Model과 마찬가지로 상속을 통해 선언함 (forms 라이브러리의 Form 클래스를 상속받음)
```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
```
- new.html의 block content 파트
→ NOW 사용자 입력을 받는 4줄(label, input으로 이뤄진 4줄)이 작성해서 받는 것 대신, view 함수에서 정의한 ArticleForm의 인스턴스 {{ form }}만 그 자리에 넣어줌으로써 label 태그, 태그의 속성 값, label의 for 등 모든 게 다 자동으로 채워짐
→ Why? forms.py의 코드가 모두 이를 생성시켜준 것!

- Form 이용 시 전과 다른 점 : textarea로 받기로 한 게 적용이 안 되고 그냥 input 태그임, 그룹간 띄어쓰기가 안 되어있음
  - 두 번째 문제의 해결
    ```
    {{ form.as_p }}
    # 의미 : 각각의 줄을 p 태그로 감싸겠다
    ```
    **From rendering options**
    1. as_p() : 주로 사용, 각 필드가 단락(<p>태그)로 감싸짐
    2. as_ul()
    3. as_table()
  - 첫 번째 문제의 해결 → NEXT


### Django의 2가지 HTML input 요소 표현

1. Form fields
    1. 입력에 대한 유효성 검사 로직을 처리
    2. 템플릿에서 직접 사용됨
2. Widgets
    1. 웹 페이지의 HTML input 요소 렌더링을 담당
       - input 요소의 단순한 출력 부분을 담당
    2. Widgets은 반드시 form fields 안에 할당됨
    
    → new.html의 {{}}에는 줄마다의 특성을 줄 수 없기 때문에 당연히! forms.py에서 바꿔야 함을 알 수 있음
    

### Widgets
Django의 HTML의 input element의 표현을 담당\
단순히 HTML 렌더링을 처리하는 것이며 유효성 검증과 관계 없음

[practice] 나라 선택을 choice필드로 받아서 출력하기
```python
class ArticleForm(forms.Form):
    NATION_A = 'kr'
    NATION_B = 'ch'
    NATION_C = 'jp'
    NATIONS_CHOICES = [
        (NATION_A, '한국'),
        (NATION_B, '중국'),
        (NATION_C, '일본'),
    ]

    title = forms.CharField(mex_length=10)
    content = forms.CharField(widget=forms.Textarea())
    nation = forms.ChoiceField(choices=NATIONS_CHOICES)
```

## Django ModelForm
사용자 input을 받는 필드가 많아지면 models.py에도 forms.py에도 써야 하고, 너무 많아질 수 있는 문제 발생! 
- 만약 사용자 입력이 model 필드와 동일한 필드를 받을 거라면, 그런 form으로 맵핑을 시키고 싶다면? → Model을 기반으로한 form, **ModelForm**

**ModelForm Class**
Form class를 만들 수 있는 helper class

### ModelForm 선언

forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음

정의한 ModelForm

-

```python
class ArticleForm(forms.ModelForm):

    class Meta:
        model = 어떤 모델을 기반으로 할지
        fields = 모델 필드 중 어떤 것을 출력할지
```

```python
model = Article # 호출해서 인스턴스 값 할당하는 게 아니라 클래스 참조값 자체를 사용, 등록
        # 리스트 or 튜플로 작성
        # fields = ('title', 'content')
        fields = '__all__'
```

→ ModelForm은 Model에 대한 정보를 인지하고 있고, models.py에 적혀진 title, content의 필드가 다르기 때문에 알아서 해당 필드에 맞게 바꿔준다! 그래서 아까 만든 Form은 모델과 아무런 관련이 없기 때문에 별도로 widget 설정을 따로 해줘야 했는데 ModelForm은 그럴 필요가 없다! 모델과 아주 밀접한 관련 O

### ModelForm에서의 Meta Class

- ModelForm의 정보를 작성하는 곳
- ModelForm의 사용할 경우 참조할 모델이 있어야 하는데, ~
- 엇’
- fields 속성에 ‘__all__’를 사용하여 사용자로부터 입력받아야 하는 모델의 모든 필드를 포함할 수 있고, exclude 속성 사용시 특정값은 제외할 수 있음

[참고 사항들]

- Meta data
    - 데이터를 표현하기 위한 데이터
    - ex. 사진 파일에 사진 데이터의 데이터(촬영 시각, 렌즈, 조리개 값 등)가 존재하고 이를 부가적인 데이터로서 meta data라고 불림
    - ArticleForm(데이터)에 대한 meta(데이터)를 작성한다는 의미로 Class Meta 이름 사용
- 참조 값과 반환 값
    - 호출하지 않고 이름만 작성하는 방식은 어떤 의미를 가지는가?
        
        → 함수를 이름만 출력하는 경우는 반환값이 아니라, 참조값을 반환함
        
        → 호출했을 때는 반환값을 출력함
        
        → 즉, model = Article에서는 인스턴스 만든 게 아니라 이 클래스 값 자체가 들어간 것인데, 이러한 참조 값은 다른 함수에서 “필요한 시점”에 호출하는 경우에 사용 가능함. 즉, ArticleForm이 해당 클래스를 필요한 시점에 사용하기 위함!
        
- 주의사항
    - Class 안에 Class는 ModelForm이 가지는 설계 자체이기 때문에 실제로 문법적으로 파고들지 말자

## ModelForm with view functions

#### ‘is_valid()’ method

유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

#### ‘save()’ method

- form 인스턴스에 바인딩(데이터가 들어가다)된
- 키워드 인자 instance를 제공하는데, 얘를 통해서 생성할지 수정할지 결정함. 즉, instance가 있으면 수정, 없으면 생성
    - 제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦(CREATE)
    - 제공되면 save()는 해당 인스턴스를 수정(UPDATE)
    

IS_VALID를 통과못하면 forms.errors에 왜 못 통과했는지 이유를 적어서 딕셔너리 형태로 저장됨 

### UPDATE

ModelForm의 인자 instance는 수정 대상이 되는 객체를 지정

1. *request.POST*
2. *instance*

#### Form vs ModelForm

- 공통점 : 사용자 요청을 처리한다!
- 각자 역할이 다르다
- 사용자 요청을 → 무조건 저장할지, 또는 저장하지 않고 인증 처리로 등 다른 곳에서 데이터로서 그냥 쓸지 요구가 다를 수 있음. 즉, 후자의 경우에는 ModelForm이 필요하지 않음
- Form
    - 사용자로부터 받는 데이터가 DB와 연관되어 있지 않는 경우에 사용
    - DB에 영향을 미치지 않고 단순 데이터만 사용되는 경우
    - ex. 로그인 - 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음 → model에 종속되지 않음, 묶이지 않음
- ModelForm
    - 사용자로부터 받는 데이터가 DB와 연관되어 있는 경우에 사용
    - 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할지 이미 알고 있기 때문에 곧바로 save() 호출이 가능
    

# Widgets 활용하기

그저 출력되는 input의 형식을 바꾼다

위잿을 작성하는 2가지 방법

위젯을 적용할 필드에 form필드를 적용하는 법이 권장됨

- form필드에 종속된 형태로 작성됨
- 

title 안에 label, widget 들어가고 widget 안에 attr 들어감

attr라는 키워드 인자에 딕셔너리 형태로 넣음

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
            }
        )
    )
```

```python
'maxlength': 10, # 유효성 검사의 역할을 하는가? NO 사용자의 입력을 10개까지만 입력하도록 태그에서 막는 거지, Django와는 관련 없음, 저장할 때는 상관 없고 입력할 때 막는 것
```

{{ forms.as_p }} 로 원래라면 한 줄마다 조정할 수 있던 걸 어느정도 제한이 있고 자율성이 줄어든 상태이지만 Django에서 별도로 따로 떼서 관리할 수 있는 기능을 제공함

→

### Rendering fields manually

공식문서의 django form 검색해서 Django Documentation 참고!

working with form templates의 rendering~ 

수동으로 form을 작성 가능하다

- bootstrap을 입힐 수도 있음~ 1. form control forms.py에 가서 widget의 class에 form control 추가
1. 외부 라이브러리를 설치 django-bootstrap-v5

# Handling HTTP requests

개요

HTTP requests 처리에 따른 view 함수 구조 변화

new-create, edit-update의 공통점 ,하나의 차이점

공통 : 공동의 목적 create, update로직이라는 공동의 목적을 가짐

차이점 : new, edit은 GET 요청에 대한 처리만 진행하고, create와 update는 POST 요청에 대한 처리만을 진행한다. → 즉, new-create가 edit-update가 합쳐질 것 이다! view함수의 구조가 바뀔 것!

→ 안에서 method별로 분기를 두는 방식으로 합쳐도 되겠다~ 같은 주소를 두가지 메서드로 다룰 수 있게 됐다!

- why? POST 확인을 왜 먼저 할까? 사실 else는 GET 말고 다른 메서드들도 존재한다!
    
    즉, if에 POST를 먼저 보는 이유가 POST가 아니면 DB 관련 코드를 동작시킬 필요 없으니까 아래로 떨어뜨림
    

코드 작성 순서

```python
def create(request):
    if request.method == 'POST':
        pass
    else:
        ''' 이 부분 먼저 쓰고 create 페이지 보고, create페이지에서 입력해서, 이 위에서 처리
```

# View decorators

함수의 기능을 덧붙여주는 것이었음

데코레이터란?

- 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수
- Django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공함

### Allowed HTTP methods

def index에 요청이 들어오는데 index는 메서드 안 보지? 자기한테 맞는 url 요청만 오면 페이지를 그냥 보여줌. 실제로 서비스할 땐 이러면 안 됨. HTTP 메서드들 중 어떤 메서드만 허용? index 하는 일 : 전체 글 조회, 페이지 주기

→ GET 메서드에만 올바르게 동작해야 함. URL이 맞더라도 거절해야 맞음

이때 사용하는 메서드 목록 → 알아서 cut해줌405 응답 등 적절한 응답 코드를 보내줌

1. require_safe

#### overall

- Django Form Class + ModelForm
- view 함수 구조 변화
    - HTTP requests 처리에 따른 구조 변화 → view 함수, url 하나로 줄어듦