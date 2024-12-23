import sys
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split('\n')

G = [line for line in lines]
R = len(G)
C = len(G[0])
M = defaultdict(set[tuple])

for r in range(R):
    for c in range(C):
        ch = G[r][c]
        if ch != '.':
            M[ch].add((r,c))

nodes = set()
for ch in M:
    pts = [p for p in M[ch]]
    for i in range(len(pts)):
        for j in range(len(pts)):
            if i == j:
                continue
            p1 = pts[i]
            p2 = pts[j]
            dr = p1[0]-p2[0]
            dc = p1[1]-p2[1]
            # need to calculate manhattan dist
            rr = p1[0]+dr
            cc = p1[1]+dc
            if 0<=rr<R and 0<=cc<C:# and G[rr][cc] == '.':
                nodes.add((rr,cc))
print("p1", len(nodes))


nodes = set()
for ch in M:
    pts = [p for p in M[ch]]
    for i in range(len(pts)):
        for j in range(len(pts)):
            if i == j:
                continue
            p1 = pts[i]
            p2 = pts[j]
            dr = p1[0]-p2[0]
            dc = p1[1]-p2[1]
            K = 0
            while True:
                rr = p1[0]+(K*dr)
                cc = p1[1]+(K*dc)
                if 0<=rr<R and 0<=cc<C:
                    nodes.add((rr,cc))
                    K+=1
                    continue
                break

for r in range(R):
    for c in range(C):
        if (r,c) in nodes:
            print("#",end="")
        else:
            print(G[r][c],end="")
    print()

print("p2", len(nodes)) 

