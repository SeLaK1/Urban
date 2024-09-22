
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [x for x in first_strings if len(x) > 4]
second_result = [(x, y) for x in first_result for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in first_strings+second_strings if not len(x) % 2}

print(first_result)
print(second_result)
print(third_result)