# 다중 if 실습
# 점수가 마이너스일 경우 "올바른 점수를 입력해주세요."
score = int(input("점수 입력: "))
grade = "" #빈 문자열

# if score < 0:
#     print("올바른 점수를 입력해주세요")
#     exit()
'''
if score > 0:
    if score >= 90:
        # print("A 등급")
        grade = "A"
    elif 80 <= score and score < 90:
        grade = "B"
    elif 70 <= score and score < 80:
        grade = "C"
    elif 69 <= score and score < 70:
        grade = "D"
    elif score < 60:
        grade = "E"
    print(f'{grade} 등급입니다.')
else:
    print("올바른 점수를 입력해주세요")
'''
if score < 0:
    print("올바른 점수를 입력해주세요.")
else:
    if score >= 90:
        # print("A 등급")
        grade = "A"
    elif 80 <= score and score < 90:
        grade = "B"
    elif 70 <= score and score < 80:
        grade = "C"
    elif 69 <= score and score < 70:
        grade = "D"
    elif score < 60:
        grade = "E"
    print(f'{grade} 등급입니다.')