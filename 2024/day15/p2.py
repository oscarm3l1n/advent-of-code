import sys
from collections import deque

with open(sys.argv[1], 'r') as f:
    D = f.read()

D = D.strip().split('\n\n')
lines = D[0]
cmds = D[-1]
EMPTY = 0
BOX_LEFT = 1
BOX_RIGHT = 2
ROBOT = 3
WALL = 4

_G = []
G = []
for line in lines.split('\n'):
    lst = []
    s = ''
    for ch in line:
        if ch == '.':
            lst += [EMPTY, EMPTY]
            s += '..'
        if ch == '#':
            lst += [WALL, WALL]
            s += '##'
        if ch == 'O':
            lst += [BOX_LEFT, BOX_RIGHT]
            s += '[]'
        if ch == '@':
            lst += [ROBOT, EMPTY]
            s += '@.'
    _G.append(s)
    G.append(lst)

R, C = len(G), len(G[0])
sr, sc = -1, -1
for r in range(R):
    for c in range(C):
        if G[r][c] == ROBOT:
            sr, sc = r, c


def ok(r, c):
    return 0 <= c < C and 0 <= r < R


up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)


def shift(pos, dir):
    r, c = pos
    dr, dc = dir
    rr, cc = r + dr, c + dc
    if not ok(rr, cc):
        return
    if G[rr][cc] == WALL:
        return
    if G[rr][cc] == EMPTY:
        G[r][c] = EMPTY
        G[rr][cc] = ROBOT
        return rr, cc

    Q = deque([(r, c)])
    seen = set()
    while Q:
        r, c = Q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        rr, cc = r + dr, c + dc
        if ok(rr, cc) and G[rr][cc] in (BOX_LEFT, BOX_RIGHT):
            print('dir', dir)
            print('box', '[' if G[rr][cc] == BOX_LEFT else ']')
            if G[rr][cc] == BOX_LEFT:
                Q.append((rr, cc))
                Q.append((rr, cc + 1))
            if G[rr][cc] == BOX_RIGHT:
                print(rr, cc, 'is box right')
                Q.append((rr, cc))
                Q.append((rr, cc - 1))

    print(seen)
    # now we have set of boxes
    new = set()
    dr, dc = dir
    for box in seen:
        r, c = box
        rr, cc = r + dr, c + dc
        if ok(rr, cc) and G[rr][cc] == WALL:
            return
        else:
            new.add((r, c, rr, cc, G[r][c]))
    for n in new:
        r, c, _, _, _ = n
        G[r][c] = EMPTY
    for n in new:
        _, _, r, c, t = n
        G[r][c] = t

    sr, sc = pos
    G[sr][sc] = EMPTY
    dr, dc = dir
    rr, cc = sr + dr, sc + dc
    G[rr][cc] = ROBOT
    return rr, cc


for cmd in cmds:
    print('COMMAND', cmd)
    pos = None
    if cmd == '^':
        pos = shift((sr, sc), up)
    elif cmd == 'v':
        pos = shift((sr, sc), down)
    elif cmd == '>':
        pos = shift((sr, sc), right)
    elif cmd == '<':
        pos = shift((sr, sc), left)
    if pos is not None:
        sr, sc = pos

p2 = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == BOX_LEFT:
            p2 += 100 * r + c
print(p2)
