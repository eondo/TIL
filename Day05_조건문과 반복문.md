### Introduction
- 제어문 (Control Statment)  
특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 코드가 필요함
  - 조건문
  - 반복문

## 조건문

## 복수 조건문
- 복수의 조건식을 활용할 경우, elif를 활용하여 표현함
- 조건식을 동시에 검사하는 것(X) 순차적으로 비교(O)
  
  ```
  dust = int(input())
  if dust > 150:
      print('매우 나쁨')
  elif dust > 80:
      print('나쁨')
      ...
  else:
      print('좋음')
  ```
  - else문은 위의 모든 조건에서 다 False인 경우에 실행하고 싶은 코드가 있다면 넣음 (필수 X)

## 중첩 조건문
조건문 안에다 또 조건문을 넣는 것 (ex. 상의가 빨간색인데, 모자도 빨간색인 경우)
- [조건] and [조건] 으로 연산자도 넣을 수 있음

### 조건 표현식
- 조건 표현식(Conditional Expression)을 일반적으로 조건에 따라 값을 정할 때 활용
- 삼항 연산자(Ternary Operator)로 부르기도 함
  ```
  'true인 경우 값' if '조건' esle 'false인 경우 값'
  ```
- 절댓값을 저장하기 위한 코드
  ```
  value = num if num >= 0 else -num
  ```
  ```
  ## 삼항 연산자로 바꾸기

  num = 2
  if num % 2? :
      result = '홀수입니다.'
  else:
      result = '짝수입니다.'

  # 삼항 연산자
  result = '홀수입니다.' if num % 2 == 1 else result = '짝수입니다.'
  ```

## 반복문
특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
- 종류
  - while 문
    - 종료 조건에 해당하는 코드를 통해 반복문을 종료시킴
  - for 문
    - 반복가능한 객체를 모두 순회하면 종료 (별도의 종료 조건이 필요 없음)
    - 일반적으로 횟수에 따라 반복하고 싶을 때 사용
  - 반복 제어
    - break, continue, for-else
    - ex. 쿠키가 죽을 때까지 달리는데 특정 아이템 같은 거 먹으면 별을 만나면 break하고 우주로 감, 특정 상황에 따라서 반복문을 멈출 때 사용

## while문
조건식이 참인 경우 반복적으로 코드를 실행
- 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
- while문은 무한 루프를 하지 않도록 '종료 조건'이 반드시 필요
```
a = 0
while a < 5: ## 종료 조건
    print(a)
    a += 1 ## 이게 없으면 무한 루프
print('끝')
```
- 복합 연산자(In-Place Operator)
  - 복합 연산자는 연산과 할당을 합쳐 놓은 것 (ex. a += 1)

## for문
시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회
```
for 변수명 in iterable한 자료형:
```
- Iterable
  - 순회할 수 있는 자료형 (string, list, dict, tuple, tuple, range, set 등)
  - 순회형 함수 (range, enumerate)
  
- 딕셔너리 순회 : 기본적으로 key 순회, dict[key]로 값까지 순회 가능
  - 추가 메서드를 활용한 딕셔너리 순회
    - key() : key로 구성된 결과
    - values() : value로 구성된 결과
    - items() : (key, value)의 튜플로 구성된 결과
    ```
    grades = {'john':80, 'eric':90}
    for student, grade in grades.items():
        print(student, grade)

    ## john 80
    ## eric 90
    ```

- emumerate 순회  
  인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환, (index, value) 형태의 tuple로 구성된 열거 객체를 반환
    - print(list(enumerate(members))) # [(0, '민수'), ...]
    - for i, v enumerate a
      - print(f"{i}번째 데이터는 {v}입니다")

- (*중요) List Comprehension
  - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
  - [code for 변수 in interable]
    - [1, 2, 3, 4]를 모두 * 2 한 리스트 만들 때 많이 씀
  ```
  # 1~3의 세제곱 리스트 만들기
  cubic_list = []
  for number in range(1, 4):
      cubic_list.append(number ** 3)
  print(cubic_list)

  # 동일
  cubic_list = [number ** 3 for number in range(1, 4)]
  ```
  ```
  a = []
  for i in range(5):
      if i % 2 ==1:
          a.append(i)

  # 동일
  a = [i for i in range(5) if i % 2 ==1]
  ```
  ```
  odd_ports = []
  for i, v in enumerate(ports):
      if (i + 1) % 2 ==1:
          odd_ports.append(v)
  
  # list comprehension 사용
  odd_ports = [v for i, v in enumerate(ports) if (i + 1) % 2 == 1]
  ```

- Dictionary Comprehension
  ```
  cubic_dict = {}

  for number in range(1, 4):
      cubic_dict[number] = number ** 3 ## cubic_dict[1(키)] = 1(밸류)
  print(cubic_dict)
  ## {1: 1, 2: 8, 3: 27}

  cubic_dict = {number: number ** 3 for number in range(1, 4)}
  print(cubic_dict)
  ```

## 반복문 제어
- break : 반복문을 종료
  
- continue : continue 이후의 코드 블록은 수행하지 않고(스킵, 건너뛰기), 다음 반복을 수행
  - continue를 만나면 그 위 조건문으로 다시 돌아가기 때문에 continue 위에 a += 1를 넘어야 if 조건문 아래 코드로 넘어갈 수 있음
  
- for-else : 끝까지 반복문을 실행한 이후에 끝나고 else문 실행 (do while?)
  - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음
  - for의 반복문을 정상적으로 끝내면 else문 실행됨
  - 알고리즘 풀 때 좋음 : 중첩 for문에서 나올 때 유용  
  
- pass : 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)
  - if문에서 뭔가 해야 하는데 일단 나중에 채우기 위해서 pass를 넣는 것이며 아예 아무것도 안 함