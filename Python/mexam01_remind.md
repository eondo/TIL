## recursion
자기 자신을 호출하는 함수, 상의(원래)문제를 좁은 범위로 생각해서 풂
- 1) 종료 조건 base-case
- 2) 점화식

```
if n < 2:
    return str(n)
else:
    dec_to_bin(n // 2) + str(n % 2)
    
    #[    5에 대하여    ] + 1
    #...
    #[1에 대하여] +1
```

## 특정 범위에서 순환하는 형태로 만들기
index 넘어가면 앞으로 다시 돌아오는 형태 -> ex. 3보다 커지면 (n = n % 4)로 갱신 -> 처음으로 돌아옴
- 숫자가 넘어갔을 때 어떻게 할 것인가 (how to Z -> A) : 나머지 연산자 이용!
``` 
A = [1, 2, 3, 4]
     0, 1, 2, 3 으로 index 순환

## A(:65) . . . . . . 90(:Z) 를 A(0) ~ Z(25)로 맞춰주고 
이 index를 len(A ~ Z)으로 나눈 나머지로 n 갱신 
(ex. 26이 넘어가면 26으로 나눈 나머지로 앞으로 돌려주고 마지막에 65를 더해서 알파벳으로 바꿔줌)
```

## 2차원 리스트에서의 상하좌우 이동
이차원 리스트 == 행렬
상하좌우 이동 : 델타 이동
```
a = [
  [0, 0, 0]
  [0, 1, 0]
  [0, 0, 0]
]
now = [1, 1]

# 상
now[0] -= 1
now[1] ## 아무것도 바뀌지 않음
print(now) ## [0, 1]
.
.
.
-> '상하좌우' 4개를 1개로 합치면?
# 델타값 선언 (상하좌우 이동에 관한 토대, x: 행, y: 열)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
```
c.f.
```
for i in range(4):
    now[0] += dx[i]
    now[1] += dy[i]
```
- 문제 풀이
```
n = 3 ## 행렬 크기
m = 0 ## 상하좌우 어디로 갈지에 대한 인덱스

now[0] += dx[m]
now[1] += dy[m]

# 판단
if now[0] < 0 or now[0] >= n or now[1] < 0 or now[1] >= n:
    print("범위 벗어남")
else:
    print("정상 범위")
```