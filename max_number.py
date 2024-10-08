number_list = []

for index, number in enumerate(range(3)):
    num = float(input(f"Enter the {index + 1} number: "))
    number_list.append(num)

print(number_list)
print(f"The largest of the three number is {max(number_list)}")
