import sys
from collections import defaultdict, Counter
import re

with open(sys.argv[1]) as f:
    D = f.read().strip()


segments = D.split('\n\n')

PAT_A = re.compile(r"Button A: X\+(?P<X>.*\d+?).*Y\+(?P<Y>.*\d+?)")
PAT_B = re.compile(r"Button B: X\+(?P<X>.*\d+?).*Y\+(?P<Y>.*\d+?)")
PAT_PRIZE = re.compile(r"Prize: X=(?P<PX>.*\d+?).*Y=(?P<PY>.*\d+)?")


class Button:
    def __init__(self, d, is_a=None):
        if is_a:
            self.cost = 3
        else:
            self.cost = 1
        self.x = int(d.get("X", 0))
        self.y = int(d.get("Y", 0))

    @classmethod
    def parse(cls, s, is_a=True):
        if is_a:
            pat = PAT_A
        else:
            pat = PAT_B
        x = [m.groupdict() for m in pat.finditer(s)]
        return cls(next(iter(x)), is_a)
    
    def __repr__(self):
        return f'Button(X={self.x}, B={self.y}, cost={self.cost})'

class Prize:
    def __init__(self, d):
        self.x = int(d.get("PX", 0))
        self.y = int(d.get("PY", 0))

    @classmethod
    def parse(cls, s):
        x = [m.groupdict() for m in PAT_PRIZE.finditer(s)]
        return cls(next(iter(x)))

    def __repr__(self):
        return f'PRIZE(X={self.x}, B={self.y})'



def solve(b1: Button, b2: Button, prize_pos: Prize):
    tx,ty = prize_pos.x, prize_pos.y
    ax, ay = b1.x, b1.y
    bx, by = b2.x, b2.y
    cost_a, cost_b = b1.cost, b2.cost

    M = {}
    def dfs(x, y, da: int, db: int):
        key = (x,y,da,db)
        if key in M:
            return M[key]
        if da >= 100 or db >= 100:
            # not possible
            return float("inf")
        if x == tx and y == ty:
            print(f'{da=} {db=}')
            print(f'{cost_a=} {cost_b=}')
            print(f'{da*cost_a=} {db*cost_b=}')
            return da*cost_a + db*cost_b
        ans = float("inf")
        if x+ax <= tx and y+ay <= ty:
            ans = min(ans, dfs(x+ax, y+ay, da+1, db))
        if x+bx <= tx and y+by <= ty:
            ans = min(ans, dfs(x+bx, y+by, da, db+1))
        #print(f'{x+ax <= tx and y+ay <= ty}')
        #print(f'{x+bx <= tx and y+by <= ty}')
        M[key] = ans
        return ans
        
    return dfs(0,0,0,0)


    

ans = 0
for seg in segments:
    xy_pat = re.compile(r"Button \w: X\+(?P<X>.*\d+?).*Y\+(?P<Y>.*\d+?)")
    prize_pat = re.compile(r"Prize: X=(?P<PX>.*\d+?).*Y=(?P<PY>.*\d+?)")

    print("SEG")
    print(seg)

    A = Button.parse(seg, is_a=True)
    B = Button.parse(seg, is_a=False)
    PRIZE = Prize.parse(seg)
    tx,ty = PRIZE.x, PRIZE.y
    ax,ay = A.x, A.y
    bx,by = B.x, B.y
    ac,bc = A.cost, B.cost

    x = solve(A, B, PRIZE)
    if x != float('inf'):
        ans += x
print('p1', ans)
