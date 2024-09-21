
purchase_amt = (float(input('Enter Amount of purchase: $')))
raw_tax = (float(input('Enter Tax percentage (e.g., 6.85): ')))
tax_amt = round(purchase_amt * raw_tax / 100, 2)
total = round(purchase_amt + tax_amt, 2)

print('Total tax: $' + str(tax_amt))
print('Amount of purchase plus Total tax: $' + str(total))
