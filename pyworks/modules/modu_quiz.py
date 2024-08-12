# 실습 1
import random

random_numbers = list()
for i in range(4):
    random_number = random.randint(1, 100)
    random_numbers.append(random_number)

random_numbers.sort()

print(random_numbers)
import random


random_numbers = list()
cnt = 0
while True:
    random_number = random.randint(1, 45)
    if random_number not in random_numbers:
        random_numbers.append(random_number)
        cnt += 1
    if cnt == 6:
        break
        
random_numbers.sort()

print(random_numbers)

