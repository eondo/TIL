# # 실패함

# N = int(input())

# for tc in range(1, N + 1):
#     cards = list(map(int, input().split()))
#     baby_gin = 0 ## baby_gin이 2이어야 baby_gin 조건을 만족하는 것

#     for i in range(len(cards)):
#         count = 0

#         for j in range(len(cards) - 1):
#             if cards[i] ==(cards.remove(cards[i]))[j]:
#                 count += 1

#         if count == 2:
#             baby_gin += 1

# 

# # 3. set 이용한 것 -실패
# N = int(input())

# for tc in range(1, N + 1):
#     cards = list(map(int, input().split()))
#     cards_wo_t = []
#     baby_gin = 0  ## baby_gin이 2이어야 baby_gin 조건을 만족하는 것
#     baby_gin_bool = 0
#     triplet_set = set()

    # # triplet 검사

    # for i in range(len(cards)):
    #     if cards.count(cards[i]) == 3:
    #         triplet_set.add(cards[i])
    # baby_gin += len(triplet_set)

    # # run 검사
    # cards_wo_t = [k for k in cards if k not in triplet_set]

    # for j in range(len(cards_wo_t)):
    #     if {cards_wo_t[j], cards_wo_t[j] + 1, cards_wo_t[j] + 2} == set(cards_wo_t):
    #         baby_gin += 1

#     if baby_gin == 2:
#         baby_gin_bool = 1
#     else:
#         baby_gin_bool = 0

#     print(f'#{tc} {baby_gin_bool}')

# 4번째 시도
N = int(input())

for tc in range(1, N + 1):
    cards = list(map(int, input().split()))
    cards_counts = [0] * 12

    baby_gin = 0
    baby_gin_bool = 0
    
    # cards의 값을 index, 해당 값의 개수를 value로 갖는 리스트 완성
    for i in cards:
        cards_counts[cards] += 1
    
    # triplet 검사
    for j in cards_counts:
        if cards_counts[j] >= 3:
            baby_gin += 1
            cards_counts[j] == cards_counts[j] - 3 ## 해당 값을 triplet 수 없앤 값으로 초기화

    # run 검사
    for k in cards_counts:
        if cards_counts[k] >= 1 and cards_counts[k + 1] >= 1 and cards_counts[k + 2] >= 1:
            cards_counts[k] -= 1
            cards_counts[k + 1] -= 1
            cards_counts[k + 2] -= 1

            baby_gin += 1

    
    if baby_gin == 2:
        baby_gin_bool = 1
    else:
        baby_gin_bool = 0

    print(f'#{tc} {baby_gin_bool}')

# 5번째 시도
N = int(input())

for tc in range(1, N + 1):
    cards = list(map(int, list(input()))) ## list(map(int, input().split()))
    cards_counts = [0] * 12

    baby_gin = 0
    baby_gin_bool = 0

    # cards의 값을 index로, 해당 값의 개수를 value로 갖는 리스트 완성
    for i in cards:
        cards_counts[i] += 1

    # triplet 검사
    for j in cards_counts:
        if cards_counts[j] >= 3:
            baby_gin += 1
            cards_counts[j] = cards_counts[j] - 3  ## 해당 값을 triplet 수 없앤 값으로 초기화

    # run 검사
    for k in cards_counts: ## [..., 2, 2, 2, ...]인 경우에도 괜찮은가?
        if cards_counts[k] >= 1 and cards_counts[k + 1] >= 1 and cards_counts[k + 2] >= 1:
            cards_counts[k] -= 1
            cards_counts[k + 1] -= 1
            cards_counts[k + 2] -= 1

            baby_gin += 1

    if baby_gin == 2:
        baby_gin_bool = 1
    else:
        baby_gin_bool = 0

    print(f'#{tc} {baby_gin_bool}')

# 진짜 이제 예외 빼면 코드는 맞는듯 틀리면 진짜 울거임
N = int(input())

for tc in range(1, N + 1):
    cards = list(map(int, list(input()))) ## list(map(int, input().split()))
    cards_counts = [0] * 12

    print(cards)

    baby_gin = 0
    baby_gin_bool = 0

    # cards의 값을 index로, 해당 값의 개수를 value로 갖는 리스트 완성
    for i in cards:
        cards_counts[i] += 1

    print(cards_counts)

    # triplet 검사
    for j in range(len(cards_counts)):
        if cards_counts[j] >= 3:
            baby_gin += 1
            cards_counts[j] = cards_counts[j] - 3  ## 해당 값을 triplet 수 없앤 값으로 초기화
            continue

    # run 검사
    for k in range(len(cards_counts)): ## [..., 2, 2, 2, ...]인 경우에도 괜찮은가? 아니. 안된다. 한 번 더 돌아야 할 것 같은데?
        if cards_counts[k] >= 1 and cards_counts[k + 1] >= 1 and cards_counts[k + 2] >= 1:
            cards_counts[k] -= 1
            cards_counts[k + 1] -= 1
            cards_counts[k + 2] -= 1

            baby_gin += 1
            continue

    if baby_gin == 2:
        baby_gin_bool = 1
    else:
        baby_gin_bool = 0

    print(f'#{tc} {baby_gin_bool}')



    