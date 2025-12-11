from functools import lru_cache

def solveDay_11():
    graph = {}

    with open("day_11.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            src, dsts = line.split(":")
            src = src.strip()
            dst_list = dsts.strip().split()
            graph[src] = dst_list

    @lru_cache(None)
    def count_paths(node):
        if node == "out":
            return 1
        
        if node not in graph:
            return 0

        total = 0
        for nxt in graph[node]:
            total += count_paths(nxt)
        return total

    return count_paths("you")


if __name__ == "__main__":
    print(solveDay_11())