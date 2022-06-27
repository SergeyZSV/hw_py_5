#Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1. Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.
import functools

langs = ['python', 'csharp', 'java', 'go', 'php']
nums = [i for i in range(1, len(langs) + 1)]

dictionary = {
    'A': '41',
    'B': '42',
    'C': '43',
    'D': '44',
    'E': '45',
    'F': '46',
    'G': '47',
    'H': '48',
    'I': '49',
    'J': '4A',
    'K': '4B',
    'L': '4C',
    'M': '4D',
    'N': '4E',
    'O': '4F',
    'P': '50',
    'Q': '51',
    'R': '52',
    'S': '53',
    'T': '54',
    'U': '55',
    'V': '56',
    'W': '57',
    'X': '58',
    'Y': '59',
    'Z': '5A'
}


def corteges(number_list: list, string_list: list) -> list:
    upper_list = []
    for string in string_list:
        upper_list.append(string.upper())
    result = list(zip(number_list, upper_list))
    return result


sort_list = corteges(nums, langs)
print(sort_list)


def filt(some_list: list) -> int:
    result_list = []
    result_nums = []
    suma = 0
    result = 0
    for element in some_list:
        for i in range(0, len(element[1]) - 1):
            point = int(str(dictionary[element[1][i]]), 16)
            suma += point
        if suma % element[0] == 0:
            result_list.append((suma, element[1]))
            result_nums.append(suma)
        suma = 0
    print(result_list)
    result = functools.reduce(lambda x, y: x + y, result_nums)
    return result


print(filt(sort_list))