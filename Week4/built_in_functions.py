print( "Program Started!")
print( "Please enter a standard character:")
standard_char = input()
if len(standard_char) == 1:
    print(f"The ASCII code for {standard_char} is {ord(standard_char)}.")
else:
    print("Character is more than or less than one.")
print("Program Ended!")