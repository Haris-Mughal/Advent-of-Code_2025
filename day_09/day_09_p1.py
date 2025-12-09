def solveDay_09():
    points = []
    with open("day_09.txt") as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            points.append((x, y))

    n = len(points)
    max_area = 0

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    for i in range(n):
        x1, y1 = xs[i], ys[i]
        for j in range(i + 1, n):
            dx = abs(x1 - xs[j])
            dy = abs(y1 - ys[j])

            if dx == 0 or dy == 0:
                continue

            area = (dx + 1) * (dy + 1)
            if area > max_area:
                max_area = area

    print(max_area)


if __name__ == "__main__":
    solveDay_09()
