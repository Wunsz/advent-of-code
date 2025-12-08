from __future__ import annotations
from itertools import combinations

from puzzle1 import JunctionBox

if __name__ == "__main__":
    with open("input.in", "r") as f:
        boxes: list[JunctionBox] = [JunctionBox.parse(l) for l in f.readlines() if l.strip() != ""]
        pairs = sorted(((a, b, a.distance(b)) for a, b in combinations(boxes, 2)), key=lambda p: p[2])

        last_pair = None
        for a, b, _ in pairs:
            a.connect(b)

            if len(a.circuit) == len(boxes):
                last_pair = (a, b)
                break

        if last_pair is None:
            print("No solution found")
            exit(1)

        a, b = last_pair

        print(a.x * b.x)
