import random
import time


# 메모장 파일 읽어오기
# 단어 읽기 - 랜덤하게 추출
with open('words.txt', 'r') as f:
    # print(f.read())
    word = f.read().split() #공백 문자로 구분(리스트로 반환)
    # print(random.choice(data))

n = 1 #문제 번호(1~10)
input("[타자 게임] 준비되면 엔터!")
start = time.time()
while n < 11:
    print("문제", n)
    question = random.choice(word) #단어 출제
    print(question)
    user = input() #유저가 단어 입력
    if user == question:
        print("통과!!")
        n += 1 #다음 문제 출제
    else:
        print("오타!, 다시 도전!")
end = time.time()
et = end-start
print(f"게임 소요 시간: {et: .2f}초")
print("프로그램이 종료")
# with open("word.txt", "r") as f:
#     word = f.read().split()