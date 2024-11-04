import os
import glob


def list_files():
    path = input("Enter the path: ")
    if not os.path.isdir(path):
        return print("Its not a directory")

    extension = input("Enter the filename: ")

    filenames = glob.glob(path + extension)

    for file in filenames:
        print(file)


list_files()
