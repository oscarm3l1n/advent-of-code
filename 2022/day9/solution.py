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


def move_tail(knot, tup):
    tmp = list(knot)
    tmp[0] += tup[0]
    tmp[1] += tup[1]
    return tuple(tmp)


def solution(data, n):

    # Initial state
    T = [0, 0]
    S = [0, 0]
    H = [0, 0]

    knots = [(0, 0) for _ in range(n)]

    visited = set()

    visited.add((T[0], T[1]))

    positions = [
        (0, 1),  # right,
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down right
        (1, -1),  # down left
        (-1, 1),  # up right
        (-1, -1)  # up left
    ]

    def get_dist(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

    for dir, n_steps in data:

        for i in range(n_steps):
            knots[0] = move_head(knots[0], dir)
            if get_dist(knots[0], knots[-1]) > math.sqrt(2):
                # Try all 8 directions around
                # T and pick the one where dist is < 1
                # # but not 0
                for position in positions:
                    row_incr, col_incr = position

                    tmp_pos = [knots[-1][0] + row_incr,
                               knots[-1][1] + col_incr]

                    if get_dist(tmp_pos, knots[0]) == 1.0:
                        knots[-1] = move_tail(knots[-1], (row_incr, col_incr))
                        visited.add(knots[-1])
                        break

    print("Part 1: ", len(visited))


with Path('test.in').open('r') as f:
    # converts ['R', '4'] into ('R', 4) for each line
    data = [tuple([line.strip().split()[0],
                   int(line.strip().split()[1])])
            for line in f.readlines()]

solution(data, 2)
