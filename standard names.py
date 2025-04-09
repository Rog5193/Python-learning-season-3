names = []
def standard(name):
    lowered_case = name.lower()
    capitaled_case = lowered_case.capitalize()
    return capitaled_case

number_of_guests = int(input("Please enter the number of guests: "))
while number_of_guests > 0:
    name = input("please enter the guest name: ")
    names.append(name)
    number_of_guests -= 1

for guest_name in names:
    print(standard(guest_name))
