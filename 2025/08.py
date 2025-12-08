import sys
from collections import defaultdict

D = sys.stdin.read().rstrip()
vs = []
for ln in D.splitlines():
    x, y, z = list(map(int,ln.split(",")))
    vs.append((x,y,z))

X = []
for i in range(len(vs)):
    for j in range(i+1, len(vs)):
        x1,y1,z1 = vs[i]
        x2,y2,z2 = vs[j]
        d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        X.append((d, i, j))

X = sorted(X)

union_find = {i: i for i in range(len(vs))}

def find(x):
    if x == union_find[x]:
        return x
    union_find[x] = find(union_find[x])
    return union_find[x]

def mix(x, y):
    union_find[find(x)] = find(y)

connections = 0
for i, (_, x, y) in enumerate(X):
    if i == 1000:
        count = defaultdict(int)
        for x in range(len(vs)):
            count[find(x)] += 1
        S = sorted(count.values())
        print(S[-1] * S[-2] * S[-3])
    if find(x) != find(y):
        connections += 1
        if connections == len(vs)-1:
            print(vs[x][0] * vs[y][0])
        mix(x, y)

