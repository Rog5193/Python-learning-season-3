summation = input("What summation are you trying to solve? ")
to_remove = "+"
for char in to_remove:
    removed_sum = summation.replace(char,"")
sorted_chars = sorted(removed_sum)
sorted_sum = sorted_chars[0]
for i in sorted_chars[1:]:
    sorted_sum += "+" + i

print(sorted_sum)