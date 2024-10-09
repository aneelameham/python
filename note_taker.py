notes = []

while True:
    choose = int(input("""Menu:
   1. add a note
   2. view a note
   3. Exit
   Choose any of the option(1, 2, 3): """))

    match choose:
        case 1:
            text = input("Add a note: ")
            notes.append(text)
        case 2:
            for index, note in enumerate(notes):
                print(f"{index}: {note}")
        case 3:
            exit()
