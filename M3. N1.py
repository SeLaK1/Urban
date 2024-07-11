import random
def count_calls():
    global colls
    colls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, ist_to_search):
    count_calls()
    for i in range(len(ist_to_search)):
        if string.upper() == ist_to_search[i].upper():
            return True
    return False


colls = 0

print(string_info('qwErT'))
print(string_info('agrtejd'))
print(string_info('asHvbTe3'))
print(is_contains('UrbAn', ['032', 'UrBaN', 'dfesfe']))
print(is_contains('VHdujfdhY', ['032', 'URbaN', 'dfesfe']))
print(colls)