origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter the discount: '))
discCalc = (1-discount/100) * origPrice
calculation = '${:.2f} discounted by {:.0f}% is ${:.2f}'.format(origPrice, discount, discCalc)
print(calculation)
