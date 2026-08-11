numbers = [4,2,9,1,5,6]

length = len(numbers)
print(f"Length og the list: {length}")

total_sum = sum(numbers)
print(f"Sum of all elements: {total_sum}")

max_value = max(numbers)
print(f"Maximun value: {max_value}")

min_value = min(numbers)
print(f"Minimun value: {min_value}")

sorted_number = sorted(numbers)
print(f"Sorted list: {sorted_number}")

bool_list = [False,True,False]
any_true = any(bool_list)
print(f"Is any element True? {any_true}")

all_true = all(bool_list)
print(f"Are all element True? {all_true}")

string = 'hello'
char_list = list(string)
print(f"List of characters: {char_list}")

reversed_numbers = list(reversed(numbers))
print(f"Reversed list: {reversed_numbers}")

enumerate_numbers = list(enumerate(numbers))
print(f"Enumerated list: {enumerate_numbers}")