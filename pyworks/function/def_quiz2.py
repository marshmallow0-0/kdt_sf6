

# 실습 4

def times():
    numbers = []
    n = 3
    for i in range(1, 31):
        if(i%n==0):
            numbers.append(i)
    return numbers, len(numbers)

num = []
num, cnt = times()

for i in num:
    print(i, end=" ")
print()

print(f'3의 배수의 개수: {cnt}')