number_list = []

for index, number in enumerate(range(3)):
    num = float(input(f"Enter the {index + 1} number: "))
    number_list.append(num)

average = sum(number_list) / len(number_list)
print(round(average, 2))