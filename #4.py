import re

def hide_ban_words(stop_words_file, content_file):
    stop_words_list = []
    with open(stop_words_file, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            stop_words_list.extend(
                line.split()
            )

    pattern = r'\b(?:' + '|'.join(map(re.escape, stop_words_list)) + r')\b'

    with open(content_file, 'r', encoding='utf-8') as file:
        file_ = file.read().replace('\n', ' ').lower()
        return re.sub(pattern, lambda match: '*' * len(match.group()), file_)


print(hide_ban_words('stop_words.txt', 'wordstoban.txt'))