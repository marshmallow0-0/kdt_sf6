# 별찍기
for i in range(1, 5):
    print("*"*i)

print("="*25)

# 공백이 먼저인 직각삼각형
for i in range(1, 5):
    print(" "*(5-i)+"*"*i)
print("*"*25)

# 정삼각형
for i in range(5, 1, -1):
    print(" "*i+(2*(5-i)+1)*"*" + " "*i)