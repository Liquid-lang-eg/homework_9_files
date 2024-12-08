import re

def replace_name_in_file(file):
    with open(file, 'r+', encoding='utf-8') as file:
        file_ = file.read()
        name = re.sub('(([ |-][А-Я]+[а-яА-Я]+){3,4})', ' N',file_ )
        file.seek(0)
        file.write(name)

replace_name_in_file('some_string.txt')

