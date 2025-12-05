# day05_part2.py

def parse_ranges(lines):
    ranges = []
    for line in lines:
        if not line.strip():
            break
        a, b = map(int, line.split('-'))
        ranges.append((a, b))
    return ranges


def merge_ranges(ranges):
    if not ranges:
        return []
    ranges.sort()
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # overlapping or touching
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def solve():
    with open("day_05.txt") as f:
        lines = f.read().splitlines()

    # Only the first section (fresh ranges) matters
    blank_index = lines.index("")
    range_lines = lines[:blank_index]

    ranges = parse_ranges(range_lines)
    merged = merge_ranges(ranges)

    # Count how many IDs are included in merged ranges
    total_fresh_ids = sum((end - start + 1) for start, end in merged)

    print(total_fresh_ids)


if __name__ == "__main__":
    solve()
