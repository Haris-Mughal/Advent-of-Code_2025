#!/usr/bin/env python3
"""
solve_day_10.py

Advent of Code 2025 — Day 10: Factory
Reads 'day_10.txt' and prints the minimal total presses across all machines,
plus per-machine minimal presses.

Approach:
- Represent each button as a bitmask over lights (variables).
- Represent each equation (one per light) as an integer mask of button coefficients.
- Perform Gaussian elimination over GF(2) to obtain a particular solution and
  a basis for the nullspace.
- Enumerate nullspace combinations (with an increasing-weight search) to find
  the minimum-Hamming-weight solution.
"""

import re
import itertools
import sys
from typing import List, Tuple

# --------------------------
# Parsing helpers
# --------------------------
BRACKET_RE = re.compile(r"\[([^\]]*)\]")
PAREN_RE = re.compile(r"\(([^)]*)\)")
# curly braces ignored (joltage), but present possibly — we'll not use them

def parse_line(line: str) -> Tuple[str, List[List[int]]]:
    """
    Returns (pattern_str, list_of_buttons) for a single input line.
    Each button is a list of ints (indices).
    """
    # extract pattern inside [ ... ]
    b = BRACKET_RE.search(line)
    if not b:
        raise ValueError("No indicator pattern found in line: " + line)
    pattern = b.group(1).strip()

    # extract all parenthesis groups (buttons)
    buttons = []
    for g in PAREN_RE.findall(line):
        s = g.strip()
        if s == "":
            # empty button (toggle nothing) - represent as empty list
            buttons.append([])
            continue
        # split by comma and convert to ints
        parts = [p.strip() for p in s.split(",") if p.strip() != ""]
        nums = [int(x) for x in parts]
        buttons.append(nums)

    return pattern, buttons

# --------------------------
# Gaussian elimination over GF(2)
# --------------------------

def gauss_rref(rows: List[int], rhs: List[int], n_vars: int):
    """
    Perform Gaussian elimination to RREF on the system:
      rows[i] (bitmask of length n_vars)  XOR-sum of variables = rhs[i]
    rows: list of integer masks, one per equation (light)
    rhs: list of 0/1 ints, one per equation
    Returns:
      - rows (modified in-place to RREF form)
      - rhs (modified)
      - pivot_row_to_col: dict mapping row_index -> pivot_col_index
      - pivot_cols_set: set of pivot columns
    """
    m = len(rows)
    r = 0
    pivot_row_to_col = {}
    pivot_cols_set = set()

    for col in range(n_vars):
        # find a row i >= r with bit col set
        sel = None
        for i in range(r, m):
            if (rows[i] >> col) & 1:
                sel = i
                break
        if sel is None:
            continue
        # swap into row r
        if sel != r:
            rows[r], rows[sel] = rows[sel], rows[r]
            rhs[r], rhs[sel] = rhs[sel], rhs[r]
        # eliminate the col bit from all other rows (RREF)
        for i in range(m):
            if i != r and ((rows[i] >> col) & 1):
                rows[i] ^= rows[r]
                rhs[i] ^= rhs[r]
        pivot_row_to_col[r] = col
        pivot_cols_set.add(col)
        r += 1
        if r == m:
            break

    return rows, rhs, pivot_row_to_col, pivot_cols_set

