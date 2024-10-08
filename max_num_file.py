number = []

with open("numbers.txt", "r+") as file:
    for line in file:
        line = float(line.strip())
        number.append(line)

print(f"The largest number in the file is: {max(number)}")
