import json

data = []
with open('test.in', 'r') as f:
    for line in f.readlines():
        data.append(line.strip())


len_latest_dir = 0
filesystem = {}

curr_dir = None
filesystem = {}
len_latest_dir = 0
for i, line in enumerate(data):
    line = line.split()
    if line[0] == '$' and line[1] == 'cd':
        if line[2] == '..':
            len_latest_dir = len(line[2])
            curr_dir = curr_dir[:-len_latest_dir]
        else:
            if line[2] == '/':
                curr_dir = '/'
            else:
                curr_dir = curr_dir + line[2] + '/'
    elif line[0] == '$' and line[1] == 'ls':
        stuff = []
        for inner in data[i+1:]:
            inner = inner.split()
            if inner[0] == '$':
                break
            stuff.append((inner[0], inner[1]))

        filesystem[curr_dir] = stuff


sizes = {}
for k, _ in filesystem.items():
    sizes[k] = 0

new_sizes = {}
#for k, v in filesystem.items():
for k, v in filesystem.items():
    curr_folder = k
    size = 0
    while curr_folder != '/' or len(curr_folder)==0:
        for item in filesystem[curr_folder]:
            first, second = item
            if first != 'dir':
                size += int(first)
        
        sizes[curr_folder] = size

        # /a/e/ --> remove e/ part so we end up in /a/
        length = 0
        backslash_counter = 0
        for ch in curr_folder[::-1]:
            if ch == '/':
                backslash_counter += 1
                if backslash_counter == 2:
                    break
            length += 1

        curr_folder = curr_folder[:-length]
    
print(json.dumps(sizes,indent=2))

tot = 0
for k, v in sizes.items():
    if v <= 100_000:
        tot += v

print(tot)
