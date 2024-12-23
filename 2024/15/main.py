import sys

with open(sys.argv[1], 'r') as f:
    D = f.read()


D = D.strip().split('\n\n')
lines = D[0]
cmds = D[-1]
EMPTY = 0
BOX = 1
ROBOT = 2
WALL = 3

_G = [line for line in lines.split('\n')]
G = [[0 for _ in range(len(lines.split('\n')))] for _ in range(len(lines.split('\n')))]

R, C = len(G), len(G[0])


sr, sc = -1, -1
for r in range(R):
    for c in range(C):
        ch = _G[r][c]
        t = None
        if ch == '@':
            t = ROBOT
            sr, sc = r, c
        elif ch == '.':
            t = EMPTY
        elif ch == 'O':
            t = BOX
        elif ch == '#':
            t = WALL
        G[r][c] = t


def shift(pos, dir):  # --> new pos | None
    r, c = pos
    dr, dc = dir
    rr, cc = r + dr, c + dc

    if 0 <= cc < C and 0 <= rr < R and G[rr][cc] == WALL:
        return
    if 0 <= cc < C and 0 <= rr < R and G[rr][cc] == EMPTY:
        G[r][c] = EMPTY
        G[rr][cc] = ROBOT
        return rr, cc

    steps = 0
    while True:
        rr, cc = r + dr, c + dc
        if not (0 <= rr < R and 0 <= cc < C):
            break
        if G[rr][cc] == WALL:
            break
        if G[rr][cc] == EMPTY:
            for i in range(steps):
                pr, pc = rr - dr, cc - dc
                G[pr][pc] = EMPTY
                G[rr][cc] = BOX
                rr = pr
                cc = pc
            G[rr - dr][cc - dc] = EMPTY
            G[rr][cc] = ROBOT
            return rr, cc
        steps += 1
        r = rr
        c = cc


up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
for cmd in cmds:
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

p1 = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == BOX:
            p1 += 100 * r + c
print(p1)
