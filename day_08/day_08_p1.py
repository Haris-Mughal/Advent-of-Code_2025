from heapq import heappush, heappop
from math import prod
import sys

K = 1000

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

def k_smallest_pairs_indices(pts, k=K):

    n = len(pts)
    if n < 2:
        return []

    
    heap = [] 

    for i in range(n):
        pi = pts[i]
        for j in range(i+1, n):
            d = squared_dist(pi, pts[j])
            if len(heap) < k:
                heappush(heap, (-d, i, j))
            else:

                if d < -heap[0][0]:
                    heappop(heap)
                    heappush(heap, (-d, i, j))

    pairs = [(i, j) for (_negd, i, j) in heap]
    return pairs

def solveDay_08(filename="day_08.txt", k=K):
    pts = read_points(filename)
    n = len(pts)
    if n == 0:
        print("No points found.")
        return

    pairs = k_smallest_pairs_indices(pts, k)

    dsu = DSU(n)

    for i, j in pairs:
        dsu.union(i, j)

    comp_sizes = {}
    for i in range(n):
        r = dsu.find(i)
        comp_sizes[r] = comp_sizes.get(r, 0) + 1

    sizes = sorted(comp_sizes.values(), reverse=True)

    top3 = sizes[:3]
    while len(top3) < 3:
        top3.append(1)

    result = prod(top3)
    print("Three largest component sizes:", top3)
    print("Product:", result)
    return result

if __name__ == "__main__":

    fname = "day_08.txt"
    k_val = K
    if len(sys.argv) >= 2:
        fname = sys.argv[1]
    if len(sys.argv) >= 3:
        k_val = int(sys.argv[2])
    solveDay_08(filename=fname, k=k_val)
