from collections import deque
import sys

production = "input" in sys.argv[1]

with open(sys.argv[1], "r") as f:
    D = f.read().split("\n")

if production:
    C = int(3000)
    R = int(3000)
    r, c = 1000,1000
else:
    C = 20
    R = 20
    r,c=0,0

G=[['.' for _ in range(C)] for __ in range(R+1)]
G[r][c]="#"
for line in D:
    line = line.split()
    direction, n = line[0], int(line[1])
    print(direction, n)
    if direction=="R":
        for i in range(n):
            G[r][c+i+1]="#"
        c+=n
    elif direction=="L":
        for i in range(n):
            G[r][c-1-i]="#"
        c-=n
    elif direction=="U":
        for i in range(n):
            G[r-1-i][c]="#"
        r-=n
    elif direction=="D":
        for i in range(n):
            G[r+1+i][c]="#"
        r+=n

for g in G:
    print("".join(g))

q=deque()
q.append((r+1,c+1))
visited=set()
while q:
    r, c = q.popleft()

    if r<0 or r>=R or c<0 or c>=C:
        continue
    if (r,c) in visited:
        continue
    if G[r][c]=="#":
        continue

    visited.add((r,c))

    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        rr=r+dr
        cc=c+dc
        q.append((rr,cc))

for (r,c) in visited:
    G[r][c]="#"

for g in G:
    print("".join(g))

ans=0
for row in G:
    ans += "".join(row).count("#")
print(ans)
