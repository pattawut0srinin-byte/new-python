def my_function():
    local_variable = "I'm inside the function"
    print(local_variable)

my_function()



global_variabel = "I'm outside the function"

def my_function():
    print(global_variabel)

my_function()

print(global_variabel)



import random

HEADS = 1
TAILS = 2
TOSSES = 10

def tosses_coin():
    for toss in range(TOSSES):
        if random.randint(HEADS,TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

tosses_coin()



counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()

print(counter)
