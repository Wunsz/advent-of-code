with open("input.in", "r") as f:
    ranges: list[tuple[int, int]] = [
        (int(s), int(e)) for s, e in (r.split('-') for r in f.readline().strip().split(","))
    ]

    sum_of_invalid_ids = 0

    for start, end in ranges:
        for number in range(start, end + 1):
            string = str(number)

            if len(string) % 2 != 0:
                continue

            substr_len = len(string) // 2

            if string[:substr_len] == string[substr_len:]:
                sum_of_invalid_ids += number

    print(sum_of_invalid_ids)
