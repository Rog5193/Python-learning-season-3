word = input("Please enter the word: ")
lowered = word.lower()

filtered_string = ""
to_keep = {"h": 1, "e": 1, "l": 2, "o": 1}
count = {char: 0 for char in to_keep}

for char in lowered:
    if char in to_keep and count[char] < to_keep[char]:
        filtered_string += char
        count[char] += 1

if filtered_string == "hello":
    print("YES")
else:
    print("NO")
