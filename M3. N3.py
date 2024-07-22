def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

value_list = [1, 'строка', True]
value_dict = {'a': 1, 'b': 'строка', 'c': True}
value_list_2 = [1, 2]

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print()
print_params(*value_list)
print_params(**value_dict)
print()
print_params(*value_list_2, 2123)
