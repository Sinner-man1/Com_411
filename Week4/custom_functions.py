# Task 3
def listen():
    print("Enter a word representing sound")
    user_input = input()
    print(f"That was a loud {user_input}!")


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


# Task 5
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")


# Task 6
def cross_bridge(steps):
    print("Crossed step \n" * steps, end="")

    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("we must keep going!")


cross_bridge(3)
cross_bridge(6)


# Task 7
def climb_ladder(gunclimbed, climbed):
    if unclimbed > climbed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)
