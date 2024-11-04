num = []

for index, number in enumerate(range(3)):
    # num[index] = float(input(f"Enter {index + 1} number: "))
    num.append(float(input(f"Enter {index + 1} number: ")))

if num[1] < num[0] > num[2]:
    print(f"Number {num[0]} is greater, if 1")
elif num[0] < num[1] > num[2]:
    print(f"Number {num[1]} is greater, if 2")
elif num[0] < num[2] > num[1]:
    print(f"Number {num[2]} is greater, if 3")
