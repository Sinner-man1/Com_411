# Task 3
def listen():
    print("Enter a word representing sound")
    user_input = input()
    print (f"That was a loud {user_input}!")
listen(
)

# Task 4
def identity():
    print("What do you see?")
    user_view = input()
    if user_view == "a large boulder":
        print("it's time to run!")
    else:
        print("We will be fine.")
identity()