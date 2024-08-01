# 실습1
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")
print(f'안녕하세요! {name}님 ({age})세')

# 실습2
try:
    name = input("이름을 입력하세요.")
    birth_year = int(input("태어난 년도를 입력하세요."))
    current_year = int(input("올해 년도를 입력하세요."))
    age = current_year - birth_year + 1
    print(f"올해는{current_year}년,{name}님의 나이는{age}세 입니다.")
except ValueError:
    print("숫자로 입력해주세요")
