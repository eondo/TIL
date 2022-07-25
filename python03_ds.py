# 문자열
word = 'ssafy'
print(id(word)) # 메모리 주소 확인 2037702460592
word = 'test'
print(id(word)) # 메모리 주소 확인 2037702195696
## word가 변경된 게 아니고, ssafy라는 건 없어지고 test라는 새로운 것이 만들어졌다고 이해
## python에서는 변수 안에 주소만 들어감
## 기존에 ssafy 라는 값으로 생성된 메모리 객체에 새로운 값으로 변경되고 
# 새로운 주솟값을 갖기 때문에, ssafy 값을 가진 주소는 
# 더 이상 메모리에 존재하지 않습니다. 
# 다만 파이썬은 메모리 관리를 개발자에게 맡기지 않기 때문에 되도록 해당 부분은 신경쓰지 않고 핵심 개발에 집중하시는 걸 권장합니다.

print('apple'.find('p'))

print('abc'.isalpha()) # True
print('abc123'.isalpha()) # False

msg = 'hI! Everyone, I\'m ssafy'
print(msg)

print('*'.join('ssafy')) # s*s*a*f*y
print(' '.join(['3', '5', '8', '9'])) # 3 5 8 9


## 튜플

day_name = ('월', '화', '수', '목', '금')
# 연산 가능
print(day_name[-3]) # 수
print(day_name * 2)
print(day_name + 2)
day_name += False, True
print(id(day_name))
# 멤버십 연산자


## 셋
a = {'사과', '바나나', '수박'}
print(a.add('딸기'))
print(a)
print(a)
## 계속 딸기가 위치가 랜덤으로 바뀌면서 a 출력값이 나옴

# update
a = {'사과', '바나나', '수박'}
print(a)
a.update(['딸기', '바나나', '참외'])
## Q. 근데 여기서 update 뒤가 리스튼데 리스트를 요소인자로 넣어도 되나요?


## 딕셔너리
# pop

my_dict = {'apple': '사과', 'banana': '바나나'}
data = my_dict.pop('apple')
print(data, my_dict) # 사과 {'banana': '바나나'}
data = my_dict.pop('apple', 0)
print(data) # 0

# update
my_dict = {'apple': '사', 'banana': '바나나'}
my_dict.update(apple='사과')
print(my_dict) 
