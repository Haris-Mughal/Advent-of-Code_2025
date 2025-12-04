def solveDay_04():
    with open("day_04.txt") as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    R, C = len(grid), len(grid[0])

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    adj = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] != '@':
                continue
            cnt = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '@':
                    cnt += 1
            adj[r][c] = cnt

    from collections import deque
    q = deque()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '@' and adj[r][c] < 4:
                q.append((r, c))

    removed = 0

    while q:
        r, c = q.popleft()
        if grid[r][c] != '@':
            continue 

        grid[r][c] = '.'
        removed += 1

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] == '@':
                    adj[nr][nc] -= 1
                    if adj[nr][nc] == 3:
                        q.append((nr, nc))

    print(removed)


if __name__ == "__main__":
    solveDay_04()
