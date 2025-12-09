from itertools import combinations


def parse_line(line: str) -> tuple[int, int]:
    a, b = line.strip().split(",")

    return int(a), int(b)


def get_area(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


with open("input.in", "r") as f:
    tiles = [parse_line(l) for l in f.readlines() if l.strip() != ""]
    pairs = sorted(((a, b, get_area(a, b)) for a, b in combinations(tiles, 2)), key=lambda p: p[2], reverse=True)

    print(pairs[0][2])
