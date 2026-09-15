try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide bt zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric valuse.")
finally:
    print("Execution completed, whether an excption occurrred or not.")

print("End of program")