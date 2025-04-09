user_input = input("Please enter a word: ")

lowered_case = user_input.lower()

if lowered_case == lowered_case[::-1]:
    print("palindrome")
else:
    print("not palindrome")