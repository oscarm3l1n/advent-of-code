import sys
from collections import deque, Counter
import heapq

dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]

is_test = sys.argv[1] == "test.in"
with open(sys.argv[1], "r") as f:
    D = f.read().strip()

G = [line for line in D.split("\n")]
R = len(G)
C = len(G[0])

sr,sc = -1,-1
tr,tc = -1,-1

for r in range(R):
    for c in range(C):
        if G[r][c] == "S":
            sr,sc = r,c
        if G[r][c] == "E":
            tr,tc = r,c

MAX_CHEATS = 20


def manhattan(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def find_shortest():
    Q = deque([(sr,sc,0)])
    seen = set()
    def ok(r,c):
        return 0<=r<R and 0<=c<C and G[r][c] != "#"
    while Q:
        r,c,cost = Q.popleft()
        if (r,c) == (tr,tc):
            return cost
        if (r,c) in seen:
            continue
        seen.add((r,c))
        for dr,dc in dirs4:
            assert r is not None and c is not None
            rr,cc = r+dr, c+dc
            if ok(rr,cc):
                Q.append((rr,cc, cost+1))
    return -1

def calc_dists(from_):
    sr,sc = from_
    Q = deque([(sr,sc,0)])
    seen = {}
    while Q:
        r,c,cost = Q.popleft()
        if (r,c) in seen:
            continue
        seen[r,c] = cost
        for dr,dc in dirs4:
            rr, cc = r+dr, c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc] != "#":
                Q.append((rr,cc,cost+1))
    return seen

dist2start = calc_dists((sr,sc))
dist2end = calc_dists((tr,tc))
shortest = find_shortest()
SAVE = 50 if is_test else 100


saved = Counter()
i = 0
for r,c in dist2start:
    print(f'{i}/{len(dist2start)}')
    for rr,cc in dist2end:
        if (x:=manhattan((r,c),(rr,cc))) <= MAX_CHEATS:
            d = dist2start[r,c] + dist2end[rr,cc] + x
            if d <= shortest - SAVE:
                saved[shortest-d] += 1
    i += 1
ans = 0
for k in saved:
    if k >= SAVE:
        ans += saved[k]
print(ans)

