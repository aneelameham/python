name_list = []
phone_list = []


def contact_func(name_list, phone_list):
    return dict(zip(name_list, phone_list))


def contact_write():
    for key, value in contact_list.items():
        with open("conacts.txt", 'a+') as file:
            file.writelines(f"{key}: {value}\n")

while True:
    name = input("Enter the name of the contact or type done: ")
    if name == 'done':
        contact_list = contact_func(name_list, phone_list)
        contact_write()
        exit()
    elif name:
        phone_number = int(input(f"Enter the phone number of {name}: "))
        name_list.append(name)
        phone_list.append(phone_number)
