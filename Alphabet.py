import string

class Alphabet:
    def __init__(self,lang,letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        for i in self.letters:
            print(i,end=' ')
    def letters_num(self):
        print(len(self.letters))

class EngAlphabet(Alphabet):

    __leters_num = len(string.ascii_lowercase)

    def __init__(self):
        super().__init__('En',string.ascii_lowercase)

    def is_en_letter(self,letter):
        if letter in string.ascii_lowercase:
            return True
        else:
            return False

    def letters_num(self):
        return self.__leters_num

    @staticmethod
    def example():
        return "I'm author of this text."

engAlphabet = EngAlphabet()
engAlphabet.print()
print() # пустой принт для красоты
print(engAlphabet.letters_num())
if engAlphabet.is_en_letter('F'.lower()):
    print('Относится к английскому языку')
if engAlphabet.is_en_letter('Щ') == False:
    print('Не относится к английскому языку')

print(EngAlphabet.example())
