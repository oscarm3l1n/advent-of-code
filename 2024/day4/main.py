import sys
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split("\n")

G = [line for line in lines]
R = len(G)
C = len(G[0])
T = []

def chars(r,c,pts):
    res = []
    tups = []
    for pt in pts:
        rr = r+pt[0]
        cc = c+pt[1]
        if 0 <= rr < R:
            if 0 <= cc < C:
                res.append(G[rr][cc])
                tups.append((rr, cc))
                T.append((rr,cc))
    
    if len(res) != 4:
        return False, False

    tups = sorted(tups, key=lambda x: x[0])
#    tup = (tups[0][0], 
#           tups[0][1],
#           tups[1][0],
#           tups[1][1],
#           tups[2][0],
#           tups[2][1],
#           tups[3][0],
#           tups[3][1],)

    return sorted(res) == sorted('XMAS'), tuple(tups)



def pg(tups=None):
    for r in range(R):
        for c in range(C):
            if (r,c) in T:
                print(G[r][c], end='')
            else:
                print('.',end='')
        print()
# A M S X
ans = 0
seen = set()
for r in range(R):
    for c in range(C):
        pts_up = [(r-i,c) for i in range(4)]
        pts_left = [(r,c-i) for i in range(4)]
        pts_right = [(r,c+i) for i in range(4)]
        pts_down = [(r+i,c) for i in range(4)]

        pts_nw = [(r-i,c-i) for i in range(4)]
        pts_sw = [(r+i,c-i) for i in range(4)]
        pts_ne = [(r-i,c+i) for i in range(4)]
        pts_se = [(r+i,c+i) for i in range(4)]

            
        right = chars(r, c, pts_right)
        up = chars(r, c, pts_up)
        down = chars(r, c, pts_down)
        left = chars(r, c, pts_left)
        
        nw = chars(r,c, pts_nw)
        ne = chars(r,c, pts_ne)
        sw = chars(r,c, pts_sw)
        se = chars(r,c, pts_se)
        for dir, tup in (right, up, down, left, nw, ne, sw, se):
            if dir:
                print(tup)
                ans += dir
                print(dir, int(dir), ans)
                seen.add(tup)
                pg()
                input()
print(ans)



