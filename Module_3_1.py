print('практическое задание "Счётчик вызовов"')
calls = 0 # создание переменной для подсчета вызовов функций
def count_calls():
    global calls # использование глобальной переменной
    calls += 1 # увеличиваем счет вызовов на 1

def string_info(string):
    count_calls() # обращаемся к первой функции увеличиваем счетчик
    return (len(string), string.upper(), string.lower()) # кол-во символов, все заглавные, все строчные

def is_contains (string ,list_to_search):
    count_calls() # обращаемся к первой функции увеличиваем счетчик
    return string.lower() in [item.lower() for item in list_to_search] # преобразовываем первую строку в строчные символы,
    #сравнение строки со списком, в списке преобразовываем все символы строк в строчные

# вывод результата функций

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban', 'BaNaN','urBAN']))
print(is_contains('cycle',['recycle', 'cyclic']))
print(calls)
