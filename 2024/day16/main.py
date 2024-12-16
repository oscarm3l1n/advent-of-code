import sys
from collections import deque
from heapq import heappop, heappush

with open(sys.argv[1], "r") as f:
    D = f.read().strip()

#D="""#################
##...#...#...#..E#
##.#.#.#.#.#.#.#.#
##.#.#.#...#...#.#
##.#.#.#.###.#.#.#
##...#.#.#.....#.#
##.#.#.#.#.#####.#
##.#...#.#.#.....#
##.#.#####.#.###.#
##.#.#.......#...#
##.#.###.#####.###
##.#.#...#.....#.#
##.#.#.#####.###.#
##.#.#.........#.#
##.#.#.#########.#
##S#.............#
##################"""

G = [line for line in D.split('\n')]
R,C = len(G), len(G[0])

north,south,east,west = (-1,0),(1,0),(0,1),(0,-1)
sr,sc=-1,-1
tr,rc = -1,-1
dir = east
for r in  range(R):
    for c in range(C):
        if G[r][c] == 'E':
            tr,tc = r,c
        if G[r][c] == 'S':
            sr,sc = r,c

def ok(r,c):
    return 0<=r<R and 0<=c<C and G[r][c] != "#"


pq = []
dirs = [west, north, east, south]
d = 2
heappush(pq, (0, sr,sc,d, set()))
seen = set()
best_paths = set()
while pq:
    cost,r,c,d,m = heappop(pq)
    if G[r][c] == "E":
        print("GOAL", cost)
        best_paths |= m
    if (r,c,d) in seen:
        continue
    seen.add((r,c,d))
    nm = m.copy()
    nm.add((r,c))
    dr,dc = dirs[d]
    rr,cc = r+dr, c+dc
    if ok(rr,cc):
        heappush(pq, (cost+1, rr,cc, d, nm))
    heappush(pq, (cost+1000, r,c, (d-1)%4, nm))
    heappush(pq, (cost+1000, r,c, (d+1)%4, nm))

for r in range(R):
    for c in range(C):
        if (r,c) in best_paths:
            print("O",end="")
        else:
            print(G[r][c], end='')
    print()

p2 = 0
for r in range(R):
    for c in range(C):
        if (r,c) in best_paths:
            p2 += 1
print(p2)

