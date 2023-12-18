import sys
import copy

with open(sys.argv[1], "r") as f:
    data = f.read().split("\n\n")


def solve(x):
    for r in range(1, len(x)):
        above = x[:r][::-1]
        below = x[r:]
        # if above == below:
        #     return r
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0

ans = 0
rows_cols=[]
for i, x in enumerate(data):
    grid = x.split("\n")
    row = solve(grid)

    T = list(zip(*grid))
    T = ["".join(x) for x in T]
    col = solve(T)

    if row != 0:
        ans += (row*100)
        rows_cols.append((row, None))
    if col != 0:
        ans += (col)
        rows_cols.append((None, col))
print(ans)

# p2
ans = 0
for i, x in enumerate(data):
    grid = x.split("\n")
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C):
            new_grid = copy.deepcopy(grid)
            ch = new_grid[r][c]
            tmp = list(new_grid[r])
            tmp[c] = "#" if ch == "." else "."
            tmp = "".join(tmp)
            new_grid[r] = tmp
            
            row = solve(new_grid)
            T = list(zip(*new_grid))
            T = ["".join(t) for t in T]
            col = solve(T)
            ans += 100*row
            ans += col
          
print(ans)
 

    
        
        


