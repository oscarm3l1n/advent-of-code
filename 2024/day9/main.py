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
        ss.append(('.', ch))
    else:
        for i in range(ch):
            s.append(str(idx))
        ss.append((str(idx), ch))
        idx+=1
    free_space = not free_space

def pr(s):
    for ch,size in s:
        print(ch*size,end='')
    print()
pr(ss)

class Block:
    def __init__(self, tup):
        self.tup = tup
    @property
    def size(self):
        return self.tup[1]
    @property
    def char(self):
        return self.tup[0]
    def __repr__(self) -> str:
        return f'Block(char={self.char}, size={self.size})'


i = len(ss)-1
while i >= 0:
    print(i)
    back = Block(ss[i])
    if back.char != '.':
        for j in range(len(ss)):
            front = Block(ss[j])
            if i < j:
                break
            if back.size < front.size and front.char == '.':
                #print('reverse is smaller than front')
                # remove old pos
                ss.pop(j)
                # insert new block
                ss.insert(j, (back.char, back.size))
                # insert empty block
                ss.insert(j+1, ('.', front.size - back.size))
                # remove old block
                ss.pop(i+1)
                # insert dots at old pos
                ss.insert(i+1, ('.', back.size))
                break
            elif back.size == front.size and front.char == '.':
                #print('back == front')
                # remove old block
                ss.pop(j)
                # insert new block
                ss.insert(j, (back.char, back.size))
                # remove old block
                ss.pop(i)
                # insert dots at old pos
                ss.insert(i, ('.', back.size))
                break
    i -= 1

lst = []
for x in ss:
    b = Block(x)
    for _ in range(b.size):
        lst.append(b.char)

ans = 0
for i in range(len(lst)):
    if lst[i] != '.':
        ans += i*int(lst[i])
print("p2", ans)




