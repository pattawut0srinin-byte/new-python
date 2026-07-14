hwork = int(input("Enter your hourswork: "))
payrate = int(input("Enter payrate: "))

if hwork <= 40:
    pay = hwork * payrate
else:
    pay = 