def get_largest_joltage(line: str) -> int:
    max_joltage = 0

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            joltage = int(line[i] + line[j])

            if joltage > max_joltage:
                max_joltage = joltage

    return max_joltage

with open("input.in", "r") as f:
    total_output = sum(
        get_largest_joltage(line.strip()) for line in f.readlines()
    )

    print(total_output)


