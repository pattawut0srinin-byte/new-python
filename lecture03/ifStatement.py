#age = int(input("Please input age: "))
#if age >= 18:
    #print("you are adult.")

#num_employees = int(input("Enter the number of employees: "))
#if num_employees < 50:
    #print("This is a small company.")
#elif num_employees < 250:
    #print("This is a medium company.")
#elif num_employees >= 250:
    #print("This is a large company.")

#score = 75
#if score >= 90:
    #print("Grade: A")
#elif score >= 80:
    #print("Grade: B")
#elif score >= 70:
    #print("Grade: C")
#else:
    #print("Grade D or F")

#num_employees = int(input("Enter the number of employees: "))
#if num_employees < 50:
    #print("This is a small company.")
#elif num_employees < 250:
    #print("This is a medium company.")
#else:
    #print("This is a large company.")


#inchar = input("input one charactor: ")
#if inchar >= 'A' and inchar <= 'Z':
    #print("You in put Upper Case Letter ", inchar)
#elif inchar >= 'a' and inchar <= 'z':
    #print("You in put Lower Csae Letter ", inchar)
#elif inchar >= '0' and inchar <='9':
    #print("You in put Number ", inchar)
#else:
    #print("It's not a Letter or Number.", inchar)


#num = float(input("Enter a number: "))
#if num > 0:
    #print("Positive number")
#elif num == 0:
    #print("Zero")
#else:
    #print("Negative number")

#num = float(input("Enter a number: "))
#if num >= 0:
    #if num == 0:
        #print("Zero")
    #else:
        #print("Positive number")
#else:
    #print("Negative number")



#x = 10
#y = 20

#print(x == y)
#print(x != y)
#print(x > y)
#print(x < y)
#print(x >= y)
#print(x <= y)



string1 = "Mary"
string2 = "Mark"
if string1 == string2:
    print(f'"{string1}" and "{string2}" are equal.')
else:
    print(f'"{string1}" and "{string2}" are not equal.')

if string1 < string2:
    print(f'"{string1}" come before "{string2}" in lexicographical order.')
elif string1 > string2:
    print(f'"{string1}" come after "{string2}" in lexicographical order.')

if string1.lower() == string2.lower():
    print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
    print(f'"{string1}" and "{string2}" are not equal when case is ignored.')