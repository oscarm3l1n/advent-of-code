import sys
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split("\n")

G = [line for line in lines]
R = len(G)
C = len(G[0])

def pg(t):
    for r in range(R):
        for c in range(C):
            if (r,c) in t:
                print(G[r][c],end='')
            else:
                print('.',end='')
        print()

# A M S X
ans = 0
for r in range(R):
    for c in range(C):
        no = [(0,0), (-1,0), (-2,0), (-3,0)]
        so = [(0,0), (1,0), (2,0), (3,0)]
        ea = [(0,0), (0,1), (0,2), (0,3)]
        we = [(0,0), (0,-1), (0,-2), (0,-3)]

        nw = [(0,0), (-1,-1), (-2,-2), (-3,-3)]
        ne = [(0,0), (-1,1), (-2,2), (-3,3)]
        sw = [(0,0), (1,-1), (2,-2), (3,-3)]
        se = [(0,0), (1,1), (2,2), (3,3)]

        for d in (no, so, ea, we, nw, ne, sw, se):
            ok = True
            t = []
            for i in range(4):
                rr = r + d[i][0]
                cc = c + d[i][1]
                if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == 'XMAS'[i]:
                    t.append((rr,cc))
                    continue
                ok = False
                break
            if ok:
                ans += 1

print(ans)




