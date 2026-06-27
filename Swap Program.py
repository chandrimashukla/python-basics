def swap_variables(a, b):
    try:
        print(f"Before swap: a = {a}, b = {b}")

        a, b = b, a

        print(f"After swap: a = {a}, b = {b}")

    except ValueError as e:
        print("Invalid input")

        return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
swap_variables(a, b)






