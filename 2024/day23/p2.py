import sys
import networkx as nx
from networkx.algorithms import find_cliques

with open(sys.argv[1], "r") as f:
    D=f.read().strip()
lines = D.split("\n")
g = nx.Graph()
for line in lines:
    a, b = line.split("-")
    g.add_edge(a,b)
    g.add_edge(b,a)

c = find_cliques(g)
best_g = []
for x in c:
    if len(x) > len(best_g):
        best_g = x

print(",".join(sorted(best_g)))

