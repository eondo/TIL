# 분할 정복 & 백트래킹
- 분할 정복 == '사고방식'
- 분할 정복 기법의 대표적인 알고리즘 : 퀵 정렬, 병합 정렬
- 상태 공간 트리의 모든 노드를 검색하는 백트래킹
- 반복 알고리즘을 분할 정복 기반의 알고리즘으로 푼다면? 시간 복잡도 down

### 병합 정렬
여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 활용
  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
  - top-down 방식
  - 시간 복잡도 : O(n log n)
  - 단점 : 매 단계별로 메모리가 많이 쓰이기 때문에 인덱스만 넘겨주는 방식으로 구현하는 경우 O

## 퀵 정렬
주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
- 병합 정렬과의 차이점
1. 병합 정렬은 그냥 두 부분으로 나눔, 퀵 정렬은 분할할 때 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴
2. 각 부분 정렬이 끝난 후, 병합정렬은 '병합'이란 후처리 작업(합치는 작업)이 필요하나, 퀵 정렬은 필요로 하지 않음
3. 시간 복잡도가 O(n^2)이 나올 때가 존재 : 이미 정렬되어 있음 or pivot이 정확하게 반을 나누지 않는 경우 (ex. pivot 값이 하필 해당 리스트의 가장 작은 값으로 뽑힘) → 퀵 정렬은 pivot을 어떻게 고르냐가 성능이 결정됨
4. BUT 일반적인 케이스는 무작위로 들어오기 때문에 퀵 정렬이 가장 빠르다고 취급!

- 알고리즘
```python
quickSort(A[], l, r)
    if l < r # → (*중요) l부터 r까지 정렬할 구간의 인덱스가 왼쪽, 오른쪽 구분되어 있어야 함
    # 피봇의 위치를 정함
    # 피봇 왼쪽 구간에서 동일한 작업 진행
    # 피봇 오른쪽 구간에서 동일한 작업 진행
```
### Hoare-Partition 알고리즘
i, j를 옮겨가면서 서로 교환하는 방식
```python
# 왼쪽 끝을 i, 오른쪽 끝 j으로 두고, i, j가 교차할 때까지 움직임
# 두 개가 떨어져있다면 자리를 바꿈
# 피봇이 자기 자리를 찾아감
```
🧷 아이디어
- P(피봇)값들 보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치하도록 함
- 피봇을 두 집합의 가운데에 위치시킴
- ? 참고 : 순서를 맞추진 않고 몰아놓음

🧷 __과정__
1. i는 왼쪽 끝에서 시작해서 오른쪽으로 움직이다가 p보다 큰 값을 찾으면 멈춤
2. j는 오른쪽 끝에서 시작해서 p보다 작은 값을 만나면 멈추고
3. 두 개의 자리를 바꿈
4. 그리고 i는 다시 거기서 p보다 큰 애를 찾아 이동, j는 p보다 작은 값 찾아 이동하다가
5. 결국 둘이 교차되면 일단 멈춤 → 왼쪽은 p보다 작음, 오른쪽은 p보다 큰 값들로 나눠진 상황이라고 이해! 
6. 작은 애들의 맨 끝 값과 pivot과 교환! 즉, pivot은 자리를 잡음 → 나머지 분할 된 두 경우를 다시 quicksort 진행(l부터 s - 1까지, s + 1에서 r까지)

```python
# 퀵정렬 - 1) 호어 방식

def partition(l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s - 1)
        qsort(s + 1, r)


A = [7, 2, 5, 3, 4, 5]
N = len(A)
qsort(0, N - 1)
print(A)
```
- qsort(A, l, r, compare) : sorting해야 하는 대상이 일차원 배열이 아닌 경우, 비교하는 작업을 한 개의 함수로 만들어서 별도로 구현하는 코드도 볼 수 있음 → 위 코드에서 비교해서 인덱스 정해주는 부분만 정렬할 대상에 맞게 바꿔주면 됨 ex. pivot = A[l][1], while문 안의 A[i][1], A[j][1]로 수정

### Lomuto Partition 알고리즘

