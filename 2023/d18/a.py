import sys

with open(sys.argv[1], "r") as f:
    D = f.read().split("\n")

points = [(0,0)]
directions={
    "D":(1,0),
    "U":(-1,0),
    "R":(0,1),
    "L":(0,-1)
}
boundary_points = 0
for line in D:
    line = line.split()
    d, n = line[0], int(line[1])
    dr,dc = directions[d]
    r,c=points[-1]
    points.append((r+dr*n, c+dc*n))
    boundary_points+=n

def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0 
                         for ((x0,y0), (x1,y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:]+[p[0]])

# shoe lace theorem
# & pick's theorem
# A = i + (b/2) - 1
# i = A - (b/2) + 1
# i + b = interior points + boundary points
def solve(b, P):
    A = area(P)
    i = A - (b//2) + 1
    return i + b 

print("p1",solve(boundary_points, points))

# p2
new_points=[(0,0)]
b=0
for line in D:
    line = line.split()[-1][2:-1]
    d = "RDLU"[int(line[-1])]
    dr, dc = directions[d]
    n = int(line[:-1], 16)
    r,c = new_points[-1]
    new_points.append((r+n*dr, c+n*dc))
    b+=n

print("p2", solve(b, new_points))