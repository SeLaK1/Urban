
def add_everything(a, b):
    try:
        c = a + b
    except TypeError as exp:
        return str(a) + str(b)
    else:
        return c

print(add_everything(123.456, 'строка'))
print(add_everything('яблоко', 4215))
print(add_everything(123.456, 7))
