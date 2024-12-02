print('практическое задание "Рекурсия"')
# Создаём функцию get_multiplied_digits и параметр number в ней
def get_multiplied_digits(number):
    #промежуточные работы со строкой numder, преобразовываем в список
    lst = []
    for i in str(number): lst.append(int(i)) #поочередно вытвскивем каждый символ(значение) и перезаписываем его в список
    a = []
    for j in lst: # цикл для удаления повторяющихся значений !! корректно работает с 0
        if j not in a:
            a.append(j)
            str_number = ''
    for k in a:    #цикл преобразования списка в строку
        str_number =  str_number + str(k)
    #основное решение задачи
    # Отделение первой цифры в числе: создание переменной first
    first = int(str_number[0])
    if len(str_number) == 1: #если строка состоит из одного значения, возвращяем это число
        return int(str_number)
    elif len(str_number) > 1: #условие при котором строка состоит более чем одно значение
       #Возвращаем значение first
       first = first * get_multiplied_digits(int(str_number[1:]))
    return first

# Вывод результата
result1 = get_multiplied_digits(40203)
print(result1)
result2 = get_multiplied_digits(402030)
print(result2)