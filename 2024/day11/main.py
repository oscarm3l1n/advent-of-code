import sys
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    D = f.read().strip()

xs = [int(x) for x in D.split()]

"""
1. if stone == 0 --> replace with 1
2. if stone == len(str(stone)) % 2 == 0 --> 100000 == 10 0 (leading zeroes are stripped)
3. multiply by 2024
"""

# if x == 0:
#     xs[i] = 1
# elif len(str(x)) % 2 == 0
#     s = xs.pop(i)
#     s = str(s)
#     n = len(s)//2
#     le = s[n:]
#     ri = s[:n]
#     xs.insert(i, int(le))
#     xs.insert(i+1,int(ri))
#     i+=1
# else:
#     xs[i] *= 2024


M = {}


# would also work with
# from functools import cache
# @cache
def calc(x, i, N):
    if (x, i, N) in M:
        return M[(x, i, N)]
    if i == N:
        ans = 1
    elif x == 0:
        ans = calc(1, i + 1, N)
    elif len(str(x)) % 2 == 0:
        s = str(x)
        slen = len(s)
        le = s[: slen // 2]
        ri = s[slen // 2 :]
        le = int(le)
        ri = int(ri)
        ans = calc(le, i + 1, N) + calc(ri, i + 1, N)
    else:
        ans = calc(2024 * x, i + 1, N)
    M[(x, i, N)] = ans
    return ans


for N in (25, 75):
    ans = 0
    for i in range(len(xs)):
        print(f'{i}/{len(xs)}')
        ans += calc(xs[i], 0, N)
    print('p1' if N == 25 else 'p2', ans)
