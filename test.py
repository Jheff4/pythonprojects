def computepay(h,r):
    if h>40:
        p=(h-40)*(r*1.5)+(40*r)
    else:
        p=h*r
    return p

hrs = input("Enter Hours:")
hr = float(hrs)
rate = input("Enter Rate:")
rt = float(rate)

p = computepay(hr,rt)
print("Pay=",p)
