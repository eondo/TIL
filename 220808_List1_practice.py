

# 최대값의 위치 구하기 (같은 값이 있을 때는 맨 오른쪽)

N = int(input())
arr = list(map(int, input().split()))

maxIdx = 0 ## 가정 : 맨 앞에 것이 가장 큰 수 들어있다!
for i in range(1, N):
    if arr[maxIdx] <= arr[i]:
        maxIdx = i 

# 버블 정렬
## 맨 오른쪽에 가장 큰 수 옮겨놓고, 남은 구간에서 또 남은 수 중 가장 큰 수...
N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1): ## 구간의 맨 끝 인덱스를 줄여나감
    for j in range(i) ## 인접원소 중 왼쪽 원소 인덱스
        if arr[j] > arr[j+1]: # 오름차순
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# 카운트 정렬
N = int(input())
arr = list(map(int, input().split()))
tmp = [0] * N ## 이거 왜 만드는 거지?

c = [0] * 101 ## 0부터 100까지의 숫자 개수, 인덱스가 100까지 있어야 함
for i in range(N):
    c[arr[i]] += 1

for j in range(1, 101): ## 개수 누적
    c[j] += c[j-1]

for i in range(N-1, -1, -1) ## 원본을 뒤에서부터 읽으면서 정렬 결과를 tmp에 저장
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]

print(tmp)