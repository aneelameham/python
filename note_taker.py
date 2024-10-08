notes = []

while True:
    choose = int(input("Menu:\n"
                       "1. add a note\n"
                       "2. view a note\n"
                       "3. Exit\n"
                       "Choose any of the option(1, 2, 3): "))

    match choose:
        case 1:
            text = input("Add a note: ")
            notes.append(text)
        case 2:
            for index, note in enumerate(notes):
                print(f"{index}: {note}")
        case 3:
            exit()
