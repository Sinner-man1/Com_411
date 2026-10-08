print("what type of book is this?")
book_type = input()
if book_type == "adventure":
   print(f"I like {book_type} books!")
print("Finished reading book.")

print("Please enter the activity to be performed:")
activity = input()
if activity == 'calculate':
   print("Performing calculations...")
else :
   print("performing activity...")
print("Activity Completed!")



print("Towards which direction should I go (up, down, left or right)?")
direction = input()
if direction == 'up':
   print("I am moving in an upward direction!")
elif direction == 'down':
   print("I am moving in a downward direction!")
elif direction == 'left':
   print("I am moving in a left direction!")
else:
   print("I am moving in a right direction")


print("Please enter a whole number.")
number = int(input())
if number%2 == 0:
   print(f"The number {number} is an even number.")
else:
   print(f"The number {number} is an odd number.")


print("Please enter the first number")
first_number = int(input())
print("Please enter the second number")
second_number = int(input())
if first_number < second_number:
   print("The first number is the smallest")
elif first_number > second_number:
   print("The second number is the smallest")
else:
   print("Both are equal!")
