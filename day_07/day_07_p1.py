def solveDay_07():
    with open("day_07.txt") as f:
        grid = [list(line.rstrip("\n")) for line in f]

    R = len(grid)
    C = len(grid[0])

    start_col = grid[0].index("S")

    active = {start_col}

    splits = 0

    for r in range(R - 1):
        next_active = set()

        for c in active:
            nr = r + 1

            if 0 <= c < C:
                cell = grid[nr][c]

                if cell == '.':
                    next_active.add(c)

                elif cell == '^':
                    splits += 1

                    if c - 1 >= 0:
                        next_active.add(c - 1)

                    if c + 1 < C:
                        next_active.add(c + 1)

                else:
                    next_active.add(c)

        active = next_active

        if not active:
            break

    print(splits)

if __name__ == "__main__":
    solveDay_07()
