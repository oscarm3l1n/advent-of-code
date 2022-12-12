
def solve(grid, starts):
    paths = []
    for start in starts:
        Q = [start]

        visited = {}

        depth = 0
        run = True
        while len(Q) and run:
            node = Q.pop(0)
            curr_y, curr_x = node
            depth += 1

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx = curr_x + x
                dy = curr_y + y

                if      0 <= dx < len(grid[0]) \
                    and 0 <= dy < len(grid) \
                    and (dy, dx) not in visited:

                    a = ord('a') if grid[curr_y][curr_x] == 'S' else ord(grid[curr_y][curr_x])
                    b = ord('z') if grid[dy][dx] == 'E' else ord(grid[dy][dx])

                    # can climb
                    if  a-b > -2:
                        if grid[dy][dx] == 'E':
                            end = (dy, dx)
                            visited[(dy, dx)] = (curr_y, curr_x)
                            run = False
                            break
                        Q.append((dy, dx))
                        visited[(dy, dx)] = (curr_y, curr_x)
                    
        
        path = []
        current = end
        if end in visited:
            while current != start:
                path.append(current)
                current = visited[current]
            path.append(current)
            paths.append(path)
    paths = [len(p) - 1 for p in paths]
    paths = sorted(paths)
    return paths


with open('input.in', 'r') as f:
    grid = [line.strip() for line in f.readlines()]

start = (0, 0)
starts = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i, j)
            starts.append((i, j))
        if grid[i][j] == 'a':
            starts.append((i, j))

print("part 1:", solve(grid, [start])[0])
print("part 2:", solve(grid, starts)[0])
