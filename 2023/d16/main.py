from collections import deque
import sys

with open(sys.argv[1], "r") as f:
    D = f.read().split("\n")

G = [[c for c in row]for row in D]
R = len(G)
C = len(G[0])

import copy
def print_heatmap(my_set):
    grid = copy.deepcopy(G)
    for elem in my_set:
        r, c, dr, dc = elem
        if grid[r][c] == ".":
            if dr == -1:
                grid[r][c] = "^"
            elif dr == 1:
                grid[r][c] = "v"
            elif dc == 1:
                grid[r][c] = ">"
            elif dc == -1:
                grid[r][c] = "<"
    
    for g in grid:
        print("".join(g))


def bfs(start_r, start_c, start_dr, start_dc):
    q = deque()
    q.append((start_r, start_c, start_dr, start_dc))
    visited = set()
    unique = set()
    while q:
        r, c, dr, dc = q.popleft()

        rr = r+dr
        cc = c+dc
        if (r, c, dr, dc) in visited:
            continue

        if (0 <= r < R) and (0 <= c < C):
            ch = G[r][c]
            # print(r, c, dr, dc, ch)
            visited.add((r, c, dr, dc))
            unique.add((r,c))
            # print_heatmap(visited)
            rr = r+dr
            cc = c+dc
            # print(r, c, dr, dc, ch)
            # print(rr, cc, G[rr][cc])
            # input()

            if ch == ".":
                q.append((rr, cc, dr, dc))
            elif ch == "\\":
                if dr < 0:
                    q.append((r, c-1, 0, -1))
                elif dr > 0:
                    q.append((r, c+1, 0, 1))
                elif dc < 0:
                    q.append((r-1, c, -1, 0))
                elif dc > 0:
                    q.append((r+1, c, 1, 0))
            elif ch == "-":
                if dc != 0:
                    q.append((rr, cc, 0, dc))
                elif dr != 0:
                    q.append((r, c+1, 0, 1))
                    q.append((r, c-1, 0, -1))
            elif ch == "/":
                if dc < 0:
                    q.append((r+1, c, 1, 0))
                elif dc > 0:
                    q.append((r-1, c, -1, 0))
                elif dr < 0:
                    q.append((r, c+1, 0, 1))
                elif dr > 0:
                    q.append((r, c-1, 0, -1))
            elif ch == "|":
                if dr != 0:
                    q.append((rr, cc, dr, 0))
                elif dc != 0:
                    # print(c)
                    q.append((r+1, c, 1, 0))
                    q.append((r-1, c, -1, 0))
    # print_heatmap(visited)
    return len(unique)

# print("p1",bfs(0,0,0,1))
best=0
# for c in range(C):
#     best = max(best, bfs(0, c, 1, 0))

best = max([bfs(0,c,1,0) for c in range(C)])
print(best)
best = max([bfs(C-1, c, -1, 0) for c in range(C)]+[best])
print(best)
best = max([bfs(r,0,0,1) for r in range(R)] + [best])
print(best)
best = max([bfs(R-1,r,0,-1) for r in range(R)]+[best])
print(best)



# print_heatmap(visited)