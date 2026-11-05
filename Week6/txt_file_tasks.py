import os
from fileinput import close


def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print(f"The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run():
    print("Processing...")
    cwd()


if __name__ == "__main__":
    run()


#Task 2


def display_chars(path, chars):
    with open(path) as file:
      data = file.read(chars)
      print (data)


def display_line(path):
    with open(path) as file:
        reader = file.readline().strip()
        print (reader)


def display_text(path):
    with open(path) as file:
        reader = file.read()
        print (reader)


def run_task2():
    display_chars("library.txt",5 )
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run_task2()