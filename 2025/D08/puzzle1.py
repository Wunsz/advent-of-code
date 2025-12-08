from __future__ import annotations
from itertools import combinations


class Circuit(set):
    def __hash__(self):
        return hash(tuple(sorted(self)))


class JunctionBox:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

        self.circuit = Circuit()
        self.circuit.add(self)

    def distance(self, other: JunctionBox) -> float:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

    def connect(self, other: JunctionBox):
        self.circuit |= other.circuit

        for box in other.circuit:
            box.circuit = self.circuit

    @classmethod
    def parse(cls, line: str):
        return cls(*map(int, line.split(",")))

    def as_number(self):
        return self.distance(JunctionBox(0, 0, 0))

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.as_number() < other.as_number()

    def __gt__(self, other):
        return self.as_number() > other.as_number()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


if __name__ == "__main__":
    with open("input.in", "r") as f:
        boxes: list[JunctionBox] = [JunctionBox.parse(l) for l in f.readlines() if l.strip() != ""]
        pairs = sorted(((a, b, a.distance(b)) for a, b in combinations(boxes, 2)), key=lambda p: p[2])

        for i in range(1000):
            a, b, _ = pairs[i]

            a.connect(b)

        circuits: set[Circuit] = {box.circuit for box in boxes}

        largest_three = sorted(circuits, key=lambda c: len(c), reverse=True)[:3]

        print(len(largest_three[0]) * len(largest_three[1]) * len(largest_three[2]))
