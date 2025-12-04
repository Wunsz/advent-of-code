directions = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def is_roll(grid: list[str], pos: tuple[int, int], direction: tuple[int, int]) -> bool:
    return (
            0 <= pos[0] + direction[0] < len(grid) and
            0 <= pos[1] + direction[1] < len(grid[0]) and
            grid[pos[0] + direction[0]][pos[1] + direction[1]] == "@"
    )


with open("input.in", "r") as f:
    grid = [line.strip() for line in f.readlines() if line.strip()]

    accessible_rolls = 0
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell != "@":
                continue

            if sum(1 for direction in directions if is_roll(grid, (y, x), direction)) < 4:
                accessible_rolls += 1

    print(accessible_rolls)
