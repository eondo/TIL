print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액
costs_ordered = sorted(costs, reverse=True)
print(costs_ordered)

while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

    # 여기부터 코드를 작성하세요.
    if money > 0:
        budget = budget + money
        print("현재 누적 금액은 ", budget, "원 입니다.", sep="")
        continue

    elif money < 0:
        print("금액은 1원 이상 넣어주세요.")
        continue
    else:
        break

## 메뉴 출력
print(" ")
print(budget, "원으로 구매 가능한 메뉴는 다음과 같습니다", sep="")
menu_avail = []

if budget >= costs_ordered[0]:
    # print(budget, "원으로 구매 가능한 메뉴는 다음과 같습니다", sep="")
    # 내 생각 iterable 돌면서 검사를 하는 거지 너 지금 이 budget보다 크니? 작니? 이걸 물어보면서 돌면서
    # budget보다 작거나 같으면 해당 값의 번호와 이름이랑 가격을 주문가능란 리스트에 하나씩 추가하는 건?...?
    for j in range(6):
        if costs[j] <= budget:
            print(j + 1, ". ", menus[j], " ", costs[j], "원", sep="")
            menu_avail.append(j + 1)

elif budget >= costs_ordered[1]:
    for j in range(6):
        if costs[j] <= budget:
            print(j + 1, ". ", menus[j], " ", costs[j], "원", sep="")
            menu_avail.append(j + 1)

elif budget >= costs_ordered[2]:
    for j in range(6):
        if costs[j] <= budget:
            print(j + 1, ". ", menus[j], " ", costs[j], "원", sep="")
            menu_avail.append(j + 1)

elif budget >= costs_ordered[3]:
    for j in range(6):
        if costs[j] <= budget:
            print(j + 1, ". ", menus[j], " ", costs[j], "원", sep="")
            menu_avail.append(j + 1)

elif budget >= costs_ordered[4]:
    for j in range(6):
        if costs[j] <= budget:
            print(j + 1, ". ", menus[j], " ", costs[j], "원", sep="")
            menu_avail.append(j + 1)

elif budget >= costs_ordered[5]:
    for j in range(6):
        if costs[j] <= budget:
            print(j + 1, ". ", menus[j], " ", costs[j], "원", sep="")
            menu_avail.append(j + 1)
else:
    print(budget, "원으로 구매 가능한 메뉴가 없습니다.", sep="")
    quit()

print(menu_avail)

## 3. 메뉴 선택
while True:
    print()
    choice = int(input('구매하실 메뉴의 번호를 입력하세요. : '))
    # 여기부터 코드를 작성하세요.
    if choice in menu_avail:
        print(menus[choice - 1], "를 구매하셨습니다.", sep="")
        print("거스름돈은 ", (budget - costs[choice - 1]), "원입니다. 감사합니다!", sep="")
        break
    else:
        print("구매할 수 없는 메뉴입니다.")
        continue
