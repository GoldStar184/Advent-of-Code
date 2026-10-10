from pprint import pprint as print

with open("2015/2.txt", "+r") as file:
    puzzle_input = file.read()


#puzzle_input = """2x3x4"""

dimentions = [ [int(dimention) for dimention in line.split("x") ]  for line in  puzzle_input.split("\n")  ]


part_one = 0
part_two = 0
for present in dimentions:
    c =  (present[0] * present[1], present[1] * present[2], present[0] * present[2])
    part_one += (sum(c) * 2 + min(c))


    b = (sum(present) - max(present)) * 2
    b += present[0] * present[1] * present[2] 

    part_two += b

print(f"Part one: {part_one}")
print(f"Part two: {part_two}")


