import sys

with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

def expand_galaxies():
    pass

R = len(data)
C = len(data[0])

r = 0
EMPTY_R=[]
while r < R:
    empty = True
    for c in range(C):
        if data[r][c]=="#":
            empty = False
    if empty:
        EMPTY_R.append(r)
    r+=1

c=0
EMPTY_C=[]
while c < C:
    empty=True
    for r in range(R):
        if data[r][c]=="#":
            empty=False
    if empty:
        EMPTY_C.append(c)
    c+=1

galaxies = []
for r in range(R):
    for c in range(C):
        ch = data[r][c]
        if ch == "#":
            galaxies.append((r,c))

ans = 0
for i, (r,c) in enumerate(galaxies):
    for j in range(i, len(galaxies)):
        r2,c2=galaxies[j]
        expansion=10**6-1
        d = abs(r-r2)+abs(c-c2)
        for er in EMPTY_R:
            if min(r,r2)<=er<=max(r,r2):
                ans+=expansion
        for ec in EMPTY_C:
            if min(c,c2)<=ec<=max(c,c2):
                ans+=expansion
        ans += d

print(ans)