
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


