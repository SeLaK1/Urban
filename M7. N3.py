
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        self.all_words = {}
        taboo = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for name_of_file in self.file_names:
            spisok_slov = []
            with open(name_of_file, encoding='utf-8') as file:
                slovo = ''
                for stroka in file.readlines():
                    for simvol in stroka:
                        if simvol == ' ' or simvol in taboo:
                            spisok_slov.append(slovo.lower())
                            slovo = ''
                        else:
                            slovo += simvol
            spisok_slov = list(filter(('').__ne__, spisok_slov))
            self.all_words[name_of_file] = spisok_slov
        return self.all_words

    def find(self, word):
        rezult = {}
        for key in self.all_words:
            slovo_count = 0
            for slovo in self.all_words[key]:
                slovo_count += 1
                if slovo == word.lower():
                    rezult[key] = slovo_count
                    break
        return rezult

    def count(self, word):
        rezult = {}
        for key in self.all_words:
            slovo_count = 0
            for slovo in self.all_words[key]:
                if slovo == word.lower():
                    slovo_count += 1
            rezult[key] = slovo_count
        return rezult


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
