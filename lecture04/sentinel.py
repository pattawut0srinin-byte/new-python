keep_going = 'y'
while keep_going == 'y':
    wholesale = float(input("Enter the item's wholesale cost: "))
    retailprice = wholesale * 2.5
    print(f'The retailprice is ${retailprice:.2f}')
    keep_going = input('Do you want to calculate another' + \
                       'retailprice (Enter y for yes): ')