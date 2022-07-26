c.f. 숫자가 넘어갔을 때 어떻게 할 것인가 Z -> A로 어떻게?
나머지 연산자 이용!
>>> 꺽새 나오면 exit()으로 빠져나오면 됨
자료구조를 활용하는 방법을 배워보도록 하자 (활용을 메서드를 통해 할 것)


### 데이터 구조 활용
데이터 구조를 활용하기 위해서는 메서드(method)를 활용
- 메서드는 클래스 내부에 정의한 함수로 함수와 동일
- 객체의 기능 (추후 객체 지향 프로그래밍에서 학습)
- 활용 형태 : 데이터 구조.메서드() (ex. List.append(10))
  ```  
  # 원하는 횟수만큼 바꾸는 메서드
  str.replace(old, new[, count])
  ## old, new는 필수 인자 / [,count]는 선택적 인자
  ```
## 순서가 있는 데이터 구조
### 문자열
문자들의 나열로서 모든 문자는 str 타입(변경 불가능한 immutable)
- 문자열 조회/탐색 및 검증 메서드
  - s.find(x) : x의 첫 번째 위치를 반환, 없으면 -1 반환
  - s.index(x) : x의 첫 번째 위치를 반환, 없으면 오류 발생
  - s.isalpha() : 알파벳 문자 여부 *단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)
  - s.isupper() : 대문자 여부
  - s.islower() : 소문자 여부
  - s.istitle() : 타이틀 형식 여부

- .find(x) / .index(x)
  ```
  print('apple'.find('p')) # 1
  print('apple'.find('c')) # -1
  ```
- isalpha() : 숫자냐, 알파벳이냐 검증

- 문자열 관련 검증 메서드 (엄격<)
  - idecimal() : 숫자인지 확인
  - .isdigit() : 소수점 있는 것까지 판단 가능
  - .isnumeric() : 숫자스러운 것까지 True
  
- 문자열 변경 메서드
  - s.replace(old, new[, count]) : 바꿀 대상 글자를 count번만 새로운 글자로 바꿔서 반환 / vs .sort() : 문자열은 immmutable이니까 repalce해도 후에 원본을 print하면 원본이 유지된다
  - s.strip([chars]) : 공백이나 특정 문자를 제거 / stirp, lstrip, rstrip
  - s.split(sep = None, maxsplit = -1) : 공백이나 특정 문자를 기준으로 분리해서 리스트로 만들어짐
    - sep이 None이면 연속된 공백문자를 단일한 공백문자로 간주, 
  - 'separator'.join([iterable]) : 구분자로 iterable 합침
    - 예시 추가하기!
  - s.capitalize() : 가장 첫 번째 글자를 대문자로 변경
  - s.swapcase : 대<->소문자 변경
  - 추가

### 리스트
- 리스트 메서드
  - L.append(x) : 리스트 마지막에 항목 x 추가
  - L.insert(i, x) : 리스트 인덱스 i에 항목 x 삽입
  - L.remove(x) : 리스트 가장 왼쪽에 있는 항목 x를 제거, 없으면 ValueError
  - L.pop() : 리스트의 가장 오른쪽에 있는 항목을 반환 후 제거
  - L.pop(i) : 리스트의 인덱스 i에 있는 항목을 제거 후 항목을 반환
  - L.extend(m) : 순회형 m의 모든 항목들을 리스트 끝에 추가함 (+= 기능)
  - L.index(x, start, end)
  - L.reverse() : 원본 리스트를 뒤집기, None 반환
  - L.sort() : 원본 리스트를 정렬, None 반환 / vs sorted(numbers) : 원본은 그대로 두고 복사해서 새로운 것을 만듦
  - L.count(x)
  
  ### 튜플
  - 확장연산자?
  - 멤버십 연산자
    - in을 통해 요소가 속해있는지 확인
    ```
    print('apple' in 'a')
    ```
  - 반복연산자 : 시퀀스를 반복
  - 
