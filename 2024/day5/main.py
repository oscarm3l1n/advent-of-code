import sys
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split('\n\n')[0]
lines = lines.split('\n')
left = defaultdict(list[int])
right = defaultdict(list[int])


for line in lines:
    d = line.split('|')
    le, ri = int(d[0]), int(d[1])
    left[le].append(ri)
    right[ri].append(le)

lines = D.split('\n\n')[-1].split('\n')

inc = []
ans = 0
for line in lines:
    xs = [int(x) for x in line.split(',')]
    ok = True
    for i in range(len(xs)):
        curr = xs[i]
        for j in range(i + 1, len(xs)):
            if curr in left.get(xs[j], {}):
                ok = False
                inc.append(list(xs))
                break
        if not ok:
            break
    if ok:
        ans += xs[len(xs) // 2]
print('p1', ans)

ans = 0
for k in range(len(inc)):
    xs = inc[k]
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] in right.get(xs[j], {}):
                tmp = xs[j]
                xs[j] = xs[i]
                xs[i] = tmp
    ans += xs[len(xs) // 2]
print('p2', ans)
