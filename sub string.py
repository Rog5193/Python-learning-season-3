user_input = input("Please enter a word: ")
upper_cased = user_input.upper()

sub_string_1 = "ABBA"
sub_string_2 = "BAAB"

if sub_string_1 in upper_cased or sub_string_2 in upper_cased:
    print("Yes!")
else:
    print("No!")