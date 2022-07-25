다양한 종류의 매개변수를 입력 받기 위해서는 지정된 순서를 따른다.
위에서 소개한 내용을 종합해보면 결국 파이썬 매개변수는 아래와 같은 순서에 따라 입력을 받아야 한다.

미리 정의된 매개변수
- 이름과 개수가 정의되어 있지 않은 매개변수 (*args) – 리스트, 튜플
- 미리 정의된 키워드 매개변수 – 딕셔너리
- 이름과 개수가 정의되어 있지 않은 키워드 매개변수 (*kwargs) – 딕셔너리
- 예를 들어 텍스트 파일 본문에서 특정 단어들은 동일한 단어로(예를 들면 빈 문자열””로) 대체 혹은 삭제하고, 특정 단어들은 각각 지정된 다른 단어로 대체하는 함수를 만든다고 하면 이렇게 써볼 수 있겠다.
```
def remove(filename, *args, **kwargs):
    with open(filename) as file_obj:
        text = file_obj.read()
    for arg in args:
        text = text.replace(arg, "")
    for kwarg, replacement in kwargs.items():
        text = text.replace(kwarg, replacement)
    return text
print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))
```