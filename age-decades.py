
age = int(input('Enter your age in years:\n'))

decades_decimal = float(age/10)
decades = int(decades_decimal)
years = age % 10

decades_descriptor = ''
if decades == 1:
    decades_descriptor = ' decade'
else:
    decades_descriptor = ' decades'
years_descriptor = ''
if years == 1:
    years_descriptor = ' year'
else:
    years_descriptor = ' years'

print('You are ' + str(decades_decimal) + decades_descriptor + ' old.')
print('Put another way, you are ' + str(decades) + decades_descriptor + ' and ' + str(years) + years_descriptor +  ' old.')
