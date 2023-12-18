import sys

with open(sys.argv[1], "r") as f:
    D = f.read().split("\n")

ans = 0
ans2 = 0
ns = [1 for i in range(len(D))]
for i, line in enumerate(D):
    line = line[len(f"Card {i+1}: "):]
    facit = [x for x in line.split("|")[0].split(" ") if x != ""]
    mine = [x for x in line.split("|")[-1].split(" ") if x != ""]
    facit = set(facit)
    mine = set(mine)
    power = 0
    for n in mine:
        if n in facit:
            power += 1
    if power > 0:
        ans += 2 ** (power-1)
        for _ in range(ns[i]):
            for ii in range(i+1, power+i+1):
                ns[ii] += 1

print("part1",ans)
print("part2", sum(ns))
