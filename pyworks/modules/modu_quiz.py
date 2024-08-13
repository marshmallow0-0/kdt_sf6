# 실습 1
import random

random_numbers = list()
for i in range(4):
    random_number = random.randint(1, 100)
    random_numbers.append(random_number)

random_numbers.sort()

print(random_numbers)
import random


# 실습2
lotto_numbers = list()
cnt = 0
while True:
    lotto_number = random.randint(1, 45)
    if lotto_number not in lotto_numbers:
        lotto_numbers.append(lotto_number)
        cnt += 1
    if cnt == 6:
        break
        
lotto_numbers.sort()

print(lotto_numbers)

# lotto = []
#
# for i in range(6):
#     n = random.randint(1, 45)
#     if n not in lotto: #중복 방지
#         lotto.append(n)
#
#
# lotto.sort()
# print(lotto)

lotto = []
while len(lotto) < 6:
    print(len(lotto)) # 중복확인
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)

lotto.sort()
print(lotto)