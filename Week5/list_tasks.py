from Week2.multiple_conditions import user_input


def direction():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def run_task1():
    print(direction())


if __name__ == "__main__": run_task1()


#Task 2

def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")
    path = movements()
    for i in range(0, len(path), 2):
        print(f"{path[i]} for  {path[i + 1]} steps")


if __name__ == "__main__":
    run_task2()



#Task 3

def menu():
    print("Please select a direction:")
    returned = direction()
    for i in range(len(returned)):
        print(f"{i}: {returned[i]}")


def run_task3():
    return menu()




#Task 4



def menu_and_input():
    print("Please select a direction:")
    returned = direction()
    for i in range(len(returned)):
        print(f"{i}: {returned[i]}")
    user_input = int(input())
    return returned[user_input]




def run_task4():
    route= []
    print("Working out escape route...")
    for i in range(5):
        route.append(menu_and_input())
    print(f"Escape route: {route}")

if __name__ == "__main__":
    run_task4()