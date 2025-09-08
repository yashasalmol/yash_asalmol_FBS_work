def Calculator():
    try:
        num1 = int(input("Enter a number1: "))
        num2 = int(input("Enter a number2 :"))
        operator = input("Enter operator: ")
        
        if operator == "+":
            print("result: ",num1 + num2)
        elif operator == "-":
            print("Result: ",num1 - num2)
        elif operator == "*":
            print("Result: ",num1 * num2)
        elif operator == "/":
            try:
                print("Result: ",num1 / num2)

            except ZeroDivisionError:
                print("Division by zero error")
        else:
            print("Invalid Operator")

    except:
        print("Please enter valid numbers")

Calculator()