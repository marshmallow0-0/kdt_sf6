# 실습 1
'''
def operation(x, y):
    if x==y:
        return x*y
    else:
        return x+y

print(f"결과(곱): {operation(2,2)}")
print(f"결과(합): {operation(2,3)}")
'''
# 실습 2
'''
def get_price(unit_price, cnt):
    total_price = unit_price * cnt
    if total_price < 20000:
        total_price += 2500
        return total_price
    else:
        return total_price

product1 = get_price(10000,3)
product2 = get_price(5000,3)

# print(f"상품1 가격: {format(product1, ',d')}원")
# print(f"상품2 가격: {format(product2, ',d')}원")
'''
# 실습 3
'''
vending_machine = ['게토레이', '레쓰비', '생수','게토레이', '이프로', '생수']

def check_machine(): # 남은 음료수를 출력하는 함수
    print("남은 음료수: ", vending_machine)

def is_drink():  # 음료수가 있는지 확인하는 함수
    if drink in vending_machine:
       return True
def add_drink():  # 음료수를 추가하는 함수
    vending_machine.append(drink)  # 입력된 drink 추가

def remove_drink():  # 음료수를 제거하는 함수
    vending_machine.remove(drink)

while True:
    who = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")
    if who == '1':
        drink = input("마시고 싶은 음료? ")
        if is_drink():
            print(drink, "드릴게요")
            remove_drink()
            check_machine()
        else:
            print(f"{drink}는 지금 없네요")
    elif who == '2':
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        print(todo)
        if todo == '1':
            check_machine()
            drink = input("추가할 음료수? ")
            add_drink()
            vending_machine.sort()  # 오름차순 정렬되면서 같은 값끼리 연결됨
            print("추가 완료")
            check_machine()
        elif todo == '2':
            check_machine()
            drink = input("삭제할 음료수? ")
            if is_drink():
                remove_drink()
                print("삭제 완료")
                check_machine()
            else:
                print("음료 없음")
'''
# 실습 3

def check_machine(remain_drink):
        print("남은 음료는", remain_drink)

def is_drink(drink):
    if drink in vending_machine:
        vending_machine.remove(drink)
        print(f"{drink} 드릴게요")
    else:
        print(f"{drink}는 지금 없네요")

def is_drink():
    if drink in vending_machine:
        return True

def add_drink():
    drink = input("추가할 음료수? ")
    vending_machine.append(drink)  # drink 추가
    vending_machine.sort()  # 오름차순 정렬
    check_machine(vending_machine)
    print("추가 완료")

def remove_drink():
    drink = input("삭제할 음료수? ")
    if drink in vending_machine:
        vending_machine.remove(drink)
        print("삭제 완료")
        check_machine(vending_machine)
    else:
        print("음료 없음")


vending_machine = ['게토레이', '레쓰비', '생수','게토레이', '이프로', '생수']

while True:
    who = input("시용자 종류를 입력하세요:\n1.소비자 \n2.주인 \n")
    if who == '1':
        check_machine(vending_machine)
        drink = input("마시고 싶은 음료? ")
        is_drink(drink)

    elif who == '2':
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        if todo == '1':
            check_machine(vending_machine)
            add_drink()

        elif todo == '2':
            check_machine(vending_machine)
            remove_drink()
