## 배열 2

### 2차원 배열
```python
# [참고] 2차원 배열을 받을 때
N = int(input()) # 행 개수
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 원소에 접근하고 싶을 때 (N,M 활용)
for i in range(N):
  for j in range(N):
    print(arr[i][j], end=' ')
  print()

for i in range(len(arr)): # N = len(arr)
  for j in range(len(arr[0])): # M = len(arr[0])
    print(arr[i][j], end=' ')
  print()
```
#### 2차원 배열의 접근
- 배열 순회
- 행 우선 순회
- 열 우선 순회
- 지그재그 순회
  ```python
  # i 행의 좌표
  # j 열의 좌표

  for i in range(n):
    for j in range(m):
      Array[i][j + (m-1-2*j) * (i%2)] ## (짝수일 때 i%2가 0, 뒤에 날아가고 그냥 j만 남음)

- 델타를 이용한 2차 배열 탐색
어떤 원소를 기준으로 그 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
  ```python
  # 현재 기준 i,j에다 델타를 더해서 업데이트해줌
  # 가장자리 칸 등 접근할 수 없는 인덱스 경우도 고려해서 if문으로 유효한지 체크

  di = [0, 1, 0, -1]
  dj = [1, 0, -1, 0]
  N =  3
  arr = [[1,2,3,4],[4,5,6,7]]
  for i in range(N):
    for j in range(M):
      for k in range(4): # for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]
        ni = i + di[k] # ni, nj = 1+ di, j +dj
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
          print(ni, nj)

  # 상하좌우의 d칸씩 다 탐색도 가능
  for i in range(N):
    for j in range(M):
      for d in range(1, 3):
        for k in range(4):
          ni = i + di[k] * d
          nj = j + dj[k] * d
        
          if 0 <= ni < N and 0 <= nj < M:
            print(ni, nj)
  ```          
- 전치 행렬

#### 부분집합의 합(Subset Sum) 문제
유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모든 더한 값이 0이 되는 경우가 있는지 알아내는 문제

- 부분집합 생성하기
  ```
  bit = [0,0,0,0] # 있다, 없다 여부에 관한 리스트
  ```
  다른 방법 - 비트 연산자
  
  - 비트 연산자
[practice] 부분집합의 합 문제 구현하기
10개의 정수를 입력받아 부분집합의 합의 0이 되는 것이 존재하는지 계산하는 함수를 작성하라.
```python
t = int(input())
for tc in range(1, t + 1):
    numbers = list(map(int, input().split()))
    n = len(numbers)

    for i in range(1, 1 << n):  # i는 1부터 2^n - 1까지 돌면서
        total = 0               # 하나의 i마다 하나의 부분집합의 합 total을 가짐

        for j in range(n):      # 1을 0부터 n - 1만큼 옮기면서
            if i & (1 << j):    # i의 이진수 자릿수와, 옮긴 1의 자리가 둘 다 1이면
                total += numbers[j] # 그 자리를 인덱스값으로 하는 numbers 원소가 부분집합에 포함된다는 뜻!

        if total == 0:          # 만약 구한 그렇게 하나의 부분집합의 합이 0이면
            answer = 1          # 답을 1로 하고
            break               # 0인 경우가 하나 나온 거니까 중단
    else:                       # break로 중단된 적이 없다면
        answer = 0              # 조건을 만족하는 경우가 하나도 없다는 거니까 answer는 0으로 만듦

    print(f'#{tc} {answer}')
```
![image](https://user-images.githubusercontent.com/109258497/193445057-43dc7303-87e3-4678-838c-3d34ff901a42.png)
[practice] 부분집합을 순열(재귀)로 푸는 방법
```python
# s1
def powerset(arr, depth, total):
    if total > 10:
        return
    if depth == len(numbers):
        if total == 10:
            print(arr)
        return

    else:
        powerset(arr + [numbers[depth]], depth + 1, total + numbers[depth])
        powerset(arr, depth + 1, total)


numbers = list(range(1, 11))
powerset([], 0, 0)

# s2
def powerset(arr, start, total):
    if total > 10:
        return

    if total == 10:
        print(arr)
        return

    for i in range(start, len(numbers)):
        arr.append(numbers[i])

        powerset(arr, i + 1, total + numbers[i])

        arr.pop()


numbers = list(range(1, 11))
powerset([], 0, 0)
```

#### 검색(Search)
- 탐색 키 : 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
  - 순차 검색
  - 이진 검색
  - 해쉬

#### 순차 검색
배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
- 정렬되어 있지 않은 경우 / 정렬되어 있는 경우

#### 이진 검색
- (*중요) 반복 구조 이용 (좀 더 효율적)
  ```python
  def binarySearch(a, N, key)
      start = 0
      end = N - 1
      while start <= end: # start랑 end가 같은 경우에도 key값이 찾고자 하는 값이랑 일치하는지 확인해야 하기 때문에 등호도 꼭 넣어야 함
        middle = (start + end) // 2
        if a[middle] == key: 
          return true
        elif a[middle] > key:
          end = middle - 1
        else:
          start = middle + 1
      return false # 검색 실패

- 재귀 함수 이용

#### 인덱스
배열을 사용한 인덱스

#### 선택 정렬
주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 정렬 과정
  - 주어진 리스트 중에서 최소값의 인덱스를 찾는다
  - 그 인덱스에 든 값을 리스트의 맨 앞에 위치한 값과 교환한다
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다
```python
def selctionSort(a, N):
  for i in range(N-1): # 구간 시작
    minIdx = i
    for j in range(i+1 , N): # 나 자신 그다음부터 하면 되니까 i일 필요 X
```
```python
arr = [7, 2, 5, 3, 4, 3]
N = len(arr)

for i in range(N-1):
  minIdx = i # 구간의 맨 앞으로 최소값으로 가정
  for j in range(i+1, N) # 실제 최소값 인덱스 찾기
      if arr[minIdx] > arr[j]
          minIdx = j
  arr[minIdx], arr[i] = arr[i], arr[minIdx]
print(arr) # [2, 3, 3, 4, 5, 7]
```

#### 셀렉션 알고리즘
저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
앞에서부터 한 세 번째 구간까지만 한다면? 3번만 실행하면 됨

#### 정렬 알고리즘 비교

### live practice
 