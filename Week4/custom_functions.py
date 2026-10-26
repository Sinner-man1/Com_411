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


# Task 10
print("Please enter a word")
print("Choose on of the following:")
print("""1) Display in a Box – display the word in an ASCII art box /n
2) Display Lower-case – display the word in lower-case e.g. hello /n
3) Display Upper-case – display the word in upper-case e.g. HELLO /n
4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH /n
5) Repeat – ask the user how many times to display the word and then display the 
word that many times alternating between upper-case and lower-case.""")

def display_box(user_input):
    num_dashes = 4 + len(user_input)
    print("-" * num_dashes)
    print(f"| {user_input} |")
    print("-" * num_dashes)



def to_lower(user_input):
    lower = user_input.lower()
    return lower


def to_upper(user_input):
    upper = user_input.upper()
    return upper

user_input = (input())
if user_input == 1:
    display_box(user_input)
elif user_input == 2:
       print(to_lower(user_input))
elif user_input == 3:
        print(to_upper(user_input))
elif user_input == 4:
