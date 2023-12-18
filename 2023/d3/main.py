import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

G = [[c for c in row] for row in data]
R = len(data)
C = len(data[0])
D = [1, 0, -1]
n = 0
ans = 0
has_part = False
is_gear = False
gears = {}
parts = set()
row = 0
col = 0
for r in range(R+1):
    for c in range(C+1):
        if c<C and r<R and G[r][c].isdigit():
           n = n*10 + int(G[r][c])
           for rr in D:
               for cc in D:
                   if 0 <= r+rr < R and 0 <= c+cc < C:
                        ch = G[r+rr][c+cc]
                        if ch != "." and not ch.isdigit():
                            has_part = True
                        if ch == "*":
                            is_gear = True
                            row = r+rr
                            col = c+cc
        elif n > 0:
            if has_part:
                ans += n
                parts.add(n)
            if is_gear:
                try:
                    gears[f"{row}{col}"].append(n)
                except:
                    gears[f"{row}{col}"] = [n]
            n = 0
            row = 0
            col = 0
            is_gear = False
            has_part = False
print(f"p1: {ans}")

ans = 0
print(gears)
for _, arr in gears.items():
    if len(arr) == 2:
        if arr[0] in parts and arr[1] in parts:
            ans += arr[0] * arr[1]
print(f"p2: {ans}")