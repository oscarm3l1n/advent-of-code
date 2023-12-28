
from collections import deque
import sys
with open(sys.argv[1], "r") as f:
    D = f.read().split("\n")

# G = [[ch for ch in row] for row in D]

G = []
R = len(D)
C = len(D[0])
start = (0,0)
for r in range(R):
    tmp =[]
    for c in range(C):
        ch = D[r][c]
        tmp.append(ch)
        if ch == "S":
            start=(r,c)

    G.append(tmp)




steps = 64
q = deque([(start[0], start[1], steps)])
visited=set()
ans=set()
while q:
    r, c, s = q.popleft()

    if r<0 or r>=R or c<0 or c>=C:
        continue
    if (r,c) in visited:
        continue

    if G[r][c] == "O" or G[r][c] == "#":
        continue

    if s % 2 == 0:
        ans.add((r,c))

    if s == 0:
        continue

    visited.add((r,c))

    for dr, dc in [(0,1),(0,-1),(-1,0),(1,0)]:
        rr=r+dr
        cc=c+dc
        if 0<=cc<C and 0<=rr<R:
            q.append((rr,cc, s-1))


for (r,c) in visited:
    G[r][c]="O"

for g in G:
    print("".join(g))

print(len(ans))
