largest = None
smallest = None
zork = 0
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        num=float(num)
    except:
        print('Invalid input')
        continue

    zork=zork+num

    if largest is None:
        largest=num
    elif largest<num:
        largest=num

    if smallest is None:
        smallest=num
    elif smallest>num:
        smallest=num

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
print('Total is',int(zork))
