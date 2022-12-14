from pathlib import Path

AIR = 1
ROCK = 2
SAND = 3

def print_map(grid):
    def get_char(obj):
        char = ''
        if obj == ROCK:
            char = '#'
        elif obj == AIR:
            char = '.'
        elif obj == SAND:
            char = 'o'
        return char

    width = len(grid[0])

    for y in range(max_y + 3):
        for x in range(490,600):
            print(get_char(grid[y][x]),end="")
        print()



with Path('input.in').open('r') as f:
    data = [line.strip() for line in f.readlines()]


max_y = -99999

for line in data:
    arr = line.replace(' ','').split('->')

    for i in range(1, len(arr)):
        src_x, src_y = arr[i-1].split(',')
        dest_x, dest_y = arr[i].split(',')

        src_x = int(src_x)
        src_y = int(src_y)

        dest_x = int(dest_x)
        dest_y = int(dest_y)

        max_y = max(src_y, max_y)
        max_y = max(dest_y, max_y)

max_x = 2000
grid = [[AIR for _ in range(max_x+1)] for _ in range(max_y+3)]



for line in data:
    arr = line.replace(' ','').split('->')

    for i in range(1, len(arr)):
        src_x, src_y = arr[i-1].split(',')
        dest_x, dest_y = arr[i].split(',')

        src_x = int(src_x)
        src_y = int(src_y)

        dest_x = int(dest_x)
        dest_y = int(dest_y)


        if src_x - dest_x == 0:
            # move y-led
            start = src_y if src_y < dest_y else dest_y
            end = dest_y if start == src_y else src_y
            for y in range(start, end+1):
                grid[y][src_x] = ROCK
        else:
            # move x-led
            start = src_x if src_x < dest_x else dest_x
            end = dest_x if src_x == start else src_x
            for x in range(start, end+1):
                grid[src_y][x] = ROCK


for i in range(max_x):
    grid[max_y+2][i] = ROCK

# Map is filled, now start dropping sand
sand_start = (0, 500)

y = 0
x = sand_start[1]

outer_run = True
sand_ctr = 0
while outer_run:
    curr_symbol = grid[y][x]

    run = True
    while run:
        if len(grid) <= y+1 or len(grid[0]) <= x+1 or x < 0:
            outer_run = False
            break

        down = grid[y+1][x]
        left = grid[y+1][x-1]
        right = grid[y+1][x+1]
        if (down == ROCK or down == SAND) \
            and (left == ROCK or left == SAND) \
            and (right == ROCK or right == SAND):
            # all paths blocked
            run = False
            #print("Stop running!")
        else:
            if down == AIR:
                y += 1
            elif left == AIR:
                y += 1
                x -= 1
            elif right == AIR:
                y += 1
                x += 1
    
    
    if outer_run:
        #print(f'curr pos: {(y, x)}')
        grid[y][x] = SAND
        if (y, x) == sand_start:
            sand_ctr += 1
            outer_run = False
            break
        sand_ctr += 1

        #print_map(grid)
        y, x = sand_start

print("part 2",sand_ctr)