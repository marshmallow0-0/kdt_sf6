# 실습 1
import sys
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y

    def div(self):
        if self.y == 0:
            print("0으로 나눌 수 없음")
            return sys.exit(0)
        else:
            return self.x / self.y

cal = Calculator(4,2)

print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())