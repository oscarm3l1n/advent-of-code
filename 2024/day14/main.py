import sys
import re
from collections import defaultdict, Counter, deque, namedtuple

infile = sys.argv[1]
with open(sys.argv[1]) as f:
    D = f.read().strip()
R, C = (103, 101) if infile == 'input.in' else (7, 11)

G = []
for r in range(R):
    G.append(['.' for _ in range(C)])

lines = D.split('\n')


robots = []
for line in lines:
    c, r, dc, dr = [int(x) for x in re.findall(r'-?\d+', line)]
    robots.append([r, c, dr, dc])

i = 0
while True:
    for idx in range(len(robots)):
        robot = robots[idx]
        r, c, dr, dc = robot
        rr, cc = (r + dr) % R, (c + dc) % C
        robots[idx][0] = rr
        robots[idx][1] = cc
        G[r][c] = '.'
        G[rr][cc] = '#'
    seen = set()
    if i == 99:
        q1, q2, q3, q4 = 0, 0, 0, 0
        for robot in robots:
            r, c, _, _ = robot
            if r < R // 2 and c < C // 2:
                q1 += 1
            elif r < R // 2 and c > C // 2:
                q2 += 1
            elif r > R // 2 and c < C // 2:
                q3 += 1
            elif r > R // 2 and c > C // 2:
                q4 += 1
        print(q1, q2, q3, q4)
        ans = q1 * q2 * q3 * q4
        print('p1', ans)
    for r in range(R):
        for c in range(C):
            parts = 0
            if G[r][c] == '#':
                seen.add((r, c))
                seen = set()
                Q = deque([(r, c)])
                while Q:
                    nr, nc = Q.popleft()
                    if (nr, nc) in seen:
                        continue
                    parts += 1
                    seen.add((nr, nc))
                    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        rr, cc = nr + dr, nc + dc
                        if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == '#':
                            Q.append((rr, cc))
                if parts >= 220:
                    print('steps', i + 1)
                    exit()
    i += 1
