import sys
from collections import deque

with open(sys.argv[1]) as f:
    D = f.read().strip()

lines = D.split('\n')

G = [line for line in lines]
R = len(G)
C = len(next(iter(G)))
start = None
start_r, start_c = 0, 0
for r in range(R):
    for c in range(C):
        if G[r][c] == "^":
            start_r, start_c = r, c

# r c dr dc
do = (1,0)
up = (-1, 0)
le = (0, -1)
ri = (0, 1)
Q = deque([(start_r, start_c, -1, 0)])
ans = 0
seen = set()
while Q:
    r, c, dr, dc = Q.popleft()
    rr, cc = r+dr, c+dc
    seen.add((r,c))
    if not (0<=rr<R and 0<=cc<C):
        break
    if G[rr][cc] == "#":
        # change direction
        if (dr, dc) == up:
            dr, dc = ri
        elif (dr, dc) == le:
            dr, dc = up
        elif (dr, dc) == ri:
            dr, dc = do
        elif (dr, dc) == do:
            dr, dc = le
    rr, cc = r+dr, c+dc
    if 0 <= rr < R and 0<=cc<C:
        Q.append((rr, cc, dr, dc))
print("p1", len(seen))


ans = 0
for _r in range(R):
    for _c in range(C):
        d=0
        seen = set()
        Q = deque([(start_r, start_c, 0)])
        while Q:
            r, c, d = Q.popleft()
            if (r,c,d) in seen:
                ans += 1
                break
            seen.add((r,c,d))
            
            dr, dc = [up, ri, do, le][d]
            rr, cc = r+dr, c+dc

            if not (0<=rr<R and 0<=cc<C):
                break
            if G[rr][cc] == "#" or ((rr, cc) == (_r, _c)):
                d = (d+1)%4
                rr = r
                cc = c
            if 0 <= rr < R and 0<=cc<C:
                Q.append((rr, cc, d))
print("p2", ans)
