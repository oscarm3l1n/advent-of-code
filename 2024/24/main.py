import sys
from collections import deque

with open(sys.argv[1], "r") as f:
    chunks = f.read().strip().split("\n\n")

lns = chunks[0].split("\n")

conns = {}
for ln in lns:
    conn, val = ln.split(": ")
    conns[conn] = val == "1"

lns = chunks[1].split("\n")
should = set()
change = True
while change:
    change = False
    for ln in lns:
        a, op, b, _, c = ln.split()
        if c.startswith("z"):
            should.add(c)
        if a in conns and b in conns and c not in conns:
            a, b = conns[a], conns[b]
            if op == "AND":
                conns[c] = a and b
            elif op == "OR":
                conns[c] = a or b
            elif op == "XOR":
                conns[c] = a != b
            change = True


zs = {k:v for k,v in conns.items() if k.startswith("z")}
ans = 0
for i,k in enumerate(sorted(zs)):
    if zs[k]:
        ans += 2**i
print(ans)


