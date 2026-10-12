from hashlib import md5

loop = True
puzzle_input = "ckczppom"  


x = 0
while True:
    attempt = puzzle_input + str(x)
    result = md5(attempt.encode("utf-8")).hexdigest()
    if result[0:6] == "000000":
        print(x)
        break
    if x > 9999999999:
        print("no reasonable number found")
        break
    x += 1