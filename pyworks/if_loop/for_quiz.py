# 실습 1
# 1부터 사용자가 입력한 수까지 합계
# 조건: 홀수의 합계
num = int(input("어디까지 계산할까요? "))
result = 0
for i in range(1, num+1):
    if i % 2 == 1:
        result += i
print(f'1부터 {num}까지의 합: {result}')

# 실습 2
num = int(input("몇 초?: "))
for i in range(num, 0, -1):
    print(i, end=" ")
print("발사!!")


