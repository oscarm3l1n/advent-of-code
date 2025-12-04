inp = "real.in"
with open(inp) as f:
    D = f.read().rstrip().split("\n")
    R = len(D)
    C = len(D[0])

def solve(r, c, seen):
    num = 0
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]:
        rr, cc = r+dr, c+dc
        if 0<=rr<R and 0<=cc<C:
            if (rr,cc) not in seen and D[rr][cc] == "@":
                num += 1
    return num

def p1():
    ans = 0
    for r in range(R):
        for c in range(C):
            if D[r][c] == "@":
                if solve(r, c, {}) < 4:
                    ans += 1
    print(ans)

def p2():
    ans = 0
    mark = set()
    run = True
    seen = set()
    while run:
        run = False
        mark = set()
        for r in range(R):
            for c in range(C):
                if (r,c) not in seen and D[r][c] == "@":
                    if solve(r, c, seen) < 4:
                        mark.add((r,c))
                        ans += 1
                        run = True
        seen |= mark
    print(ans)

p1()
p2()
