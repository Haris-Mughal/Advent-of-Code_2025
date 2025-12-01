def solve():
    pos = 50
    zero_count = 0

    with open("day_01.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            value = int(line[1:])

            for _ in range(value):
                if direction == 'L':
                    pos = (pos - 1 + 100) % 100
                else:
                    pos = (pos + 1) % 100

                if pos == 0:
                    zero_count += 1

    print(zero_count)


if __name__ == "__main__":
    solve()