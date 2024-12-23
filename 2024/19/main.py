import sys

with open(sys.argv[1], 'r') as f:
    D = f.read().strip()

lookup = D.split('\n\n')[0]
lookup = lookup.split(', ')
lookup = set(lookup)

lines = D.split('\n\n')[1]
lines = lines.split('\n')

memo = {}


def dfs(s: str):
    print(s)
    if s == '':
        return 1
    if s in memo:
        return memo[s]
    ans = 0
    for pat in lookup:
        if s.startswith(pat):
            ans += dfs(s[len(pat) :])
    memo[s] = ans
    return ans


ans = 0
ans2 = 0
for i, line in enumerate(lines):
    print(f'{i}/{len(lines)}')
    found = dfs(line)
    ans2 += found
    if found > 0:
        ans += 1

print(ans)
print(ans2)
