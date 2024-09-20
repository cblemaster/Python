mon = float((input('Expenses for Monday: $')))
tue = float((input('Expenses for Tuesday: $')))
wed = float((input('Expenses for Wednesday: $')))
thu = float((input('Expenses for Thursday: $')))
fri = float((input('Expenses for Friday: $')))

total = round(float(mon + tue + wed + thu + fri) , 2)
avg = round(float(total / 5), 2)

print('Your total weekly expenses are: $', str(total))
print('Your average daily expense for the week is: $', str(avg))
