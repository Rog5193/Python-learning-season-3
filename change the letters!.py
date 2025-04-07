string = input("Please enter a sentence!")
to_remove = "aueio"
for char in to_remove:
    string = string.lower()
    lower_cased = string.replace(char,"")
    dot_added = ""
for i in lower_cased:
    dot_added += "." + i
print(dot_added)




