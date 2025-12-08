with open("input.in", "r") as f:
    lines = f.readlines()
    beams: set[int] = set()
    splits = 0

    for line in lines:
        if line.strip() == "":
            continue

        for index, char in enumerate(line.strip()):
            if char == "S":
                beams.add(index)

            elif char == "^" and index in beams:
                beams.remove(index)
                splits += 1

                if line[index - 1] == "." and (index - 1) not in beams:
                    beams.add(index - 1)

                if line[index + 1] == "." and (index + 1) not in beams:
                    beams.add(index + 1)
print(splits)
