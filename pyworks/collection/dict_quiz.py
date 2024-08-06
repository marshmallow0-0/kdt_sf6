# 실습1

students= {"Alice": 85, "Bob": 90, "Charlie": 95}
students["David"] = 80
students["Alice"] = 88
students.pop("Bob")

for student in students.keys():
    print(f'{student}의 점수는 {students.get(student)}')
