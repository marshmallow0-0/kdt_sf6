# 실습 5

# sum()
# print(sum([1,2,3])) #6
# print(max([1,2,3])) #3

input_num = input("숫자 입력: ").split(" ")

numbers = []
for i in input_num:
    numbers.append(int(i))

max_num = max(numbers)
min_num = min(numbers)
print("가장 큰 값: ", max_num)
print("가장 작은 값: ", min_num)

numbers_size = len(numbers)-2
numbers_avg = (sum(numbers) - max_num - min_num)/numbers_size

print("나머지 값의 평균", numbers_avg)
