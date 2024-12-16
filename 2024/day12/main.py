import collections
import sys
from collections import defaultdict, Counter, deque

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split('\n')

G = [line for line in lines]
R = len(G)
C = len(G[0])
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

tests = {'A': 4, 'B': 4, 'D': 4, 'E': 4, 'C': 8}


def bfs(target, pos):
    Q = deque([(pos[0], pos[1])])
    seen = set()
    perims = set()
    perim = 0
    perim2 = 0
    while Q:
        r, c = Q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in DIRS:
            if dr == 0 and dc == 0:
                continue
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == target:
                Q.append((rr, cc))
            else:
                perim += 1
                perims.add((rr, cc, dr, dc))
                if dr != 0:
                    # moving rows
                    if not any(
                        [
                            (rr, cc - 1, dr, dc) in perims,
                            (rr, cc + 1, dr, dc) in perims,
                        ]
                    ):
                        perim2 += 1
                elif dc != 0:
                    if not any(
                        [
                            (rr - 1, cc, dr, dc) in perims,
                            (rr + 1, cc, dr, dc) in perims,
                        ]
                    ):
                        perim2 += 1

                # if any([
                #    (rr, cc-1, dr, dc) in perims,
                #    (rr, cc+1, dr, dc) in perims,
                #    (rr-1, cc, dr, dc) in perims,
                #    (rr+1, cc, dr, dc) in perims,
                #    ]):
                #        pass
                # else:
                #    perim2 += 1

    return seen, len(seen), perim, perims, perim2


ans = 0
p2 = 0
seen = set()
for r in range(R):
    for c in range(C):
        if (r, c) in seen:
            continue
        ch = G[r][c]
        S, a, p, perims, perim2 = bfs(ch, (r, c))
        seen |= S
        ans += a * p
        p2 += a * perim2
print('p1', ans)
print('p2', p2)
assert p2 == 902742, f'{p2=}'
