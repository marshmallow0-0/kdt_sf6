import datetime

# now = datetime.datetime.now()
now = datetime.datetime.today()
print(now)

print(now.year)   #년
print(now.month)  #월
print(now.day)    #일
print(now.hour)   #시
print(now.minute) #분
print(now.second) #초

# 날짜만 출력
print(f'{now.year}--{now.month}--{now.day}')

# 시간 출력
print(f'{now.hour}:{now.minute}:{now.second}')

# 2023년 7월 31일 출력
the_day = datetime.date(2024, 7, 31)
print(the_day)

# 오늘 날짜만 출력
today = datetime.date.today()
print("★ 지금까지 몇 일? ★ ")
passed_time = today-the_day
print(passed_time)
print(f'개강 이후 {passed_time.days}일 지났습니다.')

# 추석까지 D-day 사용해서 구현
print("♠ 추석까지 몇 일? ♠")
the_day = datetime.date(2024, 9, 17)
today = datetime.date.today()
remaining_day = the_day - today
print(f'D-{remaining_day.days}일 남았습니다.')