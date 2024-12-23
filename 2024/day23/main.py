import sys
from collections import defaultdict

with open(sys.argv[1], 'r') as f:
    D = f.read().strip()

lines = D.split('\n')

graph = defaultdict(set)
for line in lines:
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

ans = 0
seen = set()
for a in graph:
    for b in graph:
        if a <= b:
            continue
        if b not in graph[a]:
            continue
        at = a.startswith('t')
        bt = b.startswith('t')
        C = graph[a] & graph[b]
        for c in C:
            print(a, b, c)
            if c > a and c > b:
                if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                    seen.add((a, b, c))
                    ans += 1
print(ans)
print(len(seen))
