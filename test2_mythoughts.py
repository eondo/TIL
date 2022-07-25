def func(*args):
    print(args)
    print(type(args))

func(1, 2, 3, 'a', 'b')

def print_family_name(father, mother, *pets):
    print(f'아버지 : {father}')
    print(f'어머니 : {mother}')
    print('반려동물들..')
    for name in pets:
        print(f'반려동물: {name}')

print_family_name('아부지', '어무니')

a = '135'
while a:
    print(a[-1])
    a = a[:-1]