import sys

sys.setrecursionlimit(10**6)
with open(sys.argv[1], "r") as f:
    chunks = f.read().strip().split("\n\n")
vals,regs = chunks
g={}
for ln in vals.split("\n"):
    a,b = ln.split(": ")
    b = int(b)
    g[a] = b
gd={}
for ln in regs.split("\n"):
    a,op,b,_,reg=ln.split()
    gd[reg] = (a,op,b)

gd["nnt"], gd["gws"] = gd["gws"], gd["nnt"]
gd["z13"], gd["npf"] = gd["npf"], gd["z13"]
gd["cph"], gd["z19"] = gd["z19"], gd["cph"]
gd["hgj"], gd["z33"] = gd["z33"], gd["hgj"]
print(",".join(sorted(list({
    "nnt", "gws", "gws", "nnt",
    "z13", "npf", "npf", "z13",
    "cph", "z19", "z19", "cph",
    "hgj", "z33", "z33", "hgj"}))))

def pprint(reg,d=0,maxdepth=3):
    if d > maxdepth:
        return
    if reg in g:
        print("  "*d + reg)
    else:
        a,op,b = gd[reg]
        print("  "*d + reg +f" = {op} {a} {b}")
        pprint(a, d+1, maxdepth)
        pprint(b, d+1, maxdepth)

def evaluate(x,y, i, j):
    gloc = g.copy()

    #x00
    xs = [f'x{i:02d}' for i in range(45)]
    ys = [f'y{i:02d}' for i in range(45)]
    for x in xs:
        gloc[x] = 0
    for y in ys:
        gloc[y] = 0
    key = f'y{j:02d}'
    gloc[key] = 1
    key = f'x{i:02d}'
    gloc[key] = 1

    def dfs(reg):
        if reg not in gloc:
            a,op,b = gd[reg]
            left = dfs(a)
            right = dfs(b)
            if op == "AND":
                res = left & right
            elif op == "OR":
                res = left | right
            else:
                res = left ^ right
            gloc[reg] = res
        return gloc[reg]

    zouts = {}
    for reg in gd.keys():
        if reg.startswith("z"):
            zouts[reg] = dfs(reg)


    zs = sorted([ch for ch in zouts if ch.startswith("z")])
    s=""
    for z in zs:
        if zouts[z]:
            s += "1"
        else:
            s+="0"

    nx = "".join([ch for ch in reversed(s)])
    nx = int(nx,2)
    return nx

for i in range(45):
    for j in range(45):
        x = (1 << i)
        y = (1 << j)
        if x+y != evaluate(x,y,i,j):
            print(i,j)

