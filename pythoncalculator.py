while True:
    try:
        num1 = float(input("Enter a number: "))
        operator = input("Enter an operator (+, -, *, /):")
        num2 = float(input("Enter another number: "))

        def add():
            print(num1 + num2)

        def subtract():
            print(num1 - num2)

        def multiply():
            print(num1 * num2)

        def divide():
            print(num1 / num2)


        if operator == "+":
            add()
        elif operator == "-":
            subtract()
        elif operator  == "*":
            multiply()
        elif operator == "/":
            divide()
        else:
            print("Please enter a valid operator.")
        break
    except ValueError:
        print("Please enter a valid number. Try again.")


