import sys

"""
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

D = sys.stdin.read()
D = D.split("\n\n")
print(D)
sizes = []
for r in D[:-1]:
    R = len(r.splitlines()[1:])
    C = len(r.splitlines()[1:][0])
    sizes.append((R,C))

areas = D[-1]
ans = 0
for area in areas.splitlines():
    r, c = area.split(":")[0].split("x")
    xs = [int(x) for x in area.split(":")[1:][0].lstrip().split()]
    tot_available = int(r) * int(c)
    #tot_size = sum(x * sizes[i] for i, x in enumerate(xs))
    tot_size = sum(x * 9 for i, x in enumerate(xs))
    if tot_size <= tot_available:
        ans += 1
print(ans)




