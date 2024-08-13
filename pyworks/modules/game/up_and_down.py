# 숫자 추측 게임 - 1부터 100 사이
import random

# 컴의 랜덤값
com = random.randint(1, 100)
min_v = 1
max_v = 100
print(com)
while True:
    try:
        guess = int(input(f"숫자 입력: (%d ~ %d): " % (min_v, max_v)))
        if guess < 0 or guess > 100:
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답입니다.")
            break
        elif com > guess:
            min_v = guess
            print("랜덤수보다 작아요")
        else:
            max_v = guess
            print("랜덤수보다 커요")
    except ValueError:
        print("숫자만 입력 가능합니다.")
