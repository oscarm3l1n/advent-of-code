import sys
from collections import deque

with open(sys.argv[1], 'r') as f:
    D = f.read().strip()

lines = D.split('\n')

G = [line for line in lines]
R = len(G)
C = len(G[0])


starts = []
ends = []
sr, sc = 0, 0
for r in range(R):
    for c in range(C):
        if G[r][c] == '9':
            starts.append((r, c))
        if G[r][c] == '0':
            ends.append((r, c))


def bfs(pos):
    Q = deque([(pos[0], pos[1])])
    ans = 0
    seen = set()
    while Q:
        r, c = Q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if G[r][c] == '0':
            ans += 1

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr = r + dr
            cc = c + dc
            if (
                0 <= rr < R
                and 0 <= cc < C
                and G[rr][cc] != '.'
                and (int(G[rr][cc]) - int(G[r][c])) == -1
            ):
                Q.append((rr, cc))
    return ans


def _f(r, c):
    if G[r][c] == '9':
        return 1
    ans = 0
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        rr = r + dr
        cc = c + dc
        if (
            0 <= rr < R
            and 0 <= cc < C
            and G[rr][cc] != '.'
            and int(G[rr][cc]) == int(G[r][c]) + 1
        ):
            ans += _f(rr, cc)
    return ans


ans = 0
for start in starts:
    ans += bfs(start)
print(ans)

ans = 0
for end in ends:
    ans += _f(*end)
print(ans)
