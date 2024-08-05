# while True: 무한반복문 - if ~ break(빠져나옴)
"""
while True:
    lunch = input("오늘 점심 메뉴? ")
    print(lunch + "!!")
    if lunch == "그만":
        break
print("Done")
"""

# 1부터 10까지 출력하기
count = 0
while True:
    count+=1
    if(count > 10):
        break
    print(count, end=" ")
print("끝")

