import sys
from collections import defaultdict, Counter
import random

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split('\n')


def _f(target, lst):
    if len(lst) == 1:
        return next(iter(lst)) == target
    if _f(target, [int(str(lst[0]) + str(lst[1]))] + lst[2:]):
        return True
    if _f(target, [lst[0] * lst[1]] + lst[2:]):
        return True
    if _f(target, [lst[0] + lst[1]] + lst[2:]):
        return True


correct = []
ans = 0
for i, line in enumerate(lines):
    print(f'{i=} of {len(lines)}')
    Y, xs = line.split(':')
    Y = int(Y)
    xs = [int(x) for x in xs.split()]
    if _f(Y, xs):
        ans += Y

print(ans)
