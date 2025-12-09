import sys
import math

D = sys.stdin.read()

vs = []
for ln in D.splitlines():
    c, r = list(map(int, ln.split(",")))
    vs.append((r,c))

ans = 0
for i,v1 in enumerate(vs):
    for j,v2 in enumerate(vs):
        if i < j:
            x1,y1 = v1
            x2,y2 = v2
            w = abs(x1-x2) + 1
            h = abs(y1-y2) + 1
            if w*h > ans:
                ans = w*h
print(ans)
