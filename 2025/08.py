import sys
import math
from collections import defaultdict

D = sys.stdin.read()
vs = []
for ln in D.splitlines():
    x, y, z = list(map(int, ln.split(",")))
    vs.append((x, y, z))

N = len(vs)


def calc_dist(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


V = []
for i in range(N):
    for j in range(N):
        if i < j:
            d = calc_dist(vs[i], vs[j])
            V.append((d, i, j))

V = sorted(V)

UnionFind = {i: i for i in range(N)}


def find(node):
    p = UnionFind[node]
    while p != UnionFind[p]:
        UnionFind[p] = UnionFind[UnionFind[p]]
        p = UnionFind[p]
    return p


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    UnionFind[root_x] = root_y


def p1():
    for _, i, j in V[:1000]:
        union(i, j)

    C = defaultdict(int)
    for i in range(N):
        C[find(i)] += 1

    S = sorted(C.values())
    print(S[-3] * S[-2] * S[-1])


def p2():
    global UnionFind
    conns = 0
    V = []
    for i in range(N):
        for j in range(N):
            if i < j:
                d = calc_dist(vs[i], vs[j])
                V.append((d, i, j))

    V = sorted(V)
    UnionFind = {i: i for i in range(len(V))}
    for _, i, j in V:
        if find(i) != find(j):
            conns += 1
            if conns == len(vs) - 1:
                print(vs[i][0] * vs[j][0])
            union(i, j)


p1()
p2()
