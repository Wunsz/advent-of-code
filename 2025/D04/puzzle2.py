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


def is_roll(grid: list[list[str]], pos: tuple[int, int], direction: tuple[int, int]) -> bool:
    return (
            0 <= pos[0] + direction[0] < len(grid) and
            0 <= pos[1] + direction[1] < len(grid[0]) and
            grid[pos[0] + direction[0]][pos[1] + direction[1]] == "@"
    )


with open("input.in", "r") as f:
    grid = [[c for c in line.strip()] for line in f.readlines() if line.strip()]

    removed_rolls = 0
    rolls_to_remove = []
    while True:
        for y, line in enumerate(grid):
            for x, cell in enumerate(line):
                if cell != "@":
                    continue

                if sum(1 for direction in directions if is_roll(grid, (y, x), direction)) < 4:
                    rolls_to_remove.append((y, x))

        if len(rolls_to_remove) == 0:
            break

        for y, x in rolls_to_remove:
            grid[y][x] = "."

        removed_rolls += len(rolls_to_remove)
        rolls_to_remove = []

    print(removed_rolls)
