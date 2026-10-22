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
def climb_ladder(unclimbed, climbed):
    if unclimbed > climbed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)


# Task 8
def display_ladder(steps):
    for step in range(steps):
        print("| |")
        print("***")


def create_ladder():
    user_input = input()
    steps = int(user_input)
    display_ladder(steps)
    print("| |")


create_ladder()


# Task 9
def sum_weights(weight1, weight2):
    return weight1 + weight2


def calc_avg_weight(weight1, weight2):
     avg_weight = (weight1 + weight2) / 2
     return avg_weight


def run():
    print("What is the weight of the person?")
    weight1 = float(input())
    print("What is the weight of their inventory?")
    weight2 = float(input())
    print("What would you like to calculate (sum or average)?")
    answer = input().lower().strip()
    if answer == "sum":
        action = sum_weights(weight1, weight2)
        print(f"The sum of weights is {action}")
    elif answer == "average":
        action = calc_avg_weight(weight1, weight2)
        print(f"The average of weights is {action}")
    else:
        print("Sorry, I didn't understand.")


run()
