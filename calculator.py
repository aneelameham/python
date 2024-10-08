number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
symbol = input("Enter the second number (+, -, /, *): ")

match symbol:
    case '+':
        add = number1 + number2
        print(f"result of the numbers is {add}")
    case '-':
        add = number1 - number2
        print(f"result of the numbers is {add}")
    case '/':
        add = number1 / number2
        print(f"result of the numbers is {add}")
    case '*':
        add = number1 * number2
        print(f"result of the numbers is {add}")
    case _:
        print(f"Bad operator")
