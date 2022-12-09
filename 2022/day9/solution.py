from pathlib import Path
import math

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}

def move_head(knot, dir):
    tmp = list(knot)
    tmp[0] += directions[dir][0]
    tmp[1] += directions[dir][1]
    return tuple(tmp)


def print_map(knots):
    w, h = (50, 40)
    map = []
    for row in range(h):
        map.append(['.' for _ in range(w)])

    for i, knot in enumerate(knots):
        x, y = knot
        map[x][y] = str(i) if i != 0 else 'H'
    for row in map:
        for col in row:
            print(col, end="")
        print()


def move(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail
    elif abs(dx) >= 2 and abs(dy) >= 2:
        tail = (head[0]-1 if tail[0]<head[0] else head[0]+1,
                head[1]-1 if tail[1]<head[1] else head[1]+1)
    elif abs(dx) >= 2:
        tail = (head[0]-1 if tail[0]<head[0] else head[0]+1, head[1])
    elif abs(dy) >= 2:
        tail = (head[0], head[1]-1 if tail[1]<head[1] else head[1]+1)
    return tail


def solution(data, n):

    knots = [(25, 10) for _ in range(n)]

    visited = set()

    visited.add(knots[-1])

    for dir, n_steps in data:

        for i in range(n_steps):
            knots[0] = move_head(knots[0], dir)
            
            # then update rest of tails
            for i in range(1, len(knots)):
                knots[i] = move(knots[i-1], knots[i])

            #print(dir, i)
            #print_map(knots)
            #input()
            visited.add(knots[-1])

    return len(visited)


with Path('input.in').open('r') as f:
    # converts ['R', '4'] into ('R', 4) for each line
    data = [tuple([line.strip().split()[0],
                   int(line.strip().split()[1])])
            for line in f.readlines()]

print("p1:", solution(data, 2))
print("p2:", solution(data, 10))
