def most_frequently_words(file):
    with open(file, 'r', encoding='utf-8') as file:
        list_of_lines = file.readlines()

        counter = 0
        for line in list_of_lines:
            duplicates = {}
            list_ = line.split(' ')

            for elem in list_:
                if elem in duplicates:
                    duplicates[elem] += 1
                else:
                    duplicates[elem] = 1

            counter += 1
            max_el = max(duplicates, key=duplicates.get)
            print(f'В строке {counter} самым большим элементом является '
                  f'{max_el} '
                  f'встречается в строке {duplicates[max_el]} раз')

most_frequently_words('txt.txt')