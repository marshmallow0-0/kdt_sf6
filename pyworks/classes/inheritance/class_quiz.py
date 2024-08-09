# 실습 3
class Calculator():
    def __init__(self):
        self.value = 100
    def sub(self, value):
        self.value -= value

class MinLimitCalculator(Calculator):
    def sub(self, value):
        super().sub(value)
        if self.value < 0:
            self.value = 0
        return self.value

cal = MinLimitCalculator()
cal.sub(20)
cal.sub(90)
print(cal.value)