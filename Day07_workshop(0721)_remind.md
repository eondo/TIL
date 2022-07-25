### P01
list comprehension으로 해서 언패킹하는 거 자주 씀

### P02
### P03
리스트 안에 딕셔너리가 들어가 있는 형태
0번째 index로 한 딕셔너리, 1번째 index로 하나 딕셔너리 들어가 있음. 리스트 자체가 argument로서 input에 들어감
return하려는 값을 for 위에다 선언해놓고 시작

### P04
2차원 리스트의 전체 합 구하기

## 2차원 리스트 개념
리스트를 원소로 가지는 리스트
```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0]) # 1
```
행렬로 생각!
- 2차원 리스트의 순회
  - 이중 반복문 활용
  - for문 안과 index를 어떻게 작성하냐에 따라 순회에 따라 달라짐
    ```
    # 열 우선 순회

    for i in range(4):
        for j in range(3):
            print(matrix[j][i], end=" ")
        print()

        # 1 5 9
        # 2 6 0
        # 3 7 1
        # 4 8 2

    ## 여기서 3,4를 바꾸고 i,j를 바꾸면 행 우선 순회가 된다
    matrix = [[1, 2, 3, 4]
            , [5, 6, 7 ,8]]
    total = sum(map(sum, matrix))
    print(total)

    max_value = max(map(max, matrix)) # !max,sum([리스트]) 가능!
    ```
### PJT 중 개념 설명
dictionary의 get method
a["key"] = a.get("key")
a.get("name", "기본값(name이라는 키가 없으면 기본값으로 뭘 가져올거냐)")