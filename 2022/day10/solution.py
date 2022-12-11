from pathlib import Path

with Path('input.in').open('r') as f:
    data = [l.strip() for l in f.readlines()]

Q = [-1 for _ in range(250)]
cycles = 1
X = 1
for line in data:
    line = line.split()

    command = line[0]
    if command == 'addx':
        n = int(line[1])

        for i in range(2):
            Q[cycles] = X
            cycles += 1
        X += n
        Q[cycles] = X
    else:
        Q[cycles] = X
        cycles += 1
    

ans = []
for cycle in range(1, 241):
    if cycle in [20, 60, 100, 140, 180, 220]:
        ans.append(cycle * Q[cycle])

import numpy as np
print("p1:", np.sum(ans))


### part 2
for i in range(240):
    cycle = i + 1
    currentX = Q[cycle]
    print(
            '#' if (i % 40) in [currentX-1, currentX, currentX+1]
            else '.'
            , end=""
        )
    if i % 40 == 0:
        print()