from math import prod

def solveDay_06():
    with open("day_06.txt", "r", encoding="utf-8") as f:
        rows = [line.rstrip("\n") for line in f]

    width = max(len(r) for r in rows)
    rows = [r.ljust(width) for r in rows]

    n_rows = len(rows)
    op_row = n_rows - 1 

    grand_total = 0
    col = 0

    while col < width:
        if all(rows[r][col] == " " for r in range(n_rows)):
            col += 1
            continue

        block_cols = []
        while col < width and not all(rows[r][col] == " " for r in range(n_rows)):
            block_cols.append(col)
            col += 1

        ops = [rows[op_row][c] for c in block_cols if rows[op_row][c] in "+*"]
        op = ops[0] 

        nums = []
        for c in block_cols:
            digits = "".join(rows[r][c] for r in range(op_row)).strip()
            if digits:
                nums.append(int(digits))

        if op == "+":
            result = sum(nums)
        else:
            result = prod(nums)

        grand_total += result

    print(grand_total)


if __name__ == "__main__":
    solveDay_06()