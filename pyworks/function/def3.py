# 1부터 n까지 곱하는 함수

def gob_n(n):
    gob_v = 1
    for i in range(1, n+1):
        gob_v *= i
    return gob_v
'''
    i=1     1 = 1 * 1
    i=2     2 = 1 * 2
    i=3     6 = 2 * 3
    i=4     24 = 6 * 4
    
    4! = 4 * 3 * 2 * 1 (팩토리얼)
    4! = 4 * (4-1)!
    3! = 3 * (3-1)!
    2! = 2 * 1 (팩토리얼)
'''
# print("결과값 : ", gob_v)

print(gob_n(5))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))