## 비시퀀스형 데이터 구조
### 셋(Set)
- 셋 메서드
  - s.copy() : 셋의 얕은 복사본을 반환
  - s.add(x) : 항목 x가 셋 s에 없다면 추가
  - s.pop() : 셋 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거, set이 비어있을 경우 KeyError
    - 순서가 보장되지 않기 때문에 랜덤으로 삭제 및 반환됨
  - s.remove(x) : 항목 x를 셋 s에서 삭제, 항목이 존재하지 않을 경우 KeyError
  - s.discard(x) : 항목 x가 셋 s에 있는 경우 항목 x를 셋에서 삭제, Error가 나지 않음
  - s.update(t) : 셋 t에 잇는모든 항목 중 셋 s에 없는 항목을 추가
  - s.clear() : 모든 항목 제거
  - s.isdisjoint(t) : 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않는 경우 True 반환(서로소)
  - s.issubset(t) : 셋 s가 셋 t의 하위 셋인 경우 True 반환
  - s.issuperset(t) : 셋 s가 셋 t의 상위 셋인 경우 True 반환

### 딕셔너리
- 딕셔너리 메서드
  - d.clear()
  - d.copy()
  - d.keys() / 기본적으로 딕셔너리를 순회할 땐 key를 순회함
  - d.values()
  - d.items()
  - d.get(k) : 키 k의 값을 반환하는데, 키 k가 딕셔너리에 없을 경우 None을 반환 / vs my_dict['pineapple']으로 값에 접근하면 KeyError 발생
  - d.get(k, v) : 키 k의 값을 반환하는데, 키 k가 딕셔너리에 없을 경우 v를 반환
  - d.pop(key[, default]) : key가 딕셔너리에 있으면 제거하고 해당 값을 반환, default값이 없으면 KeyError
  - d.update() : 값을 제공하는 key, value로 덮어씀, key는 문자열이 아니라 '' 뗀 key값으로 넣음

## 얕은 복사와 깊은 복사
- 복사 방법
  - 할당 (Assignment)
  - 얕은 복사 (Shallow copy)
  - 깊은 복사 (Deep copy)

### 할당
대입 연산자(=)
- 대입 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사함
- original list랑 copy list는 주소를 공유하기 때문에 주소를 복사해서 쓴다고 이해

### 얕은 복사와 깊은 복사
slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사 (다른 주소)
mutable과 immutable에 대한 이해 필요
```
a = "hello"
a += "python"
print(a) ## "hellopython" 이지만 이걸로 바뀐 것은 아니다

```
```
a = [1, 2, 3]
b = a[:] ## 내용물 복사해옴 (1차원에서만 가능)
print(a, b) ## [1, 2, 3] [1, 2, 3]
b[0] =5
print(a, b) ## [1, 2, 3] [5, 2, 3]
```
- 주의사항 : 복사하는 리스트의 원소가 주소를 참조하는 경우, 2차원 리스트의 경우
  - [1, 2, ['a', 'b']]를 복사하면 리스트 안의 리스트는 그대로 주소만 복사해오기 때문에 리스트 안의 리스트는 동시에 값 수정됨
  - 해결책 -> 깊은 복사, deepcopy 함수 이용
  ```
  import copy
  a = [1, 2, ['a', 'b']]
  b = copy.deepcopy(a)
  print(a, b)
  b[2][0] = 0
  print(a, b) ## [1, 2, ['a', 'b']] [1, 2, [0, 'b']]
  ```
1) 할당
```
a = [1, 2, 3]
b = a
print(a, b) ## [1, 2, 3] [1, 2, 3]
b[0] = 4
print(a, b) ## [4, 2, 3] [4, 2, 3]

# String의 경우
a = "hello"
b = a
a += "Python"
print(a, b) ## helloPython hello

## 왜 얜 다를까? 문자열은 더해질 때 새롭게 만든다 because immutable
```
2) 얕은 복사
```
a = [1, 2, 3]
b = a[0:3] ## 동일: b = a[:], b = list(a)
b[0] = 4
print(a, b) ## [1, 2, 3] [4, 2, 3]

# list 안에 list가 있는 경우
또 그대로 수정한 그대로 둘 다 반영됨
```
3) 깊은 복사
```
import copy
a = 1, 2, ['5', '6']
b = copy.deepcopy(a)
a[2][0] = 7
print(a, b) ## 깊은 복사를 통해 가리키는 [5, 6]을 담은 리스트가 따로 생성되어 독립적인 개체가 됨
```
