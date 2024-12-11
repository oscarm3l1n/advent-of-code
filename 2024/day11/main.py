import sys
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    D = f.read().strip()

xs = [int(x) for x in D.split()]

# number on a stone can change

# a stone can split in two

# these rules are in order

"""
1. if stone == 0 --> replace with 1
2. if stone == len(str(stone)) % 2 == 0 --> 100000 == 10 0 (leading zeroes are stripped)
3. multiply by 2024
"""

def r2(s):
    return (len(str(s)) % 2) == 0
def r1(s):
    return s == 0

N = 25
for _ in range(N):
    print(f'{_} / {N}')
    #print(xs)
    i = 0
    while i < len(xs):
        st = xs[i]

        if r1(st):
            xs[i] = 1
        elif r2(st):
            s = xs.pop(i)
            s = str(s)
            n = len(s)//2
            if n*2 == 2:
                le = s[0]
                ri = s[1]
            else:
                le = s[:n]
                ri = s[n:]
            #print(f'{le=} {ri=} {st=}')
            #print(xs)
            xs.insert(i, int(le))
            xs.insert(i+1,int(ri))
            #print(xs)
            #print("-----")
            i+=1
        else:
            xs[i] *= 2024
        i+=1

print("p1", len(xs))

# 100 --> 10 0
# 100/10
