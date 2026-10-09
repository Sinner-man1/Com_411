print("What type of cover does the book have(hard/soft)?")
Cover_type = input()
if Cover_type == "soft":
    print("Is the book perfect-bound?")
    bound_type = input()
    if bound_type   == "yes":
        print("soft cover, perfect bound books are very popular!")
    else:
        print("soft cover with coils and stitches are great for sort books")
else:
    print("Books with hard covers can be more expensive!")


print("You are looking for your phone...It was literally in your hand a second ago!")
print("Where should i look?")
look = input()
if look == "in the bedroom":
    print("Where in the  bedroom should I look?")
    bed_location = input()
    if bed_location == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone")
if look == "in the bathroom":
    print("Where in the bathroom should I look?")
    bathroom_location = input()
    if bathroom_location == "in the bathtub ":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone")
if look == "in the living room":
    print("Where in the living room should I look?")
    living_location = input()
    if living_location == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone!")
else:
    print("I do not know where that is but i will keep looking")



