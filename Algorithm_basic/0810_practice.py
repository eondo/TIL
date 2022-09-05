N = 3 # 행의 크기
M = 4 # 열의 크기

# N개의 원소를 갖는 0으로 초기화된 1차원 배열

arr1 = [0] * N

# 크기가 NxM이고 0으로 초기화된 2차원 배열

arr2 = [[0] * M for _ in range(N)] ## N,M 순서 주의

# # 주의
# arr3 = [[0] * M] * N
# arr3[0][0] = 1 ## 모든 리스트 0 index 값이 다 1로 바뀐다 -> 세 리스트가 같은 reference를 참조

arr3 = [[1], [2, 3], [3, 4, 5]] # 각 행의 크기가 동일하지 않아도 됨

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 행의 합을 구하고 그 중 최대값을 출력하시오 ## 초기화 위치를 유의해야 함
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0 # 최대 행의 합

for i in range(N):
    rs = 0 # 행의 합
    for j in range(N):
        rs += arr[i][j] # i행의 j열에 접근
    if maxV < rs:
        maxV = rs
print(maxV) # 24 

# 대각선 합
s = 0
for i in range(N):
    for j in range(M):
        if i == j:
            s += arr[i][j]
# 왼 -> 오
s = 0
for i in range(N)
    s += arr[i][i]
# 오 -> 왼
s = 0
for i in range(N):
    s += arr[i][N - 1 - i]

# X자 대각선 합 (위의 2 단계를 더함, 홀수의 경우엔 N//2 인덱스 값을 한 번 빼줌)

# 대각선 기준 나머지 둘의 합 중 더 큰 값
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 답안
s1 = 0
s2 = 0
for i in range(N):
    for j in range(M):
        if i > j:
            s1 += arr[i][j]
        elif i < j:
            s2 += arr[i][j]

# 그 블럭만 접근하고 싶다면?
s1 = 0
s2 = 0
for i in range(N):
    for j in range(i + 1, N):
        s2 += arr[i][j]
        s1 += arr[j][i]

# 사선의 합
## 사선값마다 요롷게 더해서 그걸 최대값이랑 비교하면서 하는 건 인덱스 값 설정이 어려움
## 그냥 왼쪽에서 오른쪽으로 한줄 씩 읽어나가면서 
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = [0] * (2 * N - 1)
for i in range(N):
    for j in range(N):
        s[i + j] += arr[i][j]

print(s) 

# 9386. 연속한 1의 개수

for i -> N - 1:
    arr[i]=arr[i-1]*arr[i]+arr[i]



# 9489. 고대 유적
## 행에 대해서만?
maxV = 0
for i : 0 -> N - 1
    cnt = 0
    for j : 0 -> M - 1:
        if arr[i][j] == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
for i : 0 -> M - 1:
    cnt = 0
    for j : 0 -> N - 1:
        if arr[j][i] == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt