# Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

initial_string = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
for_delete = 'абв'

def lower_register(string :str) -> str:
    result = ''
    for i in string:
        if i.isupper():
            result += i.lower()
        else:
            result += i
    return result


def delete_symbols(string: str) -> str:
    new_str = string.replace('абв', '')
    return new_str


def string_from_list(some_list: list) -> str:
    new_str = ''
    for i in some_list:
        new_str += i + ' '
    return new_str


print(initial_string)

temp_list = lower_register(initial_string).split(' ')
temp_list = list(map(delete_symbols, temp_list))

result_str = string_from_list(temp_list)

print(result_str)