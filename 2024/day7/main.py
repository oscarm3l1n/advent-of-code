import sys
from collections import defaultdict, Counter
import random

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split('\n')


ops = ['+', '*', '|']


def lst2str(lst):
    return ''.join(lst)


# 292: 11 6 16 20
def _eval(s):
    ops_cnt = 0
    i = 0
    tot = 0
    while True:
        if ops_cnt == 1 and not i < len(s):
            if '|' in s[:i]:
                x = s[:i].replace('|', '')
            else:
                x = eval(s[:i])
            tot += int(x)
            break
        if not i < len(s):
            break
        if s[i] in ops:
            ops_cnt += 1
        if ops_cnt == 2:
            ops_cnt = 0
            if '|' in s[:i]:
                x = s[:i].replace('|', '')
            else:
                x = eval(s[:i])
            new_s = f'{x}{s[i:]}'
            i = 0
            s = new_s
        i += 1
    return tot


correct = []
lne = 0
for line in lines:
    print(f'line {lne} of {len(lines)}')
    lne += 1
    Y, xs = line.split(':')
    Y = int(Y)
    xs = [int(x) for x in xs.split()]
    s = ''
    for i, x in enumerate(xs):
        if i == len(xs) - 1:
            s += f'{x}'
            continue
        s += f'{x}+'
    s = [ch for ch in s]
    Q = [s]
    seen = set()
    while Q:
        curr = Q.pop()
        seen.add(lst2str(curr))
        if Y == _eval(lst2str(curr)):
            correct.append((_eval(lst2str(curr)), lst2str(curr), line))
        else:
            for i, ch in enumerate(curr):
                if ch in ops:
                    op = '+'
                    test = curr[:i] + [op] + curr[i + 1 :]
                    if lst2str(test) not in seen:
                        Q.append(test)
                    op = '*'
                    test = curr[:i] + [op] + curr[i + 1 :]
                    if lst2str(test) not in seen:
                        Q.append(test)

                    op = '|'
                    test = curr[:i] + [op] + curr[i + 1 :]
                    if lst2str(test) not in seen:
                        Q.append(test)


ans = 0
seen = set()
for i in range(len(correct)):
    a, b, c = correct[i]
    if c not in seen:
        ans += a
        seen.add(c)
print(ans)