def solve_min_weight(rows_masks: List[int], rhs_bits: List[int], n_vars: int) -> int:
    """
    Solve rows_masks * x = rhs_bits over GF(2) and return minimal Hamming weight of x.
    If no solution, returns a large sentinel (or could raise).
    """
    # Copy lists (we'll modify them)
    rows = rows_masks[:]  # list of ints (m equations)
    rhs = rhs_bits[:]     # list of 0/1 ints
    m = len(rows)

    # RREF
    rows, rhs, pivot_row_to_col, pivot_cols_set = gauss_rref(rows, rhs, n_vars)

    # Check inconsistency: any row with mask == 0 and rhs == 1 -> no solution
    for i in range(m):
        if rows[i] == 0 and rhs[i] == 1:
            # No solution (problem statement implies this shouldn't happen)
            return 10**12

    # Build particular solution x0 (length n_vars)
    x0 = 0
    # For each pivot row p, pivot column c: x[c] = rhs[p]
    for r, c in pivot_row_to_col.items():
        if rhs[r] & 1:
            x0 |= (1 << c)

    # Build nullspace basis vectors:
    # For each free column f (not a pivot), set free var f = 1 and compute pivot vars:
    pivot_col_for_row = {c: r for r, c in pivot_row_to_col.items()}
    free_cols = [c for c in range(n_vars) if c not in pivot_cols_set]
    basis = []  # each basis vector is integer mask length n_vars
    for f in free_cols:
        vec = 0
        # free var f = 1
        vec |= (1 << f)
        # For every pivot column c, the value of that pivot in homogeneous solution is
        # the coefficient in the pivot row at column f (since b=0 for homogeneous)
        # After RREF, rows[r] has 1 at pivot col c and may have bits at free columns.
        # Find the pivot row for c:
        r = pivot_col_for_row.get(f, None)  # usually None; pivot rows are keyed by col -> row
        # Instead iterate all pivot rows:
        for prow, pcol in pivot_row_to_col.items():
            # if the pivot row has a 1 at column f, then x[pcol] toggles when free f=1
            if ((rows[prow] >> f) & 1):
                vec |= (1 << pcol)
        basis.append(vec)

    # If no free vars, just return weight of x0
    if not basis:
        return x0.bit_count()

    # We need minimal weight among x = x0 XOR (XOR subset of basis vectors)
    k = len(basis)

    # If k small enough, brute-force all 2^k combos. But we avoid enumerating huge 2^k when k large.
    # Strategy: search by increasing number of free bits set (combinatorial generation),
    # because minimal weight often small and this allows early exit.
    best = x0.bit_count()

    # Quick early return if best already 0 (can't beat 0)
    if best == 0:
        return 0

    # Precompute basis as integers
    basis_ints = basis

    # If k <= 22, do full enumeration (fast enough)
    if k <= 22:
        # iterate all subsets
        total = 1 << k
        for mask in range(total):
            comb = 0
            # accumulate basis vectors where mask bit set
            # bit-iteration trick:
            mm = mask
            idx = 0
            while mm:
                if mm & 1:
                    comb ^= basis_ints[idx]
                idx += 1
                mm >>= 1
            x = x0 ^ comb
            wc = x.bit_count()
            if wc < best:
                best = wc
                if best == 0:
                    return 0
        return best

    # If k > 22, search by increasing number of free bits set (w = 0..k)
    # Stop as soon as we find a solution with weight < current best, and we explore all combinations
    # for that w to be sure nothing smaller exists at same w. This is exact but may still be expensive
    # in worst-case; AoC sizes typically keep k small.
    for w in range(1, k + 1):
        # prune: if w >= best, flipping w free vars will change x0 weight by at most w + some, but
        # we can't guarantee lower bound; we'll still attempt but we can break if w >= best
        if w >= best:
            break
        for combo in itertools.combinations(range(k), w):
            comb = 0
            for idx in combo:
                comb ^= basis_ints[idx]
            x = x0 ^ comb
            wc = x.bit_count()
            if wc < best:
                best = wc
                if best == 0:
                    return 0
        # if we found any improvement to best that is <= w (rare), we continue; the loop's pruning will stop when w >= best
    return best

# --------------------------
# Top-level driver
# --------------------------

def solve_file(filename: str) -> None:
    machines_min = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f if ln.strip() != ""]

    for idx, line in enumerate(lines):
        try:
            pattern, buttons = parse_line(line)
        except Exception as e:
            print(f"Error parsing line {idx+1}: {e}", file=sys.stderr)
            continue

        m = len(pattern)  # number of lights
        # target vector b: bit i -> 1 if target is '#', else 0
        b_bits = [(1 if pattern[i] == "#" else 0) for i in range(m)]

        # number of variables = number of buttons
        n = len(buttons)
        # Build rows: for each light i (equation), build bitmask over n variables
        rows_masks = []
        for i in range(m):
            mask = 0
            for j, btn in enumerate(buttons):
                # if button j toggles light i, set bit j
                if i in btn:
                    mask |= (1 << j)
            rows_masks.append(mask)

        # Solve minimal presses for this machine
        min_presses = solve_min_weight(rows_masks, b_bits, n)
        machines_min.append(min_presses)
        print(f"Machine {idx+1}: min presses = {min_presses}")

    total = sum(machines_min)
    print("\nTotal minimal presses across all machines:", total)

if __name__ == "__main__":
    FILE = "day_10.txt"
    try:
        solve_file(FILE)
    except FileNotFoundError:
        print(f"Input file '{FILE}' not found. Please create the file in the same directory and try again.")
