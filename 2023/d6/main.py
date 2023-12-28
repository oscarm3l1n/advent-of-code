import sys
from tqdm import tqdm

with open(sys.argv[1], "r") as f:
    data = f.read().rstrip().split("\n")

time = []
dist = []
t2 = 0
d2 = 0
for i, l in enumerate(data):
    d = l.split()[1:]
    if i == 0:
        time = [int(x) for x in d]
        t2 = int("".join(x for x in d))
    if i == 1:
        dist = [int(x) for x in d]
        d2 = int("".join(x for x in d))

ans = 1
for t, record in zip(time, dist):
    visited = set()
    combs = 0
    for i in range(t+1):
        a = t-i
        b = i
        comb = a*b
        if comb > record and (f"{a}{b}" not in visited):
            combs += 1
            visited.add(f"{a}{b}")
    ans *= combs
print("p1",ans)

# p2
combs=0
visited = set()
for i in tqdm(range(t2+1)):
    a = t2-i
    comb=a*i
    if comb > d2 and (f"{a}{i}" not in visited):
        combs+=1
        visited.add(f"{a}{i}")
print("p2",combs)