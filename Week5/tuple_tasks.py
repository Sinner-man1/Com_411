def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)



def run_task1():
    others = likelihood()
    print(f"Minimum likelihood of falling: {others}%")


if __name__ == "__main__":
    run_task1()
