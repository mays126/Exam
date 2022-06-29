# ООП
class Tomato:
    __states = {
        1:'Семечко',
        2:'Росток',
        3: 'Плод'
    }
    # создаём статическое свойство со стадиями роста

    def __init__(self,index=1):
        self._index = index
        self.__one = 1
        self._state = self.__states[self.__one] # делаем конструктор класса и т.к я не понимаю на кой чёрт тут индекс я просто обьявил свойство one

    def grow(self):
        if self.__one < 3:
            self.__one += 1
            self._state = self.__states[self.__one]
        else:
            self._state = self.__states[3]

    def is_ripe(self):
        if self.__one == 3:
            print('Помидор достиг последней стадии')
            return True
        else:
            return False

class TomatoBush():
    def __init__(self,count):
        self.count = count
        self.tomatoes = []
        for i in range(count):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        result = []
        for i in self.tomatoes:
            if i.is_ripe() == False:
                result.append(i.is_ripe())
        if len(result) > 0:
            return False
        else:
            return True

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, tomatoes):
        self.name = name
        self._plant = tomatoes

    def work(self):
        self._plant.grow_all()
        print('Томаты выращенны')

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Томаты собранны')
        else:
            print('Томаты не выросли!')

    @staticmethod
    def knowledge_base():
        print('work = вырастить все помидоры. harvest = собрать помидоры если они выросли')


Gardener.knowledge_base()
tomatobush = TomatoBush(5)
gardener = Gardener('Пэтро',tomatobush)
while True:
    gardener.work()
    if gardener._plant.all_are_ripe():
        gardener.harvest()
        break
