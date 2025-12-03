import itertools

inp = "real.in"

with open(inp) as f:
    D = f.read()
    R = len(D.strip().split("\n"))


def p1():
    ans = 0
    for ln in D.rstrip().split("\n"):
        best = 0
        xs = list(map(int, ln))
        N = len(xs)
        nxs = []
        for comb in itertools.combinations(xs, 2):
            nxs.append(10*comb[0] + comb[1])
        ans += max(nxs)

    print(ans)


def p2():
    ans = 0
    for i, ln in enumerate(D.rstrip().split("\n")):
        xs = tuple(map(int, ln))
        print(f"it: {i}/{R}")
        k = 12
        start = 0
        best = 0
        numDigits = 0
        n = len(ln)
        for _ in range(k):
            rem = k - numDigits - 1
            end = n - rem
            idx = start + xs[start:end].index(max(xs[start:end]))
            numDigits += 1
            best = 10*best + xs[idx]
            start = idx + 1
        ans += best

    print(ans)

p1()
p2()
