def get_largest_battery(line: str, min_index: int, max_index: int) -> tuple[int, str]:
    return max(((i, b) for i, b in enumerate(line[min_index:max_index + 1])), key=lambda x: x[1])

def get_largest_joltage(line: str) -> int:
    joltage = ""

    range_start = 0
    range_end = len(line) - 11

    for i in range(0, 12):
        index, battery = get_largest_battery(line, range_start, range_end)

        range_start = index + range_start + 1
        range_end = len(line) - (11 - i)

        joltage += battery

    return int(joltage)

with open("input.in", "r") as f:
    total_output = sum(
        get_largest_joltage(line.strip()) for line in f.readlines()
    )

    print(total_output)
