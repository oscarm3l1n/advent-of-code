
import re

inp = "real.in"

with open(inp) as f:
    D = f.read()

MAX = 100

def p1():
    start = 50
    ans = 0
    for ln in D.rstrip().split("\n"):
        m = re.search(r"([a-zA-Z])([0-9]+)", ln)
        dir, dx = m.groups()
        dx = int(dx)
        print(ln, dir, dx)
        if dir == "L":
            start = (start - dx) % MAX
        elif dir == "R":
            start = (start + dx) % MAX
        else:
            raise NotImplementedError
        print(start)
        if start == 0:
            ans += 1
    print("p1", ans)

def p2():
    start = 50
    ans = 0
    for ln in D.rstrip().split("\n"):
        m = re.search(r"([a-zA-Z])([0-9]+)", ln)
        dir, dx = m.groups()
        dx = int(dx)
        if dir == "L":
            for i in range(dx):
                start = (start - 1) % MAX
                if start == 0:
                    print("CLICK", ln)
                    ans += 1
        elif dir == "R":
            for i in range(dx):
                start = (start + 1) % MAX
                if start == 0:
                    print("CLICK", ln)
                    ans += 1
        else:
            raise NotImplementedError
    print("p2", ans)

#p1()
p2()
