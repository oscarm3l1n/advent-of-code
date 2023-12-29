import sys
with open(sys.argv[1] ,"r") as f:
    D = f.read().split("\n")

instructions = D[0]
D = D[2:]
M = {}
for item in D:
    k, pair = item.split("=")
    k=k[:-1]
    pair = pair[2:-1]
    p1, p2 = pair.split(",")
    p2 = p2[1:]
    M[k] = (p1,p2)

    
key = "AAA"
ans=0
while True:
    for instr in instructions:
        i=-1
        if instr=="R":
            i=1
        elif instr=="L":
            i=0

        new_key=M[key][i]
        if new_key=="ZZZ":
            print(ans+1)
            exit()
        key=new_key
        ans+=1