positions = [
    int(input("Enter position 1: ")),
    int(input("Enter position 2: ")),
    int(input("Enter position 3: "))
]

distance_covered = max(positions) - min(positions)
print("Shortest distance for the friends to meet:", distance_covered)