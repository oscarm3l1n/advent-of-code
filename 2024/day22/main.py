import sys
from collections import defaultdict, deque, Counter

with open(sys.argv[1], 'r') as f:
    D = f.read().strip()
lines = D.split('\n')


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
C = Counter()
for line in lines:
    x = int(line)
    Q = deque([])
    sequences = {}
    for i in range(2000):
        prev = x % 10
        nx = run(x)
        curr = nx % 10
        if len(Q) < 4:
            Q.append(curr - prev)
            if len(Q) == 4:
                key = (Q[0], Q[1], Q[2], Q[3])
                if key not in sequences:
                    sequences[key] = curr
        else:
            Q.popleft()
            Q.append(curr - prev)
            key = (Q[0], Q[1], Q[2], Q[3])
            if key not in sequences:
                sequences[key] = curr
        x = nx
    for k, v in sequences.items():
        C[k] += v

    ans += x
print('p1', ans)
print('p2', max(C.values()))
