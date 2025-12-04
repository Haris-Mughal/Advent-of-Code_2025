def solveDay_03():
    
    ans = 0
    k = 12  # number of batteries to turn on

    with open("day_03.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            digits = [int(x) for x in line]
            n = len(digits)
            stack = []

            for i, d in enumerate(digits):
                # while we can pop and still have enough digits to fill k
                while stack and stack[-1] < d and len(stack) - 1 + (n - i) >= k:
                    stack.pop()
                stack.append(d)

            # take exactly k digits from stack
            selected_digits = stack[:k]
            value = int(''.join(map(str, selected_digits)))
            ans += value

    print(ans)


if __name__ == "__main__":
    solveDay_03()
