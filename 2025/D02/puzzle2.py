def get_factors(n: int) -> list[tuple[int, int]]:
    factors = []
    for i in range(1, int(n)):
        if n % i == 0:
            factors.append((n // i, i))

    return factors


def is_repeated(string: str) -> bool:
    factors = get_factors(len(string))

    for repeats, length in factors:
        if all(string[0:length] == string[i * length:(i + 1) * length] for i in range(repeats)):
            return True

    return False


with open("input.in", "r") as f:
    ranges: list[tuple[int, int]] = [
        (int(s), int(e)) for s, e in (r.split('-') for r in f.readline().strip().split(","))
    ]

    sum_of_invalid_ids = 0

    for start, end in ranges:
        for number in range(start, end + 1):
            string = str(number)

            if is_repeated(string):
                sum_of_invalid_ids += number

    print(sum_of_invalid_ids)
