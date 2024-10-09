filename = "text_file.txt"

for i in range(3):
    text = input("Add text to the file: ")
    with open(filename, 'a+') as file:
        file.writelines(f"{text}\n")
        file.writelines(f"{10 * '-'}\n")

print("all the sentence have been saved to the file successfully")
