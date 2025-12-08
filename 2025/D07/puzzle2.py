from functools import cache


@cache
def traverse(beam: int, lines: tuple[str]) -> int:
    if len(lines) == 0:
        return 1

    if lines[0][beam] == "^":
        return traverse(beam - 1, lines[1:]) + traverse(beam + 1, lines[1:])

    if lines[0][beam] == ".":
        return traverse(beam, lines[1:])

    raise Exception("Invalid input!")

with open("input.in", "r") as f:
    lines = tuple([line for line in f.readlines() if line.strip() != ""])
    beams: set[int] = set()

    start_index = lines[0].index("S")

    result = traverse(start_index, lines[1:])

    print(result)
