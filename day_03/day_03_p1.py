def solveDay_02():  # you can rename to solveDay_03 if needed
    
    ans = 0

    with open("day_03.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            digits = [int(x) for x in line]

            best_tens = -1  # largest tens digit so far
            best_value = 0  # best 2-digit number for this bank

            for d in digits:
                # treat d as the ones digit if we already have a tens digit
                if best_tens != -1:
                    val = best_tens * 10 + d
                    if val > best_value:
                        best_value = val

                # update best tens digit
                if d > best_tens:
                    best_tens = d

            ans += best_value

    print(ans)


if __name__ == "__main__":
    solveDay_02()   # or solveDay_03()
