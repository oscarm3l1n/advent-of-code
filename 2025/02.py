inp = "real.in"
with open(inp) as f:
    D = f.read()
    D = D.split(",")

for p1 in [True, False]:
    ans = 0
    for ln in D:
        lo, hi = ln.split("-")
        lo, hi = int(lo), int(hi)
        invalid = []
        for i in range(lo, hi+1):
            s = str(i)
            n = len(s)
            if p1:
                if n % 2 == 0:
                    if s[:n//2] == s[n//2: ]:
                        ans += i
            else:
                for j in range(1, n//2 + 1):
                    ns = s[:j]
                    count = n // j
                    if ns * count == s:
                        ans += i
                        break

    print("p1" if p1 else "p2", ans)
