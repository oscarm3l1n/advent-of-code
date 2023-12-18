import sys

with open(sys.argv[1], "r") as f:
    D = f.read().split("\n")

G = []
start_pos = None
for r, rr in enumerate(D):
    row = []
    for c, cc in enumerate(rr):
        if cc == "S":
            start_pos = (r, c)
        row.append(cc)
    G.append(row)


S=(1, 0)
N=(-1, 0)
W=(0, -1)
E=(0, 1)
visited = set()

def ok(r, c):
    return all([
    0 <= r < len(G),
    0 <= c < len(G[0]),
    (r, c) not in visited,
    G[r][c] != "."
    ])

def get_neighbours(start, directions):
    result = []
    for dr, dc in directions:
        rr = start[0] + dr
        cc = start[1] + dc
        if ok(rr, cc):
            result.append((rr, cc))
    return result
        

new_start = None
for dr, dc in [N, W, S, E]:
    rr = start_pos[0] + dr
    cc = start_pos[1] + dc
    if ok(rr, cc):
        new_start = (rr, cc)

loops = 0
Q = [new_start]
while Q:
    r, c = Q.pop()
    visited.add((r, c))
    ch = G[r][c]

    # add neighbours
    neighbours = None
    if ch == "|":
        neighbours = get_neighbours((r, c), [N, S])
    if ch == "-":
        neighbours = get_neighbours((r, c), [E, W])
    if ch == "L":
        neighbours = get_neighbours((r, c), [N, E])
    if ch == "J":
        neighbours = get_neighbours((r, c), [N, W])
    if ch == "7":
        neighbours = get_neighbours((r, c), [S, W])
    if ch == "F":
        neighbours = get_neighbours((r, c), [S, E])

    if neighbours:
        Q.extend(neighbours)
    loops += 1
print(loops / 2)



R = len(D)
C = len(D[0])
G2 = [['.' for c in range(C*3)] for r in range(R*3)]

possible_pipes = {"F", "7", "L", "J", "-", "|"}
r, c = start_pos[0], start_pos[1]


up_valid = (G[r-1][c] in {"|", "7", "F"})
down_valid = (G[r+1][c] in {"|", "L", "J"})
right_valid = (G[r][c+1] in {"-","J", "7"})
left_valid = (G[r][c-1] in {"-", "F", "L"})
token = None
if up_valid and down_valid:
    token = "|"
elif up_valid and right_valid:
    token = "L"
elif up_valid and left_valid:
    token = "J"
elif down_valid and right_valid:
    token = "F"
elif down_valid and left_valid:
    token = "7"
elif left_valid and right_valid:
    token = "-"

G = [row.replace("S", token) for row in D]


def print_map(data):
    for g in data:
        print("".join(g))
print_map(D)

for r in range(R):
    for c in range(C):
        if G[r][c]=='|':
            G2[3*r+0][3*c+1] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+2][3*c+1] = 'x'
        elif G[r][c]=='-':
            G2[3*r+1][3*c+0] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+1][3*c+2] = 'x'
        elif G[r][c]=='7':
            G2[3*r+1][3*c+0] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+2][3*c+1] = 'x'
        elif G[r][c]=='F':
            G2[3*r+2][3*c+1] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+1][3*c+2] = 'x'
        elif G[r][c]=='J':
            G2[3*r+1][3*c+0] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+0][3*c+1] = 'x'
        elif G[r][c]=='L':
            G2[3*r+0][3*c+1] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+1][3*c+2] = 'x'
        elif G[r][c]=='.':
            pass
        else:
            assert False, G[r][c]

print_map(G2)

from collections import deque

# find start inside borders
R2 = R*3
C2 = C*3
Q = deque()
Q.append((0, 0))
# for r in range(R2):
#     Q.append((r, 0))
#     Q.append((r, C2-1))
# for c in range(C2):
#     Q.append((0, c))
#     Q.append((R2-1, c))

DR = [-1,0,1,0]
DC = [0,1,0,-1]
SEEN = set()
while Q:
    # either (r,c) for ground or (r,c,in_or_out) for pipe
    r, c = Q.popleft()
    if (r,c) in SEEN:
        continue
    if not (0<=r<R2 and 0<=c<C2):
        continue
    SEEN.add((r,c))
    if G2[r][c] == 'x':
        continue
    G2[r][c] = "x"
    for d in range(4):
        Q.append((r+DR[d],c+DC[d]))

ans = 0
for r in range(R):
    for c in range(C):
        seen = False
        for rr in [0, 1, 2]:
            for cc in [0, 1, 2]:
                if (3*r+rr, 3*c+cc) in SEEN:
                    seen = True
            if not seen:
                ans += 1
print(ans)


