# 연산자(operator)
# 산술 연산 - +, -, *, /, //(몫), %(나머지)
# 입력
n1 = 10
n2 = 4

# 산술 연산 
sum = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2

#출력
#print(n1, n2)
print(sum) #14
print(sub) #6
print(mul) #40
print(div) #2.5
print(n1 // n2)#2
print(n1 % n2) #2


print(n1 ** n2) #10000 거듭제곱
print(2**3)


# 실습 - 빵 30, 사람 - 4
bread = 30
person = 4

bread_cnt = bread//person
bread_remain = bread%person

print(f"빵의 개수: {bread_cnt}")
print(f"남의 빵의 개수 : {bread_remain}")
