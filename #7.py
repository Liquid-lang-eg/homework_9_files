def caesar_cypher(file):
    new_txt = open('new.txt', 'w', encoding='utf-8')
    with open(file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        great_shift = 1
        for line in lines:
            result = ''
            for char in line:
                if char.isupper():
                    result += chr((ord(char) - 65 + great_shift) % 26 + 65)

                elif char.islower():
                    result += chr((ord(char) - 97 + great_shift) % 26 + 97)

                else:
                    result += char

            new_txt.write(result)
            great_shift += 1
        new_txt.close()

caesar_cypher('hello.txt')