# Conditional Execution
def payment(h,r):
    if h<=40:
        Pay+h*r
    elif h>40:
        Pay=40*r+(h-40)*r*1.5
    return Pay

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter rate:")
r=float(rate)
pay=payment(h,r)
print(pay)
