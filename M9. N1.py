
def apply_all_func(int_list, *functions):
    _dict = {}
    for function in functions:
        _dict[function] = map(function, int_list)
    return _dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))