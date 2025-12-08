import operator
import re
from collections.abc import Callable
from functools import reduce

with open("input.in", "r") as f:
    lines = [list(line.replace("\n", "")) for line in f.readlines() if line.strip() != ""]

    # Fix missing spaces
    widest_line = max(len(l) for l in lines)
    for line in lines:
        line += " " * (widest_line - len(line))

    problems: list[tuple[list[int], Callable[[int, int], int]]] = []
    numbers: list[int] = []
    operation: Callable[[int, int], int] | None = None

    for i in range(len(lines[0]) - 1, -1, -1):
        if all(lines[l][i] == " " for l in range(len(lines))):
            if operator is None:
                raise Exception("Invalid input!")

            problems.append((numbers, operation))
            numbers = []
            operation = None
        else:
            numbers.append(
                int("".join(line[i] for line in lines[:-1]))
            )

            if lines[-1][i] == "*":
                operation = operator.mul
            elif lines[-1][i] == "+":
                operation = operator.add

    if operation is not None:
        problems.append((numbers, operation))

    result = sum(
        reduce(o, elements) for elements, o in problems
    )

    print(result)
