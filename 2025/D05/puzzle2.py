with open("input.in", "r") as f:
    ranges: list[tuple[int, int]] = []

    for line in f.readlines():
        if "-" in line:
            start, end = line.strip().split("-")

            ranges.append((int(start), int(end)))

    ranges = sorted(ranges, key=lambda x: x[0])

    ingredients = 0
    previous_end = 0

    for start, end in ranges:
        if end <= previous_end:
            # Whole overlap
            continue

        if previous_end < start:
            # No overlap
            ingredients += end - start + 1
            previous_end = end
        else:
            # Partial overlap
            ingredients += end - previous_end
            previous_end = end

    print(ingredients)
