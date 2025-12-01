rotation = 50
zeroes = 0

with open("input.in", "r") as f:
    for line in f.readlines():
        entry = line.strip()

        if not entry:
            continue

        direction = -1 if entry[0] == "L" else 1
        value = int(entry[1:])

        for i in range(value):
            rotation = (rotation + direction) % 100

            if rotation == 0:
                zeroes += 1

    print(zeroes)
