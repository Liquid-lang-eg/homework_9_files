import re
from functools import reduce

def sum_of_nums(file):
    with open(file, 'r', encoding='utf-8') as file:
        file_py = file.read()
        res = 0
        return reduce(lambda x, y: int(y) + int(x), re.findall(r'\d+', file_py))


print(sum_of_nums(input('Введите файл: ')))