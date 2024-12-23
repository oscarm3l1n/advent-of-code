import sys
import re
from collections import deque


def nums(s):
    return [int(x) for x in re.findall(r'\d+', s)]


is_test = sys.argv[1] == 'test.in'

R, C = (7, 7) if is_test else (71, 71)

with open(sys.argv[1], 'r') as f:
    D = f.read().strip()

lines = D.split('\n')
points = set()
sr, sc = (0, 0)
d4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]

i = 0
for line in lines:
    c, r = nums(line)
    points.add((r, c))
    G = []

    for r in range(R):
        row = []
        for c in range(C):
            if (r, c) in points:
                row.append('#')
            else:
                row.append('.')
        G.append(row)

    def ok(r, c):
        return 0 <= r < R and 0 <= c < C and (r, c) not in points

    seen = set()
    Q = deque([(sr, sc, 0)])
    found = False
    while Q:
        nr, nc, steps = Q.popleft()
        if (nr, nc) == (R - 1, C - 1):
            print('GOAL', steps, i)
            found = True
            if is_test and i == 11:
                input()
            elif i == 1023:
                input()
            break

        if (nr, nc) in seen:
            continue
        seen.add((nr, nc))
        for dr, dc in d4:
            nrr, ncc = nr + dr, nc + dc
            if ok(nrr, ncc):
                Q.append((nrr, ncc, steps + 1))
    if found == False:
        print(line)
        exit()
    i += 1
