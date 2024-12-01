import sys
from collections import defaultdict

D = open(sys.argv[1]).read().strip()
lines = D.split("\n")
lst1, lst2 = [], []
C = defaultdict(int)

for line in lines:
    x, y = line.split()
    x, y = int(x), int(y)
    lst1.append(x)
    lst2.append(y)
    C[y] += 1

lst1 = sorted(lst1)
lst2 = sorted(lst2)
ans = 0
for x, y in zip(lst1, lst2):
    ans += abs(x - y)
print(f"p1 {ans=}")

ans = 0
for x in lst1:
    ans += x * C[x]
print(f"p2 {ans=}")
