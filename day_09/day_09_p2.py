from collections import defaultdict

def build_allowed_intervals(filename):
    red = []
    with open(filename) as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            red.append((x, y))

    n = len(red)
    intervals_by_row = defaultdict(list)

    for i in range(n):
        x1, y1 = red[i]
        x2, y2 = red[(i + 1) % n]

        if x1 == x2: 
            ymin, ymax = min(y1,y2), max(y1,y2)
            for y in range(ymin, ymax+1):
                intervals_by_row[y].append((x1, x1))
        elif y1 == y2:
            xmin, xmax = min(x1,x2), max(x1,x2)
            intervals_by_row[y1].append((xmin, xmax))
        else:
            raise ValueError("Edges must be axis-aligned!")

    min_y = min(y for _,y in red)
    max_y = max(y for _,y in red)
    edges = [(red[i], red[(i+1)%n]) for i in range(n)]

    for y in range(min_y, max_y+1):
        x_intersections = []
        for (x1,y1),(x2,y2) in edges:
            if y1 == y2: continue
            if (y1 <= y < y2) or (y2 <= y < y1):

                x_int = x1 + (y - y1) * (x2 - x1) // (y2 - y1)
                x_intersections.append(x_int)
        x_intersections.sort()
        for j in range(0, len(x_intersections), 2):
            if j+1 < len(x_intersections):
                intervals_by_row[y].append((x_intersections[j], x_intersections[j+1]))

    def merge_intervals(intervals):
        if not intervals: return []
        intervals.sort()
        merged = [intervals[0]]
        for s,e in intervals[1:]:
            last_s, last_e = merged[-1]
            if s <= last_e + 1:
                merged[-1] = (last_s, max(last_e, e))
            else:
                merged.append((s,e))
        return merged

    for y in intervals_by_row:
        intervals_by_row[y] = merge_intervals(intervals_by_row[y])

    return red, intervals_by_row

def largest_rectangle(red, intervals_by_row):
    max_area = 0
    n = len(red)
    
    for i in range(n):
        x1, y1 = red[i]
        for j in range(i+1, n):
            x2, y2 = red[j]
            if x1 == x2 or y1 == y2: continue 

            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)

            valid = True
            for y in range(min_y, max_y+1):
                row_intervals = intervals_by_row.get(y, [])

                covered = any(s <= min_x and e >= max_x for s,e in row_intervals)
                if not covered:
                    valid = False
                    break

            if valid:
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                if area > max_area:
                    max_area = area

    return max_area

def solveDay_09():
    red, intervals_by_row = build_allowed_intervals("day_09.txt")
    result = largest_rectangle(red, intervals_by_row)

    print(f"{result}")

if __name__ == "__main__":
    solveDay_09()
