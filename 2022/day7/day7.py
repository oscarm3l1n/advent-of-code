import json
data = []
with open('test.in', 'r') as f:
    for line in f.readlines():
        data.append(line.strip())
        print(line.strip())


filesystem = {}
history = []

curr_dir = None

for i, line in enumerate(data):
    line = line.split()

    if line[0] == '$':
        command = line[1]

        if command == 'cd':
            curr_dir = line[-1]
            if curr_dir == '..':
                curr_dir = history.pop()
            else:
                history.append(curr_dir)

        if command == 'ls':
            inner_dict = {}

            for inner_line in data[i+1:]:
                inner_line = inner_line.split()
                if inner_line[0] == '$':
                    break
                first, second = inner_line
                if first == 'dir':
                    inner_dict[first] = second
                else:
                    inner_dict[second] = first  # name : size

            filesystem[curr_dir] = inner_dict

print(json.dumps(filesystem, indent=2))
