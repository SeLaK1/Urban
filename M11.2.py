import sys
from pprint import pprint
from pip._vendor import requests
def introspection_info(element):
    dict_ = {}
    spisok_nyznogo = ['module', 'class', 'type', 'int', 'str', 'function', 'builtin_function_or_method',
                      'method-wrapper', 'dict', 'list']
    for atrebut in dir(element):
        atrebut_info = getattr(element, atrebut)
        stroka = str(type(atrebut_info)).split("'")
        if stroka[1] in spisok_nyznogo:
            if stroka[1] == 'type' and (isinstance(element, int) or isinstance(element, str)):
                dict_[type.__name__] = str(type(element)).split("'")[1]
            elif stroka[1] == 'int' or stroka[1] == 'str' or stroka[1] == 'dict' or stroka[1] ==  'list':
                dict_.setdefault('attributes', [])
                dict_['attributes'].append(atrebut)
            elif stroka[1] != 'slot' and stroka[0][1:] != 'built-in':
                dict_.setdefault(stroka[1], [])
                dict_[stroka[1]].append(atrebut)
            else:
                dict_.setdefault(stroka[1], [])
                dict_[stroka[1]].append(atrebut)
    return dict_


pprint(introspection_info(9))