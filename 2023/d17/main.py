from heapq import heappop, heappush
import sys
def pm(g, path):
    for r, c in path:
        g[r][c] = "#"
    for gg in g:
        print("".join(gg))


with open(sys.argv[1], "r") as f:
    D = f.read().split("\n")

G = [[int(c) for c in row] for row in D]

R=len(G)
C=len(G[0])
start = (0, 0)
end = (R-1, C-1)

# r, c, dr, dc, n, cost???
q = [(0, 0, 0, 0, 0, 0)]
visited=set()
while q:
    cost, r, c, dr, dc, n  = heappop(q)
    if (r,c,dr,dc,n) in visited:
        continue

    if r < 0 or r>=R or c<0 or c>=C:
        continue

    visited.add((r,c,dr,dc,n))

    if (r,c)==(R-1,C-1):
        print(cost)
        break
    
    if n < 10 and (dr, dc) != (0, 0):
        rr=r+dr
        cc=c+dc
        if 0<=rr<R and 0<=cc<C:
            heappush(q, (cost+G[rr][cc],rr, cc, dr, dc, n+1 ))
    
    if n >= 4 or (dr,dc)==(0,0):
        for (ndr, ndc) in [(0, 1), (0, -1), (1,0),(-1,0)]:
            if (ndr,ndc) != (dr,dc) and (ndr,ndc)!=(-dr,-dc):
                nc=c+ndc
                nr=r+ndr
                if 0 <= nc < C and 0<=nr<R:
                    heappush(q, (cost+G[nr][nc],nr,nc,ndr,ndc,1))
                    # heappush(q, (nr,nc,ndr,ndc,1,cost+G[nr][nc]))
