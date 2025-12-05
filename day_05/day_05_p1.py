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
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def count_fresh_ids(merged, ingredients):
    import bisect

    starts = [s for s, _ in merged]

    fresh_count = 0
    for x in ingredients:
        idx = bisect.bisect_right(starts, x) - 1
        if idx >= 0 and merged[idx][0] <= x <= merged[idx][1]:
            fresh_count += 1
    return fresh_count


def solveDay_05():
    with open("day_05.txt") as f:
        lines = f.read().strip().splitlines()

    blank_index = lines.index("")
    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    ranges = parse_ranges(range_lines)
    merged = merge_ranges(ranges)

    ingredients = [int(x) for x in id_lines]

    result = count_fresh_ids(merged, ingredients)
    print(result)


if __name__ == "__main__":
    solveDay_05()
