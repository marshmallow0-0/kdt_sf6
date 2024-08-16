# 실습 1

# f = open("c:/pyfile/gugudan.txt", "w")
#
# for i in range(2,10):
#     for j in range(1, 10):
#         f.write(f'{i} x {j} = {i*j} ')
#         f.write('\n')
#     f.write('\n') #단과 단사이 줄바꿈
# f.close()
#
# f = open("c:/pyfile/gugudan.txt", "r")
# data = f.read()
# print(data)
# f.close()
#
'''
try:
    with open("./source/member.txt", "w") as f:
        for i in range(3):
            name = input("이름: ")
            password = input("비밀번호: ")
            f.write(f'{name} {password}\n')
except FileNotFoundError:
    print("파일을 찾을 수 없음")
'''

try:
    with open("./source/member.txt", "r") as f:
        member = f.read()
        print(member)
except FileNotFoundError:
    print("파일을 찾을 수 없음")

# 실습3
# 로그인
name = input('이름 입력: ')
pw = input('비밀번호 입력: ')
user = name + " " + pw + "\n"

with open("./source/member.txt", "r") as f:
    member_list = f.readlines()
    #print(member_list)

    # 상태 변수 - True/False
    sw = False # 상태 초기화 False
    for member in member_list:  # 리스트를 순회하면서
        if member == user: # 파일에 있는 member의 name, pw와 입력한 user의 name, pw가 일치하면
            sw = True # 상태를 True로 저장

    if sw:
        print("로그인 성공!")
    else:
        print("로그인 실패!")

# member_dict = dict()
# with open("./source/member.txt", "r") as f:
#     member_list = f.readlines()
#     for member in member_list:
#        name, password = member.split()
#        member_dict[name] = password
#
#
# for i in range(3):
#     name2 = input("이름")
#     password2 = input("비밀번호")
#     if member_dict[name2] == password2:
#         print("로그인 성공")
#     else:
#         print("로그인 실패")