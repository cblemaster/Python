
num_days_in_week = 5

mon = float(input('Monday expenses: '))
tue = float(input('Tuesday expenses: '))
wed = float(input('Wednesday expenses: '))
thu = float(input('Thursday expenses: '))
fri = float(input('Friday expenses: '))

week_total = mon + tue + wed + thu + fri
daily_avg = float(week_total / num_days_in_week)

print('You spent $', week_total, sep = '')
print('Your dai;y average was $', daily_avg, sep = '')
