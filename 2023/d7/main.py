import sys

def is_5s(h):
    ch = h[0]
    return h.count(ch) == 5


def is_4s(h):
    a1 = all([h[0] == h[1],
              h[1] == h[2],
              h[2] == h[3]])
    a2 = all([h[1] == h[2],
              h[2] == h[3],
              h[3] == h[4]])
    return a1 or a2

def is_full_house(h):
    h0,h1,h2,h3,h4=[x for x in h]
    a1 = all([
        h0==h1,
        h2==h3,
        h3==h4,
    ])
    a2 = all([
        h0==h1,
        h1==h2,
        h3==h4
    ])
    return a1 or a2

def is_3s(h):
    if is_4s(h):
        return False
    h0,h1,h2,h3,h4=[x for x in h]

    a1 = all([h0==h1,
              h1==h2])
    a2 = all([h1==h2,
              h2==h3])
    a3 = all([h2==h3,
              h3==h4])
    return a1 or a2 or a3
    
def is_22s(h):
    h0,h1,h2,h3,h4=[x for x in h]
    if is_4s(h) or is_3s(h):
        return False
    a1 = all([h0==h1, h2==h3])
    a2 = all([h0==h1, h3==h4])
    a3 = all([h1==h2, h3==h4])
    return a1 or a2 or a3

def is_2s(h):
    if is_4s(h) or is_3s(h) or is_22s(h):
        return False

    h0,h1,h2,h3,h4=[x for x in h]
    a1 = h0==h1
    a2 = h1==h2
    a3 = h2==h3
    a4 = h3==h4
    return a1 or a2 or a3 or a4


HIGH_CARD=1
ONE=2
TWO=3
THREE=4
FULL_HOUSE=5
FOUR=6
FIVE=7

import copy
def get_score(x):
    tmp = copy.deepcopy(x)
    hand = sorted(tmp)
    if is_5s(hand):
        return FIVE
    elif is_full_house(hand):
        return FULL_HOUSE
    elif is_2s(hand):
        return ONE
    elif is_22s(hand):
        return TWO
    elif is_3s(hand):
        return THREE
    elif is_4s(hand):
        return FOUR
    else:
        return HIGH_CARD


with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

ranks = {
    HIGH_CARD:[],
    ONE:[],
    TWO:[],
    THREE:[],
    FULL_HOUSE:[],
    FOUR:[],
    FIVE:[],
}


def cmp(x):
    ch2rank = {
        "2": 0,
        "3":1,
        "4":2,
        "5":3,
        "6":4,
        "7":5,
        "8": 6,
        "9": 7,
        "T":8,
        "J":9,
        "Q":10,
        "K":11,
        "A":12
    }
    
    tot = 0
    scores = [10**9,10**7,10**5,10**3,10**1]
    for i in range(len(x[0])):
        tot += scores[i]*ch2rank[x[0][i]]
    return tot

def cmp2(x):
    rs = "AKQT98765432J"
    ch2rank={k:i for i, k in enumerate(rs[::-1])}
    tot=0
    scores = [10**9,10**7,10**5,10**3,10**1]
    for i in range(len(x[0])):
        tot += scores[i]*ch2rank[x[0][i]]
    return tot


for l in data:
    hand, bid = l.split()
    bid = int(bid)
    # print(hand)
    score = get_score(hand)
    ranks[score].append((hand, bid))
    # print(score)
    # print()

rank = 1
ans = 0
res = ""
for t, arr in ranks.items():
    mysort = sorted(arr, key=lambda x: cmp(x))
 
    for thing in mysort:
        ans += thing[-1]*rank
        res += f"{thing[0]}, r={rank}\n"
        rank+=1

print(res)
print(ans)

        
        

