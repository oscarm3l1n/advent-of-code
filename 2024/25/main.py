
import sys

with open(sys.argv[1], "r") as f:
    chunks = f.read().strip().split("\n\n")

locks = []
keys = []
for chunk in chunks:
    G = chunk.split("\n")
    R = len(G)
    C = len(G[0])
    is_lock = True
    for c in range(C):
        if G[R-1][c] != ".":
            is_lock = False
    if is_lock:
        heights = []
        for c in range(C):
            ctr = 0
            for r in range(1, R):
                if G[r][c] == "#":
                    ctr += 1
            heights.append(ctr)
        locks.append(heights)
    else:
        heights = []
        for c in range(C):
            ctr = 0
            for r in range(R-2, -1, -1):
                if G[r][c] == "#":
                    ctr += 1
            heights.append(ctr)
        keys.append(heights)

ans = 0
for lock in locks:
    for key in keys:
        ok = True
        for i in range(len(lock)):
            if lock[i] + key[i] > R-2:
                ok = False
        if ok:
            print(key, lock, "FITS")
            ans += 1
        #print(lock,key, ok)
print(ans)




        




