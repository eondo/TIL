### Intro
- 디버깅
- 에러와 예외
- 예외 처리
- 예외 발생 시키기

### 디버깅
잘못된 프로그램을 수정한는 것

- 에러 메시지가 발생하는 경우
  - 해당하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
  - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
    - 전체 코드를 살펴봄
    - 휴식을 가져봄
    - 누군가에게 설명해봄
- 오류가 많이 나는 곳
  - 제어가 되는 시점 : 조건/반복, 함수

### 에러와 예외
- 문법 에러(Syntax Error)
  - Invalid syntax
  - assign to literal 
    - sum = 5 해서 sum() 함수 작동 안 하는 경우
  - EOL : 괄호 안 닫은 경우
  - EOF
- 예외(Exception)
  : 문장이 표현식이 문법적으로 올바르더라도 발생하는 에러
  모든 내장 예외는 Exception Class를 상속받아 이뤄짐
  사용자 정의 예외를 만들어 관리할 수 있음
  - NameError : namespace 상에 이름이 없는 경우
  - TypeError
  - IndexError
  - KeyError
  - ModuleNotFoundError

### 예외 처리
- 작성 방법
- try문 반드시 한 개 이상
```
try:
    num = input('숫자입력 :')
    print(num)
```
- 에러 메시지 처리 (as)
  - as 키워드를 활용하여 원본 에러 메시지를 사용할 수 있음
- 복수의 예외 처리 실습
100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성하기
- 발생 가능한 에러는? 1) 나누기 0, 문자열 입력, 
```
num = input()
print(100/int(num))

try:
    num = input()
    100/int(num)
except (ValueError, ZeroDivisonError):
    print('제대로 입력해줘.')
```
- 순차적으로 수행됨으로 가장 작은 범주부터 예외 처리를 해야함
- 예외 처리 종합
  - try : 코드를 실행함
  - except : try문에서 예외가 발생 시 실행함
  - else : try문에섯 예외가 발생하지 않으면 실행함
  - finally : 오류가 뜨든 안 뜨든 무조건 실행???
```
# 파일을 열고 읽는 코드를 작성하는 실습

```
- try,except vs if문