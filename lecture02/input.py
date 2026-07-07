#first_name = input('Enter you first name: ')
#last_name = input('Enter you last name: ')
#print('Hello', first_name , last_name)

name = input('What is your name? ')
age = int(input('What is your age '))
income = float(input('What is your income? '))

print('Here is the data you entered: ')
print('Name: ',name)
print('Age: ',age)
print('Income: ',format(income, '12,.2f'))