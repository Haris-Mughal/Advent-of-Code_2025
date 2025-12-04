def solveDay_04():
    with open("day_04.txt") as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    R, C = len(grid), len(grid[0])

    # Directions for the 8 neighbors
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    # Step 1: Precompute adjacent @ counts
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

    # Step 2: Initialize queue with all removable rolls (<4 neighbors)
    from collections import deque
    q = deque()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '@' and adj[r][c] < 4:
                q.append((r, c))

    removed = 0

    # Step 3: BFS-like cascade removal
    while q:
        r, c = q.popleft()
        if grid[r][c] != '@':
            continue  # already removed earlier

        # Remove roll
        grid[r][c] = '.'
        removed += 1

        # Update neighbors
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] == '@':
                    adj[nr][nc] -= 1
                    if adj[nr][nc] == 3:
                        # Now newly removable
                        q.append((nr, nc))

    print(removed)


if __name__ == "__main__":
    solveDay_04()
