import sys
from collections import defaultdict
from functools import cache

D = sys.stdin.read()

#aaa: you hhh
#you: bbb ccc
#bbb: ddd eee
#ccc: ddd eee fff
#ddd: ggg
#eee: out
#fff: out
#ggg: out
#hhh: ccc fff iii
#iii: out

G = defaultdict(set)
for ln in D.splitlines():
    src, nodes = ln.split()[0], ln.split()[1:]
    src = src[:-1]
    for node in nodes:
        G[src].add(node)


@cache
def solve(node, seen_dac, seen_fft, p1=False):
    if node == "out":
        if p1:
            return 1
        else:
            if seen_dac and seen_fft:
                return 1
            else:
                return 0
    ans = 0
    for adj in G[node]:
        _seen_dac = seen_dac or adj == "dac"
        _seen_fft = seen_fft or adj == "fft"
        ans += solve(adj,
                     _seen_dac,
                     _seen_fft,
                     p1)
    return ans

print("p1", solve("you", False, False, True))
print("p2", solve("svr", False, False))
