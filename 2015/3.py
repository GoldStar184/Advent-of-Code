global positions

with open("2015/3.txt", "+r") as file:
    puzzle_input = str(file.read())


# puzzle_input = "^v^v^v^v^v"



positions = [(0, 0)]




p1 = "".join([i for e, i in enumerate(puzzle_input) if e % 2 == 0])
p2 = "".join([i for e, i in enumerate(puzzle_input) if e % 2 != 0])

print(p1)

assert len(p1) + len(p2) == len(puzzle_input)


def p_map(p_input):
    x = 0
    y = 0
    for direction in p_input:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == "<":
            x -= 1
        elif direction == ">":
            x += 1
        else:
            raise ValueError(f"Did not get a proper direction, got {direction}")

        if not (x, y) in positions:
            positions.append((x,y)) 

p_map(p1)
p_map(p2)


print(len(positions))
    

