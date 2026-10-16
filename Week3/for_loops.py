print("How many mountains should I display?")
user_input = int(input())
for mountain in range(user_input):
    print("""
          /  \_  
         /^    \ 
        /  ^    \_ 
      _/ ^ ^     ^\ 
     /  ^     ^    \ """,  end=" ")