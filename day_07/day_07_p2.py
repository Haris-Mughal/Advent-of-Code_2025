from collections import defaultdict

def solveDay_07(path="day_07.txt"):
    with open(path) as f:
        grid = [line.rstrip("\n") for line in f]

    R = len(grid)
    if R == 0:
        print(0)
        return
    C = len(grid[0])

    start_col = None
    for c, ch in enumerate(grid[0]):
        if ch == "S":
            start_col = c
            break
    if start_col is None:
        raise ValueError("Start 'S' not found in top row")

    active = {start_col: 1}
    finished = 0 

    for r in range(R - 1):
        next_active = defaultdict(int)
        nr = r + 1

        for c, count in active.items():
            if count == 0:
                continue

            if c < 0 or c >= C:
                finished += count
                continue

            cell_below = grid[nr][c]

            if cell_below == '.':
                next_active[c] += count

            elif cell_below == '^':
                if c - 1 >= 0:
                    next_active[c - 1] += count
                else:
                    finished += count

                if c + 1 < C:
                    next_active[c + 1] += count
                else:
                    finished += count

            else:
                next_active[c] += count

        active = dict(next_active)

        if not active:
            break

    if active:
        finished += sum(active.values())

    print(finished)


if __name__ == "__main__":
    solveDay_07()
