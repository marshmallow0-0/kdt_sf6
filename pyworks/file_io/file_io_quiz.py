# 실습 1

f = open("c:/pyfile/gugudan.txt", "w")

for i in range(2,10):
    for j in range(1, 10):
        f.write(f'{i} x {j} = {i*j} ')
        f.write('\n')
    f.write('\n') #단과 단사이 줄바꿈
f.close()

f = open("c:/pyfile/gugudan.txt", "r")
data = f.read()
print(data)
f.close()

