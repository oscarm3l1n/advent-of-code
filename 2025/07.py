from functools import cache

inp = "real.in"
with open(inp) as f:
    D = f.read().rstrip()

G = []
for ln in D.split("\n"):
    row = []
    for ch in ln:
        row.append(ch)
    G.append(row)

R = len(G)
C = len(G[0])

sc = None
for c in range(C):
    if G[0][c] == "S":
        sc = c
        break
assert sc

def p1():
    down = (1, 0)
    q = [(1, sc, *down)]

    seen = set()
    splits = 0
    while q:
        r, c, dr, dc = q.pop()

        if not (0 <= r < R and 0 <= c < C):
            continue

        state = (r, c, dr, dc)
        if state in seen:
            continue
        seen.add(state)

        if G[r][c] == "^":
            splits += 1
            q.append((r, c-1, *down))
            q.append((r, c+1, *down))
        else:
            rr, cc = r + dr, c + dc
            q.append((rr, cc, *down))

    for r in range(R):
        for c in range(C):
            if (r,c) in seen:
                print("|", end="")
            else:
                print(G[r][c], end="")
        print()
    print(splits)

@cache
def solve(r, c):
    if c >= C or c < 0:
        return 1
    if r >= R:
        return 1
    ans = 0

    if G[r][c] == "^":
        ans += solve(r+1, c-1)
        ans += solve(r+1, c+1)
    else:
        ans += solve(r+1, c)
    return ans

def p2():
    print(solve(1, sc))

p1()
p2()
