import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")


DP = {}
def f(dots, numbers, i, ni, current):
    key = (i, ni, current)
    if key in DP:
        return DP[key]
    if i == len(dots):
        if ni==len(numbers) and current==0:
            return 1
        elif ni==len(numbers)-1 and numbers[ni]==current:
            return 1
        else:
            return 0
    ans = 0
    for c in ['.', '#']:
        if dots[i]==c or dots[i]=='?':
            if c=='.' and current==0:
                ans += f(dots, numbers, i+1, ni, 0)
            elif c=='.' and current > 0 and ni<len(numbers) and numbers[ni]==current:
                ans += f(dots, numbers, i+1, ni+1, 0)
            elif c=='#':
                ans += f(dots, numbers, i+1, ni, current+1)
    DP[key] = ans
    return ans


# ???.### 1,1,3

ans=0
for line in data:
    dots, numbers = line.split()
    numbers = [int(x) for x in numbers.split(",")]
    score = f(dots, numbers, 0, 0, 0)
    ans += score

print("part 1", ans)

ans = 0
for line in data:
    dots, numbers = line.split()
    dots = "?".join([dots, dots, dots, dots, dots])
    numbers = ",".join([numbers, numbers, numbers, numbers, numbers])
    numbers = [int(x) for x in numbers.split(",")]
    DP.clear()
    score = f(dots, numbers, 0, 0, 0)
    ans += score
print(ans)

