print('практическое задание "Распаковка позиционных параметров"')
def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list =(0.5, 'СТРОКА', False)
value_dict = {'a': 10.5, 'b': 'Строка', 'c':30}
value_list_2 = (54.32, 'Строка')

print_params()
print_params(1, 2, 3)
print_params(c = [1, 2, 3])
print_params(b = 25 )
print_params(*values_list)
print_params(**value_dict)
print_params(*value_list_2, 42)
print_params()