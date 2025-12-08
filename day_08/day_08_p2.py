from math import prod

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def read_points(filename="day_08.txt"):
    pts = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                raise ValueError(f"Invalid line (expected 3 values): {line}")
            x, y, z = map(int, parts)
            pts.append((x, y, z))
    return pts

def squared_dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]
    return dx*dx + dy*dy + dz*dz

def solveDay_08(filename="day_08.txt"):
    pts = read_points(filename)
    n = len(pts)
    if n == 0:
        print("No points found.")
        return

    all_pairs = []
    for i in range(n):
        for j in range(i+1, n):
            d = squared_dist(pts[i], pts[j])
            all_pairs.append((d, i, j))
    all_pairs.sort()

    dsu = DSU(n)
    num_components = n
    last_pair = None

    for d, i, j in all_pairs:
        if dsu.union(i, j):
            last_pair = (i, j)
            num_components -= 1
            if num_components == 1:
                break

    if last_pair is None:
        print("All points already connected.")
        return

    x_product = pts[last_pair[0]][0] * pts[last_pair[1]][0]
    print("Last pair connected:", last_pair)
    print("X coordinates:", pts[last_pair[0]][0], pts[last_pair[1]][0])
    print("Product of X coordinates:", x_product)
    return x_product

if __name__ == "__main__":
    import sys
    fname = "day_08.txt"
    if len(sys.argv) >= 2:
        fname = sys.argv[1]
    solveDay_08(filename=fname)
