print("What type of adventure should i have?")
user_input = input()
if (user_input == "scary") or (user_input == "short"):
    print("Entering the dark forest!")
elif (user_input == "safe") or (user_input == "long"):
    print("Taking the safe route")
else:
    print("Not sure which route to take.")