import collections
import sys
from collections import defaultdict, Counter, deque

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split('\n')

G = [line for line in lines]
R = len(G)
C = len(G[0])
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

tests = {'A': 4, 'B': 4, 'D': 4, 'E': 4, 'C': 8}


def bfs(target, pos):
    Q = deque([(pos[0], pos[1])])
    seen = set()
    perims = defaultdict(set)
    perim = 0
    while Q:
        r, c = Q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in DIRS:
            if dr == 0 and dc == 0:
                continue
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == target:
                Q.append((rr, cc))
            else:
                perim += 1
                perims[dr,dc].add((rr,cc))

    return seen, len(seen), perim, perims


def find_sides(perims):
    sides = []
    sides = 0
    for dr, dc in perims:
        seen = set()
        curr_ps = perims[dr,dc] # set
        for p in curr_ps:
            if p in seen:
                continue
            Q = deque([p])
            sides += 1
            while Q:
                r,c = Q.popleft()
                if (r,c) in seen:
                    continue
                seen.add((r,c))
                for dr, dc in DIRS:
                    rr, cc = r+dr, c+dc
                    if (rr,cc) in curr_ps:
                        Q.append((rr,cc))
    return sides
                
ans = 0
p2 = 0
seen = set()
for r in range(R):
    for c in range(C):
        if (r, c) in seen:
            continue
        ch = G[r][c]
        S, a, p, perims = bfs(ch, (r, c))
        seen |= S
        ans += a * p
        per2 = find_sides(perims)
        p2 += a * per2
print('p1', ans)
print('p2', p2)
