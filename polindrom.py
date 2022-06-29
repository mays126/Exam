# написать функцию которая проверяет явлеется ли слово полиндромом
def polidnrom(str1: str):
    if len(str1) == 1:
        print('Полиндром')
    elif str1[0] != str1[-1]:
        print('Не полиндром')
    else:
        polidnrom(str1[1:-1])

print(polidnrom('шалаш'))
