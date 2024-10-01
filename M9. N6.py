
def all_variants(text):
    k = 0
    natchalo = ''
    while k < len(text):
        for i in range(k, len(text)):
            yield natchalo + text[i]
            natchalo += text[i]
        natchalo = ''
        k += 1

for i in all_variants('abcd'):
    print(i)


