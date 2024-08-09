# 정보 은닉
class Health:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def getname(self):
        return self.__name

    def sethp(self, hp):
        # 범위 제한(0보다 작을 때 0으로 설정하고, 100보다 크면 100으로 설정)

        if hp < 0:
            hp = 0
        elif hp > 100:
            hp = 100
        self.__hp = hp

    def gethp(self):
        return "hp: " + str(self.__hp)

    def exercise(self, hours):
        self.sethp(self.__hp + hours)
        print("{}시간 운동하다. {}분 쉰다")
        # print("sky".format())

    def drink(self, cups):
        self.sethp(self.__hp - cups)
        print("술을 {0}잔 마시다".format(cups))

p1 = Health("나몸짱")
p1.sethp(100)
p1.exercise(3)
print(f'{p1.getname()} - {p1.gethp()}')

p2 = Health("한잔해")
p2.sethp(80)
p2.drink(4)
print(f'{p2.getname()} - {p2.gethp()}')