import numpy as np

with open('input.in', 'r') as f:
    data = f.readlines()

curr = 0
input_arr = []
for line in data:
    if len(line)==1:
        curr = 0
    else:
        curr = int(line)

    input_arr.append(curr)

elfs = []
total = 0
for n in input_arr:
    if n == 0:
        elfs.append(total)
        total = 0
    total += n

elfs.append(total)

print(f'Calories: {np.amax(elfs)}')
print(f'n elf: {np.argmax(elfs) + 1}')

# part 2

res_arr = []
for i in range(3):
    idx = np.argmax(elfs)
    n_calories = elfs.pop(idx)
    res_arr.append(n_calories)

print("Problem 2", np.sum(res_arr))