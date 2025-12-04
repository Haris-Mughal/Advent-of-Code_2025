def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible = 0

    deltas = [(-1,-1), (-1,0), (-1,1),
              ( 0,-1),         ( 0,1),
              ( 1,-1), ( 1,0), ( 1,1)]

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] != '@':
                continue
            count_adjacent = 0
            for dy, dx in deltas:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols:
                    if grid[ny][nx] == '@':
                        count_adjacent += 1

                        if count_adjacent >= 4:
                            break
            if count_adjacent < 4:
                accessible += 1

    return accessible


def solvDay_04():
    with open('day_04.txt', 'r') as f:
        grid = [line.rstrip('\n') for line in f if line.strip()]

    result = count_accessible_rolls(grid)
    print(result)


if __name__ == '__main__':
    solvDay_04()
