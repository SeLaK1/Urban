def print_params(*param_1):
    print(*param_1)

value_list = [1, 'строка', True]
value_dict = {'a': 1, 'b': 'строка', 'c': True}
value_list_2 = [1, 2]

print_params(*value_list_2, 2123)
