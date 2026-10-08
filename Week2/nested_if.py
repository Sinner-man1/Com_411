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




