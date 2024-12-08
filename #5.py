import re

def grade_separator(file):
    with open(file, 'r' , encoding='utf-8') as file:
        lines = file.readlines()
        print("Вот список учеников с оценкой ниже 3")
        for row in lines:
            if int(re.findall(r'\d+', row)[0]) < 3:
                print(re.sub(r'\d+|-', '', row))

grade_separator(input('Укажите файл: '))
