import sys
from collections import deque, Counter

dirs4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


with open(sys.argv[1], 'r') as f:
    D = f.read().strip()

G = [line for line in D.split('\n')]
R = len(G)
C = len(G[0])

sr, sc = None, None
tr, tc = None, None

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr, sc = r, c
        if G[r][c] == 'E':
            tr, tc = r, c

assert sr is not None
assert sc is not None
assert tr is not None
assert tr is not None


def ok(r, c, ok_pos):
    if (r, c) == ok_pos:
        return True
    return 0 <= r < R and 0 <= c < C and G[r][c] != '#'


def find_shortest():
    Q = deque([(sr, sc, 0)])
    seen = set()
    while Q:
        r, c, cost = Q.popleft()
        if (r, c) == (tr, tc):
            return cost
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in dirs4:
            rr, cc = r + dr, c + dc
            if ok(rr, cc, (-1, -1)):
                Q.append((rr, cc, cost + 1))
    return saved


def bfs(sr, sc, curr, n):
    Q = deque([(sr, sc, 0)])
    seen = set()
    saved = Counter()
    while Q:
        r, c, cost = Q.popleft()
        if (r, c) == (tr, tc):
            saved[n - cost] += 1
            break
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in dirs4:
            rr, cc = r + dr, c + dc
            if ok(rr, cc, curr):
                Q.append((rr, cc, cost + 1))
    return saved


n = find_shortest()
saved = Counter()
for r_ in range(R):
    print(f'{r_}/{R}')
    for c_ in range(C):
        nsaved = bfs(sr, sc, (r_, c_), n)
        for k in nsaved:
            saved[k] += nsaved[k]

ans = 0
for k in saved:
    if k >= 100:
        ans += saved[k]
print(ans)
