import collections
import sys
from collections import defaultdict, Counter,deque

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split('\n')

G = [line for line in lines]
R=len(G)
C=len(G[0])
DIRS=[(-1,0),(1,0),(0,-1),(0,1)]


def bfs(target, pos):
    Q = deque([(pos[0],pos[1])])
    seen = set()
    perim = 0
    while Q:
        r,c = Q.popleft()
        if (r,c) in seen:
            continue
        seen.add((r,c))
        for dr,dc in DIRS:
            if dr==0 and dc==0:
                continue
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc] == target:
                Q.append((rr,cc))
            else:
                perim += 1
    return seen, len(seen), perim

def find_sides(s):
    n=0
    sr,sc = next(iter(list(s)))
    ch = G[sr][sc]
    for (r,c) in s:
        for dr,dc in DIRS:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc] == ch:
                pass
            else:
                n += 1
    return n

def perimeter(s):
    return len(s)

    
ans = 0
seen = set()
for r in range(R):
    for c in range(C):
        if (r,c) in seen:
            continue
        ch = G[r][c]
        S,a,p=bfs(ch,(r,c))
        seen |= S
        ans += a*p
        #n = find_sides(S)
        #perim = perimeter(S)
        #ans += perim*n
print('p1', ans)

def find_per(pos: tuple, seen: set):
    # first find all adjacent squares
    r,c=pos
    curr_ch = G[r][c]
    print(f'{curr_ch=}')
    neighbours = []
    for s in seen:
        r,c = s
        for dr,dc in DIRS:
            rr,cc = r+dr, c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc] ==  curr_ch:
                pass
            else:
                neighbours.append((rr,cc))
    seen=set()
    lst = []
    print(neighbours)
    for i in range(len(neighbours)):
        consec_row = set()
        consec_col = set()
        pr,pc = neighbours[i]
        if (pr,pc) in seen:
            continue
        print("START NEIGH:", pr,pc)
        for j in range(len(neighbours)):
            if i==j:
                continue
            r,c = neighbours[i]
            rr,cc = neighbours[j]
            dx = abs(c-cc)
            dy = abs(r-rr)
            if dy==0 and dx <= 1:
                consec_row.add((r,c))
                consec_row.add((rr,cc))
            if dx == 0 and dy <= 1:
                consec_col.add((rr,cc))
                consec_col.add((r,c))

        seen |= consec_row
        seen |= consec_col
        if len(consec_row):
            lst.append(consec_row)
        if len(consec_col):
            lst.append(consec_col)

    for x in lst:
        print(x)
    return len(lst)

        

ans = 0
seen = set()
test = defaultdict(int)
test["A"]=4
test["B"]=4
test["E"]=4
test["D"]=4
test["C"]=8
for r in range(R):
    for c in range(C):
        if (r,c) in seen:
            continue
        ch = G[r][c]
        S,a,_=bfs(ch,(r,c))
        seen |= S
        print("STARTING", ch)
        per = find_per((r,c), S)
        assert test[ch] == per, f'{ch=} {test[ch]=} {per=}'
