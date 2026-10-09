with open("2015/1.txt", "+r") as file:
    f = file.read()


floor = 0
basment = False
for i, c in enumerate(f, 1):
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
    if floor <= -1 and not basment:
        print(f"Santa enters basment at position {i}")
        basment = True

print(f"santa ends at floor {floor}")