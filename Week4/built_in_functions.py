print( "Program Started!")
print( "Please enter a standard character:")
standard_char = input()
if len(standard_char) == 1:
    print(f"The ASCII code for {standard_char} is {ord(standard_char)}.")
else:
    print("Character is more than or less than one.")
print("Program Ended!")

# Task 2

print( "Program Started!")
print( "Please enter an ASCII code:")
standard_char = abs(int(input()))
if standard_char in range (32, 127):
    print(f"The character represented by the ASCII code {standard_char} is {chr(standard_char)}.")
else:
    print("Character is wrong.")
print("Program Ended!")



