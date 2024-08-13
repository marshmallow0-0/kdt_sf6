# try:
#     with open("./source/city.txt", "r") as f:
#         a = []
#         for i in range(6):
#             city = f.readline().split()
#             a.append(city)
#         print(a)
#         for i in a:
#             print(i)
#
# except FileNotFoundError:
#     print("파일을 찾을 수 없습니다.")

with open("./source/city.txt", "r") as f:
    # data = f.readlines()
    # data = f.readline().split()
    # print(data)

    a = [] #2차원 빈 리스트
    for i in range(6):
        data = f.readline().split() #구분 기호(공백)로 요소분리
        a.append(data)
    print(a)
    # 리스트의 요소 출력
    print(a[0])  #['서울']
    print(a[-1]) #['대구']
    print(a[0][0]) #서울
    print(a[-1][0]) #대구

    for i in a:
        print(i)


# with open("./source/member.txt", "w") as f:
#     for i in range(3):
#         name = input("이름: ")
#         password = input("비밀번호: ")
#         f.write(f'{name} {password}\n')
#
# with open("./source/member.txt", "r") as f:
#     member = f.read()
#     print(member)

member_dict = dict()
with open("./source/member.txt", "r") as f:
    member_list = f.readlines()
    for member in member_list:
       name, password = member.split()
       member_dict[name] = password


for i in range(3):
    name2 = input("이름")
    password2 = input("비밀번호")
    if member_dict[name2] == password2:
        print("로그인 성공")
    else:
        print("로그인 실패")
