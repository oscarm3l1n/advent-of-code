import sys
from collections import defaultdict, Counter
from typing import reveal_type

with open(sys.argv[1]) as f:
    D = f.read().strip()

free_space=False
print(D)
idx = 0
s = []
stack = []
ss = []  # list[tup[int, boolss, , in]]  (ch is_free len)
for ch in D:
    ch = int(ch)
    if free_space:
        for i in range(ch):
            s.append('.')
        ss.append(('.', free_space, ch))
    else:
        for i in range(ch):
            s.append(str(idx))
        stack.append(str(idx)*ch)
        ss.append((f'{idx}', free_space, ch))
        idx+=1
    free_space = not free_space

#le = 0
#ri = len(s)-1
#while True:
#    print(f'{le} of {len(s)}')
#    for i in range(len(s)):
#        if s[i]=='.':
#            le = i
#            break
#    for i in reversed(range(len(s))):
#        if s[i].isdigit():
#            ri = i
#            break
#
#    if le > ri:
#        break
#    s[le] = s[ri]
#    s[ri] = '.'
#
#ans = 0
#for i in range(len(s)):
#    if s[i]=='.':
#        break
#    ans += i*int(s[i])
#print(ans)


def pr(s):
    print(''.join(s))

pr(s)

C = defaultdict(int)
pts = defaultdict(tuple)

for i in reversed(range(len(s))):
    C[s[i]] += 1

i = 0
while i < len(s):
    ch = s[i]
    if ch == '.':
        # find slutpunkt
        for le in range(i, len(s)):
            if s[le] != '.':
                pts[i] = (i, le-1)
                i = le
                break
    i += 1

class Stop(Exception):
    """time to stop"""

prev = s[-1]
try:
    for i in reversed(range(len(s))):
        ch = s[i]
        if ch != prev and prev != '.':
            curr = C[prev]
            for k in pts:
                start, end = pts[k]
                size = (end-start)+1
                if curr <= size:
                    if start+curr > end:
                        pass
                    #print(f'{i=}')
                    #print("".join(s))
                    #print(f'{" "*start}^')
                    #print(f'{prev=} {C[prev]}')
                    #print(f'{s[start:end]=}')
                    #print(f'{start=} {end=}')
                    #print(f'{size=}')
                    #print(f'{C[prev]=}')
                    if start > i:
                        raise Stop
                    for c in range(curr):
                        s[start+c] = prev
                    pts[k] = (start+curr, end)
                    # clean up
                    for z in range(i+1, i+curr+1):
                        s[z] = '.'
                    break
        prev = ch
except Stop:
    for k in pts:
        print(pts[k])
    ans = 0
    for i in range(len(s)):
        ch = s[i]
        if ch != '.':
            ans += i*int(ch)
    print(6412390114238 - ans)
    print(ans)

