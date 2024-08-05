# 자리 배치도
# 고객수 - customer, 좌석열 - column, 행 - row

customer = int(input("고객 수 입력: "))
column = int(input("좌석 열 수 입력: "))

if customer % column == 0:
    row = customer // column
else:
    row = customer // column + 1
print(row)

for i in range(0, row):
    for j in range(1, column + 1):
        num = i * column + j
        if num > customer:
            break
        print(num, end=" ")
    print()
