
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    for elements in strings:
        file.write(f'{elements}\n')
    file.close()

    file = open(file_name, 'r', encoding='utf-8')
    strings_positions = {}
    count_lines, count_butes = 0, 0
    for line in file:
        count_lines += 1
        print(file.tell())
        strings_positions[(count_lines, count_butes)] = line[:-1]

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)