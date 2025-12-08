inp = "real.in"

with open(inp) as f:
    D = f.read()

G = D.rstrip().split("\n")
R = len(G)
C = len(G[0])

def p2():
    col = C - 1
    total_sum = 0

    while col >= 0:
        if all(col >= len(G[row]) or G[row][col] == ' ' for row in range(R)):
            col -= 1
            continue
        if col >= len(G[R-1]):
            col -= 1
            continue
        operator = G[R-1][col]
        if operator not in ('+', '*'):
            col -= 1
            continue
        numbers = []
        right_col = col + 1
        while right_col < C:
            is_separator = all(right_col >= len(G[row]) or G[row][right_col] == ' ' for row in range(R))
            if is_separator:
                break
            num_str = ""
            for row in range(R - 1):
                if right_col < len(G[row]) and G[row][right_col].isdigit():
                    num_str += G[row][right_col]
            if num_str:
                numbers.append(int(num_str))
            right_col += 1
        numbers.reverse()
        left_col = col
        left_numbers = []
        while left_col >= 0:
            is_separator = all(left_col >= len(G[row]) or G[row][left_col] == ' ' for row in range(R))
            if is_separator:
                break
            num_str = ""
            for row in range(R - 1):
                if left_col < len(G[row]) and G[row][left_col].isdigit():
                    num_str += G[row][left_col]
            if num_str:
                left_numbers.append(int(num_str))
            left_col -= 1

        numbers.extend(left_numbers)

        if operator == '*':
            result = 1
            for num in numbers:
                result *= num
        else:
            result = sum(numbers)

        total_sum += result
        col -= 1

    print(total_sum)

p2()
