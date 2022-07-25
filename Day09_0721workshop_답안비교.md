for문에서의 개념들!
enumerate 순회, list comprehension, dictionary comprehension

enumemrate
```
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
## [(0, 'Spring'), ...]
list(enumerate(seasons, start = 1))
## [(1, 'Spring'), ...]
```

삼항연산자랑 comprehension은 다르다!

[number ** 3 for number in range(1, 4)]

dictionary comprehension
{number: number ** 3 for number in range(1, 4)}

- 반복문 제어
특정 조건에 반복문을 종료시키기 위해서는 break

*는 주로 튜플이나 리스트르 언패킹하는데 사용