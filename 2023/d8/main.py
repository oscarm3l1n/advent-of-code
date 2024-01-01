import sys
import math

with open(sys.argv[1] ,"r") as f:
    D = f.read().split("\n")

directions = D[0]
D = D[2:]
M = {}
positions = []
for item in D:
    k, pair = item.split("=")
    k=k[:-1]
    if k.endswith("A"):
        positions.append(k)
    pair = pair[2:-1]
    p1, p2 = pair.split(",")
    p2 = p2[1:]
    M[k] = (p1,p2)



for part2 in [False, True]:
    cycles = []
    for position in positions:
        cycle = []
        seen = set([(position, directions[0], 0)])
        steps = 0
        while True:
            for di, direction in enumerate(directions):
                # print("from", position,end="")
                position = M[position][1 if direction=="R" else 0]
                # print("-->",position)
                steps += 1

                if position.endswith("Z" if part2 else "ZZZ"):
                    cycle.append(steps)
                    if not part2:
                        break

                if (position, direction, di) in seen:
                    break
                seen.add((position, direction, di))
            else:
                continue
            break

        cycles.append(cycle)

    ans = 0
    if part2:
        ans = math.lcm(*[x[0] for x in cycles])
    else:
        ans = [x[0] for x in cycles if x][0]
    print("p1" if not part2 else "p2", ans)

