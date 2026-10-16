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


#[Tasks 5] Repeatitive Step 

print("Calculating the sum of the first 100 numbers...")
sum = 0
total = 0
while sum <= 100:
    total += sum
    sum += 1
print(f"...Done! The answer is: {total}")  

# Sum user number 
print( "How many numbers should I sum up?")
user_number = int(input())
sum = 1
total = 0
while sum <= user_number:
    print(f"Please enter number {sum} of {user_number}")
    number = int(input())
    total += number
    sum += 1
print(f"The answer is: {total}")  

   #[Tasks 7]