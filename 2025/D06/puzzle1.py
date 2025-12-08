import operator
import re
from collections.abc import Callable
from functools import reduce

with open("input.in", "r") as f:
    lines = [
        re.sub(r'\s+', ' ', line.strip()).split(" ") for line in f.readlines()
    ]

    problems: list[tuple[list[int], Callable[[int, int], int]]] = [
        (
            [int(line[i]) for line in lines[:-1]],
            operator.mul if lines[-1][i] == "*" else operator.add
        ) for i in range(len(lines[0]))
    ]

    result = sum(
        reduce(o, elements) for elements, o in problems
    )

    print(result)
