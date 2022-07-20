# 함수

- for what? 
  - 분해 : 기능을 분해하고, 재사용 가능하게 만들고
  - 추상화 : 복잡한 내용을 모르더라도 사용할 수 있도록, 재사용성과 가독성, 생산성을 위하며 내부 구조를 변경할 게 아니라면 몰라도 무방

- 함수의 종류
  - 내장 함수
    - 파이썬에 기본적으로 포함된 함수
  - 외장 함수
    - import문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
  - 사용자 정의 함수
    - 사용자가 직접 만드는 함수

- 함수의 정의
  특정한 기능을 하는 코드의 조각(묶음), 함수 안에도 저장과 처리가 담김

- 함수 기본 구조
  - 선언 / 호출 (define & call)
  - 입력(Input)
  - 문서화(Docstring) : ex. sum이 뭐하는 건지 설명
  - 범위(Scope)
  - 결과값(Output)

  ```
  def function_name (parameter)
      Docstring 
      # code block
      ...
      return returning_value
  ```

## 함수의 결과값(Output)

  - Void function
    - 명시적인 return 값이 없는 경우, None 반환 후 종료
    - ex. print() : 값을 출력만 하고 결과물이 남진 않음
  - Value returning function
    - 함수 실행 후, return하게 되면 값 반한 후 바로 종료

  - 두 개 이상의 return 반환 -> Tuple 활용 (+ 다른 컨테이너도 가능)
  ```
  def minus_and_product(x, y):
      return x - y, x * y
      !!!!덜 적음!!!!
  ```
  ```
  # 회문으로 이뤄진 리스트 만들기

  word_list = ['우영우', '파이썬']
  def is_palindrome(word_list):
      palindrome_list = []
      for word in word_list:
          if word == word[::-1]:
              palindrome_list.append(word)
      return palindrome_list
  print(is_palindrome(word_list))
  ```

## 함수의 입력(Input)
### Parameter와 Argument
- parmater : 함수를 정의할 때, 함수 내부에서만 사용되는 변수
- argument : 함수를 호출할 때, 실제로 넣어주는 값
  - 함수의 parameter를 통해 전달되는 값
  - function_name(argument)
    - 필수 argument : 반드시 전달되어야 하는 argument
    - 선택 argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달
  
  - Positional Arguments : 기본적으로 함수 호출 시 위치에 따라 argument가 함수 내에 전달됨
  - Keyword Arguments : 직접 변수의 이름으로 특정 argument를 전달함
    - ex. def add(x, y): 에 add(x = 2, y = 5)를 써줌
    - 주의사항 : Keyword A 다음에 Positional A를 활용할 수 없음 (ex. add(x = 2, 5)는 error 발생)
  - Default Arguments Values : 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함, 정의된 것보다 적은 개수의 argument들로 호출될 수 있음

### 정해지지 않은 여러 개의 Argument 처리
print는 막 argument 줘도 괜찮음 -> 애스터리스크 or 언패킹 (연산자라고 불리는 * 덕분)

- 가변 인자(*args) : 여러 개의 Positional Argument를 합쳐준다???
- (*) 이해하기 위한 개념
  - 패킹 : 여러 개의 데이터를 묶어서 변수에 할당
    - 함수의 argument로 넣으면 언패킹
      ```
      numbers = (1, 2, 3, 4, 5)
      ```
  - 언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당
    - 함수에서 받는 parameter에 * 넣으면 어떤 argument를 받든 패킹해서 튜플 형태로 들어가서 사용할 수 있음
  
      ```
      numbers = (1, 2, 3, 4, 5)
      a, b, c, d, e = numbers
      ```
  - 활용 
    - 언패킹시 변수의 개수와 할당하고자 하는 요소 갯수 동일해야 함
    - 언패킹 시 왼쪽의 변수에 asterisk(*) 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음
        ```
        numbers = (1, ,2 ,3 ,4, 5)

        a, *rest, e = numbers
        print(rest) # [2, 3, 4]
        ```
- 애스터리스크(*)와 가변 인자
  - (*)는 주로 튜플이나 리스트를 언패킹하는데 사용
  - (*)를 활용하여 가변 인자를 만들 수 있음
