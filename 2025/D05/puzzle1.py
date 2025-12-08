with open("input.in", "r") as f:
    ingredients: list[int] = []
    ranges: list[tuple[int, int]] = []

    for line in f.readlines():
        if "-" in line:
            start, end = line.strip().split("-")

            ranges.append((int(start), int(end)))
        elif line.strip():
            ingredients.append(int(line.strip()))



    print(
        sum(1 for i in ingredients if any(start <= i <= end for start, end in ranges))
    )
