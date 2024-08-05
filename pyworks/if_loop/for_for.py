#중첩 for
# for i in range(1, 5):
#     for j in range(1, 5):
#         print("가", end=" ")
#     print()
#
# for i in range(1, 5):
#     for j in range(1, 5):
#         print("*", end=" ")
#     print()

"""
*
**
***
****
"""

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

print("====================")
print("="*20)
for i in range(1, 5):
    print("*"*i)
print()

"""
****
***
**
*
"""
# for i in range(1, 5):
#     for j in range(5, i, -1):
#         print("*", end="")
#     print()

print("*" * 20)
for i in range(1, 5):
    print("*"*(5-i))

"""
   *
  **
 ***
****
"""
for i in range(1, 5):
    print(" "*(5-i)+"*"*i)
"""
    *
   **
  ***
 ****
"""

# 숫자가 연속으로 증가하는 알고리즘
for i in range(0, 4):
    for j in range(1, 5):
        num = i * 4 + j
        if num > 15:
            break
        print(i*4+j, end=" ")
    print()
# 4의 배수 + 1~4 더함
'''
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''