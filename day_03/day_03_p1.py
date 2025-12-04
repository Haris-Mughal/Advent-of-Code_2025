def solveDay_03():
    
    ans = 0

    with open("day_03.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            digits = [int(x) for x in line]

            best_tens = -1 
            best_value = 0 

            for d in digits:
                if best_tens != -1:
                    val = best_tens * 10 + d
                    if val > best_value:
                        best_value = val

                if d > best_tens:
                    best_tens = d

            ans += best_value

    print(ans)


if __name__ == "__main__":
    solveDay_03()
