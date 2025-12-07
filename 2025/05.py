
inp = "real.in"
with open(inp) as f:
    D = f.read()

ranges, ids = D.rstrip().split("\n\n")

highest = 0

seen = []
for r in ranges.split("\n"):
    lo, hi = r.split("-")
    lo, hi = int(lo), int(hi)
    seen.append([lo, hi])


def p1():
    ans = 0
    for id in ids.split("\n"):
        id = int(id)
        fresh = False
        for s in seen:
            if s[0] <= id <= s[1]:
                fresh = True
                break
        if fresh:
            ans += 1
    print(ans)

def p2():
    seen.sort(key=lambda x: x[0])
    change = True
    while change:
        change = False
        for i in range(len(seen)-1):
            if seen[i][1] >= seen[i+1][0] - 1:
                seen[i][1] = max(seen[i][1], seen[i+1][1])
                seen.pop(i+1)
                change = True
                break

    ans = 0
    for lo, hi in seen:
        ans += (hi-lo)+1
    print(ans)

p1()
p2()
