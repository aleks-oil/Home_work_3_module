print('Дополнительное практическое задание по модулю*')

data_structure = [
  [1, 2, 3],                                # 6
  {'a': 4, 'b': 5},                         # 11
  (6, {'cube': 7, 'drum': 8}),              # 29
  "Hello",                                  # 5
  ((), [{(2, 'Urban', ('Urban2', 35))}])    # 48
]
def calculate_structure_sum(arg):
    total = 0
    if isinstance(arg, (int, float)):      # определение принадлежности аргументов к классу чисел
        total += arg                       # сумма удовлетворяющих условию
    elif isinstance(arg, str):             # определение принадлежности аргументов к классу строк
        total += len(arg)                  # счет кол-ва символов в строках
    elif isinstance(arg, (list, tuple, set)): # определение принадлежности аргументов к классам список, кортеж, набор
        for element in arg:
            total += calculate_structure_sum(element) #счет кол-ва элементов, заданного условия по типам
    elif isinstance(arg, dict):                # определение принадлежности аргументов к классу словарь
        for key, value in arg.items():      # способ перебора ключей и значений словаря.
            total = total + calculate_structure_sum(value) + calculate_structure_sum(key) # результат сумма всех вычисленных значений
    return total


result = calculate_structure_sum(data_structure)
print('Cумма всех чисел и длин всех строк:',result)
