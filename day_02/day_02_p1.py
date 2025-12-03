def solveDay_02():

    ranges = []

    with open("day_02.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            for p in parts:
                if p:
                    a, b = map(int, p.split("-"))
                    ranges.append((a, b))

    ranges.sort()
    max_val = max(r[1] for r in ranges)

    invalid_ids = []

    max_digits = len(str(max_val))

    for total_len in range(2, max_digits + 1, 2):
        n = total_len // 2
        start = 10 ** (n - 1)
        end = 10 ** n

        for x in range(start, end):
            cand = int(str(x) + str(x))
            if cand > max_val:
                break
            invalid_ids.append(cand)

    invalid_ids.sort()

    ans = 0
    ri = 0
    rcount = len(ranges)

    for val in invalid_ids:
        while ri < rcount and ranges[ri][1] < val:
            ri += 1
        if ri == rcount:
            break
        if ranges[ri][0] <= val <= ranges[ri][1]:
            ans += val

    print(ans)


if __name__ == "__main__":
    solveDay_02()