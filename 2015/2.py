from pprint import pprint as print
"""
with open("2015/2.txt", "+r") as file:
    puzzle_input = file.read()
"""

puzzle_input = """2x3x4"""

dimentions = [ [int(dimention) for dimention in line.split("x") ]  for line in  puzzle_input.split("\n")  ]


L = 0
for present in dimentions:
    c =  (present[0] * present[1], present[1] * present[2], present[0] * present[2])
    L += (sum(c) * 2 + min(c))

print(f"Part one: {L}")