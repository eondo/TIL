# 풀어서 구현

stackSize = 10
stack = [0] * stackSize
top = -1

top += 1    # push(1)
stack[top] = 1

top += 1    # push(2)
stack[top] = 2

top -= 1
temp = stack[top + 1]
print(temp)

top = stack[top]
top -= 1
print(temp)

# 그냥 구현
stack2 = []
stack2.append(10)
stack2.append(20)
print(stack2.pop())
print(stack2.pop())


## 재귀 호출
# 호출할 때마다 메모리에 어떻게 변화하는 걸 만들고 싶은 거지? 고려

def f(i, N):     # i 현재 단계, N 목표 단계
    if i == N:
        print(i)  # 목표치에서 할 일
        return
    else:
        print(i)  # 각 단계에서 할 일 
        f(i+1, N)

f(0, 3) 

# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수 : 배열 접근에 많이 쓰임
## 이때까진 for i : 0 -> N-1 해왔음

def f(i, N):
    if i == N: # 배열을 벗어남
        return
    else: # 남은 원소가 있는 경우
        B[i] = A[i]
        f(i+1, N) # 다음 원소로 이동

N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N) # 0번 원소부터 N개의 원소에 접근!
# 1
# 2
# 3