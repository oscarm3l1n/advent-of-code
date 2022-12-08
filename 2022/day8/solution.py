# test == 21 trees visible

map = []
with open('input.in', 'r') as f:
    for line in f.readlines():
        map.append([ch for ch in line.strip()])


def search(y, x, dir, map):
    my_tree = map[y][x]
    counter = 0
    if dir == 'left':
        x -= 1
        while x >= 0:
            counter += 1
            if map[y][x] >= my_tree:
                return False, counter
            x -= 1
    elif dir == 'right':
        x += 1
        while x < len(map[0]):
            counter += 1
            if map[y][x] >= my_tree:
                return False, counter
            x += 1
    elif dir == 'down':
        y += 1
        while y < len(map):
            counter += 1
            if map[y][x] >= my_tree:
                return False, counter
            y += 1
    elif dir == 'up':
        y -= 1
        while y >= 0:
            counter += 1
            if map[y][x] >= my_tree:
                return False, counter
            y -= 1
    return True, counter

w = len(map[0])
h = len(map)

n_visible =  w + (w-2) + (h - 1) + (h - 1)
for i in range(1, h-1, 1):
    for j in range(1, w-1, 1):
        
        down, _ = search(i, j, 'down', map)
        up , _ = search(i, j, 'up', map)
        right, _ = search(i, j, 'right', map)
        left, _ = search(i, j, 'left', map)

        if down or up or right or left:
            n_visible += 1

print("Ans1 : ", n_visible)

# Part 2
best = -float('inf')
for row in range(0,h):
    for col in range(0,w):
        down, c_down = search(col, row, 'down', map)
        up , c_up = search(col, row, 'up', map)
        right, c_right = search(col, row, 'right', map)
        left, c_left = search(col, row, 'left', map)
        if (c_left * c_right * c_up * c_down) > best:
            best = (c_left * c_right * c_up * c_down)

print ("Ans 2: ",best)