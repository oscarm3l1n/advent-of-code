
out = lambda x

a,b,c = 0,0,0
prog = [2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0]

# 2, 4
b = a % 8
# 1, 5
b = b ^ 5
# 7, 5
c = a >> b
# 1, 6
b = b ^ 6
# 0, 3
a = a >> 3
# 4, 6
b = b ^ c
# 5, 5
out( b % 8 )
# 3 0
# if a != 0 jump 0


# A, B, C = 4, 5, 6

# 0: A = A >> combo
# 1: B = B ^ literal
# 2: B = combo % 8
# 3: if A == 0 print out else jump to literal
# 4: B = B ^ C
# 5: out ( combo % 8 )
# 6: B = A >> combo
# 7: C = A >> combo

# program: 2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0
#
# B = A % 8
# B = B ^ 5
# C = A >> B
# B = B ^ 6
# A = A >> 3
# B = B ^ C
# out( B % 8 )
# jump 0 if A != 0

def solve(prog, a, b, c):
    if prog == []:
        return b
    ans = float("inf")
    for b in range(8):
        b = (a % 8)
        b = b ^ 5
        c = (a >> b)
        b = b ^ 6
        a = (a >> 3)
        b = b ^ c
        if b == prog[-1]:
            ans = min(ans, solve(prog[:-1], (a << 3) | b, b, c))
    return ans

program = [2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0]
for a in range(8):
    b = 0
    c = 0
    print(solve(program, a, b, c))
