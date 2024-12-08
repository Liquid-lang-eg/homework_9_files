import json
import csv
from statistics import mean


class JsonCsvManager:

    def __init__(self, json_, csv_):
        self.json = json_
        self.csv = csv_

    def interface_manager(self):
        print('''Данная программа предлагает функционал для взаимодействия с JSON, CSV файлами
              Предлагаются следующие функции, введите интересующий вариант с клавиатуры
              1. Форматирование json в csv
              2. Добавить нового сотрудника в csv файл
              3. Добавить нового сотрудника в json файл
              4. Найти данные сотрудника по имени
              5. Фильтрует сотрудников по наличию скила
              6. Выводит средний рост сотрудников младше указанного роста
              -1. Просмотреть доступные опции
              0. Выйти из программы
              ''')

        while True:
            try:
                choice = int(input('Введите значение: '))
            except ValueError:
                print('Введите значение из предложенных!')
                return self.interface_manager()
            if choice == 1:
                self.__json_to_csv()
                print('-1. Просмотреть доступные опции')

            elif choice == 2:
                form = self.__manage_form()
                self.__add_new_worker_csv(form)
                print('Was added')
                print('-1. Просмотреть доступные опции')

            elif choice == 3:
                form = self.__manage_form()
                self.__add_new_worker_json(form)
                print('Was added')
                print('-1. Просмотреть доступные опции')

            elif choice == 4:
                name = input("Введите имя которое вы ищете: ")
                employee_data = self.__find_employee(name)
                if employee_data:
                    for key, item in zip(employee_data.keys(), employee_data.values()):
                        print(f'{key}: {item}')
                else:
                    print('Данный сотрудник не был найден')
                print('-1. Просмотреть доступные опции')

            elif choice == 5:
                language = input('Введите язык: ')
                list_of_employees = self.__filter_language_skill(language)
                if list_of_employees:
                    for item in list_of_employees:
                        print(item)
                else:
                    print('Сотрудники с такими навыками не были найдены')
                print('-1. Просмотреть доступные опции')

            elif choice == 6:
                while True:
                    try:
                        year = int(input('Введите год: '))
                    except ValueError:
                        print('Введите год"')
                    else:
                        break
                height = self.__get_average_height_sort_by_year(year)
                if height:
                    print(f'Средний рост указанного возраста: {height}')
                else:
                    print('Таких данных нет')
                print('-1. Просмотреть доступные опции')

            elif choice == 0:
                break

            elif choice == -1:
                return self.interface_manager()


    def __manage_form(self):
        print('''Введите значения в следующем формате:
              1. Имя Фамилия
              2. Дата рождения в формате xx.xx.xx
              3. Рост, пример: 185
              4. Вес , пример: 65,4
              5. Владеет ли клиент машиной: True
              6. Какими языками владеет программист
              ''')

        values = []
        counter = 1
        while counter < 7:
            if counter == 1:
                value = input('Введите имя: ')

            elif counter == 2:
                value = input('Введите дату рождения в формате xx.xx.xx: ')

            elif counter == 3:
                while True:
                    try:
                        value = int(input('''Укажите рост
                        (Введите int, число пример в сантиметрах, (например: 170 ): '''))
                    except ValueError:
                        print('Третьим значением должно быть число (в фоормате int)')
                    else:
                        break

            elif counter == 4:
                while True:
                    try:
                        value = float(input('''Укажите вес
                        (Введите float, число с точкой (пример: 85.5 ): '''))
                    except ValueError:
                        print('Четвертым значением должно быть число с точкой (в фоормате float)')
                    else:
                        break

            elif counter == 5:
                while True:
                    value = input('Укажите наличие машины(Введите bool: y или n): ')
                    if value == 'y':
                        value = True
                        break

                    elif value == 'n':
                        value = False
                        break

                    else:
                        print('Введите один из указанных вариантов')



            elif counter == 6:
                value = []
                while True:
                    language = input('''
                    Введите язык программирования,
                    для когда введете все языки нажмите q
                    ''')
                    if language == 'q':
                        break
                    value.append(language)

            values.append(value)
            counter += 1
        return values

    def __json_to_csv(self):
        with open(self.json, 'r') as json_file:
            dict_from_json = json.load(json_file)

        with open('csv_from_json.csv', 'w', newline='', encoding='utf-8') as csv_:
            file_writer = csv.writer(csv_)

            if isinstance(dict_from_json, list) and dict_from_json:
                file_writer.writerow(dict_from_json[0].keys())
                for row in dict_from_json:
                    file_writer.writerow(row.values())
            else:
                print("JSON файл не содержит список словарей")

    def __add_new_worker_csv(self, values):
        with open(self.csv, 'a') as csv_file:
            csv_data = csv.writer(csv_file)
            csv_data.writerow(values)

    def __add_new_worker_json(self, values):
        with open(self.json, 'r') as json_file:
            json_data = json.load(json_file)
            keys = list(dict(json_data[0]).keys())
            new_dict = {}

            for value, key in zip(values, keys):
                new_dict[key] = value

            json_data.append(new_dict)

        with open(self.json, 'w') as json_file_1:
            json.dump(json_data, json_file_1)

    def __find_employee(self, name):
        with open(self.json, 'r', ) as json_file:
            json_data = json.load(json_file)
            for dict_ in json_data:
                if name == dict_['name']:
                    return dict_

    def __filter_language_skill(self, language):
        employee_with_skill = []
        check = False
        with open(self.json, 'r', ) as json_file:
            json_data = json.load(json_file)
            for dict_ in json_data:

                for lang in dict_['languages']:
                    if lang == language:
                        check = True
                if check:
                    employee_with_skill.append(dict_['name'])
                check = False
            return employee_with_skill

    def __get_average_height_sort_by_year(self, year):
        list_of_heights = []
        with open(self.json, 'r', ) as json_file:
            json_data = json.load(json_file)
            for employee in json_data:
                if int(employee['birthday'].split('.')[-1]) < year:
                    list_of_heights.append(int(employee['height']))
            # функция mean высчитывает среднее значение из списка интов
            if list_of_heights:
                return f'Средний рост данной группы: {mean(list_of_heights)} см'
            else:
                return 'сотрудников родившехся раньше этой даты не существует'


json_csv_manager = JsonCsvManager("employees.json", "csv_from_json.csv")
json_csv_manager.interface_manager()

