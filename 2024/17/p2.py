test = [0, 3, 5, 4, 3, 0]


def test_prog(a, b, c) -> list[int]:
    out = []
    while a != 0:
        a = a >> 3
        out.append(a % 8)
    return out


real = [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]


def real_prog(a, b, c) -> list[int]:
    out = []
    while a != 0:
        b = a % 8
        b = b ^ 5
        c = a // (2**b)
        b = b ^ 6
        a = a // (2**3)
        b = b ^ c
        out.append(b % 8)
    return out


B = 0
C = 0
A = 0
prog = list(real)
good = {0}
for i in range(1, len(prog)):
    goal = prog[-i:]
    new_good = set()
    for ii in range(8):
        for ok in good:
            out: list[int]
            out = real_prog(ok * 8 + ii, B, C)
            if out == goal:
                new_good.add(ok * 8 + ii)
    good = new_good.copy()
    print(good)
    A = min(good)

final = set()
for i in range(8):
    for num in good:
        goal = [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]
        out = real_prog(num * 8 + i, 0, 0)
        if out == goal:
            final.add(num * 8 + i)
print(min(final))
