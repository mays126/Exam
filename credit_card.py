#Написать функцию принимаюшую номер кредитной карты и возвращающую последние четыре цифры
def get_nuber(number: str):
    str_len = len(number)
    new_number = '' #номер карты после выполнения функции
    for i in range(str_len):
        if i >= str_len - 4:
            new_number = new_number + number[i]
        elif number[i] == ' ':
            new_number = new_number + ' '
        else:                                                       # если i равно последним четырём цифрам то записываем их
            new_number = new_number + '*'                           # иначе записываем *


    return new_number

print(get_nuber('1234 5678 9999 9999'))