🧷 __과정__
1. j가 이동하는데 p부터 r - 1까지 가는데 p가 가리키는 애가 피봇 이하면, i가 따라감, 둘의 자리를 바꿈
2. 즉, i는 피봇보다 작은 것들 중 가장 마지막 자리를 가리킴
3. i는 고정된 채로 j는 오른쪽으로 움직이다가 j가 피봇보다 작은 조건 만나면 i를 한 칸 옮겨서 피봇보다 큰 자리를 가리키고 i는 피봇보다 작은 값을 가리키고 있으니까 둘을 교환
<<<<<<< HEAD
4. j가 r - 1까지 오면 for문을 끝내고 i + 1 자리로 피봇을 보내고 원래 자리에 있던 값은 끝응로 보내서 교환
```python
# 퀵정렬 - 2) 로무토 방식

def partition(arr, left, right):
    pivot = arr[right]  # 가장 오른쪽 원소를 피벗으로 지정
    i, j = left - 1, left

    while j < right:
        if pivot > arr[j]:
            i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
```
__[참고]__ 안정적 정렬로서 안정적으로 같은 숫자라도 각 객체의 순서를 유지하는 방법
```python
# 퀵정렬 - 3) 파이썬스러운 방식 but 메모리 더 많이 씀

def quick_sort(arr):
    # 더 이상 분할할 수 없는 경우(종료 조건)
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 가장 왼쪽 원소를 피벗으로 지정
    arr = arr[1:]  # 피벗 제외하여 새로운 리스트 생성

    left_arr = [i for i in arr if i <= pivot]  # 피벗보다 작거나 같은 원소는 왼쪽으로 분할
    right_arr = [j for j in arr if j > pivot]  # 피벗보다 큰 원소는 오른쪽으로 분할

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
print(quick_sort(numbers))
```
=======
4. j가 r - 1까지 오면 for문을 끝내고 i + 1 자리로 피봇을 보내고 원래 자리에 있던 값은 끝으로 보내서 교환
>>>>>>> bbb6ffec1fe9f74a24659b96072a51b1becc7d90
<br>

## 이진 검색
자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 자료가 정렬된 상태여야 함
- 알고리즘 : 반복구조
  - n = 크기
  - ❗ 주의
  - low < high → 원소가 하나 남아있을 상황에도 키 값 비교가 진행되어야 하기 때문에 등호가 꼭 들어가야 함
  - mid = (low + high) // 2도 가능
  - 만약 못 찾는 경우
    - high와 low가 역전되면 검색 실패로 while문이 중단됨 → return - 1

- 알고리즘 : 재귀
  - return 값이 if, elif, else라서 셋 중 하나만 가게 되므로 어떤 값으로 오든 그 값을 밑 단계로 전해주면 됨

### 분할 정복의 활용
- 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘
- 퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘
<br>

## 백트래킹
- 더 이상 선택지가 없다면 이전의 선택지로 돌아가서 다른 선택을 함! 즉, 목표를 찾을 때까지 다 돌아야 함 → DFS
- 백트래킹 VS DFS
  - 백트래킹은 불필요한 경로를 조기에 차단
- 일반 백트래킹 알고리즘
  - ex. 최종 해가 아니면, 해당 노드 v의 다음 자식들 u에 대해서 각 자식들에 대해서 다음 단계를 진행시켜봄

- 기본 구조를 익히면 문제에 맞게 for문 부분만 바꾸어 활용할 수 있음
  - 후보를 추천하고, 그 후보들을 for문으로 인덱스를  통해 차례대로 적용해보고 더이상 단계가 없으면 찾는 개수만큼 정했으면 최종 목표와 맞는지 확인하고, ... 의 형식
  
[practice] __부분집합의 합__
```python
def f1(i, k, t):    # i : 부분집합으로 포함될지 말지 검토되는 원소 인덱스
    global cnt
    cnt += 1
    if i == k:  # 모든 검토가 다 끝나면
        s = 0   # 합을 구해본다
        for j in range(10):
            if bit[j]:
                s += A[j]
        if s == t:  # 찾는 합이면
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')    # 걔를 찍어보자
            print()
    else:
        bit[i] = 0
        f1(i + 1, k, t)
        bit[i] = 1
        f1(i + 1, k, t)


def f2(i, k, t, s, rs): # 찾고자 하는 목표값 t, 남은 애들의 합 rs
    global cnt
    cnt += 1
    if i == k:  # 모든 원소에 대한 검토가 끝났다면
        if t == s:    # 내가 찾는 합과 같으면
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif t <= s:    # 아직 원소들이 남았으나 지금까지 선택한 원소들 합이 같거나 커졌으면
        return      # 리턴해서 앞쪽 거를 좀 구성을 바꿔봐야 할 것 같아
    elif t > s + rs:    # 남은 것 다 더해도 너무 작은 경우 컷
        return
    else:
        bit[i] = 0
        f2(i + 1, k, t, s rs - A[i])  # 선택을 할 때마다, 포함하지 않는 경우
        bit[i] = 1
        f2(i + 1, k, t, s + A[i], rs - A[i])   # 포함한 경우, A[i] 더해줌
    return

A = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0

# f1(0, 10, 5)    # t = 10인 경우든 어떻든 무조건, 2047
f2(0, 10, 55, 0, sum(A))    # 남은 애들의 합으로 컷한 경우 더한 케이스, 21
print(cnt)
```


 