- 반드시 받아야 하는 인자와, 추가적인 인자를 구분해서 사용 가능
  ```
  def print_family_name(father, mother, *pets):
      print(f'아버지 : {father}')
      print(f'아버지 : {father}')

      print('반려동물들...')
      for name in pets:
          print(f'반려동물: {name}')
  print_family_name('아빠, '엄마', '멍멍이', '냥이') #pets는 아무것도 안 넣어도 됨
    ```

- 가변 키워드 인자(**kwargs)
  - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
  - 딕셔너리로 묶여 처리됨
    ```
    def family(**kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)
    family(father= '아빠', ...) ## 주의사항 : father는 문자열로 쓰지 않고 변수처럼 씀
    ```
  - 가변 인자와 가변 키워드 인자를 함께 사용할 수 있음

## Python의 범위 (Scope)
범위 = 공간이라고 이해  
함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope. 함수 내부에서만 참조가능
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수

### 변수 수명주기
변수는 각자의 수명주기가 존재
- built-in scope
  - 파이썬이 실행된 이후부터 영원히 유지
- global scope
  - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
- local scope
  - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

```
def func():
    a = 20
    print('local', a) # a는 local 변수, 여기까지 실행되면 함수 끝나는 순간 a는 없어짐 (특정 scope에만 살아있음)
func()
print('global', a) #a는 사라졌기 때문에 error 발생
```
- 이름 검색 규칙(Name Resolution)  
파이썬에서 사용되는 이름(식별자)들은 이름공간에 저장되어 있음
  - LEGB Rule
    - Local > Enclosed > Global > Built-in 순서로 이름을 찾아나감
    - 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 불가함

- global문 : local scope에서 global 변수 값의 변경 가능
  - global 키워드 사용하지 않으면, local scope에 a 변수가 밖에 있는 거랑 따로 생성됨
  - 파라미터에 global을 쓸 수 없음
  - 출력 등은 아무 문제 없는데 내부에서 외부의 a를 변경하고 싶을 때 사용(local에서 맨 바깥을 global을 바꾸고 싶을 때)
- nonlocal vs global
  - nonlocal은 미리 쓸 것을 선언해놔야 함 (중첩 함수를 감싸고 있는 다른 함수에서의 값을 바꾸고 싶을 때, local에서 global이 아니라 enclosed을 바꾸고 싶을 때)

- 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라짐

## 함수 응용
```
map(fucntion, iterable(자료구조))
```
```
filter(function, iterable)
```
  - 각각 요소마다 함수 적용시켜서 이 함수에 해당하는 것만 걸러서 새로운 리스트를 만들고 싶을 때 사용
```
zip(*iterables)
```
  - 복수의 iterable을 모아 튜플을 원소로 하는 zip object 반환, 리스트가 두 개 있으면 다른 리스트끼리 세로로 묶을 수 있음
  - 알고리즘할 때 n차원 배열 시 쓰일 수 있음
```
lambda [parameter] : 표현식(return문)
```
  - 한 줄짜리 return 값 받아올 때 def 선언 대신 이름 지정할 필요 없이 사용 (익명 함수)

### 재귀 함수(recursive function)
- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용 (ex. 점화식)
- 예시 : 팩토리얼
```
def factorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4)) # 24
```
```
# 반복문으로도 구현 가능
def fact(n):
    result = 1
    while n > 1:
    !!!!!!! 덜함!!!!!!!
```
- 주의사항 : base case에 도달할 때까지 함수를 호출함, 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨, 파이썬에서는 최대 재귀 깊이가 1,000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생
- 반복문 vs 재귀 함수
  - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우에 재귀함수 사용
  - 재귀 호출은 변수 사용을 줄여줄 수 있음
  - 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림


## 모듈과 패키지
- 모듈 : 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 거
- 패키지 : 특정 기능과 관련된 여러 모듈의 집합
```
import module
from module import var, function, Class
from module import *

from package import module
from package.module import var, function, Class
```
- 라이브러리(library) : 다양한 패키지를 하나의 묶음으로
  - 파이썬 표준 라이브러리
  - 라이브러리 vs 프레임워크 : 삽과 포크레인과 같은 개념
- pip : 파이썬 패키지 관리자, 외부 개발자들이 만든 것들 설치
- 가상환경 : 패키지의 활용 공간 (django에서 쓰임)

#### 사용자 모듈과 패키지
- vscode로 calculator 기능 구현해보기

#### 가상환경
파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트의 버전이 상이할 때 가상환경을 만들어 프로젝트별로 
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상 환경(패키지 집합 폴더)을 만들 수 있음
