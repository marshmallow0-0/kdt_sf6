# 쿠폰 추첨기
# 추첨 버튼을 누르면 3명이 랜덤하게 출력됨
from tkinter import *

import random

def click():
    namelist = ['김용준', '김용혁', '임현수', '윤종관', '정지은', '오민선',
                '최준영', '윤다빈', '박민우', '조형주', '고지수']
    # result = []
    # cnt = 0
    # final = ""
    # text.delete(0.0, END)
    # # 로또 복권 코드 참조
    # while cnt < 3:
    #     winner = random.choice(namelist)
    #     if winner not in result:
    #         cnt += 1
    #         result.append(winner)
    #
    # for i in result:
    #     final += " " + i
    #
    # text.insert(END, final)
    
    winner = set()
    while len(winner) < 3:
        name = random.choice(namelist)
        winner.add(name)

    text.delete(0.0, END)
    text.insert(END, winner)



window = Tk()
window.title('쿠폰 추첨기')

# 이미지 넣기
lbl_img = Label(window)
# 이미지 객체 생성
img = PhotoImage(file='bronx.png')
# 이미지 넣기 - Label에 이미지 넣음
lbl_img.configure(image=img)
lbl_img.grid(row=0, column=0, sticky=W)

# 추첨 버튼
Button(window, text="추첨", command=click).grid(row=1, column=0, sticky=E)

# 출력 상자(이름)
text = Text(window, width=46, height=4, bg='yellow')
text.grid(row=2, column=0, sticky=W)


window.mainloop()
