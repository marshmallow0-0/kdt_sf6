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
try:
    with open("./source/member.txt", "w") as f:
        for i in range(3):
            name = input("이름: ")
            password = input("비밀번호: ")
            f.write(f'{name} {password}\n')
except FileNotFoundError:
    print("파일을 찾을 수 없음")

try:
    with open("./source/member.txt", "r") as f:
        member = f.read()
        print(member)
except FileNotFoundError:
    print("파일을 찾을 수 없음")

# 실습3
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