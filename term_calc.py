while True:
    number = input("Enter a number expression: ").split(" ")
    if number[0].lower() == 'exit':
        exit()
    elif number[1] == '+':
        add = float(number[0]) + float(number[2])
        print(add)
    elif number[1] == '-':
        sub = float(number[0]) - float(number[2])
        print(sub)
    elif number[1] == '/':
        sub = float(number[0]) / float(number[2])
        print(sub)
    elif number[1] == '*':
        sub = float(number[0]) * float(number[2])
        print(sub)
