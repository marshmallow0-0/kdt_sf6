# 모듈(module) 불러오기
from classes.class_quiz import Calculator
import sys
class more_Calculator(Calculator):
    pass

calc = Calculator(4, 5)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())

# Calculator 상속 받기

class MoreCalculator(Calculator):
    # 거듭 제곱 계산 기능 추가
    def pow(self):
        return self.x ** self.y
    def div(self):
        try:
            # return self.x / self.y
            super().div()
        except:
            print("0으로 나눌 수 없습니다.")
            sys.exit(0)

mc = MoreCalculator(6, 0)
print(mc.pow())
print(mc.div())

