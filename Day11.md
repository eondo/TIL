- 뭐가 가변형이고 불변형인지가 중요 -> 문제해결을 위함
  - bool, int, float, tuple, str, range -> immutable
  - list, set, dict -> mutable

- 함수 vs 메서드
모든 자료형이 쓸 수 있는 것, 특정 자료형이 종속된 것

- 변수는 포스트잇이다!
: a를 선언하면 해당 데이터가 메모리 어딘가에 있고 b = a라고 하면 해당 데이터에 a라는 포스트잇이 붙어있다가 b라는 포스트잇도 함께 붙어 a와 b는 같은 값을 가짐.
단, mutable은 수정하면 같이 변하고, immutable은 수정이 안되기 때문에 달라진다

```
# 2차원 리스트의 복사

a = [[0] * 3] * 3 # 곱하면 같은 게 복사가 됨
## [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 1
## [[1, 0, 0], [1, 0, 0], [1, 0, 0]] ## id값이 다 같음

a = [[0] * 3 for i in range] ## list comprehension을 통해 깊은 복사 / int는 immutable이라서 [0] * 3로 해도 문제가 생기지 않음, 새로 만들어진 것임
## [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 1
## [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```
### workshop 푸는 도중 겪은 문제들
```
def lonely(numbers):
    numbers_nc = []

    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i + 1]:
            numbers_nc.append(
                numbers[i]
            )  ## 옆 인덱스의 값과 같으면 하나만 없애야 하는데 이걸 어떻게 표현하지...? 무작정 지워버리면
        else:
            numbers_nc.append(numbers[i + 1])

    return numbers_nc


print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))

## [1, 3, 3, 0, 1, 1]
[4, 4, 3, 3] 
```
### online_lab
- input을 Done 칠 때까지 계속 받는데 input을 받으면서 앞에 적힌 숫자가 올라가고 Done을 치려면 input의 타입을 또 어떻게 줘야 할지

- 문제
  n개의 소금물을 섞었을 때, 혼합된 소금물의 농도와 양을 계산하는 프로그램 mass_percent.py를 만드시오.

- 조건
  - 소금물 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오.
  최대 5개의 소금물을 입력할 수 있다. 출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시요.
  - 입력 예시
    - #mass percent.py 실행시
    - 1. 소금물 농도(%)와 소금물의 양(g)을 입력하십시오:1%400g
    - 2. 소금물 농도(%)와 소금물의 양(g)을 입력하십시오:8%300g
    - Done
  - 출력 예시
    - 4.0% 700.0g

### online_lab 헷갈리는 부분
```
def mass_percent(x):
    sum_d = 0
    sum_g = 0

    for i in x:
        sum_d += int(i[0]) * int(i[1])
        sum_g += int(i[1])

    d = sum_d / sum_g

    return round(d, 2), round(sum_g, 2)


dng_all = []

for i in range(5):
    dng = list(
        map(
            str,
            (input(f'{i+1}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오.:')).strip('g').split('%'),
        )
    )

    if dng == ['Done']:
        break

    else:
        dng_all.append(dng)

print((mass_percent(dng_all)))
```
여기서 출력을 4.0% 700.0g 이렇게 주려면 return을 없애야 하나, 아님 바깥문의 print에 뭔갈 처리를 해줘야 하나?
-> 수정본
```
def mass_percent(x):
    sum_d = 0
    sum_g = 0

    for i in x:
        sum_d += float(i[0]) * float(i[1])
        sum_g += float(i[1])

    d = sum_d / sum_g

    # return round(d, 2), round(sum_g, 2)
    print(f'{round(d, 2)}%{round(sum_g, 2)}g')


dng_all = []

for i in range(5):
    dng = list(
        map(
            str,
            (input(f'{i+1}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오.:')).strip('g').split('%'),
        )
    )

    if dng == ['Done']:
        break

    else:
        dng_all.append(dng)

mass_percent(dng_all)
```

### battleship 문제 헷갈렸던 부분
1. 함수를 정의하고 return sea를 안 주면 나중에 set_ship() 호출해서 쓸 때 None값이 나와서 억지로 return값 넣어줬었는데 원래 return이 없으면 None이 출력되는 게 맞고, 근데 여기선 set_ship을 처음 정의랑 player, computer 입력해서 호출하는 코드 이후엔 쓸 일이 없으니까 return 없어도 됨
```
def set_ship(index, sea):

    for n in range(3):
        sea[index - 1 + n] = 1
    return sea ## 이 line 없어도 됨 

# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
set_ship(player_index, player_sea)
set_ship(computer_index, computer_sea)
    
    ## 여기서 return값이 필요 없는 이유는 이것이 list형태이고 mutable이기 때문에 밑에서 set_ship함수를 실행시키면 해당 바다 영역 리스트 값이 유지되기 때문, 이건 이것이 list라는 mutable한 개체라서 특수한 경우라고 볼 수 있고, 정수나 string같이 immutable한 존재라면 return값을 꼭 선언해주어야 한다.
```
2. break를 꼭 else:문 아래에 넣을 필요 없는 케이스
```
while True:
    # 1-1) 플레이어의 배 시작 위치 고르기
    player_index = int(input('배를 위치시킬 시작점을 고르세요. : '))

    # 1-2) 범위를 벗어난 시작점을 고른 경우
    if player_index <= 0 or player_index > 13:
        print('-----해당 위치에는 배를 둘 수 없습니다.-----')
        continue

    break

    ## 원래 if 밑에 else:문을 두고 거기에 break를 뒀는데 사실 if에 들어가지 않는 경우라면 당연히 else 없이도 밑으로 빠져나가기 때문에 else문 없이도 break를 if문 indent라인에 맞춰 넣어주면 된다.
```
3. 고정값인 걸 함수를 자꾸 불러서 쓸데없이 낭비한 케이스
```
# 2-3) 플레이어의 공격이 성공한 경우
    if set_ship(computer_index, computer_sea)[player_attack_index - 1] == 1: ## set_ship()부분 모두 computer_sea로 수정
        print()
        print(f'<{round}라운드 결과!>')
        print(f"컴퓨터의 해역: {set_ship(computer_index, computer_sea)}")
        print(f'플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.')
        print(f'게임이 종료되었습니다! {round}라운드 만에 플레이어의 승리입니다!')

        break

# 2-6) 컴퓨터의 공격이 성공한 경우
    if set_ship(player_index, player_sea)[computer_attack_index - 1] == 1: ## set_ship()부분 모두 player_sea로 수정
        print()
        print(f'<{round}라운드 결과!>')
        print(f'플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였으나, 공격에 실패했습니다!')
        print(f'컴퓨터는 플레이어의 해역 {computer_attack_index}번째 칸을 공격하였고, 플레이어의 배는 피격되었습니다.')
        print(f'게임이 종료되었습니다! {round}라운드 만에 컴퓨터의 승리입니다!')

        break

## 
# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
set_ship(player_index, player_sea)
set_ship(computer_index, computer_sea)set_ship()
-> 이거 이후에 있는 set_ship() 함수는 모두 player_sea, computer_sea로만 줘도 된다. 지금 해당 코드 지날 때마다 쓸데없이 함수 실행하고 있음. 이미 set_ship()함수이고 이것은 변하지 않는 변수이기 때문에 그냥 결과값을 계속 주면 됨!
```
4. 잘한 부분?
```
# 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
    computer_attack_range = []
    for i in range(len(computer_attacked)):
        if computer_attacked[i] == False:
            computer_attack_range.append(i + 1)  ## False라서 빈 곳인 해당 값의 index를 넣는다

    computer_attack_index = random.choice(computer_attack_range)
```

