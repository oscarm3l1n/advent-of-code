import sys
from collections import deque
from heapq import heappop, heappush

with open(sys.argv[1], 'r') as f:
    D = f.read().strip()


G = [line for line in D.split('\n')]
R, C = len(G), len(G[0])

north, south, east, west = (-1, 0), (1, 0), (0, 1), (0, -1)
sr, sc = -1, -1
tr, rc = -1, -1
dir = east
for r in range(R):
    for c in range(C):
        if G[r][c] == 'E':
            tr, tc = r, c
        if G[r][c] == 'S':
            sr, sc = r, c


def ok(r, c):
    return 0 <= r < R and 0 <= c < C and G[r][c] != '#'


def part_1(fill_me):
    pq = []
    dirs = [west, north, east, south]
    d = 2
    heappush(pq, (0, sr, sc, d, set()))
    seen = {}
    best = float('inf')
    while pq:
        cost, r, c, d, m = heappop(pq)
        if G[r][c] == 'E' and cost <= best:
            best = min(best, cost)
            fill_me |= m
        if (r, c, d) in seen and cost > seen[r, c, d]:
            continue
        seen[r, c, d] = cost
        nm = m.copy()
        nm.add((r, c))
        dr, dc = dirs[d]
        rr, cc = r + dr, c + dc
        if ok(rr, cc):
            heappush(pq, (cost + 1, rr, cc, d, nm))
        heappush(pq, (cost + 1000, r, c, (d - 1) % 4, nm))
        heappush(pq, (cost + 1000, r, c, (d + 1) % 4, nm))
    return best


def part_2(best_paths):
    ans = 0
    for r in range(R):
        for c in range(C):
            if (r, c) in best_paths:
                ans += 1
    return ans + 1


best_paths = set()
print(part_1(best_paths))
print(part_2(best_paths))
