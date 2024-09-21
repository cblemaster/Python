age = int(input("How old are you?\n"))

decade_len = 10

decades_dec = round(float(age / decade_len), 2)
decades = age // decade_len
years = age % decade_len

if decades == 1:
      decades_word = " decade"
else:
      decades_word = " decades"
if years == 1:
      years_word = " year"
else:
      years_word = " years"

print("You are " + str(decades_dec) + decades_word + " old.")
print("Put another way, you are " + str(decades) + decades_word + " and " + str(years) + years_word + " old.")
