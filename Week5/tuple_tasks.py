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
    likelihoods= (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)



def run_task2():
  first = likelihood_min_max()
  print(f"Minimum likelihood of falling: {first[0]}%\n Maximum likelihood of falling: {first[1]}%")


if __name__ == "__main__":
    run_task2()
