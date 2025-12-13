
import sys
import z3

D = sys.stdin.read()

ans = 0

for ln in D.splitlines():
    ln = ln.split()
    buttons = []
    print(ln)

    for b_ln in ln[1:-1]:
        b_ln = b_ln[1:-1]
        buttons.append(list(map(int, b_ln.split(","))))

    joltage = ln[-1]
    joltage = joltage[1:-1]
    joltage = list(map(int, joltage.split(",")))

    n_counters = len(joltage)
    n_buttons = len(buttons)

    A = [[0] * n_buttons for _ in range(n_counters)]

    for button_idx, button in enumerate(buttons):
        for counter_idx in button:
            A[counter_idx][button_idx] = 1

    opt = z3.Optimize()
    x = [z3.Int(f'x_{i}') for i in range(n_buttons)]

    for xi in x:
        opt.add(xi >= 0)

    for counter in range(n_counters):
        constraint = sum(A[counter][button] * x[button] for button in range(n_buttons)) == joltage[counter]
        opt.add(constraint)

    opt.minimize(sum(x))

    if opt.check() == z3.sat:
        m = opt.model()
        sol = [m.eval(xi).as_long() for xi in x]
        presses = sum(sol)
        print(f"solutions: {sol}")
        print(f"btn presses: {presses}")
        ans += presses
    else:
        print("impossible")

print(ans)
