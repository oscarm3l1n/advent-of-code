import sys
from collections import deque, namedtuple

with open(sys.argv[1], 'r') as f:
    D = f.read().strip()
lines = D.split('\n')

Item = namedtuple('Item', ['diff', 'val'])


def prune(x):
    return x % 16777216


def mix(x, other):
    return x ^ other


def run(x):
    nx = x * 64
    x = mix(x, nx)
    x = prune(x)
    nx = x // 32
    x = mix(x, nx)
    nx = x * 2048
    x = mix(x, nx)
    x = prune(x)
    return x


ans = 0
Q = deque([])
all_seqs = []
sequences = {}
for i, line in enumerate(lines):
    x = int(line)
    seqs = {}
    for i in range(2000):
        nx = run(x)
        xstr = str(nx)
        if len(Q) == 4:
            item = Item(diff=int(xstr[-1]) - Q[-1].val, val=int(xstr[-1]))
            Q.popleft()
            Q.append(item)
            key = (Q[0].diff, Q[1].diff, Q[2].diff, Q[3].diff)
            if key not in seqs:
                seqs[key] = Q[-1].val
        else:

            if i == 0:
                item = Item(diff=int(xstr[-1]) - int(lines[0][-1]), val=int(xstr[-1]))
            else:
                item = Item(diff=int(xstr[-1]) - Q[-1].val, val=int(xstr[-1]))
            Q.append(item)
            if len(Q) == 4:
                key = (Q[0].diff, Q[1].diff, Q[2].diff, Q[3].diff)
                if key not in seqs:
                    seqs[key] = Q[-1].val
        x = nx
    all_seqs.append(seqs)
    ans += x
print('p1', ans)

# now we have built sequeneces
best = -(10**6)
seen = set()
it = 0
best_seq = None
for seqs in all_seqs:
    print(f'{it}/{len(all_seqs)}')
    for seq in seqs:
        if seq in seen:
            continue
        seen.add(seq)
        tot = 0
        for i in range(len(all_seqs)):
            tot += all_seqs[i].get(seq, 0)
        # best = max(best, tot)
        if tot > best:
            best = tot
            best_seq = seq
    it += 1
print(best)
print(best_seq)

it = iter(all_seqs)
tot = 0
try:
    while True:
        try:
            tot += next(it)[best_seq]
        except KeyError:
            pass
except StopIteration:
    pass
print(tot)
