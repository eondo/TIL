dictionary의 생성 및 값 추가

내가 만난 문제 : 딕셔너리의 특정 키 값에 value를 for문으로 돌려서 리스트 안의 리스트들 값을 딕셔너리의 value로 넣어주려고 하는데, 문제는 딕셔너리는 동일한 key면 마지막으로 저장한 value를 해당 키의 value로 바뀌어서 나온다. 따라서, 나는 지금 특정 키의 value를 리스트 형태로 저장하고 싶기 때문에. 단순히 dict['key이름'] = ~~ 이라고 하면 안될 것 같다. 
```
def turn(temperatures):
    max_min_dict = {}
    max_min_dict['maximum'] = []
    max_min_dict['minimum'] = []
    
    for i in temperatures:
        max_min_dict['maximum'] = [i[0]]
        max_min_dict['minimum'] = [i[1]]

    return max_min_dict

if __name__ == '__main__':
    temperatures = [[9, 3], [9, 0], [11, -3], [11, 1], [8, -3], [7, -3], [-4, -12]]
    print(turn(temperatures))
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4],
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }

## 결과 : {'maximum': [-4], 'minimum': [-12]}
```
좀 다른 경우인 것 같은데 value를 리스트로 가지는 딕셔너리의 추가 및 수정 방법을 알아보자.
- 해결! 딕셔너리를 처음부터 정의할 때 키값과 그에 해당하는 빈 리스트를 저렇게 지정해줄 수 있다는 것을 처음 알았다.
```
def turn(temperatures):
    max_min_dict = {'maximum' : [], 'minimum' : []}
    
    for i in temperatures:
        max_min_dict['maximum'].append(i[0])
        max_min_dict['minimum'].append(i[1])

    return max_min_dict
```
2번째 문제에 봉착했다. 값이 dictionary에 공란이 아닌지 확인하는 법을 판단하려 하는데, 공란임을 어떤 식으로 코드로 정의할지 모르겠음. 일단 아래 처럼 None 상태라고 생각했는데....
```
def is_user_data_valid(user_data):
    
    if user_data['id'] == None or ['password'] == None:
        return False
    else:
        return True

if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1))
    # False

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2))
    # True

    ## 결과 : 
    True
    True
```
해결 : bool함수를 이용해서 해당 값이 공란인지 확인한다.
```
def is_user_data_valid(user_data):
    
    if bool(user_data['id']) == False or bool(user_data['password']) == False:
        return False
    else:
        return True
```
- 어떤 리스트 안이든 그냥 변수든 모든 어떤 데이터에서 이 데이터가 문자열일때든 아니든 아무튼 인덱스 값을 가지는 데이터일때, 마지막 글자 혹은 마지막 인덱스 값에 접근하는 법을 모르겠음.
```
def is_id_valid(user_data):
    if user_data['id'][len(user_data['id'])-1:] in range(10):
        return True
    else:
        return False

if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1))
    # True

    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2))
    # False

    ## 결과 : 
    False
    False
```
여기서 문제가 뭘까요... 일정치 않은 길이의 문자열에 마지막 인덱스를 뽑아보는 법이 뭘까. 이거는 string[-1] 이걸 쓰면 됨, 그러면 이 문자가 0부터 9사이에 있는지 확인하는 법은? 
- 해결 : if "A" in B: 쓰면 된다! 그리고 이 문제에서 계속 오류가 났던 이유는 내가 ID에서 뽑은 마지막 글자가 str 타입이었기 때문이고, range(10)은 정수 형태로 리스트가 만들어졌기 때문에 이를 map함수 이용해서 str으로 바꿔주는 처리를 함으로써 인식이 됐다!
```
def is_id_valid(user_data):
    a = map(str, range(10))
    if user_data['id'][-1] in a:
        return True
    else:
        return False
```