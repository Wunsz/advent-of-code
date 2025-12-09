from __future__ import annotations
from itertools import combinations

type Point = tuple[int, int]


def parse_line(line: str) -> Point:
    a, b = line.strip().split(",")

    return int(a), int(b)


def get_area(a: Point, b: Point) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def get_line(a: Point, b: Point) -> set[Point]:
    line = set()
    x1, x2 = min(a[0], b[0]), max(a[0], b[0])
    y1, y2 = min(a[1], b[1]), max(a[1], b[1])

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            line.add((x, y))

    return line


def get_perimeter(tiles: list[Point]) -> set[Point]:
    perimeter = set()

    for i in range(1, len(tiles)):
        l = get_line(tiles[i - 1], tiles[i])
        perimeter |= l

    perimeter |= get_line(tiles[-1], tiles[0])

    return perimeter


def is_inside(a: Point, b: Point, perimeter: set[Point]) -> bool:
    x1, x2 = min(a[0], b[0]), max(a[0], b[0])
    y1, y2 = min(a[1], b[1]), max(a[1], b[1])

    for sx, sy in perimeter:
        if (x1 < sx < x2) and (y1 < sy < y2):
            return False
    return True


with open("input.in", "r") as f:
    tiles = [parse_line(l) for l in f.readlines() if l.strip() != ""]
    perimeter = get_perimeter(tiles)

    areas = sorted(
        ((a, b, get_area(a, b)) for a, b in combinations(tiles, 2)),
        key=lambda p: p[2],
        reverse=True
    )

    print(next(area for a, b, area in areas if is_inside(a, b, perimeter)))
