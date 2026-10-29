def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task1():
    others = likelihood()
    print(f"Minimum likelihood of falling: {others}%")


if __name__ == "__main__":
    run_task1()


#Task 6.

def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task2():
    first = likelihood_min_max()
    print(f"Minimum likelihood of falling: {first[0]}%\n Maximum likelihood of falling: {first[1]}%")


if __name__ == "__main__":
    run_task2()


#Task 7
def steps():
    likelihoods = [
        ("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)
    ]
    return likelihoods


def run_task3():
    first = steps()
    good_steps = []
    bad_steps = []
    for i in first:
        if i[1] < 50:
            good_steps.append(i)
        else:
            bad_steps.append(i)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")


if __name__ == "__main__":
    run_task3()
