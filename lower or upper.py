word = input("Please enter the word: ")

lower_case_count = 0
upper_case_count = 0

for char in word:
    if char.islower():
        lower_case_count += 1
    else:
        upper_case_count += 1

if lower_case_count > upper_case_count:
    print(word.lower())

elif upper_case_count > lower_case_count:
    print(word.upper())

else:
    print(word.capitalize())