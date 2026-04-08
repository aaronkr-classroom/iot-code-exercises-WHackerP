class SayDays:
    def __init__(self, year, month, day):
        self.y = year
        self.m = month
        self.d = day
        
        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if(self.y % 4 == 0 and self.y % 100 != 0) or (self.y % 400 == 0):
            self.is_leap = True
            self.month_days[1] = 29
        else:
            self.is_leap = False
            
    def days(self):
        """ 당해년도 1월 1일 기준으로 몇째 날인지 알려줌 """
        total = sum(self.month_days[:self.m - 1]) + self.d
        return total
    
    def days_left(self):
        """ 당해년도 12월 31일 기준으로 남은 일수를 알려줌 """
        year_total = 366 if self.is_leap else 365
        return year_total - self.days()
    
    def weekday(self):
        """ 숫자로 요일을 알려줌(0 : 토요일) """
        y = self.y
        m = self.m
        d = self.d
        
        """ zeller 계산법에 따르므로 """
        if m < 3:
            m += 12
            y -= 1
        
        k = y % 100
        """ 연도의 마지막 두 자리 """
        j = y // 100
        """ 세기 (앞의 두 자리) """
        
        """ h = (q + [13(m+1)/5] + K + [K/4] + [J/4] -2J) mod 7 """
        h = (d + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
        return h
    
    def weekday_name(self):
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]
    
    week = weekday
    week_name = weekday_name 	# 본문은 week() 와 week_name()으로 출력하라 했으므로 
    
while True:
    print("-" * 30)
    user_input = input("날짜를 입력하세요 (예: 2024 12 09, 종료: q): ")
    
    if user_input.lower() == 'q':		# Q로 입력해도 종료
        print("프로그램을 종료합니다.")
        break
    
    try:
        y, m, d = map(int, user_input.split())
        sd = SayDays(y, m, d)
        
        print(f"[{y}년 {m}월 {d}일 정보]")
        print(f"{y}년 1월 1일 기준: {sd.days()}일째")
        print(f"{y}년 12월 31일 기준 남은 일수: {sd.days_left()}일")
        print(f"요일 숫자 : {sd.week()}")
        print(f"요일을 한글로 바꾸면 : {sd.week_name()}")
    
    except ValueError:
        print("다시 입력해주세요.")