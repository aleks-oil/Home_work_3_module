print('практическое задание "Произвольное число параметров"')
def single_root_words (root_word, *other_word):
    same_words = [] #создание пустого списка
    root_word_lower = root_word.lower() #преобразовние строки в строчные буквы
    for i in other_word: #перебор подходящих слов
        other_word_lower = i.lower() #преобразовние строки в строчные буквы
        # условие при котором добавляются слова в результирующий спиок
        if root_word_lower in other_word_lower or other_word_lower in root_word_lower:
            same_words.append(i)
    # Возврат образованного функцией списка same_words
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)