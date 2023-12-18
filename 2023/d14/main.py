import sys

with open(sys.argv[1], "r") as f:
    D = f.read().split("\n")

G = [[ch for ch in r] for r in D]
R=len(G)
C=len(G[0])

def pm(g):
    print(f"{'-':*^15}")
    for x in g:
        print("".join(x))
    print(f"{'-':*^15}")

for c in range(C):
    for r in range(R):
        if G[r][c] == "O":
            rr = r
            while True:
                if rr-1 < 0:
                    break
                if G[rr-1][c] == ".":
                    G[rr-1][c] = "O"
                    G[rr][c] = "."
                elif G[rr-1][c]=="#":
                    break
                rr -= 1

ans=0
print(R)
for i in range(R):
    count = sum([1 if ch=="O" else 0 for ch in G[i]])
    ans += count*(R-i)
print(ans)



