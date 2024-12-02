import sys
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    D = f.read().strip()


lines = D.split("\n")


def rule1(nums):
    for i in range(1, len(nums)):
        if not (0 < abs(nums[i] - nums[i - 1]) < 4):
            return False
    return True


def rule2(nums):
    return any([nums == sorted(nums), nums == sorted(nums, reverse=True)])


def is_ok(nums):
    return rule1(nums) and rule2(nums)


ans = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    safe = is_ok(nums)
    if safe:
        ans += 1
print("p1", ans)

ans = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    safe = is_ok(nums)
    if safe:
        ans += 1
        continue
    tries = []
    for i in range(len(nums)):
        removed = nums.pop(i)
        tries.append(is_ok(nums))
        nums.insert(i, removed)
    if any(tries):
        ans += 1
print("p2", ans)
