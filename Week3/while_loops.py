print("How many apples should I remove?")
user_input = int(input())
removed_apples = 0
while user_input > removed_apples:
    print("Removed apple")
    removed_apples += 1




print("How many obstacles must I avoid?")
user_input1 = int(input())
obstacles = 0
while user_input1 > obstacles:
    print("Avoiding...Done!", end = " ")
    obstacles +=1
    print(f"{obstacles} obstacles avoided")
print("All obstacles have been avoided.")




print("How many bars should be charged?")
user_input2 = int(input())
bars = 0
while user_input2 > bars:
    print("Charging:")
    bars += 1
    print(f"{bars * '█' } bars charged")
print("The battery is fully charged.")





print("Please enter a phrase:")
user_input3 = len(input())
multiple = user_input3 * " hi "
print(multiple)