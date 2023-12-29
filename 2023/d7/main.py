import sys
from collections import Counter

with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

def solve(hand, part2=False):
    hand = hand.replace("T", chr(ord("9")+1))
    hand = hand.replace("J", chr(ord("1"))) if part2 else hand.replace("J", chr(ord("9")+2))
    hand = hand.replace("Q", chr(ord("9")+3))
    hand = hand.replace("K", chr(ord("9")+4))
    hand = hand.replace("A", chr(ord("9")+5))

    C = Counter(hand)
    if part2:
        target = list(C.keys())[0]
        for k in C:
            if k!='1':
                if C[k] > C[target] or target=='1':
                    target = k
        assert target != '1' or list(C.keys()) == ['1']
        if '1' in C and target != '1':
            C[target] += C['1']
            del C['1']
        assert '1' not in C or list(C.keys()) == ['1'], f'{C} {hand}'


    s = sorted(C.values())
    n = -1
    if s==[5]:
        n=10
    elif s==[1,4]:
        n=9
    elif s==[2,3]:
        n=8
    elif s==[1,1,3]:
        n=7
    elif s==[1,2,2]:
        n=6
    elif s==[1,1,1,2]:
        n=5
    elif s==[1,1,1,1,1]:
        n=4
    else:
        raise ValueError(f"{C} {hand} {s}")
    
    return (n, hand)
    

H = []
H2 = []
for line in data:
    hand, bid = line.split()
    H.append((hand, bid))
    H2.append((hand, bid))

H = sorted(H, key=lambda hb: solve(hb[0]))

H2 = sorted(H2, key=lambda hb: solve(hb[0], True))

ans=0
for i, (h,b) in enumerate(H):
    ans += (i+1)*int(b)
print("p1",ans)

ans=0
for i, (h,b) in enumerate(H2):
    ans += (i+1)*int(b)
print("p2",ans)


