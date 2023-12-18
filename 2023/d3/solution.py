import sys

def create_grid(input):
    grid = []
    for row in input:
        column = []
        for col in row:
            column.append(col)
        grid.append(column)
    return grid

with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

grid = create_grid(data)

for g in grid:
    print("".join(g))


def is_symbol(r, c):
    if r > len(grid) - 1:
        return False
    if c > len(grid[0]) - 1:
        return False
    symbol = grid[r][c]

    return symbol != "." and not symbol.isdigit()


def get_indexes_of_number(r, index):
    bwd = index
    start = None
    while True:
        if bwd < 0:
            start = 0
            break
        ch = grid[r][bwd]
        if ch.isdigit():
            bwd -= 1
        else:
            start = bwd+1
            break
    fwd = index
    end = None
    while True:
        if fwd >= len(grid[r]):
            end = len(grid[r])-1
            break
        ch = grid[r][fwd]
        if ch.isdigit():
            fwd += 1
        else:
            end = fwd
            break
    return start, end

    # print("starting at", index, "in row", r)


def skip_current_number(r, c):
    new_c = c
    for new_c in range(c, len(grid[r])-1):
        ch = grid[r][new_c]
        if not ch.isdigit():
            return new_c
    return len(grid[r])



def p1():
    result = 0
    for r in range(len(grid)):
        row = grid[r]
        # for c in range(len(row)):
        c = 0
        while c < len(row):
            current = grid[r][c]
            if current.isdigit():
                left = is_symbol(r, c-1)
                right = is_symbol(r, c+1)
                up = is_symbol(r-1, c)
                down = is_symbol(r+1, c)
                nw = is_symbol(r-1, c-1)
                ne = is_symbol(r-1, c+1)
                sw = is_symbol(r+1, c-1)
                se = is_symbol(r+1, c+1)
                if any([left, right, up, down, nw, ne, sw, se]):
                    start, end = get_indexes_of_number(r, c)
                    number = grid[r][start:end]
                    number = "".join(number)
                    print(number)
                    result += int(number)
                    new_c = skip_current_number(r, c)
                    c = new_c
                    continue
            c += 1
    print("part 1:", result)
            

p1()