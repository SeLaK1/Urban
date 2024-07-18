
def search_single_root_words(root, *list_words):
    single_root_words = []
    for words in list_words:
        if root.lower() in words.lower() or words.lower() in root.lower():
            single_root_words.append(words)
    return single_root_words

root_1 = 'rich'
root_2 = 'Disablement'
result1 = search_single_root_words(root_1, 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = search_single_root_words(root_2, 'Able', 'Mable', 'Disable', 'Bagel')
print(f'Слова, подходящие корню {root_1}:', *result1)
print(f'Слова, подходящие корню {root_2}:', *result2)