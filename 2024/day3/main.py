import sys
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    D = f.read().strip()


def get_nums(s):
    it = iter(s)
    x = 0
    while ch := next(it):
        if ch == ",":
            break
        if not ch.isdigit():
            return False, False
        x = 10 * x + int(ch)
    y = 0
    while ch := next(it):
        if ch == ")":
            break
        if not ch.isdigit():
            return False, False
        y = 10 * y + int(ch)
    return x, y


ans = 0
for i in range(len(D)):
    if D[i:].startswith("mul"):
        x, y = get_nums(D[i + len("mul") + 1 :])
        ans += x * y
print("p1", ans)

ans = 0
i = 0
enabled = True
while i < len(D):
    if D[i:].startswith("don't()"):
        enabled = False
    if D[i:].startswith("do()"):
        enabled = True
    if D[i:].startswith("mul") and enabled:
        i = i + len("mul") + 1
        x, y = get_nums(D[i:])
        ans += x * y
    i += 1

print("p2", ans)
